# -*- coding: utf-8 -*-
"""Traducción de PF-1/topic2/2.3 Scala (y su template)."""

PAIRS = [
(
"""# Topic 2. Strongly-typed vs. Dynamic languages

## 2.3 Structured programming in Scala""",
"""# Tema 2. Lenguajes de tipado fuerte frente a lenguajes dinámicos

## 2.3 Programación estructurada en Scala"""),

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
"""__[Scala book (online)](https://docs.scala-lang.org/scala3/book/introduction.html)__. A basic introduction to the basic features of Scala. Note that we will be using the Scala 3 version throughout this course. Check in particular the first trail:

- [_Prelude: a taste of Scala_](https://docs.scala-lang.org/scala3/book/taste-intro.html)""",
"""__[Scala book (online)](https://docs.scala-lang.org/scala3/book/introduction.html)__. Una introducción a las características básicas de Scala. Nótese que a lo largo del curso usaremos la versión de Scala 3. Consulta en particular el primer itinerario:

- [_Prelude: a taste of Scala_](https://docs.scala-lang.org/scala3/book/taste-intro.html)"""),

# sin prosa: solo el enlace
("[Scala Cheatsheet](https://alvinalexander.com/scala/scala-3-cheat-sheet-examples/)",
 "[Scala Cheatsheet](https://alvinalexander.com/scala/scala-3-cheat-sheet-examples/)"),

(
"""# Variables, values and types

Variables stand for values of a given type. In the next example:""",
"""# Variables, valores y tipos

Las variables representan valores de un tipo dado. En el ejemplo siguiente:"""),

("`a` is the name of the variable, `Int` represents its type, and `1`, the initial value of the variable. In order to retrieve the value of a variable, we simply refer to it:",
 "`a` es el nombre de la variable, `Int` representa su tipo y `1`, el valor inicial de la variable. Para recuperar el valor de una variable basta con referirnos a ella:"),

("Being a variable, we can _mutate_ or modify its content:",
 "Al ser una variable, podemos _mutar_ o modificar su contenido:"),

("so that the new content is now:", "de modo que su contenido es ahora:"),

("> Note that the execution of a notebook cell containing an expression always return the name of an auto-generated value `res?`, its type and the computed value. On the other hand, the assignment `a = 3` is not an _expression_, it's a _command_, and, therefore, its execution does not return any output.",
 "> Nótese que la ejecución de una celda del notebook que contiene una expresión devuelve siempre el nombre de un valor autogenerado `res?`, su tipo y el valor calculado. La asignación `a = 3`, en cambio, no es una _expresión_ sino un _comando_ y, por tanto, su ejecución no devuelve ninguna salida."),

("Now, there is another kind of variables in Scala, so-called _inmutable variables_, declared with the reserved keyword `val`:",
 "Hay además otro tipo de variables en Scala, las llamadas _variables inmutables_, que se declaran con la palabra reservada `val`:"),

("Being inmutable, their associated value can't be modified:",
 "Al ser inmutables, el valor que tienen asociado no puede modificarse:"),

("But then, in which sense inmutable variables are _variables_? They are variables very much in the same way in which we talk about variables in mathematics: they are variables because they may refer, in principle, to _any_ value of the given type. But, once they are assigned a value, they won't change.",
 "Pero entonces, ¿en qué sentido son _variables_ las variables inmutables? Lo son en el mismo sentido en que hablamos de variables en matemáticas: son variables porque pueden referirse, en principio, a _cualquier_ valor del tipo dado. Pero, una vez que se les asigna un valor, este ya no cambia."),

("> __Inmutability__ is one of the defining features of functional programming. Inmutable data allow us to reason more easily about the behaviour of our programs (no fear that some part of the program will unexpectedly mutate the value of some variable), and they play nicely with other features such as concurrency.",
 "> La __inmutabilidad__ es uno de los rasgos que definen la programación funcional. Los datos inmutables nos permiten razonar más fácilmente sobre el comportamiento de nuestros programas —sin miedo a que alguna parte del programa mute inesperadamente el valor de una variable— y encajan bien con otras características, como la concurrencia."),

(
"""# Methods

We already saw several examples of functions defined as _methods_. A new one:""",
"""# Métodos

Ya hemos visto varios ejemplos de funciones definidas como _métodos_. Uno nuevo:"""),

("Scala is primarily an __object-oriented language__, i.e. a language in which the primitive constructs are objects, classes, methods, fields, traits, inheritance, etc. But Scala is also a functional programming language insofar it supports adequately well the programming abstractions of this paradigm. We need to take into account, however, that this support ultimately builds upon the primitive object-oriented abstractions.",
 "Scala es, en primer lugar, un __lenguaje orientado a objetos__: un lenguaje cuyas construcciones primitivas son objetos, clases, métodos, campos, _traits_, herencia, etc. Pero Scala es también un lenguaje de programación funcional, en la medida en que da un soporte razonablemente bueno a las abstracciones de ese paradigma. Hay que tener en cuenta, eso sí, que ese soporte se construye en última instancia sobre las abstracciones primitivas orientadas a objetos."),

