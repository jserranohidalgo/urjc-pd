#!/usr/bin/env python3
"""Aplica una traduccion a la rama `es`.

Lee un modulo de traduccion (lista PAIRS de (ingles, espanol)), lo aplica a las
celdas markdown y a los comentarios de las celdas de codigo de los notebooks
indicados, escribe el resultado en la rama `es` con plumbing (sin tocar el
working tree, que se queda en master) y anota la procedencia en .es/manifest.json.

  python3 apply_es.py <modulo_traduccion.py> <fichero>...
"""
import hashlib, importlib.util, io, json, os, subprocess, sys, tempfile

REPO = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True,
                      text=True).stdout.strip() or os.getcwd()
IDX = os.environ.get('ES_INDEX', os.path.join(tempfile.gettempdir(), 'urjc-pd-es.index'))


def git(*args, **kw):
    env = dict(os.environ, GIT_INDEX_FILE=IDX)
    r = subprocess.run(['git', '-C', REPO] + list(args), capture_output=True, text=True,
                       env=env, **kw)
    if r.returncode:
        raise SystemExit(f'git {" ".join(args)[:80]} -> {r.stderr.strip()}')
    return r.stdout


def git_bytes(*args):
    env = dict(os.environ, GIT_INDEX_FILE=IDX)
    r = subprocess.run(['git', '-C', REPO] + list(args), capture_output=True, env=env)
    if r.returncode:
        raise SystemExit(f'git {" ".join(args)[:80]} -> {r.stderr.decode().strip()}')
    return r.stdout


def sha1(t):
    return hashlib.sha1(t.encode()).hexdigest()


def norm(t):
    """Clave de emparejado: sin espacios al final de cada linea ni al principio/fin."""
    return '\n'.join(l.rstrip() for l in t.strip().split('\n'))


def load_pairs(path):
    spec = importlib.util.spec_from_file_location('t', path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.PAIRS


def main():
    msg = sys.argv[1]
    tmod, files = sys.argv[2], sys.argv[3:]
    pairs = load_pairs(tmod)
    by_en = {norm(en): es for en, es in pairs}
    used = {norm(en): 0 for en, es in pairs}

    # el indice se reconstruye desde la punta de es en cada pasada, para que no
    # arrastre estado de ejecuciones anteriores
    git('read-tree', 'es')
    manifest = json.loads(git_bytes('show', 'es:.es/manifest.json').decode())

    # primero se traduce todo en memoria y se valida; solo despues se escribe
    blobs = {}
    staged = []
    for f in files:
        raw = git_bytes('show', f'master:{f}')
        nb = json.loads(raw.decode())
        src_blob = git('rev-parse', f'master:{f}').strip()
        cells_done = {}
        pend = []
        pend_cm = []
        n_md = n_cm = 0
        for c in nb['cells']:
            s = ''.join(c['source'])
            key = norm(s)
            if c['cell_type'] == 'markdown' and key in by_en:
                cells_done[sha1(s)] = sha1(by_en[key])
                c['source'] = by_en[key].splitlines(keepends=True)
                used[key] += 1; n_md += 1
            elif c['cell_type'] == 'markdown' and key and not key.startswith('!['):
                pend.append(key[:70])
            elif c['cell_type'] == 'code':
                out, hit = [], False
                for line in s.split('\n'):
                    st = line.strip()
                    if st.startswith('//') and norm(st) in by_en:
                        pad = line[:len(line) - len(line.lstrip())]
                        out.append(pad + by_en[norm(st)]); used[norm(st)] += 1; hit = True
                    else:
                        if st.startswith('//') and len(st) > 3:
                            pend_cm.append(st[:70])
                        out.append(line)
                if hit:
                    c['source'] = '\n'.join(out).splitlines(keepends=True); n_cm += 1
        buf = io.StringIO()
        json.dump(nb, buf, indent=1, sort_keys=True, ensure_ascii=False); buf.write('\n')
        if pend:
            print(f'  AVISO {f}: {len(pend)} celdas markdown sin traducir')
            for x in pend: print(f'      · {x}')
        if pend_cm:
            print(f'  AVISO {f}: {len(set(pend_cm))} comentarios sin traducir')
            for x in sorted(set(pend_cm)): print(f'      // {x}')
        blobs[f] = buf.getvalue()
        manifest['files'][f] = {'source_blob': src_blob, 'cells': cells_done}
        staged.append((f, n_md, n_cm))

    unused = [k[:70] for k, n in used.items() if n == 0]
    if unused:
        raise SystemExit('ABORTADO, nada escrito. Traducciones que no encajaron:\n  ' + '\n  '.join(unused))

    for f, content in blobs.items():
        blob = git('hash-object', '-w', '--stdin', input=content).strip()
        git('update-index', '--add', '--cacheinfo', f'100644,{blob},{f}')

    manifest['source_commit'] = git('rev-parse', 'master').strip()
    mblob = git('hash-object', '-w', '--stdin',
                input=json.dumps(manifest, indent=1, ensure_ascii=False) + '\n').strip()
    git('update-index', '--add', '--cacheinfo', f'100644,{mblob},.es/manifest.json')

    tree = git('write-tree').strip()
    parent = git('rev-parse', 'es').strip()
    commit = git('commit-tree', tree, '-p', parent, '-m', msg).strip()
    git('update-ref', 'refs/heads/es', commit)

    for f, n_md, n_cm in staged:
        print(f'  {f}: {n_md} celdas markdown, {n_cm} celdas con comentarios')
    print(f'  {len(pairs)} traducciones aplicadas -> commit {commit[:7]} en es')


if __name__ == '__main__':
    main()
