# ToDo — Actualización de material del curso

Tareas pendientes sobre el material de la asignatura (repo público `urjc-pd`, con
copia/trabajo en este repo privado). Creado el 2026-09-07.

---

## 1. Curry-Howard: actualizar con el nuevo juego

El juego es **The Curry–Howard Game** (repo
[`jserranohidalgo/curry-howard-game`](https://github.com/jserranohidalgo/curry-howard-game),
jugable en https://jserranohidalgo.github.io/curry-howard-game/). Es una app
standalone (Scala 3 + Scala.js) que no requiere cuenta ni servidor; el progreso se
guarda en el navegador. Incluye dos "charlas" navegables dentro de la propia
aplicación:

- **What is the Curry–Howard correspondence?** — quiénes fueron Curry y Howard,
  qué observaron, y un ejemplo completo de principio a fin.
- **How do you play the Curry–Howard game?** — el tablero, los movimientos, los
  niveles de ayuda, y una partida completa ganada y otra refutada.

También hay un plugin de Claude Code (`/plugin marketplace add
jserranohidalgo/curry-howard-game`) que actúa de tutor mientras se juega. El código
fuente y los documentos de diseño del juego aún no están publicados ("coming
soon" según el README), y está pensado como el primero de una familia de juegos
(uno por cada lógica/lenguaje: `λ→`, `λμ`, `λΠ`, `λμΠ`).
El repo ya lista este curso (`urjc-pd`) en su tabla "Where it is used".

- [x] Enlazar el juego desde el README principal de `urjc-pd` (2026-09-08): bullet
      de Topic 4 con enlace a jugar, más una sección nueva "The Curry–Howard
      Game". Hecho en local, rama `jserrano-master`, **sin commitear todavía**.
- [ ] Valorar si se anima a los alumnos a instalar/usar el plugin de Claude Code
      como apoyo (requiere Python 3).

### Propuesta de modificación de `PF-2/topic4/4.1 CurryHoward.ipynb`

Comparación hecha (2026-09-08) entre la estructura actual del notebook (81
celdas: refresco aritmética→tipos, proposiciones como tipos, pruebas como
programas con un ejemplo reescrito 3 veces, tabla de reglas, 4 teoremas más,
postura intuicionista con 3 no-teoremas, conclusión) y la charla del juego
*"What is the Curry–Howard correspondence?"* (documentada en
`curry-howard-game/spec/help.md`, sección "The first talk, slide by slide").

La forma en que el notebook presenta la tabla de reglas (reglas de deducción
natural → constructores/destructores ADT → tabla fusionada, celdas 23-32) ya
coincide bien con el enfoque progresivo de la charla — no tocar eso. Los huecos
concretos identificados, de menor a mayor esfuerzo:

- [ ] **Momento eureka de Curry y Howard** (bajo esfuerzo, alto valor). La celda
      3 ya tiene las dos fotos, pero la celda 4 pasa directo a definir la
      correspondencia en abstracto. La charla cuenta dos momentos concretos: qué
      vio Curry en 1934 (derivación axiomática de `p→r` junto al combinador
      `S (K g) f`, sin nada que los empareje) y qué vio Howard en 1969 (figura
      de deducción natural de `a∧b→b∧a` junto al programa que la habita).
      Insertar una celda breve entre 3 y 4 con esos dos ejemplos como gancho
      narrativo, antes de la definición general.
- [ ] **Nombrar el "giro de moneda"** (bajo esfuerzo). La charla usa una moneda
      que gira entre lectura-de-lógico y lectura-de-programador como hilo
      conductor visual. El notebook ya alterna programa/prueba lado a lado
      (celdas 27-28 en adelante) pero nunca lo nombra como ritual repetido.
      Añadir un callout la primera vez que aparece, tipo "▸ lo mismo, leído dos
      veces", para que se repita mentalmente en los ejemplos posteriores.
- [ ] **Secuencia "hole by hole"** (esfuerzo medio, el más valioso
      pedagógicamente). La charla incluye 4 slides de una partida real
      construyéndose paso a paso. El notebook reescribe el mismo programa 3
      veces (idiomático → verboso → combinadores, celdas 33-42), que es otra
      cosa: no muestra cómo se va rellenando el término. Añadir, junto al
      ejemplo verboso, una secuencia corta con `???` que se va rellenando
      agujero a agujero — el core loop del juego — antes de la versión final
      con combinadores.
- [ ] **Cierre con invitación a jugar** (bajo esfuerzo). La conclusión (celdas
      79-80) menciona la familia de lógicas en un párrafo denso y no apunta a
      ningún siguiente paso. Cerrar el notebook con una celda que invite a jugar
      el ejemplo (`p∧(q∨r)→p∧q∨p∧r` o `a∧b→b∧a`) en el juego, enlazando el
      mismo repo añadido al README.
- [ ] Decidir alcance final antes de implementar (p.ej. si se salta el punto del
      "hole by hole", que es el que más tiempo lleva) y aplicar los cambios
      también al template (`4.1 CurryHoward-template.ipynb`, si existe).

## 2. Traducción al español

- [ ] Traducir el material del curso (notebooks de `PF-1`, `PF-2`, `PF-3`) al
      español.
- [ ] Dejar la traducción en una rama nueva (p.ej. `es` o `traduccion-es`) sin
      mezclarla con `master`, que se mantiene en inglés.
- [ ] Decidir alcance: ¿traducir también templates, hojas de ejercicios y
      exámenes, o solo los notebooks "rellenos" de teoría?

## 3. Recursión y funciones de orden superior (prioridad en HOF)

Contexto: en clase (ramas `MOS-25-26`, `VIC-25-26`, `origin/MOS-24-25`,
`origin/VIC-24-25` del repo `urjc-pd`) se seguía sistemáticamente el esquema de
**modularización por abstracción de patrones de diseño**: problema 1 → problema 2
(mismo "esqueleto") → abstracción (función de orden superior) → refactorización
de las soluciones anteriores en términos de la abstracción. Este esquema es
justo el que se pide luego en los exámenes.

Investigación ya hecha (comparando plantillas de clase vs. `master`):

- El nº de celdas *markdown* de `6.1 HigherOrderFunctions-template.ipynb` apenas
  cambia entre `master` y las ramas de clase (~70), pero el nº de celdas de
  *código* se dispara (66 en master → 143–185 en clase): el esquema se aplica en
  vivo con código, no se explica en prosa.
- Ejemplo real (sección `map`, rama `VIC-25-26`):
  ```scala
  // map example 1
  def toChar(l: List[Int]): List[Char] = ...
  // map example 2 (mismo esqueleto)
  def length(l: List[String]): List[Int] = ...
  // map genérico
  def map[A,B](l: List[A])(f: A=>B): List[B] = ...
  // refactorización
  def toChar(l: List[Int]): List[Char] = l.map(_.toChar)
  ```
  `master` va directo de la explicación conceptual a la definición abstracta de
  `map`, sin los dos problemas previos ni la celda de refactorización explícita.
- Mismo patrón de carencia (en menor medida) en las secciones **FoldRight**,
  **FoldLeft**, **Filtering** y **FlatMapping** de
  `PF-3/topic6/6.1 HigherOrderFunctions.ipynb`.
- En `PF-3/topic5/5.1 Recursion.ipynb` el gap es menor y de otra naturaleza: en
  clase se detalla más la derivación paso a paso de cada función, pero no sigue
  el mismo patrón problema1/problema2 — prioridad más baja, como intuía Juan
  Manuel.

Acciones:

- [ ] En `PF-3/topic6/6.1 HigherOrderFunctions.ipynb`, añadir en las secciones
      FoldRight, FoldLeft, `map`, Filtering y FlatMapping: un segundo problema
      concreto con el mismo esqueleto que el primero, y una celda de
      refactorización explícita tras cada abstracción (siguiendo el patrón
      `toChar`/`length` de las ramas de clase).
- [ ] Nombrar explícitamente el esquema ("problema 1 / problema 2 / abstracción /
      refactorización") una vez en la introducción del notebook, como método
      general que se repite en el resto del tema.
- [ ] Revisar si el template (`6.1 HigherOrderFunctions-template.ipynb`) necesita
      los mismos huecos añadidos como celdas vacías para rellenar en clase.
- [ ] Repasar `PF-3/topic5/5.1 Recursion.ipynb` con el mismo criterio, con menor
      prioridad.

## 4. Extender las hojas de ejercicios con material de exámenes

- [ ] Añadir a `PF-3/topic6/6.2 HigherOrderFunctions-exercises.ipynb` ejercicios
      adaptados de exámenes reales. Candidatos a revisar:
  - `exams/Examen25-26-Ordinaria-Móstoles.ipynb` / `Examen25-26-Ordinaria-Vicálvaro-Bis.ipynb`
    (apartados con foldRight/map/filter).
  - `exams/Examen20-21-Ordinaria.ipynb`, Ejercicio 4.
  - `exams/Examen22-23-Ordinaria-Vicálvaro-Especial.ipynb`, Ejercicio 3.
- [ ] Revisar el enunciado exacto de cada candidato antes de incorporarlo, para
      no duplicar ejercicios ya presentes en la hoja.
- [ ] Hacer lo mismo para `PF-3/topic5/5.2 Recursion-exercises.ipynb` si se
      encuentran ejercicios de examen de recursión aprovechables.
- [ ] Extender también otras hojas de ejercicios del curso (topics 3, 4, 7) con
      material de exámenes, si al revisar el 6.2/5.2 el enfoque funciona bien.

## 5. Presentación del primer día 26-27 — hecha; queda alinear el .docx

La presentación de bienvenida (Google Slides, exportada al repo como
[`PF-1/Intro.pdf`](PF-1/Intro.pdf)) ya está actualizada para el 26-27:

- [x] Copia de la presentación 25-26 en la carpeta del 26-27 y calendarios
      rehechos en las slides **12 (Vicálvaro)** y **13 (Móstoles)** (2026-09-08).
- [x] Exportada a PDF y sustituida en el repo (commit `768f97d`).
- [ ] Confirmar si la desaparición de la última slide (captura de Scala Days
      Madrid; el deck pasa de 20 a 19 páginas) fue intencionada. La versión
      anterior está en `a785f53`.

Calendario que quedó en las slides, que conviene tener escrito porque **no sale
tal cual del `.docx`** (no lectivos en ambos grupos: 30-9 apertura del curso y
12-10 Fiesta Nacional; examen de PF el L 26-10 en los dos):

- **Móstoles** — 12 sesiones, 24h: Scala 11-9; Funciones 14-9 y 18-9; ADT 21-9 y
  25-9; Curry-Howard 28-9 y 2-10; Recursión 5-10 y 9-10; HOF 16-10, 19-10 y
  23-10.
- **Vicálvaro** — 10 sesiones, 20h: Scala+Funciones juntas el 14-9 (`S/F`);
  Funciones 16-9; ADT 21-9 y 28-9; Curry-Howard 23-9 y 5-10; Recursión 7-10 y
  14-10; HOF 19-10 y 21-10.
- Las 4h menos de Vicálvaro se absorbieron **fusionando Scala con Funciones en
  la primera sesión**, para que Curry-Howard conserve sus dos sesiones (que es
  lo que interesa de cara al punto 1).

### Correcciones pendientes en `PlanificacionPD-26-27.docx`

El documento de planificación (OneDrive URJC, `Asignaturas/26-27/PD-GII/`) sigue
arrastrando cuatro errores, detectados al contrastarlo con el
[calendario académico oficial](https://www.urjc.es/images/EstudiarURJC/Admision_matricula/archivos/calendario_academico_26_27.pdf)
y con el calendario real de 2026. Las slides ya están bien, pero el `.docx` es
el que se usa para coordinar con el resto del profesorado:

- [ ] **No recoge que el X 30-9 no es lectivo** (apertura del curso académico).
      Es sesión de Vicálvaro —la línea `V-X: Curry-Howard` de la semana 4—, así
      que esa semana son 2h en VIC, no 4h. Móstoles no se ve afectado (sus
      sesiones son L y V).
- [ ] **Semana 6, línea `M-L: HOF`**: el L 12-10 es Fiesta Nacional, Móstoles no
      tiene clase. Sobra esa línea: con ella salen 13 sesiones de PF (26h),
      mientras que la cabecera de la semana ("2h") y el total (6 semanas de 2h)
      exigen 12 (24h).
- [ ] **Total y reparto de Vicálvaro**: son **48h**, no 50h (1·0h + 6·2h + 9·4h;
      semanas de 2h: 4, 6, 9, 10, 14 y 16), repartidas en **20h PF + 2h examen +
      26h PL**, no "24h PF + 2h examen + 24h PL".
- [ ] **`Práctica PL nº 3 (10a sesión): L 7-12`**, en los dos grupos: el 7-12 es
      festivo, como dice la propia cabecera de la semana 14. Contando bien, la
      10ª sesión de PL es el **V 11-12 en Móstoles** y el **X 9-12 en
      Vicálvaro**.
- [ ] Menores: el 2-11 y el 7-12 están etiquetados como "Fiesta Nacional" (son
      los traslados de Todos los Santos y del Día de la Constitución; solo el
      12-10 es Fiesta Nacional); el paréntesis de la semana 1 ("12/9 fiesta
      Móstoles cae en sábado") no explica las 0h de VIC —la razón es que las
      clases empiezan el 10-9—; y en HORARIOS hay una errata:
      "VIC L L(09:00 - 11:00)".
