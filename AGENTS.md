# Guía de evaluación

Describe el formato del CSV de calificaciones y cómo se anotan las notas y el feedback en los notebooks de los alumnos. Las instrucciones son genéricas y reutilizables para cualquier examen.

> __Otras guías de este repositorio.__ Esta es la guía de evaluación. Para la
> __traducción al español__ del material —la rama `es`, cómo invocar el aplicador
> `.es/apply_es.py` y qué invariantes no romper— ver [`.es/README.md`](.es/README.md).
> Las tareas en curso y su estado están en [`ToDo.md`](ToDo.md). El __archivado de las
> ramas de cursos pasados__ como tags está al final de este fichero.

---

## Estructura de ficheros

Cada examen tiene su propia carpeta dentro de `others/<curso>/<convocatoria>/`:

```
others/<curso>/<convocatoria>/
    calificaciones-<examen>.csv     ← notas y explicaciones de todos los alumnos
    <examen>/
        NOMBRE APELLIDOS_ID_assignsubmission_file.ipynb   ← un notebook por alumno
```

Las rúbricas de corrección son compartidas entre convocatorias y se guardan en `others/`:

```
others/
    rubrica-<tipo>.md     ← una rúbrica por tipo de ejercicio
```

**Ejemplo** (Prueba 1, ordinaria 25-26):

```
others/25-26/ordinaria/
    calificaciones-p1.csv
    p1/
        ANA ROMERO JORGE_35731396_assignsubmission_file.ipynb
        ...
others/
    rubrica-curry-howard.md
    rubrica-instancias.md
    rubrica-isomorfismos.md
    rubrica-type-driven.md
```

---

## CSV de calificaciones

**Codificación:** ISO-8859-1. **Separador:** `;`. **Comillas:** `"` (solo cuando el campo contiene `;`).

### Estructura de columnas

Las dos primeras columnas identifican al alumno. A continuación, cada apartado tiene un par de columnas: la nota (float) y la explicación (texto libre). Los alumnos que no entregaron tienen estas columnas vacías.

```
Nombre ; Apellido(s) ; <apt> ; <apt>_exp ; <apt> ; <apt>_exp ; ...
```

Donde `<apt>` es el identificador del apartado, p.ej. `1a`, `1b`, `2a`, `3`, etc.

**Ejemplo** (Prueba 1 ordinaria 25-26, 10 apartados):

```
Nombre ; Apellido(s) ; 1a ; 1a_exp ; 1b ; 1b_exp ; 2a ; 2a_exp ; 2b ; 2b_exp ;
3a ; 3a_exp ; 3b ; 3b_exp ; 4a ; 4a_exp ; 4b ; 4b_exp ; 4c ; 4c_exp ; 5 ; 5_exp
```

### Leer y escribir con Python

```python
import csv

# Leer
with open('calificaciones-p1.csv', encoding='iso-8859-1', newline='') as f:
    rows = list(csv.reader(f, delimiter=';', quotechar='"'))

header = rows[0]
col = {h: i for i, h in enumerate(header)}

# Modificar una celda
rows[1][col['2a']] = '0.5'
rows[1][col['2a_exp']] = 'Signatura correcta; cuerpo incompleto.'

# Escribir
with open('calificaciones-p1.csv', 'w', encoding='iso-8859-1', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(rows)
```

> **Importante:** usar siempre `csv.reader`/`csv.writer` con `delimiter=';'`. Nunca hacer `split(';')` a mano: los campos de explicación pueden contener punto y coma y el fichero quedaría corrupto.

---

## Formato en los notebooks

Cada notebook tiene ejercicios y sub-apartados. Para cada apartado hay que añadir dos cosas:

1. **La nota**, inline en la celda de cabecera del apartado.
2. **El feedback**, en una celda markdown separada justo después de la respuesta del alumno.

### 1. Nota en la cabecera del apartado

Se añade `_Nota: X_` al final de la primera línea de la celda de cabecera, sin alterar el resto:

```markdown
#### a) __(1 punto)__ _Nota: 0.8_
```

Si la cabecera tiene contenido en líneas siguientes, solo se modifica la primera:

