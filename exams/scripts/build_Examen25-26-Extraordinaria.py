import json, copy, base64

DIAGRAM_PNG = '/tmp/frombits-pipeline.png'
DIAGRAM_NAME = 'frombits-pipeline.png'

TPL = 'exams/Examen24-25-Extraordinaria.ipynb'
SOL = 'exams/Examen25-26-Extraordinaria.ipynb'
ENU = 'exams/Examen25-26-Extraordinaria-Enunciado.ipynb'

tpl = json.load(open(TPL))

def lines(text):
    # nbformat: list of strings, each ending with \n except the last
    parts = text.split('\n')
    return [p + '\n' for p in parts[:-1]] + [parts[-1]]

def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": lines(text)}

def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": lines(text)}

def img(name, png_path, width):
    b64 = base64.b64encode(open(png_path, 'rb').read()).decode('ascii')
    cell = md('<img src="attachment:%s" width="%d">' % (name, width))
    cell["attachments"] = {name: {"image/png": b64}}
    return cell

# ---- Preamble (cells 0..13 from template) ----
pre = [copy.deepcopy(c) for c in tpl['cells'][0:14]]

# New title (cell 0)
pre[0] = md(
"""# Programación declarativa @ URJC
# Programación funcional
## Curso 25-26, convocatoria extraordinaria (junio de 2026)
## Campus de Móstoles/Vicálvaro

La duración del examen es de 1h:20m.""")

# Clean general Signatures (cell 4)
pre[4] = code(
"""object Signatures:
    abstract class List[A]:

        // Common HOFs
        def foldRight[B](nil: B)(cons: (A, B) => B): B
        def foldLeft[B](initial: B)(update: (B, A) => B): B
        def map[B](f: A => B): List[B]
        def flatMap[B](f: A => List[B]): List[B]
        def filter(f: A => Boolean): List[A]
        def forall(pred: A => Boolean): Boolean
        def exists(pred: A => Boolean): Boolean

        // Common functions
        def length: Int
        def reverse: List[A]
        def drop(i: Int): List[A]
        def appended(e: A): List[A]

        // Empareja cada elemento con su índice (empezando en 0)
        def zipWithIndex: List[(A, Int)]

        // Suma los elementos de una lista numérica
        def sum: A""")

# Plantillas de patrones de diseño: recursión general y recursión final.
# Se reemplaza cell 6 (iterative_foldLeft) y se reordena para dejar
# divideAndConquer (5) antes de iterative_tailrecursion (6).
itr = pre[5]  # iterative_tailrecursion (se conserva)
pre[5] = code(
"""def divideAndConquer[A, B](l: List[A]): B =
    l match
        case Nil => ???
        case head :: tail =>
            val tailSol: B = divideAndConquer(tail)
            ???(head, tailSol)""")
pre[6] = itr

# Función auxiliar `pow` (potencia de enteros), usada en el Ejercicio 4.
pre.insert(5, code(
"""// Potencia de enteros: pow(base, exp) = base elevado a exp
def pow(base: Int, exp: Int): Int =
    math.pow(base, exp).toInt"""))

# ---- Exercises (solution cells) ----
PH_W = "// ESCRIBE TU RESPUESTA\n\n"
PH_I = "// IMPLEMENTA TU RESPUESTA\n\n"

# A cell is (kind, content, role) where role: 'keep' | 'answer-w' | 'answer-i'
ex = []

# Ejercicio 1
ex.append(('md', "# Ejercicio 1\n__(2 puntos)__", 'keep'))
ex.append(('md', "__a) (1 punto)__ Utiliza la correspondencia de Curry-Howard para demostrar la siguiente tautología de la lógica proposicional intuicionista:", 'keep'))
ex.append(('md', r"##### $\vdash (p \vee q \rightarrow r) \rightarrow (r \rightarrow s) \rightarrow (p \rightarrow s) \wedge (q \rightarrow s)$", 'keep'))
ex.append(('code',
"""def proof[P, Q, R, S]: (Either[P, Q] => R) => (R => S) => (P => S, Q => S) =
    f => g =>
        (p => g(f(Left(p))), q => g(f(Right(q))))""", 'answer-w'))
