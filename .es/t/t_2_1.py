# -*- coding: utf-8 -*-
"""Traducción de PF-1/topic2/2.1 DynamicTyping (y su template)."""

PAIRS = [
(
"""# Topic 2. Strongly-typed vs. Dynamic languages

## 2.1 Dynamically-typed language""",
"""# Tema 2. Lenguajes de tipado fuerte frente a lenguajes dinámicos

## 2.1 Un lenguaje de tipado dinámico"""),

("# Types and values",
 "# Tipos y valores"),

(
"""Values are literals like `1`, `"hola"`, `true`, `'a'`, etc.; types allow us to classify values into different collections. For instance:
* `0`, `1`, `2` and `3` belong to the collection, or type of, _natural_ numbers
* `"hola"`, `"hi"`, `"bye"`, `"adios"` and `""` are _string_ values
* _images_, _vectors_, _binary numbers_, _week days_, etc., are also types.

Why do we need types in computing? For one thing, types allow us to explain why we can't apply a given operation to certain arguments. For instance, we can't (i.e. it's meaningless) to multiply _boolean_ values with _strings_. It only makes sense if both arguments are values of _numeric types_, such as _integers_, _reals_, etc. But types also serve of great help from a methodological point of view, as we will see when we study type-driven development in the forthcoming lectures.""",
"""Los valores son literales como `1`, `"hola"`, `true`, `'a'`, etc.; los tipos nos permiten clasificar los valores en colecciones distintas. Por ejemplo:
* `0`, `1`, `2` y `3` pertenecen a la colección, o tipo, de los números _naturales_
* `"hola"`, `"hi"`, `"bye"`, `"adios"` y `""` son valores de tipo _cadena_
* las _imágenes_, los _vectores_, los _números binarios_, los _días de la semana_, etc., son también tipos.

¿Por qué necesitamos tipos en computación? Por un lado, los tipos nos permiten explicar por qué no podemos aplicar una operación determinada a ciertos argumentos. Por ejemplo, no podemos —es decir, no tiene sentido— multiplicar valores _booleanos_ por _cadenas_. Solo tiene sentido si ambos argumentos son valores de _tipos numéricos_: _enteros_, _reales_, etc. Pero los tipos son además de gran ayuda desde el punto de vista metodológico, como veremos al estudiar el desarrollo dirigido por tipos (_type-driven development_) en las próximas clases."""),

("# Types in Python",
 "# Los tipos en Python"),

("Apparently, there are no types in Python, at least at the source level. For instance, let's consider the following function, which checks whether the length of the input string is even:",
 "Aparentemente, en Python no hay tipos, al menos a nivel de código fuente. Consideremos, por ejemplo, la siguiente función, que comprueba si la longitud de la cadena de entrada es par:"),

("Recall the definition of the `len` function:",
 "Recordemos la definición de la función `len`:"),

("Then, the following invocations work as expected:",
 "Con ella, las siguientes invocaciones funcionan como cabía esperar:"),

# el template trae "excepted" por "expected": errata del original, misma traducción
("Then, the following invocations work as excepted:",
 "Con ella, las siguientes invocaciones funcionan como cabía esperar:"),

("What does it happen if we invoke the `is_even_length` function with an argument which is not a string?",
 "¿Qué ocurre si invocamos la función `is_even_length` con un argumento que no es una cadena?"),

(
"""Now, errors show up explicitly, though not at compile time, but at _runtime_, i.e. when the program is executed. Note the difference:
* Compile-time errors. Errors reported when the Python compiler process your source code.
* Runtime errors. Errors reported while the program is being run.

An example of compile-time error might be produced by syntactically-ill programs:""",
"""Ahora los errores se manifiestan de forma explícita, aunque no en tiempo de compilación, sino en _tiempo de ejecución_, es decir, cuando el programa se ejecuta. Nótese la diferencia:
* Errores en tiempo de compilación. Los que se notifican cuando el compilador de Python procesa el código fuente.
* Errores en tiempo de ejecución. Los que se notifican mientras el programa se está ejecutando.

Un ejemplo de error en tiempo de compilación es el que producen los programas sintácticamente incorrectos:"""),

(
"""In this case, the program is not even run; the compiler prevents this and shows a syntax error instead.

On the other hand, our type error is thrown at runtime, i.e. type checking is performed at runtime. In these cases, we talk of __dynamically-typed languages__. When type checking is performed at compile-time, and the error is thrown by the compiler, we talk of __statically-typed languages__.""",
"""En este caso el programa ni llega a ejecutarse: el compilador lo impide y muestra un error de sintaxis.

Nuestro error de tipos, en cambio, se lanza en tiempo de ejecución; es decir, la comprobación de tipos se hace en tiempo de ejecución. En estos casos hablamos de __lenguajes de tipado dinámico__. Cuando la comprobación de tipos se hace en tiempo de compilación, y es el compilador el que lanza el error, hablamos de __lenguajes de tipado estático__."""),

("# Type annotations",
 "# Anotaciones de tipo"),

("Since version 3.5, however, Python allows for [typing annotations](https://docs.python.org/3/library/typing.html):",
 "Desde la versión 3.5, sin embargo, Python admite [anotaciones de tipo](https://docs.python.org/3/library/typing.html):"),

("But, alas, the compiler won't type check our code, and the following code compiles",
 "Pero, ay, el compilador no va a comprobar los tipos de nuestro código, y el siguiente programa compila"),

("The type-checking task is delegated to IDEs (like VSCode), which will highlight potential errors via warnings.",
 "La tarea de comprobar los tipos se delega en los IDEs (como VSCode), que señalan los posibles errores mediante avisos."),

("You may want to check [this post](https://towardsdatascience.com/type-annotations-in-python-d90990b172dc) for further information.",
 "Puedes consultar [esta entrada](https://towardsdatascience.com/type-annotations-in-python-d90990b172dc) si quieres más información."),
]