("> Methods represent the behaviour of classes of objects. Jupyter allows us to write methods outside any class, but this is only because the Scala runtime (almond) inserts this method in an auto-generated class named `Helper`.",
 "> Los métodos representan el comportamiento de las clases de objetos. Jupyter nos permite escribir métodos fuera de cualquier clase, pero solo porque el runtime de Scala (almond) inserta ese método en una clase autogenerada llamada `Helper`."),

("# Control structures", "# Estructuras de control"),
("### For-loops", "### Bucles `for`"),

("Let's implement a Scala function which returns the sum of a range of numbers, from $a$ to $b$, i.e. $\\Sigma_{i=a}^b i$. This will allow us to introduce `for`-loops statements:",
 "Implementemos una función en Scala que devuelva la suma de un rango de números, de $a$ a $b$, es decir, $\\Sigma_{i=a}^b i$. Nos servirá para presentar las sentencias `for`:"),

("Note that the `return` statements are optional. Some tests:",
 "Nótese que las sentencias `return` son opcionales. Algunas pruebas:"),

("Let's suppose now that we simply want the function to _print_ the square of each number between $a$ and $b$:",
 "Supongamos ahora que lo único que queremos es que la función _imprima_ el cuadrado de cada número entre $a$ y $b$:"),

("Note the return type of the function: the type `Unit` is used here to indicate that no meaningful value is returned by the function, i.e. we just want to invoke this function for its side-effects (printing in the console).",
 "Nótese el tipo de retorno de la función: el tipo `Unit` se usa aquí para indicar que la función no devuelve ningún valor significativo; es decir, que la invocamos solo por sus efectos laterales (imprimir por consola)."),

("> We will speak later on about _pure_ and _impure_ functions, an essential feature of functional programming.",
 "> Más adelante hablaremos de funciones _puras_ e _impuras_, un rasgo esencial de la programación funcional."),

("### If-then-else expressions", "### Expresiones `if-then-else`"),

("The `if-then-else` construct is not a statement, but an expression, i.e. it denotes a proper value:",
 "La construcción `if-then-else` no es una sentencia, sino una expresión; es decir, denota un valor propiamente dicho:"),

(
"""Let's implement now a function `isPrime` which tests whether a number is prime or not. We can translate the following Python program from [wikipedia](https://en.wikipedia.org/wiki/Primality_test#:~:text=The%20simplest%20primality%20test%20is,Otherwise%2C%20it%20is%20prime.):

![image-2.png](attachment:image-2.png)""",
"""Implementemos ahora una función `isPrime` que compruebe si un número es primo. Podemos traducir el siguiente programa en Python, tomado de [wikipedia](https://en.wikipedia.org/wiki/Primality_test#:~:text=The%20simplest%20primality%20test%20is,Otherwise%2C%20it%20is%20prime.):

![image-2.png](attachment:image-2.png)"""),

("The translation will use equivalent control structures to the ones shown in the Python code: `if-then-else` and `for`-loops, in particular.",
 "La traducción usará estructuras de control equivalentes a las del código Python: en particular, `if-then-else` y bucles `for`."),

("Some simple tests using `assert`:", "Algunas pruebas sencillas con `assert`:"),

(
"""Note the that the `return` statement in the inner for-loop is necessary, since we must return control inmediately and skip the rest of the computation.

The example also shows the `if ... [then] ... else if ...` common pattern, whereby several if-then-else expressions are chained.""",
"""Nótese que la sentencia `return` del bucle `for` interno es necesaria, porque hay que devolver el control de inmediato y saltarse el resto del cálculo.

El ejemplo muestra también el patrón habitual `if ... [then] ... else if ...`, en el que se encadenan varias expresiones if-then-else."""),

("### `While` statements", "### Sentencias `while`"),

("The same example using `while` to avoid the inner `return` statement:",
 "El mismo ejemplo usando `while`, para evitar el `return` interno:"),

# ------------------------------------------------------------------ comentarios
("// reveal the name of the enclosing class", "// revelar el nombre de la clase que lo contiene"),
("// Scala 2 syntax", "// sintaxis de Scala 2"),
("// Scala 3 syntax", "// sintaxis de Scala 3"),
("// scala 2", "// scala 2"),
("// scala 3", "// scala 3"),
("// Scala 2", "// Scala 2"),
("// Scala 3", "// Scala 3"),

# ------------------------------------------- comentarios que solo trae el template
("// variables, values and type", "// variables, valores y tipos"),
("// accessing the value of a variable", "// accediendo al valor de una variable"),
("// mutate variable", "// mutar la variable"),
("// get new content", "// obtener el nuevo contenido"),
("// now, inmutable variables", "// ahora, variables inmutables"),
("// not mutable!", "// ¡no es mutable!"),
("// method that computes the area of circles", "// método que calcula el área de un círculo"),
("// sum interval function", "// función que suma un intervalo"),
("// print squares: a function returning Unit", "// imprimir cuadrados: una función que devuelve Unit"),
("// if-the-else expression, assignment to vals", "// expresión if-then-else, asignación a vals"),
("// isPrime function", "// función isPrime"),
("// some assertions", "// algunas aserciones"),
]