ex.append(('md', "__b) (1 punto)__ Se desea utilizar la correspondencia de Curry-Howard para demostrar la validez de la siguiente tautología de la lógica clásica proposicional:", 'keep'))
ex.append(('md', r"##### $\vdash (p \rightarrow q) \vee (q \rightarrow p)$", 'keep'))
ex.append(('md', "Para ello, utiliza como premisa adicional la ley del tercio excluso aplicada a la proposición $q$.", 'keep'))
ex.append(('code',
"""def proof[P, Q](lem: ExcludedMiddle): Either[P => Q, Q => P] =
    lem[Q] match
        case Left(q) => Left(_ => q)
        case Right(nq) => Right(nq)""", 'answer-w'))

# Ejercicio 2
ex.append(('md', "# Ejercicio 2\n__(2 puntos)__", 'keep'))
ex.append(('md', "Demuestra que, para cualesquiera tipos `A` y `B`, los tipos de datos `Option[A] => B` y `(B, A => B)` son isomorfos, de las dos formas siguientes:", 'keep'))
ex.append(('md', "__a) (0,5 puntos)__ Utilizando la equivalencia entre tipos algebraicos de datos y las operaciones aritméticas.", 'keep'))
ex.append(('md',
"""|Option[A] => B| =

|B| ^ |Option[A]| =

|B| ^ (1 + |A|) =

|B| ^ 1 * |B| ^ |A| =

|B| * |B| ^ |A| =

|B| * |A => B| =

|(B, A => B)|""", 'answer-md'))
ex.append(('md', "__b) (1,5 puntos)__ Implementando una biyección entre ambos tipos de datos mediante una instanciación del trait `Isomorphic`.", 'keep'))
ex.append(('code',
"""class Iso[A, B] extends Isomorphic[Option[A] => B, (B, A => B)]:

    def from(f: Option[A] => B): (B, A => B) =
        (f(None), a => f(Some(a)))

    def to(p: (B, A => B)): Option[A] => B =
        case None => p._1
        case Some(a) => p._2(a)""", 'answer-w'))

# Ejercicio 3
ex.append(('md', "# Ejercicio 3\n__(3 puntos)__", 'keep'))
ex.append(('md', "Se desea implementar la función de orden superior `collect`, que recibe una función `f: A => Option[B]` y una lista de elementos de tipo `A`, y devuelve la lista de los valores `b` para los que `f` devuelve `Some(b)`, descartando los elementos en los que `f` devuelve `None` y respetando el orden original. Por ejemplo, la función deberá satisfacer los siguientes tests:", 'keep'))
ex.append(('code',
"""class TestCollect(collect: (Int => Option[String], List[Int]) => List[String]) extends AnyFlatSpec with should.Matchers:

    val f: Int => Option[String] =
        n => if n % 2 == 0 then Some(s"par($n)") else None

    "collect" should "work" in:
        collect(f, List(1, 2, 3, 4)) shouldBe List("par(2)", "par(4)")
        collect(f, List(1, 3, 5)) shouldBe List()
        collect(f, List()) shouldBe List()""", 'keep'))
ex.append(('md', "__a) (1 punto)__ Implementa la función `collect` mediante recursividad (no final).", 'keep'))
ex.append(('code',
"""def collect[A, B](f: A => Option[B], l: List[A]): List[B] =
    l match
        case Nil => Nil
        case head :: tail =>
            f(head) match
                case Some(b) => b :: collect(f, tail)
                case None => collect(f, tail)""", 'answer-i'))
ex.append(('code', "run(TestCollect(collect))", 'keep'))
ex.append(('md', "__b) (1 punto)__ Implementa la función `collect` mediante la función de orden superior `foldRight`.", 'keep'))
ex.append(('code',
"""def collect[A, B](f: A => Option[B], l: List[A]): List[B] =
    l.foldRight(Nil: List[B]): (head, tailSol) =>
        f(head) match
            case Some(b) => b :: tailSol
            case None => tailSol""", 'answer-i'))
ex.append(('code', "run(TestCollect(collect))", 'keep'))
ex.append(('md', "__c) (1 punto)__ Implementa la función `collect` mediante la función de orden superior `flatMap`.", 'keep'))
ex.append(('code',
"""def collect[A, B](f: A => Option[B], l: List[A]): List[B] =
    l.flatMap: head =>
        f(head) match
            case Some(b) => List(b)
            case None => Nil""", 'answer-i'))
ex.append(('code', "run(TestCollect(collect))", 'keep'))

