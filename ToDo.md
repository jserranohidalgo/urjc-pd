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
El repo ya lista este curso (`urjc-pd`) en su tabla "Where it is used", pero de
momento no hay ninguna referencia al juego dentro de `urjc-pd`/`urjc-pd-private`.

- [ ] Enlazar el juego desde el material del curso: README principal y
      `PF-2/topic4/4.1 CurryHoward.ipynb` (y su template), con una celda que
      explique qué es y enlace a jugarlo.
- [ ] Decidir si las dos charlas del juego sustituyen, complementan o solo se
      enlazan desde la explicación actual de la correspondencia de Curry-Howard
      en el notebook.
- [ ] Valorar si se anima a los alumnos a instalar/usar el plugin de Claude Code
      como apoyo (requiere Python 3).
- [ ] Revisar si el ejemplo "worked example" de la charla del juego coincide o
      complementa el ejemplo que ya se usa en el notebook, para no duplicar ni
      contradecir la explicación.

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
