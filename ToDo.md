# ToDo — Actualización de material del curso

Tareas pendientes sobre el material de la asignatura (repo público `urjc-pd`, con
copia/trabajo en este repo privado). Creado el 2026-09-07.

---

## 1. Curry-Howard: actualizar con el nuevo juego — HECHO (2026-09-10)

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

- [x] Enlazar el juego desde el README de este repo privado (2026-09-10): el
      título de Topic 4 es un hiperenlace al repo del juego, y hay una sección
      nueva "The Curry-Howard Game" con el enlace para jugar, las dos charlas y
      tres objetivos para empezar.
      Nota: la versión anterior de este punto decía que estaba hecho en el repo
      público `urjc-pd`, en una rama `jserrano-master` sin commitear. **Esa rama
      no existe**: no está en el clone de `~/Documents/urjc-pd` (ni en su reflog,
      así que nunca estuvo), ni en GitHub, ni en `urjc-pd-20-21`; y ninguna ref de
      ese repo menciona `curry-howard-game` en ningún fichero. La sección se ha
      escrito aquí desde cero.
- [x] Llevado al público `urjc-pd` (2026-09-10, commit `d79cbf1` allí): el
      notebook rehecho y su template, el README, `PF-1/Intro.pdf` del 26-27, los
      dos notebooks de HOF, `7.2 Data models` y los dos gifs. De paso desaparecen
      las __10 rutas de imagen rotas__ que el público arrastraba. Verificado en
      GitHub: gifs subidos, sección del README publicada y ninguna imagen roto.
- [ ] Aparcadas, sin bloquear nada: si se anima a los alumnos a instalar el plugin
      de Claude Code como tutor (requiere Python 3), y si el template del 4.1
      necesita más huecos en la secuencia de los cuatro pasos.

### Cómo quedó `PF-2/topic4/4.1 CurryHoward.ipynb` (rehecho, 2026-09-08/10)

La comparación con la charla del juego *"What is the Curry–Howard correspondence?"*
(documentada en `curry-howard-game/spec/help.md`) identificó cuatro huecos —el
momento eureka, el "giro de moneda", la secuencia agujero a agujero y el cierre
con invitación a jugar—, y al aplicarlos se acabó reestructurando el notebook
entero. El resultado, para no tener que releer el diff:

Notebook y template van a la par, de 81 a __82 celdas__ (se anadio bastante y se
quito mas). El orden nuevo:

1. Titulo, fotos y el momento eureka (lo que vio Curry en 1934, lo que vio Howard
   en 1969).
2. Introduccion reescrita como __resumen de lo que vieron ambos__: los dos
   slogans, y la tabla que extiende la correspondencia del tema anterior (tipo /
   aritmetica / logica), que es lo que hace innecesaria la seccion "A refresher:
   arithmetic and types", eliminada (y con ella el `Preamble` y el
   `trait Isomorphic`, que solo la servian). Termina con la pregunta del tutorial
   del juego —¿en que sentido son *exactamente* lo mismo?— y los dos gifs de la
   moneda (`images/icon-lambda-to-turnstile.gif` y `icon-turnstile-to-lambda.gif`,
   de `doc/icon/export/gif` del repo del juego; se eligieron los de una direccion
   porque estan horneados sobre blanco, mientras el compuesto lo esta sobre el
   `#f7f7f8` de la slide).
3. `# Now play it`, al principio: se juega antes de la teoria.
4. `# How proofs are made` — la deduccion natural con su tabla de reglas, y __el
   ejemplo__ ($p \wedge (q \vee r) \rightarrow \ldots$) con su prueba escrita en la
   __vista de lineas del juego__ (estilo Fitch: numeracion corrida, barras de
   subprueba, `hyp¹`/`prem`, citas de tramos con guion), en lugar de la numeracion
   `1 / 1.1 / 1.3.1` que habia. El formato se saco de
   `engine/.../nj/Textual.scala` y los nombres de regla (`∧E₁`, `∨I₂`, `∨E²³`) de
   `ToFigure.scala`. Los comentarios de `step2`/`step3` y de la vista combinada se
   renumeraron a esas lineas.