```markdown
#### __b) (2 puntos)__ _Nota: 1.3_

Enunciado del apartado...
```

Si un ejercicio no tiene sub-apartados y su cabecera es de nivel superior, la nota va igualmente al final de la primera línea:

```markdown
# Ejercicio 5 _Nota: 1.2_
__(1,5 puntos)__
```

### 2. Celda de feedback

Celda markdown independiente colocada **después de la celda con la respuesta del alumno**, con el formato:

```markdown
> **Feedback <apt>:** Texto breve de explicación.
```

El texto de feedback es la misma frase que el campo `<apt>_exp` del CSV.

**Ejemplos:**

```markdown
> **Feedback 1a:** Signatura correcta; cuerpo con variable no definida; no compila.
```

```markdown
> **Feedback 4b:** from correcto; to no aplica la función a Unit.
```

```markdown
> **Feedback 5:** Implementación final correcta; algunos labels de constructoras/destructoras incorrectos.
```

### Estructura resultante de un apartado

```
#### a) __(1 punto)__ _Nota: 0.7_     ← cabecera con nota inline
[celda de enunciado, si la hay]
[celda con la respuesta del alumno]
> **Feedback Xa:** Explicación.        ← celda de feedback
#### b) __(1 punto)__ _Nota: 0.5_
...
```

---

# Archivado de ramas

Las ramas de cursos pasados no se conservan como ramas. Cuando un curso termina, su rama
se convierte en un tag y la rama se borra, de forma que el listado solo muestra lo que está
en uso. No se pierde nada: el tag fija el commit exacto al que apuntaba la rama y esta se
puede recrear desde él en cualquier momento.

__Todos los tags de archivo viven en el repositorio privado__, incluidos los de las ramas
que estaban en el público:

| Patrón del tag | Dónde estaba la rama |
|---|---|
| `archive/<rama>` | este repo (`19-20/PD-VIC/3`, `exam-ord-20-21`, `jm/automata`, ...) |
| `archive/public/<rama>` | el repo público (`VIC-24-25`, `MOS-24-25`, `VIC-25-26`, `MOS-25-26`) |

Por eso el privado tiene solo `master` y `es`, y el público solo `master`, `es` y las dos
ramas del curso que se está impartiendo.

## Recuperar una rama archivada

```sh
git fetch origin --tags
git tag -l 'archive/*'
git branch VIC-25-26 archive/public/VIC-25-26
```

La rama recuperada apunta exactamente al commit al que apuntaba la borrada. Si hay que
devolverla al repo público, se empuja allí explícitamente: `git push urjc-pd-public VIC-25-26`.

## Archivar una rama

Crear el tag, empujarlo, __comprobar que ha llegado al remoto antes de borrar nada__ y solo
entonces borrar la rama:

```sh
git tag archive/public/VIC-26-27 urjc-pd-public/VIC-26-27
git push origin refs/tags/archive/public/VIC-26-27
git ls-remote --tags origin 'refs/tags/archive/public/VIC-26-27'   # debe coincidir con la punta
git push urjc-pd-public :refs/heads/VIC-26-27
```

Aviso para el repo público: todas sus ramas están cubiertas por una única regla clásica de
protección con patrón `*` y los borrados deshabilitados, así que el último paso se rechaza
mientras no se permitan temporalmente. Localizar la regla, abrirla, borrar y __volver a
cerrarla acto seguido__:

```sh
gh api graphql -f query='{repository(owner:"jserranohidalgo",name:"urjc-pd"){
  branchProtectionRules(first:10){nodes{id pattern allowsDeletions}}}}'
```

```sh
gh api graphql -f query='mutation{updateBranchProtectionRule(
  input:{branchProtectionRuleId:"<id>",allowsDeletions:true}){
  branchProtectionRule{pattern allowsDeletions}}}'
```

La misma mutación con `allowsDeletions:false` la restaura. El equivalente en la interfaz web
es la casilla "Allow deletions" de la regla `*` en Settings → Branches.

El endpoint REST por rama (`DELETE /repos/.../branches/<rama>/protection`) __no sirve__ aquí:
responde OK pero no altera una regla por patrón.
