# -*- coding: utf-8 -*-
"""Traducción de PF-2/topic3: 3 Intro y 3.1 Functions-Exercises."""

PAIRS = [
# ---------------------------------------------------------------- 3 Intro
("# Topic 3. Algebraic data types", "# Tema 3. Tipos algebraicos de datos"),

("Every programming language offers _primitive_ types, such as the types of boolean values, integer and double numeric values, strings, etc. But they also provide mechanisms to define new types, so-called user-defined types, which are designed to satisfy the needs of particular applications. For instance, user-defined types in object-oriented languages are specified through class or trait declarations; and types can also be specified from already existing user-defined types through the inheritance mechanism.",
 "Todo lenguaje de programación ofrece tipos _primitivos_: el de los valores booleanos, el de los enteros y los números en coma flotante, el de las cadenas, etc. Pero ofrece además mecanismos para definir tipos nuevos, los llamados tipos definidos por el usuario, pensados para satisfacer las necesidades de aplicaciones concretas. En los lenguajes orientados a objetos, por ejemplo, los tipos definidos por el usuario se especifican mediante declaraciones de clases o de _traits_; y también pueden especificarse a partir de otros tipos ya definidos por el usuario, mediante el mecanismo de la herencia."),

("In functional programming, the rules for declaring new types are different: no inheritance or classes, just _products_, _sums_ and _exponentiation_ of types. Because of the correspondence with arithmetic (which goes beyond the terminology!), these types are called **algebraic data types** (ADTs).",
 "En programación funcional, las reglas para declarar tipos nuevos son distintas: no hay herencia ni clases, solo _productos_, _sumas_ y _exponenciación_ de tipos. Por su correspondencia con la aritmética —que va mucho más allá de la terminología—, estos tipos se llaman **tipos algebraicos de datos** (ADTs, por sus siglas en inglés)."),

("### Goals", "### Objetivos"),

(
"""The goals of this section are the following:
* Understanding products, sums and exponents as the primary means of representing data types in functional programming.
* Understanding the _algebraic_ nature of these types.
* Being able to prove isomorphisms between algebraic data types using the methodology of _type-driven development_.""",
"""Los objetivos de esta sección son los siguientes:
* Entender los productos, las sumas y los exponentes como el medio primario de representar tipos de datos en programación funcional.
* Entender la naturaleza _algebraica_ de estos tipos.
* Ser capaz de demostrar isomorfismos entre tipos algebraicos de datos con la metodología del _desarrollo dirigido por tipos_ (_type-driven development_)."""),

(
"""### References

[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_5ed) Fifth Edition.
by Martin Odersky, Lex Spoon, and Bill Venners.

- Chapter 13. Pattern Matching

__[Scala book (online)](https://docs.scala-lang.org/scala3/book/introduction.html)__.

- [Pure functions](https://docs.scala-lang.org/scala3/book/fp-pure-functions.html)
- [Match Expressions](https://docs.scala-lang.org/scala3/book/control-structures.html#match-expressions)
- [Case classes](https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html#case-classes)
- [Case objects](https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html#case-objects)

[__Functional programming simplified__](https://alvinalexander.com/downloads/fpsimplified-free-preview.pdf), by Alvin Alexander.

- Chapters 19. Functional Programming as Algebra

[__Tony Morris on ADTs__](https://about.chatroulette.com/posts/algebraic-data-types/)

_[Optional]_ __[Why Functional Programming Matters](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf)__ John Hughes. This is a classic paper that motivates the need for functional programming by appealing to software enginerring principles such as modularity. It's written using the Miranda programming language, and it's more an academic paper that undergraduate material. Nevertheless, its reading is highly recommeded. Give it a try if you find some time!""",
"""### Referencias

[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_5ed) Quinta edición.
de Martin Odersky, Lex Spoon y Bill Venners.

- Capítulo 13. Pattern Matching

__[Scala book (online)](https://docs.scala-lang.org/scala3/book/introduction.html)__.

- [Pure functions](https://docs.scala-lang.org/scala3/book/fp-pure-functions.html)
- [Match Expressions](https://docs.scala-lang.org/scala3/book/control-structures.html#match-expressions)
- [Case classes](https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html#case-classes)
- [Case objects](https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html#case-objects)

[__Functional programming simplified__](https://alvinalexander.com/downloads/fpsimplified-free-preview.pdf), de Alvin Alexander.

- Capítulo 19. Functional Programming as Algebra

[__Tony Morris on ADTs__](https://about.chatroulette.com/posts/algebraic-data-types/)

_[Opcional]_ __[Why Functional Programming Matters](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf)__, de John Hughes. Es un artículo clásico que motiva la necesidad de la programación funcional apelando a principios de la ingeniería del software, como la modularidad. Está escrito en el lenguaje Miranda y es más un artículo académico que material de grado. Aun así, su lectura es muy recomendable. ¡Dale una oportunidad si encuentras un rato!"""),

# ------------------------------------------------- 3.1 Functions-Exercises
(
"""# Topic 3. Algebraic data types

## 3.1 Functions""",
"""# Tema 3. Tipos algebraicos de datos

## 3.1 Funciones"""),

("## Exercise 1", "## Ejercicio 1"),
("## Exercise 2", "## Ejercicio 2"),
("## Exercise 3", "## Ejercicio 3"),
("## Exercise 4", "## Ejercicio 4"),
("## Exercise 5", "## Ejercicio 5"),
("#### Solution", "#### Solución"),
("#### Your solution", "#### Tu solución"),

("Implement the following _function-methods_ as standard _function-values_ without any syntactic sugar.",
 "Implementa los siguientes _métodos-función_ como _valores-función_ estándar, sin ningún azúcar sintáctico."),

("The same as in exercise 1, but using lambda expressions. Implement alternative versions with different levels of type inference and syntactic sugar (e.g. using _underscore_ syntax).",
 "Lo mismo que en el ejercicio 1, pero usando expresiones lambda. Implementa versiones alternativas con distintos niveles de inferencia de tipos y de azúcar sintáctico (por ejemplo, con la sintaxis del _guion bajo_)."),

("Implement the function-methods as _curried_ function-values.",
 "Implementa los métodos-función como valores-función _currificados_."),

("Given the following monomorphic version of the `call` HOF",
 "Dada la siguiente versión monomórfica de la HOF `call`"),

("implement a polymorphic version as a function-method, so that it can work with multiple types (i.e. not only with functions of type `Int => Int`). Test that your implementation is correct by checking that the following examples compile and work as expected.",
 "implementa una versión polimórfica como método-función, de modo que pueda trabajar con varios tipos (es decir, no solo con funciones de tipo `Int => Int`). Comprueba que tu implementación es correcta viendo que los ejemplos siguientes compilan y funcionan como se espera."),

("As a polymorphic value:", "Como valor polimórfico:"),

("implement a polymorphic version as a curried function, so that it can work with multiple types.",
 "implementa una versión polimórfica como función currificada, de modo que pueda trabajar con varios tipos."),

("Test that your implementation is correct by checking that the following examples compile and work as expected.",
 "Comprueba que tu implementación es correcta viendo que los ejemplos siguientes compilan y funcionan como se espera."),

("As a polymorphic function type:", "Como tipo de función polimórfica:"),
("As a polymorphic meethod:", "Como método polimórfico:"),

# comentarios: son código comentado, se dejan igual
("// call[Int, Int](_ + 1, 1)", "// call[Int, Int](_ + 1, 1)"),
("// call((i: Int) => i+1, 3)", "// call((i: Int) => i+1, 3)"),
('// call("hello, " + _, "pepe")', '// call("hello, " + _, "pepe")'),
("// call((_ : Int) > 0, 3)", "// call((_ : Int) > 0, 3)"),
("// call((i: Int) => i < 0, 2)", "// call((i: Int) => i < 0, 2)"),
]