5. `# How programs are made` — la __tabla de reglas de type-driven development__
   traida de `3.4 Isomorphisms.ipynb` (celda 21, con su attachment) en lugar de
   las dos figuras al estilo Gentzen que habia; y el mismo ejemplo en programa,
   con una tabla de su estructura en operaciones (lambda, `case` sobre el par,
   `match`, `var`, construccion del par, `Left`/`Right`), en paralelo a la columna
   de reglas de la prueba.
6. `# Propositions as types` — arranca con "ya tenemos una prueba, ya tenemos un
   programa, ¿en que sentido son lo mismo?" y responde con el diccionario. La
   tabla de type-driven development que se repetia aqui esta fuera (era la misma
   imagen que la de la seccion 5): en su lugar, el texto recorre la
   correspondencia regla a regla contra las dos tablas ya vistas. Cierra el
   callout de la moneda.
7. `# Proofs as programs, step by step` — encuadrada como __el uso__ de la
   correspondencia: si las pruebas son programas, para probar una tautologia se
   traduce la proposicion a un tipo, se desarrolla el programa (type-driven
   development, con agujeros) y se lee el resultado como prueba. Lleva la figura
   del cruce (proposicion/tipo arriba, prueba/programa abajo, con flechas de doble
   punta) y el "si y solo si" que lo legitima. Luego `step0`..`step3` y la vista
   combinada, dibujada como la vista __Both / line for line__ del juego: el
   programa a la izquierda con los nombres `s1..s9` (`s4` es el valor de la linea
   4) y, en la columna del comentario, la linea de prueba que cada linea escribe.
   Se sigue la notacion del juego tambien en las formulas, sin parentesis
   redundantes (`p ∧ q ∨ p ∧ r`).
8. `# More examples` — cada ejemplo se lee __tres veces__: el programa
   idiomatico, tal como se escribiria en Scala; la prueba sola, en notacion
   lineal; y el mismo programa __refactorizado__ para que la correspondencia se
   vea sola, una linea de programa por linea de prueba con su regla al lado. La
   entrada de la seccion explica que el refactor no es otro programa, sino el
   mismo termino con cada paso nombrado: es justo lo que el Scala idiomatico
   comprime (`case (f, x)` hace dos eliminaciones de golpe) y lo que un sistema
   de pruebas, sin abreviaturas, tiene que desplegar. Las cuatro pruebas se
   verificaron contra su termino: `x._1(x._2)`, `f(a)` bajo `Left`,
   `a1(a)(a2(a))` y `nq(ifpq(p))`.
   Tambien las dos figuras del momento eureka pasaron a bloque monoespaciado: la
   de Howard en vista de lineas, y la derivacion de Curry (estilo Hilbert, sin
   subpruebas ni `hyp`) conservando su columna de terminos.
9. `# The intuitionistic stance` — el ejemplo que no es teorema intuicionista
   aunque si clasico, con __el espacio de busqueda completo__: el arbol de las
   cuatro jugadas posibles tras el lambda forzado, las dos ramas escritas en
   codigo hasta donde llegan, y por que las cuatro mueren. La conclusion es por
   agotamiento, no por falta de imaginacion.
10. `# Proving classical theorems, by assuming them` — `ExcludedMiddle` y
    `DoubleNegation` como premisas.
11. `# Conclusion`.

__Fuera la notacion logica en Scala__ (`type ⟶[A,B] = A => B`, `∧`, `∨`, `¬`,
`⟷`, `Ax`, `⊥`, `Absurd`/`Or`/`And`) y las reimplementaciones que la usaban: solo
anadia ruido. Se conservan `Not` y `<=>`, que son ASCII y los usan los ejemplos.
Los simbolos logicos siguen, por supuesto, en las figuras de deduccion natural.

