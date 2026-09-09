// ===== Preámbulo =====
type Not[P] = P => Nothing
trait ExcludedMiddle:
  def apply[P]: Either[P, Not[P]]
trait Isomorphic[A, B]:
  def from(a: A): B
  def to(b: B): A
def pow(base: Int, exp: Int): Int = math.pow(base, exp).toInt

// ===== Ej1a =====
def proof1a[P, Q, R, S]: (Either[P, Q] => R) => (R => S) => (P => S, Q => S) =
  f => g => (p => g(f(Left(p))), q => g(f(Right(q))))

// ===== Ej1b =====
def proof1b[P, Q](lem: ExcludedMiddle): Either[P => Q, Q => P] =
  lem.apply[Q] match
    case Left(q)   => Left(_ => q)
    case Right(nq) => Right(nq)

// ===== Ej2 =====
class Iso[A, B] extends Isomorphic[Option[A] => B, (B, A => B)]:
  def from(f: Option[A] => B): (B, A => B) =
    (f(None), a => f(Some(a)))
  def to(p: (B, A => B)): Option[A] => B =
    (o: Option[A]) => o match
      case None    => p._1
      case Some(a) => p._2(a)

// ===== Ej3 collect =====
def collect_a[A, B](f: A => Option[B], l: List[A]): List[B] =
  l match
    case Nil => Nil
    case head :: tail =>
      f(head) match
        case Some(b) => b :: collect_a(f, tail)
        case None    => collect_a(f, tail)

def collect_b[A, B](f: A => Option[B], l: List[A]): List[B] =
  l.foldRight(Nil: List[B]) { (head, tailSol) =>
    f(head) match
      case Some(b) => b :: tailSol
      case None    => tailSol
  }

def collect_c[A, B](f: A => Option[B], l: List[A]): List[B] =
  l.flatMap { head =>
    f(head) match
      case Some(b) => List(b)
      case None    => Nil
  }

// ===== Ej4 fromBits =====
def fromBits_a(l: List[Int]): Int =
  def step(out: Int, aux: List[Int]): Int =
    aux match
      case Nil => out
      case head :: tail => step(out * 2 + head, tail)
  step(0, l)

def fromBits_b(l: List[Int]): Int =
  l.foldLeft(0) { case (out, head) => out * 2 + head }

def fromBits_c(l: List[Int]): Int =
  l.reverse.zipWithIndex.map((bit, i) => bit * pow(2, i)).sum

@main def run(): Unit =
  // -- Ej1a: typecheck + comportamiento (eliminación de Either + composición)
  val (psa, qsa) = proof1a[Int, String, Boolean, Char](
    { case Left(i) => i > 0; case Right(s) => s.nonEmpty })(b => if b then 'T' else 'F')
  assert(psa(5) == 'T' && psa(-1) == 'F' && qsa("x") == 'T' && qsa("") == 'F', "Ej1a")

  // -- Ej1b: typecheck + comportamiento de la rama Left
  val r1b = proof1b[Int, String](new ExcludedMiddle:
    def apply[P]: Either[P, Not[P]] = Left("q".asInstanceOf[P]))
  r1b match
    case Left(pq) => assert(pq(0) == "q", "Ej1b Left")
    case Right(_) => assert(false, "Ej1b")

  // -- Ej2: leyes del isomorfismo sobre ejemplos
  val iso = new Iso[Int, String]
  val f2: Option[Int] => String = { case None => "z"; case Some(n) => "v" + n }
  val back = iso.to(iso.from(f2))
  assert(back(None) == "z" && back(Some(3)) == "v3", "Ej2 to(from)")
  val p2 = ("z", (a: Int) => "v" + a)
  val (b0, g0) = iso.from(iso.to(p2))
  assert(b0 == "z" && g0(7) == "v7", "Ej2 from(to)")

  // -- Ej3: tests de TestCollect (f: pares -> "par(n)")
  val fc: Int => Option[String] = n => if n % 2 == 0 then Some(s"par($n)") else None
  for impl <- List(collect_a[Int, String], collect_b[Int, String], collect_c[Int, String]) do
    assert(impl(fc, List(1, 2, 3, 4)) == List("par(2)", "par(4)"), "collect 1234")
    assert(impl(fc, List(1, 3, 5)) == List(), "collect impares")
    assert(impl(fc, List()) == List(), "collect vacio")

  // -- Ej4: tests de TestFromBits
  for impl <- List(fromBits_a, fromBits_b, fromBits_c) do
    assert(impl(List(1, 0, 1, 1)) == 11, "fb 1011")
    assert(impl(List(1, 0, 1, 0)) == 10, "fb 1010")
    assert(impl(List(1)) == 1, "fb 1")
    assert(impl(List()) == 0, "fb vacio")
    assert(impl(List(1, 1, 1, 1)) == 15, "fb 1111")

  println("EXAMEN COMPLETO: todas las soluciones typechequean y pasan los tests")