# Ejercicio 4
ex.append(('md', "# Ejercicio 4\n__(3 puntos)__", 'keep'))
ex.append(('md', "Se desea implementar la función `fromBits`, que recibe una lista de dígitos binarios (`0` y `1`), ordenados del más significativo al menos significativo, y devuelve el número decimal que representa. Por ejemplo, la lista `List(1, 0, 1, 1)` representa el número binario 1011, cuyo valor en decimal es 11. La función deberá satisfacer los siguientes tests:", 'keep'))
ex.append(('code',
"""class TestFromBits(fromBits: List[Int] => Int) extends AnyFlatSpec with should.Matchers:

    "fromBits" should "work" in:
        fromBits(List(1, 0, 1, 1)) shouldBe 11
        fromBits(List(1, 0, 1, 0)) shouldBe 10
        fromBits(List(1)) shouldBe 1
        fromBits(List()) shouldBe 0
        fromBits(List(1, 1, 1, 1)) shouldBe 15""", 'keep'))
ex.append(('md', "_Pista:_ un posible algoritmo para implementar la función `fromBits` consiste en recorrer la lista de izquierda a derecha manteniendo un acumulador `out`, inicializado a 0, que en cada paso se actualiza mediante la expresión `out * 2 + bit`, donde `bit` es el dígito procesado en ese paso.", 'keep'))
ex.append(('md', "__a) (1 punto)__ Implementa la función `fromBits` mediante un patrón de diseño iterativo utilizando recursividad final.", 'keep'))
ex.append(('code',
"""def fromBits(l: List[Int]): Int =

    def step(out: Int, aux: List[Int]): Int =
        aux match
            case Nil => out
            case head :: tail =>
                step(out * 2 + head, tail)

    step(0, l)""", 'answer-i'))
ex.append(('code', "run(TestFromBits(fromBits))", 'keep'))
ex.append(('md', "__b) (1 punto)__ Implementa la función `fromBits` mediante la función de orden superior `foldLeft`.", 'keep'))
ex.append(('code',
"""def fromBits(l: List[Int]): Int =
    l.foldLeft(0):
        case (out, head) =>
            out * 2 + head""", 'answer-i'))
ex.append(('code', "run(TestFromBits(fromBits))", 'keep'))
ex.append(('md', "__c) (1 punto)__ Implementa la función `fromBits` sin utilizar recursividad, mediante las funciones de orden superior `map` y `sum`. La idea consiste en invertir la lista (de modo que el bit menos significativo quede en primer lugar) y sumar cada bit multiplicado por la potencia de dos correspondiente a su posición. Es decir, si $[b_0, b_1, \\ldots, b_{n-1}]$ denota la lista de bits invertida, el valor decimal viene dado por:", 'keep'))
ex.append(('md', r"$$\mathtt{fromBits} = \sum_{i=0}^{n-1} b_i \cdot 2^{i}$$", 'keep'))
ex.append(('md', "__Es obligatorio__ implementar la función combinando exclusivamente las funciones `reverse`, `zipWithIndex`, `map`, `pow` y `sum`, sin recurrir a la recursividad ni a `foldLeft`/`foldRight`.", 'keep'))
ex.append(('code',
"""def fromBits(l: List[Int]): Int =
    l.reverse.zipWithIndex.map((bit, i) => bit * pow(2, i)).sum""", 'answer-i'))
ex.append(('code', "run(TestFromBits(fromBits))", 'keep'))


def to_cell(kind, content):
    if kind == 'img':
        return img(DIAGRAM_NAME, DIAGRAM_PNG, 430)
    return md(content) if kind == 'md' else code(content)

sol_cells = pre + [to_cell(k, c) for (k, c, r) in ex]

enu_cells = list(pre)
for (k, c, r) in ex:
    if r == 'keep':
        enu_cells.append(to_cell(k, c))
    elif r == 'answer-w':
        enu_cells.append(code(PH_W.rstrip('\n') + '\n\n'))
    elif r == 'answer-i':
        enu_cells.append(code(PH_I.rstrip('\n') + '\n\n'))
    elif r == 'answer-md':
        enu_cells.append(md(PH_W.strip()))

def write(path, cells):
    nb = {"cells": cells, "metadata": tpl['metadata'], "nbformat": tpl['nbformat'], "nbformat_minor": tpl['nbformat_minor']}
    with open(path, 'w') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

write(SOL, sol_cells)
write(ENU, enu_cells)
print('Escritos:')
print(' ', SOL, '->', len(sol_cells), 'celdas')
print(' ', ENU, '->', len(enu_cells), 'celdas')
