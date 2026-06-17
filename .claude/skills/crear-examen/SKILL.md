---
name: crear-examen
description: Crea un nuevo examen de Programación Funcional (URJC) en formato Jupyter notebook, siguiendo las plantillas de exámenes anteriores. Úsalo cuando el usuario pida crear/preparar/diseñar un examen para una convocatoria (ordinaria, extraordinaria, prueba) de un curso. Genera tanto la versión con soluciones como la versión "Enunciado" para los alumnos, respetando el preámbulo, los tipos de ejercicio y la duración habituales, y evitando repetir ejercicios de exámenes previos y hojas de ejercicios.
---

# Crear un examen de Programación Funcional

Genera un examen nuevo en Jupyter notebook (kernel Scala/Almond) coherente con los
exámenes anteriores del curso, en `exams/`, usando como material de apoyo las propuestas
de `others/`.

## 1. Recoger los datos del examen

Antes de empezar, fija (pregunta al usuario solo lo que falte):

- **Curso**: p.ej. `25-26`.
- **Convocatoria**: `ordinaria`, `extraordinaria`, o `prueba`.
- **Campus** (opcional): `Móstoles`, `Vicálvaro`, o ambos. Las extraordinarias suelen ser
  comunes (sin campus en el nombre); las ordinarias a veces se desdoblan por campus.
- **Fecha** del examen.
- **Duración**: por defecto la habitual de la convocatoria (ver §4).

## 2. Convención de nombres y ubicación

Los ficheros van en `exams/`. Dos notebooks por examen:

- **Solución** (con respuestas): `Examen<curso>-<Convocatoria>[-<Campus>].ipynb`
  p.ej. `Examen25-26-Extraordinaria.ipynb`, `Examen25-26-Ordinaria-Vicálvaro.ipynb`.
- **Enunciado** (para alumnos, sin respuestas): el mismo nombre + `-Enunciado`
  p.ej. `Examen25-26-Extraordinaria-Enunciado.ipynb`.

Si hay variantes A/B, se añade un sufijo tipo `-Bis` (ver `Examen25-26-Ordinaria-Vicálvaro-Bis.ipynb`).

## 3. Material de referencia

- **Plantillas (tipo de ejercicio y duración)**: los `Examen*.ipynb` de `exams/`. Para una
  extraordinaria, mira sobre todo las extraordinarias previas
  (`Examen24-25-Extraordinaria.ipynb`, `Examen23-24-Extraordinaria.ipynb`, etc.).
- **Propuestas / ideas de ejercicios**: notebooks de `others/` (`Ejercicios.ipynb`,
  `ExercisesADTs.ipynb`, `ExercisesCurryHoward.ipynb`, `DoubleNegation.ipynb`,
  `expressions.ipynb`, `cps.ipynb`, `pascaltriangle.ipynb`, `wordle.ipynb`, ...).
  En particular, `DoubleNegation.ipynb` contiene un buen surtido de tautologías de la
  lógica **clásica** (Łukasiewicz, Clavius/`(¬p→p)→p`, contrapositiva inversa,
  `(p→q)∨(q→p)`, De Morgan, LEM débil...) de las que sacar el apartado de Curry-Howard
  clásico; sus demostraciones se reescriben fácilmente con los traits `ExcludedMiddle` o
  `DoubleNegation` del preámbulo.

> **NO repetir ejercicios — compara por SIGNATURA, no por nombre.** El nombre de la
> función es lo de menos: dos ejercicios son el mismo si comparten la *signatura* (tipos de
> entrada y salida) y el patrón de implementación, aunque se llamen distinto. Ejemplo real:
> `unzip` con signatura `List[(A, B)] => (List[A], List[B])` (recursión / `foldRight` /
> `foldLeft`) **ya estaba** en el examen 20-21 extraordinaria con el nombre `split`. Para
> Curry-Howard, compara la *tautología* (la signatura del `proof`), no el enunciado en
> prosa. Forma fiable de comprobarlo: extraer todas las signaturas `def …: … =` de
> `exams/*.ipynb` (y las hojas de `others/`) y verificar que la signatura candidata no
> coincide con ninguna. Reutiliza el *patrón* (recursión, fold, isomorfismo...), nunca la
> signatura concreta. Las hojas de ejercicios son material ya trabajado por los alumnos.

## 4. Estructura, puntuación y duración por convocatoria

- **Extraordinaria**: más corta, **1h:20m**. Típicamente **4 ejercicios**.
- **Ordinaria**: más larga (~2h o más), normalmente 4 ejercicios con más apartados.