Un fallo que se colo al quitar los alias y se detecto al convertir los ejemplos:
el programa del cuarto ejemplo usaba `Absurd`, que era uno de los alias
eliminados; ahora usa `Nothing`.

Comprobado tras cada pasada: las celdas de codigo nuevas compilan con Scala 3
(`scalac` sobre JDK 8; con el JDK del sistema, Scala 3.0.0 no arranca), y
`S (K g) f` se verifico en ejecucion que es la composicion; ninguna celda usa
nada definido mas abajo; los attachments y todas las rutas de imagen resuelven.
De paso, corregidas rutas roscadas que ya venian de antes:
`../images/natdedrules.png` en los dos ficheros y las dos fotos de la celda 3 del
template, que apuntaban a `PF-2/images/`, inexistente.

- [x] `4.2 CurryHoward-Exercises.ipynb`: se trajo del público el arreglo del
      ejercicio 3 (commit `0b492b5`), que aquí faltaba desde 2024 — la solución
      prueba ahora la equivalencia en las dos direcciones. Por lo demás no
      necesitaba cambios:
      comprobado que es autocontenido (tiene su propio `Preamble` con `Not`,
      `ExcludedMiddle` y `DoubleNegation`) y no menciona ninguna seccion de 4.1.

## 2. Traducción al español — EN CURSO (19 de 38 notebooks)

La versión inglesa quedó cerrada y publicada el 2026-09-10 (`d79cbf1` en el
público, `0b492b5` aquí): ese es el punto de partida de la traducción.

__Cómo continuar: [`.es/README.md`](.es/README.md)__, que lleva el estado, los
pendientes con su volumen, el procedimiento y los invariantes. En resumen:

- La rama __`es`__ (en este repo, ya pusheada) es la traducción. Es __huérfana__ a
  propósito: si descendiera de `master`, subirla al público publicaría `others/`
  con las entregas de los alumnos. __No se fusiona nunca__ en ninguna dirección;
  se regenera.
- La tubería está en `.es/apply_es.py`, con los módulos de traducción en `.es/t/`.
  Traduce en memoria, valida y solo entonces escribe el commit en `es`.
- `.es/manifest.json` (en la rama `es`) guarda de qué blob de `master` salió cada
  fichero, así que "qué hay que retraducir" es un dato calculado.
- El glosario está en `.es/glosario.md` (en la rama `es`). Decidido: _hole_ →
  __hueco__; _pattern matching_ sin traducir; `foldRight`/`map`/`filter`/`flatMap`
  tampoco, por ser nombres de función.

- [x] Hecho: todo `PF-1/topic2` (2.1 a 2.5 con sus templates), el README en
      español, y de `topic3` la intro, los ejercicios de 3.1, `3.2 Products`,
      `3.3 Sums` y `3.4 Isomorphisms` con template y ejercicios.
- [ ] Pendientes: `3.1 Functions` (el mayor, 3119 palabras), todo `topic4`,
      `topic5`, `topic6` y `topic7`. La lista con volúmenes, en `.es/README.md`.
- [ ] La rama `es` __no se ha subido al repo público__ todavía, y no debería
      hasta que la traducción esté completa o al menos coherente por temas.
- [ ] Fuera de alcance por ahora: el texto incrustado en las figuras
      `images/*.svg`, que habría que redibujar.

- [ ] Traducir el material del curso (notebooks de `PF-1`, `PF-2`, `PF-3`) al
      español.
- [ ] Dejar la traducción en una rama nueva (p.ej. `es` o `traduccion-es`) sin
      mezclarla con `master`, que se mantiene en inglés.
- [ ] Decidir alcance: ¿traducir también templates, hojas de ejercicios y
      exámenes, o solo los notebooks "rellenos" de teoría?

## 3. Recursión y funciones de orden superior — HOF HECHO (2026-09-10)

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

