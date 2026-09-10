# -*- coding: utf-8 -*-
"""Traducción de PF-1/topic2: 2.2 StaticTyping (+template) y 2.5 Exercises (+Sols)."""

DIV = '<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:10px 0;">'

PAIRS = [
# ---------------------------------------------------------------- 2.2 StaticTyping
(
"""# Topic 2. Strongly-typed vs. Dynamic languages

## 2.2 Strongly-typed languages""",
"""# Tema 2. Lenguajes de tipado fuerte frente a lenguajes dinámicos

## 2.2 Lenguajes de tipado fuerte"""),

("# Types in Scala", "# Los tipos en Scala"),

("Scala is a statically-typed language, which means that types play a prominent syntactic role and that type-checking is actually enforced by the compiler itself. For instance, we can't declare functions without explicitly indicating the input types:",
 "Scala es un lenguaje de tipado estático, lo que significa que los tipos desempeñan un papel sintáctico destacado y que la comprobación de tipos la impone el propio compilador. Por ejemplo, no podemos declarar funciones sin indicar explícitamente los tipos de entrada:"),

("> __Scala__: question marks `???` are used to indicate that function body is not finished.",
 "> __Scala__: los signos de interrogación `???` se usan para indicar que el cuerpo de la función está sin terminar."),

("It's mandatory to specify the type of the input arguments:",
 "Es obligatorio especificar el tipo de los argumentos de entrada:"),

("The return type is optional (the compiler can infer it - more on this later), but it's good practice to annotate it:",
 "El tipo de retorno es opcional (el compilador puede inferirlo, y de eso hablaremos más adelante), pero es buena práctica anotarlo:"),

("Let's complete the implementation, so that we can move forward:",
 "Completemos la implementación, para poder seguir adelante:"),

("We will explain later on the syntax of the function body, in particular, the  `x.length` expression.",
 "Más adelante explicaremos la sintaxis del cuerpo de la función y, en particular, la expresión `x.length`."),

("Let's see now the differences with respect to the Python implementation. If we invoke this function with the right arguments, everything is fine:",
 "Veamos ahora las diferencias con respecto a la implementación en Python. Si invocamos esta función con los argumentos correctos, todo va bien:"),

("Similarly to the Python implementation, if we invoke the function with a non-string value, an error will be raised:",
 "Igual que en la implementación en Python, si invocamos la función con un valor que no es una cadena, se producirá un error:"),

("This error is a _type error_, as in the Python case: it was expected a value of type `String`, but an `Int` was found. However, this error is raised at _compile time_, not at runtime. This means that the program was not even executed, since \"Compilation failed\". Note that in the case of Python, the error pointed to the `len` function, meaning that the program was actually being exectued. On the contrary, the Scala compiler raises the error without actually looking at the function body.",
 "Este error es un _error de tipos_, como en el caso de Python: se esperaba un valor de tipo `String` y se encontró un `Int`. Pero este error se produce en _tiempo de compilación_, no en tiempo de ejecución. Es decir, el programa ni siquiera llegó a ejecutarse, porque «Compilation failed». Nótese que en el caso de Python el error señalaba a la función `len`, lo que significa que el programa sí se estaba ejecutando. El compilador de Scala, en cambio, lanza el error sin mirar siquiera el cuerpo de la función."),

("In Scala, there are also type errors that can be reported at runtime, but in order to get those, we have to cheat the compiler. For instance, we can force the compiler to ignore that value `111` is not an integer, but a string, using the `asInstanceOf[String]` expression:",
 "En Scala también hay errores de tipos que pueden aparecer en tiempo de ejecución, pero para conseguirlos hay que engañar al compilador. Por ejemplo, podemos forzarlo a ignorar que el valor `111` no es un entero, sino una cadena, mediante la expresión `asInstanceOf[String]`:"),

("> We write the `is_even_length` expression within the `foo` function in order to prevent the inmediate execution by Jupyter",
 "> Escribimos la expresión `is_even_length` dentro de la función `foo` para evitar que Jupyter la ejecute de inmediato"),

("In doing so, we are actually saying to the compiler: \"trust me, this is a string\". Then, the compiler will happily trust our judgement and the expression will type-check. However, when we try to execute this program:",
 "Al hacerlo le estamos diciendo al compilador: «confía en mí, esto es una cadena». Y el compilador se fía de nuestro criterio sin más, con lo que la expresión pasa la comprobación de tipos. Sin embargo, cuando intentamos ejecutar este programa:"),

("an exception will be raised _at runtime_, reporting the obvious type error. The moral is clear:",
 "se lanza una excepción _en tiempo de ejecución_, que informa del evidente error de tipos. La moraleja está clara:"),

("> DO NOT USE `asInstanceOf[_]`, it's not type-safe.",
 "> NO USES `asInstanceOf[_]`: no es seguro respecto a los tipos."),

("During this course, we won't use this unsafe features of the Scala programming language. It's completely forbidden.",
 "A lo largo de este curso no usaremos estas características inseguras del lenguaje Scala. Están completamente prohibidas."),

("This example shows that type ckecks are not only performed by the Scala compiler, but by the generated code as well. On the other hand, note that the error is reported in the form of a `ClassCastException`. Exceptions are the way in which runtime errors are reported, and there are many standard errors. For instance, if we try to divide by 0:",
 "Este ejemplo muestra que las comprobaciones de tipos no las hace solo el compilador de Scala, sino también el código generado. Por otro lado, nótese que el error se informa en forma de `ClassCastException`. Las excepciones son la manera en que se informa de los errores en tiempo de ejecución, y hay muchos errores estándar. Por ejemplo, si intentamos dividir por 0:"),

("the compiler won't detect any problem (it could with little effort, by the way), but an `ArithmeticException` will be raised if we attempt to execute that expression:",
 "el compilador no detectará ningún problema (podría, con poco esfuerzo, por cierto), pero se lanzará una `ArithmeticException` si intentamos ejecutar esa expresión:"),

("By the way, note that these exceptions are actually called `java.lang.*`. What does all this have to do with the Java language? Well, a Scala program is actually compiled into Java, and eventually run by the Java Virtual Machine. The standard library of Scala reuses some many features of Java, including the above exceptions, and basic types such as the `java.lang.String` itself.",
 "Por cierto, nótese que estas excepciones se llaman en realidad `java.lang.*`. ¿Qué tiene que ver todo esto con el lenguaje Java? Pues bien, un programa Scala se compila en realidad a Java, y acaba ejecutándose en la Máquina Virtual de Java. La biblioteca estándar de Scala reutiliza bastantes elementos de Java, incluidas las excepciones anteriores y tipos básicos como `java.lang.String`."),

("# Type-inference", "# Inferencia de tipos"),

(
"""Ok, type annotations allow us to anticipate problems at runtime, but it's annoying to have to explicitly annotate our signatures with types. For instance, the returning `Boolean` type of the `is_even_length` function is completely redundant: it's clear from the function body that the function will return a boolean value.

Fortunately, the Scala compiler is clever enough to perform this kind of type inference itself, and will allow us to get rid of the returned type in this case:""",
"""Muy bien: las anotaciones de tipo nos permiten anticipar problemas que aparecerían en tiempo de ejecución, pero resulta molesto tener que anotar explícitamente nuestras signaturas con tipos. Por ejemplo, el tipo `Boolean` de retorno de la función `is_even_length` es completamente redundante: está claro, por el cuerpo de la función, que va a devolver un valor booleano.

Por suerte, el compilador de Scala es lo bastante listo para hacer él mismo esa inferencia de tipos, y nos permite prescindir del tipo de retorno en este caso:"""),

("However, we will be commonly write the returned type of function signatures, since it will allow us to know what is (partially) doing the function, without actually looking inside the function body. It aids understanding.",
 "Con todo, lo habitual será que escribamos el tipo de retorno en las signaturas de las funciones, porque nos permite saber qué hace la función —en parte— sin necesidad de mirar dentro de su cuerpo. Ayuda a entenderla."),

("# Type-ascription", "# Ascripción de tipos"),

("Besides functions and datatype signatures, expressions can also feature type occurrences. It happens when we call _generic_ functions (e.g. `asInstanceOf[_]`), but also in the case of [_type ascriptions_](https://docs.scala-lang.org/style/types.html#ascription):",
 "Además de en las signaturas de funciones y de tipos de datos, los tipos también pueden aparecer en las expresiones. Ocurre cuando llamamos a funciones _genéricas_ (como `asInstanceOf[_]`), pero también en el caso de las [_ascripciones de tipo_](https://docs.scala-lang.org/style/types.html#ascription):"),

("With type ascriptions, we are saying to the compiler: \"note that value `1` is of type `Int`\". In this case, it's completely redundant because the compiler can figure it out itself. In other cases, however, the Scala compiler might struggle without success to find the right type of an expression, and we will have to help it a little bit. This may happen, for instance, when some value have several types because of inheritance.",
 "Con una ascripción de tipo le estamos diciendo al compilador: «fíjate en que el valor `1` es de tipo `Int`». En este caso es completamente redundante, porque el compilador puede deducirlo por sí solo. En otros casos, sin embargo, el compilador de Scala puede pelearse sin éxito por encontrar el tipo correcto de una expresión, y tendremos que ayudarlo un poco. Esto puede ocurrir, por ejemplo, cuando un valor tiene varios tipos por causa de la herencia."),

("# Advantages of static typing", "# Ventajas del tipado estático"),

(
"""We can summarize the advantages of using types at the source level as follows:

* __Self-explanatory documentation.__ Types do not allow us to dispense with comments, but they certainly reduce the burden. Indeed, type signatures can be regarded as _partial_ specifications of the required functionality, so that comments can focuse in more essential aspects.

* __Prevent errors in advance.__ As Robin Milner put it: "type-checked programs can't go wrong": if the program compiles, it won't raised errors at runtime. Going further, a popular saying in the functional community is: "if it compiles, it _works_".

* __Better aids for IDEs.__ IDEs can leverage type annotations by providing the user with extra functionality such as: showing methods to be used for those types, etc.

* __Type-driven development.__ We will speak about this in long detail in forthcoming lectures.""",
"""Podemos resumir así las ventajas de usar tipos a nivel de código fuente:

* __Documentación que se explica sola.__ Los tipos no nos permiten prescindir de los comentarios, pero desde luego aligeran la carga. De hecho, las signaturas de tipos pueden verse como especificaciones _parciales_ de la funcionalidad requerida, de modo que los comentarios pueden centrarse en los aspectos más esenciales.

* __Prevenir errores por adelantado.__ Como dijo Robin Milner: «los programas que pasan la comprobación de tipos no pueden fallar»; si el programa compila, no lanzará errores en tiempo de ejecución. Y llevándolo más lejos, hay un dicho popular en la comunidad funcional: «si compila, _funciona_».

* __Mejor ayuda de los IDEs.__ Los IDEs pueden aprovechar las anotaciones de tipo para ofrecer funcionalidad adicional: mostrar los métodos aplicables a esos tipos, etc.

* __Desarrollo dirigido por tipos.__ De esto hablaremos con detalle en clases posteriores."""),

# ------------------------------------------------- comentarios del template de 2.2
("// Missing signature", "// Falta la signatura"),
("// now with types", "// ahora con tipos"),
("// now with input and output types", "// ahora con tipos de entrada y de salida"),
("// full implementation", "// implementación completa"),
("// right invocations", "// invocaciones correctas"),
("// wrong input types: type mismatch", "// tipos de entrada incorrectos: type mismatch"),
("// cheating the compiler", "// engañando al compilador"),
("// but when we run this code: ClassCastException", "// pero al ejecutar este código: ClassCastException"),
("// Another type of runtime error, not catched by at compile-time",
 "// Otro tipo de error en tiempo de ejecución, que no se detecta al compilar"),
("// But when we run the code", "// Pero al ejecutar el código"),
("// is_even_length without explicit return type", "// is_even_length sin tipo de retorno explícito"),
("// 1+2 with type ascriptions", "// 1+2 con ascripciones de tipo"),

# ---------------------------------------------------------------- 2.5 Exercises (+Sols)
(
"""# Topic 2. Strongly-typed vs. Dynamic languages

## Exercises""",
"""# Tema 2. Lenguajes de tipado fuerte frente a lenguajes dinámicos

## Ejercicios"""),

(DIV + """
Write a function that computes the sum of the proper divisors of a given number (i.e., excluding itself)</a>.
</div>""",
 DIV + """
Escribe una función que calcule la suma de los divisores propios de un número dado (es decir, excluyéndolo a él mismo).
</div>"""),

(DIV + """
Use the `sumDivisors` function to test if two numbers are <a href="https://en.wikipedia.org/wiki/Amicable_numbers">amicable</a>, and to check wether a given number is <a href="https://en.wikipedia.org/wiki/Perfect_number">perfect</a>.
</div>""",
 DIV + """
Usa la función `sumDivisors` para comprobar si dos números son <a href="https://en.wikipedia.org/wiki/Amicable_numbers">amigos</a>, y si un número dado es <a href="https://en.wikipedia.org/wiki/Perfect_number">perfecto</a>.
</div>"""),

(DIV + """
Write a function that prints to the console the pairs of amicable numbers less than a given number.
</div>""",
 DIV + """
Escribe una función que imprima por consola las parejas de números amigos menores que un número dado.
</div>"""),

(DIV + """
Write a function that returns the product of the members of a finite arithmetic progression with an initial element <em>a</em>, common differences <em>d</em>, and <em>n</em> elements.
</div>""",
 DIV + """
Escribe una función que devuelva el producto de los términos de una progresión aritmética finita con elemento inicial <em>a</em>, diferencia común <em>d</em> y <em>n</em> elementos.
</div>"""),
]