> **La puntuación total SIEMPRE debe sumar 10.** Comprueba la suma antes de dar el examen
> por terminado (suma las cabeceras `# Ejercicio N __(X puntos)__`, y por separado la suma
> de los apartados de cada ejercicio; ambas deben dar 10). El criterio por defecto es
> **1 punto por apartado**: con ese reparto, el número total de apartados debe ser 10. Si al
> añadir/quitar apartados la suma se queda en 9 (o 11), reequilibra — por ejemplo,
> desdoblando un ejercicio en dos apartados (un isomorfismo se presta a `a)` justificación
> con aritmética de tipos + `b)` instanciación de `Isomorphic`, 1 punto cada uno) o
> fusionando apartados. Un reparto típico de extraordinaria que suma 10 con 1 punto por
> apartado: Ej1 Curry-Howard `a+b` (2), Ej2 isomorfismo `a+b` (2), Ej3 recursión/HOF
> `a+b+c` (3), Ej4 patrón iterativo/HOF `a+b+c` (3).

Patrón habitual de tipos de ejercicio (mezclar, no hace falta usar todos; para una
extraordinaria elige ~4 que cubran variedad):

1. **Curry-Howard**: demostrar tautologías de lógica proposicional implementando una
   función con la signatura correspondiente. Suele incluir un apartado intuicionista y otro
   clásico (usando `ExcludedMiddle`/`DoubleNegation` del preámbulo).
2. **Isomorfismos / ADTs**: demostrar que dos tipos son isomorfos instanciando el trait
   `Isomorphic`, y/o justificar la equivalencia con aritmética de tipos (sumas/productos).
3. **Recursión**: implementar una función mediante recursión **no final** y mediante
   recursión **final (de cola)**.
4. **Funciones de orden superior (uso)**: reimplementar la misma función con `foldRight`,
   `foldLeft`, `map`, `flatMap`, `filter`, etc.
5. **Diseño de nuevas HOFs**: abstraer un patrón repetido en una función de orden superior
   nueva y reimplementar casos concretos con ella.
6. **Patrón iterativo**: `iterative_tailrecursion` / `iterative_foldLeft` (ver preámbulo).

Combina recursión + reimplementación con HOFs + (Curry-Howard | isomorfismo) para cubrir
los objetivos del curso.

## 5. Preámbulo

El examen **siempre lleva un preámbulo** con signaturas, traits y tablas auxiliares: el
objetivo del examen NO es memorizar. Copia el preámbulo del examen más reciente de la
misma convocatoria/curso y adáptalo a lo que necesiten tus ejercicios. Contiene:

- Celda de título (curso, convocatoria, fecha, campus, duración).
- `import $ivy.\`org.scalatest::scalatest:3.2.16\`` + imports de `org.scalatest`.
- `object Signatures` con la `abstract class List[A]` (HOFs y funciones comunes). Añade a la
  signatura solo los métodos de biblioteca que use el examen (p.ej. `appended`, `sliding`,
  `reduce`, `splitAt`...), con un comentario explicando cada uno.
- Plantillas de los patrones de diseño que use el examen (incluye solo las necesarias):
  recursión general `divideAndConquer` (con la solución del resto en `val tailSol: B = …`),
  recursión final `iterative_tailrecursion`, y/o `iterative_foldLeft`. No hace falta dejar
  plantillas para `foldRight`/`foldLeft` si los apartados ya piden esas HOFs directamente.
- Si el examen usa árboles u otro ADT, incluir su `enum`/definición y el `object` con
  constructoras (`void`, `leaf`, `node`, ...) — como en `Examen25-26-Ordinaria-Vicálvaro.ipynb`.
- Sección Curry-Howard / ADTs: trait `Isomorphic[A, B]` (con `from`, `to`, `law1`, `law2`),
  `type Not[P] = P => Nothing`, `type <=>[P, Q]`, y los traits `ExcludedMiddle` y
  `DoubleNegation`. Las imágenes con tablas de constructoras/destructoras se referencian con
  `attachment:` (se reutilizan los mismos attachments del notebook plantilla; cópialos).

La forma más fiable de construir el preámbulo es **partir de una copia del notebook
plantilla** (mismos attachments de imágenes) y editar a partir de ahí.

## 6. Formato de cada ejercicio

Reproduce el estilo de los exámenes recientes:

- Cabecera del ejercicio: `# Ejercicio N (X puntos)` (o `# Ejercicio N` + línea
  `__(X puntos)__`).
