# Traducción al español: cómo continuar

La rama **`es`** es la traducción al español del material que se publica en el repo
público. `master`, en inglés, es la **fuente de verdad**: los cambios se hacen allí
primero y luego se traen aquí.

La rama es **huérfana** a propósito: no desciende de `master`. Si descendiera, subirla al
repo público publicaría también la historia de `master`, que incluye `others/` con
entregas de alumnos, `ToDo.md`, `CLAUDE.md` y `.claude/`. Tal como está, contiene solo el
conjunto público y `git push urjc-pd-public es:es` es seguro por construcción.

**Nunca se fusiona en ninguna dirección.** No se hace merge de `master` en `es` ni al
revés: la rama se *regenera*, guiada por `.es/manifest.json`.

## Estado (2026-09-10)

**Completa: 38 de 38 notebooks.** Todos los ficheros del manifiesto están al día respecto
al `master` del que se tradujeron (comprobado con el script de la sección
"El manifiesto"). Pendiente solo el paso de publicación: `git push public es:es` (ver
`CLAUDE.md`).

Fuera de alcance: los exámenes de `exams/` (ya están en español),
`PF-3/topic7/wordle/`, y el texto incrustado en las figuras `images/*.svg`.

## Cómo se traduce un notebook

1. Volcar sus celdas markdown y sus comentarios, sin duplicar los que ya se hayan visto:

   ```sh
   python3 - <<'PY'
   import json
   seen=set()
   for p in ['PF-2/topic3/3.1 Functions.ipynb','PF-2/topic3/3.1 Functions-template.ipynb']:
       nb=json.load(open(p)); print(f"##### {p}")
       for i,c in enumerate(nb['cells']):
           s=''.join(c['source'])
           if c['cell_type']=='markdown':
               k=s.strip()
               if k and k not in seen: seen.add(k); print(f"===== [{i}] =====\n{s}")
           else:
               for l in s.split('\n'):
                   st=l.strip()
                   if st.startswith('//') and len(st)>3 and st not in seen:
                       seen.add(st); print(f"  COMENT [{i}]: {st}")
   PY
   ```

2. Escribir `.es/t/t_<x>.py` con una lista `PAIRS = [(inglés, español), ...]`. Los pares
   valen tanto para celdas markdown como para líneas de comentario.

3. Aplicar:

   ```sh
   python3 .es/apply_es.py "es: 3.1 Functions" .es/t/t_3_1.py \
       "PF-2/topic3/3.1 Functions.ipynb" "PF-2/topic3/3.1 Functions-template.ipynb"
   ```

El script traduce en memoria, **valida y solo entonces escribe**: crea el commit en `es`
con plumbing, sin tocar el working tree, que se queda en `master`. Reconstruye su índice
temporal desde la punta de `es` en cada pasada.

## Los avisos del script, y por qué hay que leerlos

- **Aborta** si alguna traducción no encaja con ninguna celda. Suele significar que la
  cadena en inglés no es exacta —espacios al final de línea, una errata del original— o
  que sobra una variante. Ya evitó dos veces dejar celdas en inglés.
- **Avisa** de celdas markdown sin traducir. Las de solo imagen o solo LaTeX no necesitan
  traducción; el resto, sí.
- **Avisa** de comentarios sin traducir. Esto es importante: los templates traen
  comentarios que su notebook no tiene (12 en 2.3, 15 en 3.2, 13 en 3.3, 9 en 3.4).

El emparejado ignora los espacios al final de cada línea, pero no otras diferencias: los
pares notebook/template **no siempre comparten la prosa** (2.1 tiene un `excepted` donde
el notebook dice `expected`, y hay que traducir las dos variantes).

## El manifiesto

`.es/manifest.json`, en la rama `es`, guarda por cada fichero el blob de `master` del que
se tradujo y el hash de cada celda. Para saber qué hay que retraducir después de tocar el
inglés, basta comparar ese blob con el actual:

```sh
git show es:.es/manifest.json | python3 -c "
import json,sys,subprocess
m=json.load(sys.stdin)
for f,v in m['files'].items():
    cur=subprocess.run(['git','rev-parse',f'master:{f}'],capture_output=True,text=True).stdout.strip()
    if cur != v['source_blob']: print('DESACTUALIZADO:', f)
"
```

## Glosario

En `.es/glosario.md`, **en la rama `es`**. Fija los criterios (qué se traduce y qué no) y
la terminología. Decisiones tomadas: *hole* → **hueco**, *pattern matching* sin traducir,
`foldRight`/`map`/`filter`/`flatMap` sin traducir por ser nombres de función.
