# -*- coding: utf-8 -*-
"""Traducción de PF-1/topic2/2.4 Java-to-Scala (y su template)."""

PAIRS = [
("# Scala introduction", "# Introducción a Scala"),

(
"""This notebook offers a basic introduction to the object-oriented features of the Scala programming language. It consists of small code samples that aim at translating into Scala some of the Java examples of the following tutorial:

https://docs.oracle.com/javase/tutorial/java/TOC.html

In particular, we will talk about:
* Classes and objects
* Control flow structures
* Constructors, private and static members
* Inmutable objects
* Interfaces and inheritance
* Generics""",
"""Este notebook ofrece una introducción básica a las características orientadas a objetos del lenguaje Scala. Consiste en pequeños ejemplos de código que tratan de traducir a Scala algunos de los ejemplos en Java del siguiente tutorial:

https://docs.oracle.com/javase/tutorial/java/TOC.html

En particular, hablaremos de:
* Clases y objetos
* Estructuras de control de flujo
* Constructores, miembros privados y estáticos
* Objetos inmutables
* Interfaces y herencia
* Genéricos"""),

("### References", "### Referencias"),

(
"""[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_3ed) Third Edition.
by Martin Odersky, Lex Spoon, and Bill Venners.

This is an introductory book that covers the basic features of the language as well as its most advanced characteristics. The following chapters are the most relevant for the purpose of this notebook:

1. A Scalable Language
2. First Steps in Scala
3. Next Steps in Scala
4. Classes and Objects
5. Basic Types and Operations
7. Built-in Control Structures 117
9. Control Abstraction 167
10. Composition and Inheritance 183
11. Scala's Hierarchy 211""",
"""[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_3ed) Tercera edición.
de Martin Odersky, Lex Spoon y Bill Venners.

Es un libro introductorio que cubre tanto las características básicas del lenguaje como las más avanzadas. Los capítulos más relevantes para lo que se ve en este notebook son:

1. A Scalable Language
2. First Steps in Scala
3. Next Steps in Scala
4. Classes and Objects
5. Basic Types and Operations
7. Built-in Control Structures 117
9. Control Abstraction 167
10. Composition and Inheritance 183
11. Scala's Hierarchy 211"""),

(
"""__[Scala book (online)](https://docs.scala-lang.org/overviews/scala-book/introduction.html)__. A basic introduction to the basic features of Scala. Check in particular the first trail:

- [_Prelude: a taste of Scala_](https://docs.scala-lang.org/overviews/scala-book/prelude-taste-of-scala.html)""",
"""__[Scala book (online)](https://docs.scala-lang.org/overviews/scala-book/introduction.html)__. Una introducción a las características básicas de Scala. Consulta en particular el primer itinerario:

- [_Prelude: a taste of Scala_](https://docs.scala-lang.org/overviews/scala-book/prelude-taste-of-scala.html)"""),

("[Scala Cheatsheet](https://docs.scala-lang.org/cheatsheets/index.html)",
 "[Scala Cheatsheet](https://docs.scala-lang.org/cheatsheets/index.html)"),

(
"""# Object-Oriented Programming Concepts

https://docs.oracle.com/javase/tutorial/java/concepts/index.html""",
"""# Conceptos de la programación orientada a objetos

https://docs.oracle.com/javase/tutorial/java/concepts/index.html"""),

("### Classes", "### Clases"),
("### Objects and method invocation", "### Objetos e invocación de métodos"),
("Some syntactic sugar for method invocations:", "Algo de azúcar sintáctico para la invocación de métodos:"),
("### Inheritance", "### Herencia"),
("### Interfaces", "### Interfaces"),

(
"""# Language basics

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/index.html""",
"""# Fundamentos del lenguaje

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/index.html"""),

("### Control flow statements", "### Sentencias de control de flujo"),
("### If-Else-If demo", "### Ejemplo de if-else-if"),
("### while statements", "### Sentencias `while`"),
("### For statement", "### La sentencia `for`"),

(
"""### Exceptions

https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html""",
"""### Excepciones

https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html"""),

(
"""# Classes and objects

https://docs.oracle.com/javase/tutorial/java/javaOO/index.html""",
"""# Clases y objetos

https://docs.oracle.com/javase/tutorial/java/javaOO/index.html"""),

("### Constructors", "### Constructores"),
("### Super-constructors", "### Constructores de la superclase"),
("### Private members", "### Miembros privados"),
("### Static members", "### Miembros estáticos"),

(
"""### Inmutable objects
https://docs.oracle.com/javase/tutorial/essential/concurrency/immutable.html""",
"""### Objetos inmutables
https://docs.oracle.com/javase/tutorial/essential/concurrency/immutable.html"""),

("Immutable objects in Java:", "Objetos inmutables en Java:"),
("Immutable objects in Scala:", "Objetos inmutables en Scala:"),

(
"""# Interfaces and inheritance

https://docs.oracle.com/javase/tutorial/java/IandI/index.html""",
"""# Interfaces y herencia

https://docs.oracle.com/javase/tutorial/java/IandI/index.html"""),

("### Extends + Implements", "### Extends + Implements"),
("### Default and static interface methods", "### Métodos por defecto y estáticos en las interfaces"),

(
"""### Inheritance Hierarchy

In Java:
![Java Inheritance Hierarchy](https://docs.oracle.com/javase/tutorial/figures/java/classes-object.gif)""",
"""### Jerarquía de herencia

En Java:
![Java Inheritance Hierarchy](https://docs.oracle.com/javase/tutorial/figures/java/classes-object.gif)"""),

("""In Scala:
![](https://docs.scala-lang.org/resources/images/tour/unified-types-diagram.svg)""",
 """En Scala:
![](https://docs.scala-lang.org/resources/images/tour/unified-types-diagram.svg)"""),

("https://www.scala-lang.org/api/2.12.10/scala/Any.html",
 "https://www.scala-lang.org/api/2.12.10/scala/Any.html"),

(
"""# Generics

https://docs.oracle.com/javase/tutorial/java/generics/index.html""",
"""# Genéricos

https://docs.oracle.com/javase/tutorial/java/generics/index.html"""),

("### Generic classes", "### Clases genéricas"),
("### Generic methods", "### Métodos genéricos"),
("### Bounded type parameters", "### Parámetros de tipo acotados"),

("[java.lang.Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html)",
 "[java.lang.Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html)"),

("Also for classes:", "También para las clases:"),

(
"""### Variance (Scala)

https://docs.scala-lang.org/tour/variances.html""",
"""### Varianza (Scala)

https://docs.scala-lang.org/tour/variances.html"""),

(
"""Some examples with Arrays (invariant in T):

/*
class Array[T]{ ... }
*/""",
"""Algunos ejemplos con Arrays (invariantes en T):

/*
class Array[T]{ ... }
*/"""),

("This compiles, how can it be?", "Esto compila. ¿Cómo puede ser?"),

("Check out the signature of [:+](https://www.scala-lang.org/api/2.11.12/#scala.Array)",
 "Mira la signatura de [:+](https://www.scala-lang.org/api/2.11.12/#scala.Array)"),

(
"""Some examples with [List](https://www.scala-lang.org/api/2.11.12/#scala.collection.immutable.List) (covariant in T)

/* class List[+T] { ... } */""",
"""Algunos ejemplos con [List](https://www.scala-lang.org/api/2.11.12/#scala.collection.immutable.List) (covariante en T)

/* class List[+T] { ... } */"""),

# ------------------------------------------------------------------ comentarios
("// Create two different Bicycle objects", "// Crear dos objetos Bicycle distintos"),
("// Invoke methods on those objects", "// Invocar métodos sobre esos objetos"),
("// new fields and methods defining", "// aquí irían los nuevos campos y métodos"),
("// a mountain bike would go here", "// que definen una bicicleta de montaña"),
("//  wheel revolutions per minute", "//  revoluciones de la rueda por minuto"),
("// The compiler will now require that methods", "// Ahora el compilador exigirá que los métodos"),
("// changeCadence, changeGear, speedUp, and applyBrakes", "// changeCadence, changeGear, speedUp y applyBrakes"),
("// all be implemented. Compilation will fail if those", "// estén todos implementados. La compilación fallará si esos"),
("// methods are missing from this class.", "// métodos faltan en esta clase."),
('// the "if" clause: bicycle must be moving', '// la cláusula "if": la bicicleta debe estar en movimiento'),
('// the "then" clause: decrease current speed', '// la cláusula "then": reducir la velocidad actual'),
("// return speed > 0", "// return speed > 0"),
("// the MountainBike subclass has one field", "// la subclase MountainBike tiene un campo"),
("// the MountainBike subclass has one constructor", "// la subclase MountainBike tiene un constructor"),
("// the MountainBike subclass has one method", "// la subclase MountainBike tiene un método"),
("// Companion object", "// Objeto compañero (companion object)"),
("// ClassName.methodName(args)", "// ClassName.methodName(args)"),
("// vars vs. vals", "// vars vs. vals"),
("// We can mutate `i`", "// Podemos mutar `i`"),
("// But `j` is immutable", "// Pero `j` es inmutable"),
("// j = 1", "// j = 1"),
("// Note that immutable variables may refer to mutable objects",
 "// Nótese que las variables inmutables pueden referirse a objetos mutables"),
("// Values must be between 0 and 255.", "// Los valores deben estar entre 0 y 255."),
("// color1.red = 5", "// color1.red = 5"),
("// field, constructor, and method declarations", "// declaraciones de campos, constructor y métodos"),
("// Type inference!", "// ¡Inferencia de tipos!"),
("// With type inference", "// Con inferencia de tipos"),
("// Integer = java.lang.Integer", "// Integer = java.lang.Integer"),
("// 2: scala.Int", "// 2: scala.Int"),
("// ...", "// ..."),
("// Will this compile? No, it doesn't compile, since Array[T] is invariant in T",
 "// ¿Compilará esto? No, no compila, porque Array[T] es invariante en T"),
("// var arr3: Array[Animal] = arr1", "// var arr3: Array[Animal] = arr1"),
("// Compiles: class List[+T], covariant in T", "// Compila: class List[+T], covariante en T"),
("// Similarly to arrays, adding new elements may change the type of the list",
 "// Igual que con los arrays, añadir elementos nuevos puede cambiar el tipo de la lista"),
("// Signature is like: def +:[B >: T](elem: B)(...): List[B]",
 "// La signatura es del estilo: def +:[B >: T](elem: B)(...): List[B]"),
("// class Animal", "// class Animal"),
("// Some animals", "// Algunos animales"),
]
