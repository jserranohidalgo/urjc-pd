PAIRS = [
("# Topic 3. Algebraic data types\n\n## 3.1 Functions",
 "# Tema 3. Tipos algebraicos de datos\n\n## 3.1 Funciones"),

("""This is a small introduction to functions from the point of view of functional programming _and_ software engineering. It ends with a discussion about the algebraic nature of functions and the basic way in which functions are represented in an object-oriented programming language like Scala.

These are the goals of this section:

* Understanding the difference between impure vs. pure functions: the main tenet of functional programming
* Understanding how functions act as a modularity mechanism: the software engineering perspective
* Introducing functions as values: enabling higher-order functions
* Currying and composition: HOFs in action as modularity mechanism
* Understanding _generic_ signatures: parametric polymorphism as another modularity mechanism
* Understanding the algebraic nature of functions
* Knowing how Scala represents function-values and different syntactic niceties""",
 """Esta es una pequeña introducción a las funciones desde el punto de vista de la programación funcional _y_ de la ingeniería del software. Termina con una discusión sobre la naturaleza algebraica de las funciones y la forma básica en que se representan las funciones en un lenguaje de programación orientado a objetos como Scala.

Estos son los objetivos de esta sección:

* Entender la diferencia entre funciones impuras y puras: el principio fundamental de la programación funcional
* Entender cómo las funciones actúan como mecanismo de modularidad: la perspectiva de la ingeniería del software
* Introducir las funciones como valores: lo que habilita las funciones de orden superior
* Currificación y composición: las HOF en acción como mecanismo de modularidad
* Entender las signaturas _genéricas_: el polimorfismo paramétrico como otro mecanismo de modularidad
* Entender la naturaleza algebraica de las funciones
* Conocer cómo representa Scala los valores función y sus distintas facilidades sintácticas"""),

("## What are (pure) functions?", "## ¿Qué son las funciones (puras)?"),

("Functions are computational devices that transform input _values_ into output _values_, and do nothing _else_.",
 "Las funciones son dispositivos computacionales que transforman _valores_ de entrada en _valores_ de salida, y no hacen nada _más_."),

("If we run this function, the only thing that happens is the computation of a new value:",
 "Si ejecutamos esta función, lo único que ocurre es el cálculo de un nuevo valor:"),

("Functions that do something else, besides returning values, are called _impure_ functions. Functional programming deals only with _pure_, or mathematical, functions. For instance, this is not a pure function:",
 "Las funciones que hacen algo más, además de devolver valores, se llaman funciones _impuras_. La programación funcional trata solo con funciones _puras_, o matemáticas. Por ejemplo, esta no es una función pura:"),

("If we run this function, we will see an _effect_ in the console (besides the pure computation of `input + 1`):",
 "Si ejecutamos esta función, veremos un _efecto_ en la consola (además del cálculo puro de `input + 1`):"),

("There are many kinds of effects: writing to the console, reading from the keyboard, reading from a socket, calling a web service, executing a query over the database, updating a global variable, etc. Clearly, we need effects if we want our programs to do something useful, so pure functions alone are not enough. We will talk about this later on.",
 "Hay muchos tipos de efectos: escribir en la consola, leer del teclado, leer de un socket, llamar a un servicio web, ejecutar una consulta sobre la base de datos, actualizar una variable global, etc. Está claro que necesitamos efectos si queremos que nuestros programas hagan algo útil, así que las funciones puras por sí solas no son suficientes. Hablaremos de esto más adelante."),

("""#### Exercise
<div class="alert alert-info">
    Given the following program, evaluate whether it is pure or impure, and specify the type of side effect if the program is considered impure.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Dado el siguiente programa, evalúa si es puro o impuro, y especifica el tipo de efecto secundario si el programa se considera impuro.
</div>"""),

("##### Solution", "##### Solución"),

("The function is impure since it does something else to simple calculating the power of two numbers: it updates the global variable `i` each time the function executes.",
 "La función es impura ya que hace algo más aparte de calcular simplemente la potencia de dos números: actualiza la variable global `i` cada vez que la función se ejecuta."),

("##### Your solution", "##### Tu solución"),

("## Functions as modularity devices", "## Las funciones como dispositivos de modularidad"),

("""Modularity can be explained in reference to the process whereby we refactor a piece of monolythic code in order to obtain a better design (one with better reusability guarantees, undertandability, maintenance, etc.). A monolyth is characterised by a number of intermingled features, represented in the image by blue, red and green _spaghetti_. The important thing is that the blue concern is repeated in programs _p1_ and _p2_, not only conceptually, but physically - in the sense that this code is copy-pasted. How could we design these components so that we can reuse this blue concern? We can abstract that blue concern in a new abstract module, and design components _p1_ and _p2_ in a more modular way combining this new reusable module with the red and green concerns.

The important thing to remember is that a modular component is characterised by being made of different subcomponents that implement different concerns.""",
 """La modularidad puede explicarse en referencia al proceso mediante el cual refactorizamos un fragmento de código monolítico para obtener un diseño mejor (uno con mejores garantías de reutilización, comprensibilidad, mantenimiento, etc.). Un monolito se caracteriza por un conjunto de funcionalidades entremezcladas, representadas en la imagen como _espagueti_ azul, rojo y verde. Lo importante es que la responsabilidad azul se repite en los programas _p1_ y _p2_, no solo conceptualmente, sino físicamente, en el sentido de que este código está copiado y pegado. ¿Cómo podríamos diseñar estos componentes para poder reutilizar esa responsabilidad azul? Podemos abstraer esa responsabilidad azul en un nuevo módulo abstracto, y diseñar los componentes _p1_ y _p2_ de una forma más modular combinando este nuevo módulo reutilizable con las responsabilidades roja y verde.

Lo importante que hay que recordar es que un componente modular se caracteriza por estar formado por distintos subcomponentes que implementan distintas responsabilidades."""),

("Why are functions so important in programming? Because they help us to _modularize_ our code; they are modularity devices. For instance, let's consider the following programs, which access the following data structure of key-value pairs (we will talk about this structure in detail later on):",
 "¿Por qué son tan importantes las funciones en programación? Porque nos ayudan a _modularizar_ nuestro código; son dispositivos de modularidad. Por ejemplo, consideremos los siguientes programas, que acceden a la siguiente estructura de datos de pares clave-valor (hablaremos de esta estructura en detalle más adelante):"),

("""Our first program access the configuration data for the value of the "URL" key. If it's not found, then the default value "default.url" is returned (similarly, we will discuss the `match` keyword further in the course).""",
 """Nuestro primer programa accede a los datos de configuración para obtener el valor de la clave "URL". Si no se encuentra, se devuelve el valor por defecto "default.url" (de forma similar, hablaremos de la palabra clave `match` más adelante en el curso)."""),

("""Our second program accesses the configuration data for the value of the "PORT" key. If it's not found, then the default value "8080" is returned.""",
 """Nuestro segundo programa accede a los datos de configuración para obtener el valor de la clave "PORT". Si no se encuentra, se devuelve el valor por defecto "8080"."""),

("These two programs do _almost_ the same. The only differences lie in the particular keys and default values the programs refer to, but, otherwise, they do the same thing. However, this _common factor_ is not reflected in the code. Indeed, we may get one program from the other by copy-pasting, a clear signal of [code-smell](https://en.wikipedia.org/wiki/Code_smell).",
 "Estos dos programas hacen _casi_ lo mismo. Las únicas diferencias residen en las claves concretas y los valores por defecto a los que se refieren los programas, pero, por lo demás, hacen lo mismo. Sin embargo, este _factor común_ no se refleja en el código. De hecho, podemos obtener un programa a partir del otro copiando y pegando, una señal clara de [code smell](https://en.wikipedia.org/wiki/Code_smell)."),

("These programs are _monolythic_, in the sense that they are not made by composing large enough modules. In this case, the common logic of the program and the values it operates on are intermingled in the same code.",
 "Estos programas son _monolíticos_, en el sentido de que no están hechos componiendo módulos suficientemente grandes. En este caso, la lógica común del programa y los valores sobre los que opera están entremezclados en el mismo código."),

("How can we abstract away the differences and package the common logic in a single module? With functions:",
 "¿Cómo podemos abstraer las diferencias y empaquetar la lógica común en un único módulo? Con funciones:"),

("This is an abstract module which we can be combined with other modules to get back the very same functionality:",
 "Este es un módulo abstracto que podemos combinar con otros módulos para recuperar exactamente la misma funcionalidad:"),

("""In this case, we combine the module `getKeyFrom` with the modules (data values and variables, in particular) `config`, `"URL"` and `"default.url"`. The composition method is just simple function application.""",
 """En este caso, combinamos el módulo `getKeyFrom` con los módulos (valores de datos y variables, en particular) `config`, `"URL"` y `"default.url"`. El método de composición es simplemente la aplicación de la función."""),

("Which are the advantages of using functions? As in the general case, having a more modular solution enables _reuse_, particularly of those modules which are abstract or parameterised. For instance, we can benefit from this level of reuse by re-implementing the `url` program in the following way:",
 "¿Cuáles son las ventajas de usar funciones? Como en el caso general, tener una solución más modular habilita la _reutilización_, en particular de aquellos módulos que son abstractos o parametrizados. Por ejemplo, podemos beneficiarnos de este nivel de reutilización reimplementando el programa `url` de la siguiente manera:"),

("""#### Exercise
<div class="alert alert-info">
    Reimplement the following monolithic program in a more modular way, using the <code>getKeyFrom</code> function.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Reimplementa el siguiente programa monolítico de una forma más modular, usando la función <code>getKeyFrom</code>.
</div>"""),

("## Functions as methods", "## Las funciones como métodos"),

("In an object-oriented language, functions are implemented through _methods_, i.e. using the `def` keyword. Note that these methods are invariably part of an `object`, `class` or `trait` declaration. Typically, pure functions are declared as part of objects. For instance, we may declare a set of arithmetic functions as follows:",
 "En un lenguaje orientado a objetos, las funciones se implementan mediante _métodos_, es decir, usando la palabra clave `def`. Nótese que estos métodos son invariablemente parte de una declaración `object`, `class` o `trait`. Habitualmente, las funciones puras se declaran como parte de objetos. Por ejemplo, podemos declarar un conjunto de funciones aritméticas de la siguiente manera:"),

("The functions `circle` and `rectangle` are defined as _methods_ of the object `Areas`. So, we execute these functions by invoking these methods:",
 "Las funciones `circle` y `rectangle` se definen como _métodos_ del objeto `Areas`. Así, ejecutamos estas funciones invocando estos métodos:"),

("In notebooks and the Scala REPL, `def` declarations appear to be independent from any object or class:",
 "En los notebooks y en la REPL de Scala, las declaraciones `def` parecen ser independientes de cualquier objeto o clase:"),

("But they are not, they are actually methods defined for an internal class of the almond kernel named `Helper`. So, when we execute our function `foo`:",
 "Pero no lo son: en realidad son métodos definidos para una clase interna del kernel almond llamada `Helper`. Así, cuando ejecutamos nuestra función `foo`:"),

("This is a convenient abbreviation of the following invocation:",
 "Esto es una abreviatura conveniente de la siguiente invocación:"),

("which shows that `fooCell` is the object of class `Helper` where the method `foo` is defined.",
 "lo que muestra que `fooCell` es el objeto de la clase `Helper` donde se define el método `foo`."),

("""#### Exercise
<div class="alert alert-info">
    Implement a function that computes the area of an ellipse as a method of the object <code>Areas</code>. Recall the area of an ellipse is <code>Pi*a*b</code>, where <code>a</code> and <code>b</code> are the lengths of the semi-major and semi-minor axes.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Implementa una función que calcule el área de una elipse como método del objeto <code>Areas</code>. Recuerda que el área de una elipse es <code>Pi*a*b</code>, donde <code>a</code> y <code>b</code> son las longitudes de los semiejes mayor y menor.
</div>"""),

("## Functions as values", "## Las funciones como valores"),

("Functions can also be represented as _values_, i.e. as objects. This allows us to implement functions that receive other functions as arguments, or return functions as results. This special functions are called _higher-order functions_ (HOF), and they serve as a great modularity device.",
 "Las funciones también pueden representarse como _valores_, es decir, como objetos. Esto nos permite implementar funciones que reciben otras funciones como argumentos, o que devuelven funciones como resultado. Estas funciones especiales se llaman _funciones de orden superior_ (HOF), y sirven como un gran dispositivo de modularidad."),

("In order to represent functions as values, first we need to make extremely clear the difference between variables, values and types. For instance:",
 "Para representar las funciones como valores, primero tenemos que dejar extremadamente clara la diferencia entre variables, valores y tipos. Por ejemplo:"),

("""In these definitions:
* We found three __variables__: `i`, `s` and `b`.
* These variables are assigned three __values__: `3`, `"hi"` and `true`.
* The __types__ of these values are, respectively: `Int`, `String` and `Boolean`.""",
 """En estas definiciones:
* Encontramos tres __variables__: `i`, `s` y `b`.
* A estas variables se les asignan tres __valores__: `3`, `"hi"` y `true`.
* Los __tipos__ de estos valores son, respectivamente: `Int`, `String` y `Boolean`."""),

("Now, let's consider these other variables `addOneV` and `substractOneV`. They are intended to represent values equivalent to the following function-methods:",
 "Ahora, consideremos estas otras variables `addOneV` y `substractOneV`. Su intención es representar valores equivalentes a las siguientes funciones-método:"),

("""Here, we also have variables, values and types:
* The two _variables_ are named `addOneV` and `substractOneV`.
* They are assigned the _function values_ `(a: Int) => a+1` and `(a: Int) => a - 1`.
* The type of these values is the same _function type_ `Int => Int`.

A function-value is also known as a _lambda expression_. Note that a function value is made of two parts: the input arguments and the function body: `(...input...) => body`. The input arguments declare new variables, each of them of a particular type, that will be assigned to certain values when they are passed to the function (upon invocation). The function body has to be an expression of the type specified as output by the function type.""",
 """Aquí, también tenemos variables, valores y tipos:
* Las dos _variables_ se llaman `addOneV` y `substractOneV`.
* Se les asignan los _valores función_ `(a: Int) => a+1` y `(a: Int) => a - 1`.
* El tipo de estos valores es el mismo _tipo función_ `Int => Int`.

Un valor función también se conoce como _expresión lambda_. Nótese que un valor función está formado por dos partes: los argumentos de entrada y el cuerpo de la función: `(...entrada...) => cuerpo`. Los argumentos de entrada declaran nuevas variables, cada una de un tipo concreto, a las que se asignarán ciertos valores cuando se pasen a la función (en el momento de la invocación). El cuerpo de la función debe ser una expresión del tipo especificado como salida por el tipo función."""),

("Function-values are equivalent to function-methods in the sense that they behave exactly in the same way, i.e. they allow us to compute values from other values that we pass as input:",
 "Los valores función son equivalentes a las funciones-método en el sentido de que se comportan exactamente igual, es decir, nos permiten calcular valores a partir de otros valores que pasamos como entrada:"),

("> ![image.png](../../images/scala3api3.jpg) As any other value in Scala, functions are objects and they have a class. In the case of functions that receive a single argument, this class is named [Function1](https://dotty.epfl.ch/api/scala/Function1.html)",
 "> ![image.png](../../images/scala3api3.jpg) Como cualquier otro valor en Scala, las funciones son objetos y tienen una clase. En el caso de las funciones que reciben un único argumento, esta clase se llama [Function1](https://dotty.epfl.ch/api/scala/Function1.html)"),

("""#### Exercise
<div class="alert alert-info">
    Implement a function which receives a single argument of type Char and returns its decimal representation. Assign this function to a variable named <code>code</code>. Assign the codes of chars 'c' and '@' to variables <code>codeOfc</code> and <code>codeOfaT</code>.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Implementa una función que reciba un único argumento de tipo Char y devuelva su representación decimal. Asigna esta función a una variable llamada <code>code</code>. Asigna los códigos de los caracteres 'c' y '@' a las variables <code>codeOfc</code> y <code>codeOfaT</code>.
</div>"""),

("## Higher-order functions", "## Funciones de orden superior"),

("But then, which are the advantages of function values? Basically, they allow us to implement higher-order functions (HOFs), i.e. functions that receive and/or return other functions. For instance, let's say that we want to implement a HOF that receives an integer-to-integer function, such as `addOneM`and `substractOneM`, and calls this function over a given number. We may want to write something like this:",
 "Entonces, ¿cuáles son las ventajas de los valores función? Básicamente, nos permiten implementar funciones de orden superior (HOF), es decir, funciones que reciben y/o devuelven otras funciones. Por ejemplo, supongamos que queremos implementar una HOF que reciba una función entero-a-entero, como `addOneM` y `substractOneM`, y llame a esta función sobre un número dado. Podríamos querer escribir algo así:"),

("where the first argument `int2int` attempts to represent any function that receives an integer and returns another integer.",
 "donde el primer argumento `int2int` intenta representar cualquier función que reciba un entero y devuelva otro entero."),

("But this code is not legal in Scala, because arguments to functions need to be values, not methods. That's why we need function-values!",
 "Pero este código no es válido en Scala, porque los argumentos de las funciones tienen que ser valores, no métodos. ¡Por eso necesitamos valores función!"),

("which we can use as follows:", "que podemos usar de la siguiente manera:"),

("And we can even pass function-methods that are converted on the fly to function-values!",
 "¡E incluso podemos pasar funciones-método que se convierten sobre la marcha en valores función!"),

("This conversion is the so-called _eta-expansion_.", "Esta conversión es la llamada _eta-expansión_."),

("""#### Exercise
<div class="alert alert-info">
    Implement a function <code>square</code> which calculates the square of an integer both as a function-method and as function-value. Obtain the square of numbers 2 and 3 using the <code>call</code> HOF using both versions.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Implementa una función <code>square</code> que calcule el cuadrado de un entero, tanto como función-método como función-valor. Obtén el cuadrado de los números 2 y 3 usando la HOF <code>call</code> con ambas versiones.
</div>"""),

("## Currying", "## Currificación"),

("What about functions that receive more than one argument? We would like to implement the function-value equivalent of this function-method:",
 "¿Qué pasa con las funciones que reciben más de un argumento? Nos gustaría implementar el equivalente en función-valor de esta función-método:"),

("We do that as follows:", "Lo hacemos de la siguiente manera:"),

("> ![image.png](../../images/scala3api3.jpg) Functions of two arguments are represented as values/objects of the [`Function2`](https://dotty.epfl.ch/api/scala/Function2.html) class.",
 "> ![image.png](../../images/scala3api3.jpg) Las funciones de dos argumentos se representan como valores/objetos de la clase [`Function2`](https://dotty.epfl.ch/api/scala/Function2.html)."),

("However, function types of two, three, etc., arguments are not extrictly necessary, and sometimes we can get along with functions of one argument. But, how can we create a function of two arguments with functions of one argument alone? HOFs to the rescue! The trick is the following:",
 "Sin embargo, los tipos función de dos, tres, etc., argumentos no son estrictamente necesarios, y a veces podemos arreglárnoslas con funciones de un único argumento. Pero, ¿cómo podemos crear una función de dos argumentos usando solo funciones de un argumento? ¡Las HOF al rescate! El truco es el siguiente:"),

("Note that brackets in `Int => (Int => Int)` are used for clarity, but are not needed. Basically, we created a function of one argument that returns another function of one argument. So, the expression:",
 "Nótese que los paréntesis en `Int => (Int => Int)` se usan por claridad, pero no son necesarios. Básicamente, hemos creado una función de un argumento que devuelve otra función de un argumento. Así, la expresión:"),

("returns a function that can be applied again:", "devuelve una función que puede volver a aplicarse:"),

("We can apply this strategy to functions with any number of arguments. This process is known as currying, and the resulting functions are called curried functions. The analogous concept in function-methods involves using [multiple-parameter lists](https://docs.scala-lang.org/tour/multiple-parameter-lists.html):",
 "Podemos aplicar esta estrategia a funciones con cualquier número de argumentos. Este proceso se conoce como currificación, y las funciones resultantes se llaman funciones currificadas. El concepto análogo en las funciones-método implica usar [listas de parámetros múltiples](https://docs.scala-lang.org/tour/multiple-parameter-lists.html):"),

("Note that `Function2` functions have a method `curried` that allows us to transform a _function2_ function into its curried form:",
 "Nótese que las funciones `Function2` tienen un método `curried` que nos permite transformar una función _function2_ en su forma currificada:"),

("""#### Exercise
<div class="alert alert-info">
    Implement the following function as a curried function-value.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Implementa la siguiente función como una función-valor currificada.
</div>"""),

("## Functions compose", "## Las funciones componen"),

("We can create new functions by composing other functions whose signatures match. This is great from a modularity perspective. For instance, the following function is implemented in a non-modular way:",
 "Podemos crear nuevas funciones componiendo otras funciones cuyas signaturas encajen. Esto es estupendo desde una perspectiva de modularidad. Por ejemplo, la siguiente función está implementada de una forma no modular:"),

("This function is somehow the combination of two more basic functions `length` and `isEven`:",
 "Esta función es, en cierto modo, la combinación de dos funciones más básicas, `length` e `isEven`:"),

("We can observe the same pattern in the following function:", "Podemos observar el mismo patrón en la siguiente función:"),

("which somehow is made up of functions `_.toInt` and `isOdd`:",
 "que, en cierto modo, está formada por las funciones `_.toInt` e `isOdd`:"),

("However, the composition pattern is _not_ explicit in the implementations of the `isEvenLength` and `isOddNumber` functions . How can we redefine these functions using its function components (`length` and `isEven`, and `_.toInt` and `isOdd`, respectively)? We can use a HOF which helps us to compose functions:",
 "Sin embargo, el patrón de composición _no_ es explícito en las implementaciones de las funciones `isEvenLength` e `isOddNumber`. ¿Cómo podemos redefinir estas funciones usando sus componentes función (`length` e `isEven`, y `_.toInt` e `isOdd`, respectivamente)? Podemos usar una HOF que nos ayude a componer funciones:"),

("Then, we can redefine `isEvenLength` in a modular way from the `length` and `isEven` building blocks:",
 "Entonces, podemos redefinir `isEvenLength` de forma modular a partir de los bloques constructivos `length` e `isEven`:"),

("Similarly, the redefinition of the `isOddNumber` function would be as follows:",
 "De forma similar, la redefinición de la función `isOddNumber` sería la siguiente:"),

("The HOF `compose` is actually defined by `Function1`:", "La HOF `compose` está en realidad definida por `Function1`:"),

("or using infix notation:", "o usando notación infija:"),

("Note that a similar function to `compose`, called `andThen`, is also available in the standard library:",
 "Nótese que en la biblioteca estándar también está disponible una función similar a `compose`, llamada `andThen`:"),

("""#### Exercise
<div class="alert alert-info">
    Implement the function <code>isEvenNumberOfAsAndBs</code> using the HOF <code>compose</code>.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Implementa la función <code>isEvenNumberOfAsAndBs</code> usando la HOF <code>compose</code>.
</div>"""),

("## Generics, aka parametric polymorphism", "## Genéricos, alias polimorfismo paramétrico"),

("What if we want to apply the composition pattern to this function?", "¿Qué pasa si queremos aplicar el patrón de composición a esta función?"),

("In this case, we are implicitly composing the following functions:", "En este caso, estamos componiendo implícitamente las siguientes funciones:"),

("Alas, we can't reuse our current `compose` function, because its implementation is _monomorphic_, i.e. it only works with specific types, namely, functions of types `String => Int` and `Int => Boolean`. Can we obtain a more generic version of `compose` which allows us to compose functions of arbitrary types? Parametric polymorphism to the rescue!",
 "Por desgracia, no podemos reutilizar nuestra función `compose` actual, porque su implementación es _monomórfica_, es decir, solo funciona con tipos específicos, en concreto, funciones de tipos `String => Int` e `Int => Boolean`. ¿Podemos obtener una versión más genérica de `compose` que nos permita componer funciones de tipos arbitrarios? ¡El polimorfismo paramétrico al rescate!"),

("Note that `A`, `B` and `C` are parameters of the function `compose`, much in the same way that parameters `f1` and `f2`. In the former case, they are _type_ parameters, and in the latter case they are _value_ parameters. But they are parameters nonetheless.",
 "Nótese que `A`, `B` y `C` son parámetros de la función `compose`, del mismo modo que lo son los parámetros `f1` y `f2`. En el primer caso, son parámetros de _tipo_, y en el segundo caso son parámetros de _valor_. Pero son parámetros al fin y al cabo."),

("We can also write the generic `compose` polymorphic method in the form of a function-value, using so-called [_polymorphic function types_](https://docs.scala-lang.org/scala3/reference/new-types/polymorphic-function-types.html):",
 "También podemos escribir el método polimórfico genérico `compose` en forma de función-valor, usando los llamados [_tipos función polimórficos_](https://docs.scala-lang.org/scala3/reference/new-types/polymorphic-function-types.html):"),

("Please, pay attention to the following table, which summarizes the different types of functions described above, together with their representation as methods and values:",
 "Presta atención a la siguiente tabla, que resume los distintos tipos de funciones descritos anteriormente, junto con su representación como métodos y valores:"),

("""#### Exercise
<div class="alert alert-info">
    There is a function which behaves as the identity element with respect to the operation `compose`, i.e. no matter which other function we choose to compose with the [`identity`](https://www.scala-lang.org/api/current/scala/Predef$.html) function, the result will be that function:

1. `identity[B] compose f == f` for all `f: A => B`
2. `f compose identity[A] == f` for all `f: A => B`

Implement the <code>identity</code> function both as a polymorphic method and as a polymorphic function type.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Existe una función que se comporta como el elemento identidad respecto a la operación `compose`, es decir, sin importar con qué otra función elijamos componer la función [`identity`](https://www.scala-lang.org/api/current/scala/Predef$.html), el resultado será esa misma función:

1. `identity[B] compose f == f` para todo `f: A => B`
2. `f compose identity[A] == f` para todo `f: A => B`

Implementa la función <code>identity</code> tanto como método polimórfico como función-valor polimórfica.
</div>"""),

("or using lambda expressions:", "o usando expresiones lambda:"),

("## Exponent types", "## Tipos exponenciales"),

("""In general, types may be regarded as sets of values. For instance, primitive types may be defined as follows:
* `Boolean = {false, true}`
* `Int = {..., -2, -1, 0, 1, 2, ...}`
* etc.

Given a type $A$, we can thus talk about its cardinality $|A|$, i.e. the number of elements they are made of. For instance:
* $|Boolean|=2$
* $|Int|=2^{32}$

What about about complex types like functions? Given types $A$ and $B$, how many functions are there of type $A => B$, i.e. which is the value of $|A => B|$. Let's consider how many functions are there of type `Boolean => Boolean`:""",
 """En general, los tipos pueden considerarse como conjuntos de valores. Por ejemplo, los tipos primitivos pueden definirse de la siguiente manera:
* `Boolean = {false, true}`
* `Int = {..., -2, -1, 0, 1, 2, ...}`
* etc.

Dado un tipo $A$, podemos así hablar de su cardinalidad $|A|$, es decir, el número de elementos de los que está formado. Por ejemplo:
* $|Boolean|=2$
* $|Int|=2^{32}$

¿Qué pasa con tipos complejos como las funciones? Dados los tipos $A$ y $B$, ¿cuántas funciones hay de tipo $A => B$, es decir, cuál es el valor de $|A => B|$? Consideremos cuántas funciones hay de tipo `Boolean => Boolean`:"""),

("There are exactly four different functions of type `Boolean => Boolean`, and this is because a function is characterised as a mapping which assigns a single value for each possible input value. Since we have two possible input values of type Boolean, and for each of them we can choose one boolean value (we have two possibilities), the resulting number of different mappings, i.e. functions, is `2*2`.",
 "Hay exactamente cuatro funciones distintas de tipo `Boolean => Boolean`, y esto es porque una función se caracteriza como una correspondencia que asigna un único valor para cada posible valor de entrada. Como tenemos dos posibles valores de entrada de tipo Boolean, y para cada uno de ellos podemos elegir un valor booleano (tenemos dos posibilidades), el número resultante de correspondencias distintas, es decir, de funciones, es `2*2`."),

("""In general, $|X\\Rightarrow Y|=|Y|^{|X|}$, since for each input value of type $X$ we have $|Y|$ values available. This is the reason why function types are called _exponential types_.""",
 """En general, $|X\\Rightarrow Y|=|Y|^{|X|}$, ya que para cada valor de entrada de tipo $X$ tenemos $|Y|$ valores disponibles. Esta es la razón por la que los tipos función se llaman _tipos exponenciales_."""),

("This justifies calling functions _algebraic_ data types, but why are functions _data types_ at all? Shouldn't functions be characterised more precisely as _behaviour_, as it's done in object-oriented programming? As we already discussed, functions are special _values_ and, hence, data of a special type encoding certain information. In particular, the information is encoded in the form of a input-output mapping.",
 "Esto justifica llamar a las funciones tipos de datos _algebraicos_, pero ¿por qué son las funciones _tipos de datos_ siquiera? ¿No deberían caracterizarse las funciones más precisamente como _comportamiento_, como se hace en la programación orientada a objetos? Como ya hemos comentado, las funciones son _valores_ especiales y, por tanto, datos de un tipo especial que codifica cierta información. En particular, la información se codifica en forma de una correspondencia entrada-salida."),

("Last, similarly to the other algebraic data types (products and sums), we can characterise functions from the point of view of its _constructors_ and _destructors_ (or _observers_). Constructors allow us to create or construct values of a given kind, whereas destructors allow us to extract or observe information encoded in that data type. In the particular case of function types, the *only* way to create a function (value) is through lambda expressions, and the only way to extract information from a function is to apply that function to a given input value.",
 "Por último, de forma similar a los demás tipos algebraicos de datos (productos y sumas), podemos caracterizar las funciones desde el punto de vista de sus _constructores_ y _destructores_ (u _observadores_). Los constructores nos permiten crear o construir valores de un tipo dado, mientras que los destructores nos permiten extraer u observar información codificada en ese tipo de datos. En el caso particular de los tipos función, la *única* forma de crear una función (valor) es mediante expresiones lambda, y la única forma de extraer información de una función es aplicar esa función a un valor de entrada dado."),

("""#### Exercise
<div class="alert alert-info">
    How many functions are there of type <code>(Boolean, Boolean, Boolean) => Boolean</code>? Write two of them.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    ¿Cuántas funciones hay de tipo <code>(Boolean, Boolean, Boolean) => Boolean</code>? Escribe dos de ellas.
</div>"""),

("""The function `(Boolean, Boolean, Boolean) => Boolean` is equivalent to its curried form `Boolean => (Boolean => (Boolean => Boolean))`. The number of values of this type is:

$|Boolean => (Boolean => (Boolean => Boolean))| = \\\\
    |Boolean => (Boolean => Boolean)|^{|Boolean|} = \\\\
    (|Boolean => Boolean|^{|Boolean|})^{|Boolean|} = \\\\
    ((|Boolean|^{|Boolean|})^{|Boolean|})^{|Boolean|} = \\\\
    |Boolean|^{|Boolean|*|Boolean|*|Boolean|} = \\\\
    2^{2*2*2} = \\\\
    256$""",
 """La función `(Boolean, Boolean, Boolean) => Boolean` es equivalente a su forma currificada `Boolean => (Boolean => (Boolean => Boolean))`. El número de valores de este tipo es:

$|Boolean => (Boolean => (Boolean => Boolean))| = \\\\
    |Boolean => (Boolean => Boolean)|^{|Boolean|} = \\\\
    (|Boolean => Boolean|^{|Boolean|})^{|Boolean|} = \\\\
    ((|Boolean|^{|Boolean|})^{|Boolean|})^{|Boolean|} = \\\\
    |Boolean|^{|Boolean|*|Boolean|*|Boolean|} = \\\\
    2^{2*2*2} = \\\\
    256$"""),

("## Syntactic sugar for function-values", "## Azúcar sintáctico para valores función"),

("We discuss now some syntactic facilities offered by Scala when writing lambda expressions.",
 "Comentamos ahora algunas facilidades sintácticas que ofrece Scala al escribir expresiones lambda."),

("First, we can omit the types of input arguments and let Scala figure out them:",
 "Primero, podemos omitir los tipos de los argumentos de entrada y dejar que Scala los infiera:"),

("Second, we can get extra level of conciseness using so-called _underscore_ syntax:",
 "Segundo, podemos obtener un nivel extra de concisión usando la llamada sintaxis de _guión bajo_:"),

("This kind of syntactic sugar also applies to functions of more than one argument:",
 "Este tipo de azúcar sintáctico también se aplica a funciones de más de un argumento:"),

("""#### Exercise
<div class="alert alert-info">
    Write the following function using underscore syntax.
</div>""",
 """#### Ejercicio
<div class="alert alert-info">
    Escribe la siguiente función usando sintaxis de guión bajo.
</div>"""),

("## Appendix: How are functions represented as values in Scala",
 "## Apéndice: Cómo se representan las funciones como valores en Scala"),

("Now, we just want to focus on how are functions actually represented as values in a OO language like Scala. This representation builds essentially upon methods, in particular, _reified_ methods. For instance, let's consider the following functions:",
 "Ahora, queremos centrarnos en cómo se representan realmente las funciones como valores en un lenguaje OO como Scala. Esta representación se basa esencialmente en métodos, en particular, métodos _reificados_. Por ejemplo, consideremos las siguientes funciones:"),

("In order to create a type of functions that receive an integer and return another one, we can create a new class whose only method is the function that we want to actually implement:",
 "Para crear un tipo de funciones que reciben un entero y devuelven otro, podemos crear una nueva clase cuyo único método sea la función que realmente queremos implementar:"),

("Now, we can implement the `call` HOF as follows:", "Ahora, podemos implementar la HOF `call` de la siguiente manera:"),

("In order to use this HOF with the `addOneM` and `substractOneM` functions, we must create reified versions for them:",
 "Para usar esta HOF con las funciones `addOneM` y `substractOneM`, debemos crear versiones reificadas de ellas:"),

("Or, alternatively, we can also create instances using `object` declarations:",
 "O, alternativamente, también podemos crear instancias usando declaraciones `object`:"),

("We call the `addOneV` and `substractOneV` function-values, i.e. functions represented as values. Now, we can use the `call` HOF as follows:",
 "A `addOneV` y `substractOneV` los llamamos valores función, es decir, funciones representadas como valores. Ahora, podemos usar la HOF `call` de la siguiente manera:"),

("Actually, function types such as `Int => Int` and `Boolean => String` are syntactic sugar for the types `Function1[Int, Int]` and `Function1[Boolean, String]`, where [`Function1`](https://www.scala-lang.org/api/current/scala/Function1.html) is a generalization of the type `FunctionInt2Int` that we wrote above. We have also [`Function2`](https://www.scala-lang.org/api/current/scala/Function2.html), [`Function3`](https://www.scala-lang.org/api/current/scala/Function3.html), etc., that are roughly implemented as follows:",
 "En realidad, los tipos función como `Int => Int` y `Boolean => String` son azúcar sintáctico para los tipos `Function1[Int, Int]` y `Function1[Boolean, String]`, donde [`Function1`](https://www.scala-lang.org/api/current/scala/Function1.html) es una generalización del tipo `FunctionInt2Int` que escribimos antes. También tenemos [`Function2`](https://www.scala-lang.org/api/current/scala/Function2.html), [`Function3`](https://www.scala-lang.org/api/current/scala/Function3.html), etc., que están implementadas aproximadamente de la siguiente manera:"),

("Using these standard classes, we can create the `addOneV` function-value in a similar way than before:",
 "Usando estas clases estándar, podemos crear el valor función `addOneV` de forma similar a antes:"),

("or using `object` declarations:", "o usando declaraciones `object`:"),

("and invoke functions as follows:", "e invocar funciones de la siguiente manera:"),

("However, as we saw throughout this notebook, we can also invoke the function without explicitly naming the `apply` method, i.e.",
 "Sin embargo, como vimos a lo largo de este notebook, también podemos invocar la función sin nombrar explícitamente el método `apply`, es decir,"),

("This is just another syntactic nicety of Scala. In sum, in an object-oriented language like Scala, function-values are ultimately methods in disguise.",
 "Esto es solo otra sutileza sintáctica de Scala. En resumen, en un lenguaje orientado a objetos como Scala, los valores función son, en última instancia, métodos disfrazados."),

# --- comentarios ---
("// `add one` function", "// función que suma uno"),
("// An impure function", "// Una función impura"),
("// Program 1", "// Programa 1"),
("// Program 2", "// Programa 2"),
("// this to be explained later", "// esto se explicará más adelante"),
("// Function-methods", "// Funciones-método"),
("// Function-values", "// Funciones-valor"),
("// up to Function22", "// hasta Function22"),

("// with the explicit object", "// con el objeto explícito"),
("// Three variables, types and values", "// Tres variables, tipos y valores"),
("// invociations", "// invocaciones"),
("// call invocations", "// invocaciones de call"),
("// call invocationts with function-methods", "// invocaciones de call con funciones-método"),
("// function-method of two arguments", "// función-método de dos argumentos"),
("// function-value of two arguments", "// función-valor de dos argumentos"),
("// Curried functions", "// Funciones currificadas"),
("// Partially-applied function", "// Función parcialmente aplicada"),
("// Function applied completely", "// Función aplicada completamente"),
("// function-method with multiple-parameter lists", "// función-método con listas de parámetros múltiples"),
("// standard curried method", "// método currificado estándar"),
("// isEvenLenght monolyth", "// isEvenLenght monolítico"),
("// compose HOF", "// HOF compose"),
("// defined using standard `compose`", "// definida usando el `compose` estándar"),
("// defined using `andThen`", "// definida usando `andThen`"),
("// Polymorphic method", "// Método polimórfico"),
("// Polymorphic function value", "// Función-valor polimórfica"),
("// four functions", "// cuatro funciones"),
("// `call` invocation using underscore notation", "// invocación de `call` usando notación con guión bajo"),
("// `call` invocations", "// invocaciones de `call`"),
("// Standard Function1 and Function2", "// Function1 y Function2 estándar"),
("// addOneV using standard Function1 vals", "// addOneV usando vals Function1 estándar"),
("// addOneV using standard function1 objects", "// addOneV usando objetos function1 estándar"),
("// addOneV invocations explicitly using `apply`", "// invocaciones de addOneV usando `apply` explícitamente"),
("// without `apply`", "// sin `apply`"),
("// write you solution here", "// escribe aquí tu solución"),
]