- Apartados: `#### a) (Y puntos)` seguido del enunciado en markdown.
- Para ejercicios de implementación, incluir una clase de test `TestX(impl: ...) extends
  AnyFlatSpec with should.Matchers` con casos representativos, y una celda final
  `run(TestX(impl))` que ejecuta los tests (`run` lo provee el entorno del curso).
- Para Curry-Howard, enunciar la tautología en LaTeX (`##### $\vdash ...$`) y dar la
  signatura `def proof[...]: ... = ` a completar.
- Para isomorfismos, dar la cabecera `class Iso[...] extends Isomorphic[Tipo1, Tipo2]:` a
  completar. Si se pide la justificación con aritmética de tipos, la respuesta del alumno es
  una **celda markdown** con la cadena de igualdades `|T1| = … = |T2|` (en el enunciado el
  hueco es una celda markdown con `// ESCRIBE TU RESPUESTA`).

### Convenciones de redacción de los enunciados

- **Enuncia siempre en términos de la función, no de la plantilla ni de pasos previos.**
  Escribe «Implementa la función `f` mediante `foldLeft`», NO «implementa el algoritmo
  iterativo anterior...» ni «de acuerdo con la plantilla `iterative_foldLeft` del
  preámbulo». El patrón de diseño está implícito en la HOF que se pide usar.
- **Pistas:** márcalas explícitamente, p.ej. `_Pista:_ un posible algoritmo para implementar
  la función ... consiste en ...`.
- **Funciones de uso obligatorio:** cuando un apartado exija implementar la solución con un
  conjunto concreto de funciones, dilo de forma inequívoca y en negrita, y prohíbe las
  alternativas. P.ej.: «__Es obligatorio__ implementar la función combinando exclusivamente
  las funciones `reverse`, `zipWithIndex`, `map`, `pow` y `sum`, sin recurrir a la
  recursividad ni a `foldLeft`/`foldRight`.» Si esas funciones no están ya en el preámbulo
  (`Signatures` o como `def` auxiliar, p.ej. `pow`), **añádelas**.
- **Coherencia de nombres con las plantillas:** al implementar por recursión general, nombra
  la solución del resto como `tailSol` (coherente con la plantilla `divideAndConquer`), tanto
  en la recursión como en el `foldRight`.

## 7. Generar las dos versiones

1. **Solución**: ejercicios con la implementación correcta rellenada. Verifica
   mentalmente (o ejecutando, ver §8) que cada solución pasa sus tests / typechecks.
2. **Enunciado**: copia de la solución donde cada celda de respuesta del alumno se sustituye
   por un placeholder, respetando el comentario habitual:
   - `// IMPLEMENTA TU RESPUESTA` (implementaciones de funciones/HOFs),
   - `// ESCRIBE TU RESPUESTA` (Curry-Howard / isomorfismos / código en general),
   - para respuestas en prosa (p.ej. la justificación con aritmética de tipos), el hueco es
     una **celda markdown** con `// ESCRIBE TU RESPUESTA`.
   Se sustituye la celda de respuesta **completa** (incluida la signatura del `proof`/`Iso`),
   dejando intactas las celdas de enunciado, tests y `run(...)`.

   El número de celdas del Enunciado es el mismo que el de la solución salvo las celdas de
   respuesta; compara con un par solución/Enunciado existente para no desalinear.

## 8. Construcción del notebook (.ipynb) y verificación

- Los `.ipynb` son JSON. Constrúyelos/edítalos por programa (Python con `json`) o con la
  herramienta de notebooks, **no a mano**, para no corromper el JSON. Conserva
  `metadata`/`kernelspec` (Scala/Almond) copiándolos del notebook plantilla.
- Reutiliza la sección `attachments` del notebook plantilla para las imágenes del preámbulo.
- **Verificación (recomendada)**: si hay un kernel Scala/Almond disponible, ejecuta la
  versión solución para confirmar que todos los `run(TestX(...))` pasan y que las
  demostraciones Curry-Howard typechecan. Si no es posible ejecutar, revisa cuidadosamente
  tipos y casos de test a mano y dilo explícitamente al usuario.

## 9. Calificación (después del examen)

La corrección, el CSV de calificaciones y el feedback en los notebooks de los alumnos se
rigen por las instrucciones de `CLAUDE.md` y las rúbricas `others/rubrica-*.md`. Esto queda
fuera del alcance de crear el examen, pero al diseñar los apartados conviene que sean
fácilmente puntuables por apartado (`1a`, `1b`, ...).