- [x] Sección `map` de `PF-3/topic6/6.1 HigherOrderFunctions.ipynb` (2026-09-10):
      añadidos `toChar` (problema 1) y `length` (problema 2) con el mismo
      esqueleto, tomados de las ramas de clase; una celda que nombra lo que
      comparten antes de la abstracción; y la celda de refactorización, donde los
      dos problemas quedan en una línea vía `map`. La definición genérica lleva
      ahora el comentario `// map generically`, para que la correspondencia con el
      template sea exacta. Verificado que las cuatro celdas compilan con Scala 3 y
      que hacen lo que dicen (`toChar(List(98,99,100)) == List('b','c','d')`,
      `length(List("abc","hola","")) == List(3,4,0)`, igual antes y después de
      refactorizar).
- [x] Esquema nombrado explícitamente (problema 1 / problema 2 / abstracción /
      refactorización) en una celda nueva tras la introducción, que además remite a
      la sección __Functions as modularity devices__ de `PF-2/topic3/3.1
      Functions.ipynb` —el mismo método un nivel de abstracción más abajo— y
      señala la diferencia: allí lo que se repetía se abstraía en una función
      normal; aquí lo que cambia entre los dos problemas es una operación, así que
      el parámetro es una función y la abstracción, de orden superior.
- [x] El template no necesitaba huecos nuevos para `map`: **ya los tenía**
      (`// map example 1`, `// map example 2`, `// map generically`). Solo se le
      añadió el hueco de la refactorización.
- [x] `Filtering` y `FlatMapping` con el mismo esquema (2026-09-10). A Filtering,
      que no tenía ningún problema concreto, se le añaden dos —`evens` sobre
      `List[Int]` y `nonEmpty` sobre `List[String]`, en el estilo de guardas que ya
      usa `filterR`, de modo que la abstracción es literalmente esas dos con la
      guarda sustituida por `predicate(head)`— y la refactorización. A FlatMapping,
      que ya tenía uno (`words`), se le añade el segundo (`chars`: de una lista de
      palabras a la lista de sus caracteres, misma forma y distinta expansión) y su
      refactorización, con lo que el "esta combinación es tan común que tiene
      nombre" llega apoyado en dos casos y no en uno.
      Verificado en ejecución: `evens(List(1,2,3,4)) == List(2,4)`,
      `nonEmpty(List("a","","b")) == List("a","b")` y
      `chars(List("ab","c")) == List('a','b','c')`, iguales antes y después de
      refactorizar.
- [x] __Corrección del diagnóstico anterior__: `FoldRight` y `FoldLeft` __ya
      seguían el esquema completo__ (`sum`/`multiply` → `combine` → refactor;
      `length`/`reverse` → `foldLeft` → refactor), así que no se han tocado. Y en
      las dos ramas de clase (`MOS-25-26`, `VIC-25-26`) los marcadores
      `example 1`/`example 2`/`generically` aparecían __solo__ en `map`.
__Nota__ para futuras validaciones: este notebook usa sintaxis __fewer-braces__
      (`xs.flatMap: x =>`, `xs.foldRight(z):`), que necesita Scala 3.3 — la versión
      del curso. El `scalac` local es 3.0.0 y rechaza esas celdas, incluidas las que
      ya estaban; para comprobarlas hay que usar el kernel del curso o instalar 3.3.
- [x] Rutas de imagen corregidas en todo el repo (2026-09-10): eran __18
      referencias en 10 ficheros__, todas apuntando un nivel por debajo de donde
      están las imágenes (`../images/` en vez de `../../images/`). Afectaba a
      `3.1 Functions`, `3.3 Sums`, `3.4 Isomorphisms`, `6.1 HigherOrderFunctions`
      y `7.2 Data models`, cada uno con su template. Verificado que ya no queda
      ninguna referencia de imagen roto en el repo.
- [ ] Aparcado: repasar `PF-3/topic5/5.1 Recursion.ipynb`. Allí el hueco es de otra
      naturaleza —en clase detallas más la derivación paso a paso, pero no sigues
      problema1/problema2—, así que es otro tipo de trabajo.

## 4. Extender las hojas de ejercicios con material de exámenes — APLAZADO

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
