PAIRS = [
("### Preamble", "### Preámbulo"),
("# Topic 6. Higher-order functions and modular programming", "# Tema 6. Funciones de orden superior y programación modular"),

("In this notebook, we will see that higher-order functions (HOFs) are essential modularity devices, and we will introduce the most common higher-order functions that operate over many different data structures.",
 "En este notebook, veremos que las funciones de orden superior (HOF) son dispositivos de modularidad esenciales, e introduciremos las funciones de orden superior más comunes que operan sobre muchas estructuras de datos distintas."),

("""Before we start, it is worth naming the method that runs through the whole notebook, because you have met it already: it is the modularity by abstraction of [__Functions as modularity devices__](../../PF-2/topic3/3.1%20Functions.ipynb), in Topic 3, one level of abstraction up.

1. __problem 1__ — solve a concrete problem, recursively;
2. __problem 2__ — solve a second one, which turns out to have the __same skeleton__;
3. __abstraction__ — pull that skeleton out into a function, leaving the differences as parameters;
4. __refactoring__ — go back and re-implement both problems in terms of it.

There, two programs read a key out of a configuration with a default value, the concern they repeated was abstracted into a plain function, and both were rewritten in terms of it. Here the story is the same, with one twist: what differs between our two problems is not a value but __an operation__, so the parameter has to be a function — and the abstraction, therefore, a __higher-order__ one. The `foldRight` section right below is exactly these four steps, and so are `foldLeft` and `map`.""",
 """Antes de empezar, merece la pena ponerle nombre al método que recorre todo el notebook, porque ya lo has visto: es la modularidad por abstracción de [__Las funciones como dispositivos de modularidad__](../../PF-2/topic3/3.1%20Functions.ipynb), en el Tema 3, un nivel de abstracción más arriba.

1. __problema 1__ — resuelve un problema concreto, recursivamente;
2. __problema 2__ — resuelve un segundo problema, que resulta tener el __mismo esqueleto__;
3. __abstracción__ — extrae ese esqueleto a una función, dejando las diferencias como parámetros;
4. __refactorización__ — vuelve atrás y reimplementa ambos problemas en términos de ella.

Allí, dos programas leían una clave de una configuración con un valor por defecto, la responsabilidad que repetían se abstrajo en una función normal, y ambos se reescribieron en términos de ella. Aquí la historia es la misma, con un giro: lo que difiere entre nuestros dos problemas no es un valor sino __una operación__, así que el parámetro tiene que ser una función — y la abstracción, por tanto, una función __de orden superior__. La sección de `foldRight` justo debajo es exactamente estos cuatro pasos, y también lo son `foldLeft` y `map`."""),

("""Before we start, it is worth naming the method that runs through the whole notebook, because it is the one the exams ask for — and because you have met it already: it is the modularity by abstraction of [__Functions as modularity devices__](../../PF-2/topic3/3.1%20Functions.ipynb), in Topic 3, one level of abstraction up.

1. __problem 1__ — solve a concrete problem, recursively;
2. __problem 2__ — solve a second one, which turns out to have the __same skeleton__;
3. __abstraction__ — pull that skeleton out into a function, leaving the differences as parameters;
4. __refactoring__ — go back and re-implement both problems in terms of it.

There, two programs read a key out of a configuration with a default value, the concern they repeated was abstracted into a plain function, and both were rewritten in terms of it. Here the story is the same, with one twist: what differs between our two problems is not a value but __an operation__, so the parameter has to be a function — and the abstraction, therefore, a __higher-order__ one. The `foldRight` section right below is exactly these four steps, and so are `foldLeft` and `map`.""",
 """Antes de empezar, merece la pena ponerle nombre al método que recorre todo el notebook, porque es el que piden los exámenes — y porque ya lo has visto: es la modularidad por abstracción de [__Las funciones como dispositivos de modularidad__](../../PF-2/topic3/3.1%20Functions.ipynb), en el Tema 3, un nivel de abstracción más arriba.

1. __problema 1__ — resuelve un problema concreto, recursivamente;
2. __problema 2__ — resuelve un segundo problema, que resulta tener el __mismo esqueleto__;
3. __abstracción__ — extrae ese esqueleto a una función, dejando las diferencias como parámetros;
4. __refactorización__ — vuelve atrás y reimplementa ambos problemas en términos de ella.

Allí, dos programas leían una clave de una configuración con un valor por defecto, la responsabilidad que repetían se abstrajo en una función normal, y ambos se reescribieron en términos de ella. Aquí la historia es la misma, con un giro: lo que difiere entre nuestros dos problemas no es un valor sino __una operación__, así que el parámetro tiene que ser una función — y la abstracción, por tanto, una función __de orden superior__. La sección de `foldRight` justo debajo es exactamente estos cuatro pasos, y también lo son `foldLeft` y `map`."""),

("""### References

[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_3ed) Third Edition.
by Martin Odersky, Lex Spoon, and Bill Venners.

- Chapter 6. Functional objects
- Chapter 8. Functions and closures
- Chapter 16. Working with Lists
- Chapter 23. For Expressions Revisited

[__Functional programming in Scala__](https://www.manning.com/books/functional-programming-in-scala), by Paul Chiusano and Runar Bjarnason.

- Chapter 3. Functional data structures

[__Functional programming simplified__](https://alvinalexander.com/downloads/fpsimplified-free-preview.pdf), by Alvin Alexander.

- Chapter 22. Functions Are Variables, Too
- Chapter 23. Using Methods As If They Were Functions
- Chapter 24. How to Write Functions That Take Functions as Input Parameters
- Chapter 25. How to Write a ‘map’ Function
- Chapter 27. Functions Can Have Multiple Parameter Groups
- Chapter 28. Partially-Applied Functions (and Currying)""",
 """### Referencias

[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_3ed) Tercera edición.
por Martin Odersky, Lex Spoon, y Bill Venners.

- Capítulo 6. Objetos funcionales
- Capítulo 8. Funciones y clausuras
- Capítulo 16. Trabajando con listas
- Capítulo 23. Las expresiones for revisitadas

[__Functional programming in Scala__](https://www.manning.com/books/functional-programming-in-scala), por Paul Chiusano y Runar Bjarnason.

- Capítulo 3. Estructuras de datos funcionales

[__Functional programming simplified__](https://alvinalexander.com/downloads/fpsimplified-free-preview.pdf), por Alvin Alexander.

- Capítulo 22. Las funciones también son variables
- Capítulo 23. Usar métodos como si fueran funciones
- Capítulo 24. Cómo escribir funciones que reciben funciones como parámetros de entrada
- Capítulo 25. Cómo escribir una función 'map'
- Capítulo 27. Las funciones pueden tener múltiples grupos de parámetros
- Capítulo 28. Funciones parcialmente aplicadas (y currificación)"""),

("## `FoldRight`: divide and conquer", "## `FoldRight`: divide y vencerás"),
("HOFs shine when the time comes to break monoliths. For instance, let's consider the following two functions:",
 "Las HOF brillan cuando llega el momento de romper monolitos. Por ejemplo, consideremos las siguientes dos funciones:"),
("These functions clearly share a common logic: their only differences are the value which is returned when the list is empty, and the function used to combine numbers (`+` and `*`, respectively). We can abstract away these differences and arrive to a more generic function which encodes that common logic:",
 "Estas funciones claramente comparten una lógica común: sus únicas diferencias son el valor que se devuelve cuando la lista está vacía, y la función usada para combinar números (`+` y `*`, respectivamente). Podemos abstraer estas diferencias y llegar a una función más genérica que codifique esa lógica común:"),
("which allows us to re-define in a modular way the `sum` and `multiply` functions:",
 "que nos permite redefinir de forma modular las funciones `sum` y `multiply`:"),
("But we don't need to constrain ourselves to integers. In its generic version, the `combine` function is actually the `foldRight` higher-order function (for `List`s):",
 "Pero no tenemos por qué limitarnos a los enteros. En su versión genérica, la función `combine` es en realidad la función de orden superior `foldRight` (para `List`s):"),
("Graphically, we can explain the behaviour of `foldRight` as follows:",
 "Gráficamente, podemos explicar el comportamiento de `foldRight` de la siguiente manera:"),

("""![with elements](../../images/foldRight.1.svg)

(all images credit to [Scala Visual Reference](https://superruzafa.github.io/visual-scala-reference/))""",
 """![with elements](../../images/foldRight.1.svg)

(todas las imágenes son cortesía de [Scala Visual Reference](https://superruzafa.github.io/visual-scala-reference/))"""),

("""We can understand `foldRight` as an implementation of the divide-and-conquer design pattern: first, divide your problems in subproblems; second, solve these sub-problems; last, compose their solutions to obtain the solution to the overall problem. If the sub-problems are simple enough they can be solved directly; otherwise, they are solved recursively. In the case of lists:
- The problem is obtaining a value of type `B` for a given list.
- The only sub-problem corresponds to the tail of that list.
- The arguments of the `foldRight` function tell us how to obtain the solution for the empty list (the atomic problem which can not be further decomposed), and how to obtain the solution from the solution to the sub-problem.""",
 """Podemos entender `foldRight` como una implementación del patrón de diseño divide y vencerás: primero, divide tus problemas en subproblemas; segundo, resuelve esos subproblemas; por último, compón sus soluciones para obtener la solución al problema global. Si los subproblemas son lo bastante simples pueden resolverse directamente; si no, se resuelven recursivamente. En el caso de las listas:
- El problema es obtener un valor de tipo `B` para una lista dada.
- El único subproblema corresponde a la cola de esa lista.
- Los argumentos de la función `foldRight` nos dicen cómo obtener la solución para la lista vacía (el problema atómico que no puede descomponerse más), y cómo obtener la solución a partir de la solución del subproblema."""),

("From this perspective, the implementation of `sum` and `multiply` is exactly the same as before when we used the function `combine`, although we can explain them differently:",
 "Desde esta perspectiva, la implementación de `sum` y `multiply` es exactamente la misma que antes cuando usábamos la función `combine`, aunque podemos explicarlas de forma distinta:"),

("#### HOFs in the Scala API", "#### Las HOF en la API de Scala"),
("The `foldRight` HOF, as all the HOFs that we will explain in this notebook, are actually part of the standard Collections library of Scala. Typically, they are implemented as member methods of the corresponding collection class. For lists, the [Scala API](https://www.scala-lang.org/api/2.13.1/scala/collection/immutable/List.html) offers something like this:",
 "La HOF `foldRight`, como todas las HOF que explicaremos en este notebook, forman en realidad parte de la biblioteca estándar de colecciones de Scala. Habitualmente, se implementan como métodos miembro de la clase de colección correspondiente. Para las listas, la [API de Scala](https://www.scala-lang.org/api/2.13.1/scala/collection/immutable/List.html) ofrece algo así:"),
("So, invocations of the standard `foldRight` do not receive the list as argument, but are common method invocations on some `List` instance:",
 "Así, las invocaciones del `foldRight` estándar no reciben la lista como argumento, sino que son invocaciones de método normales sobre alguna instancia de `List`:"),
("Normally, we will use standard HOFs instead of our home-made versions, once they are explained.",
 "Normalmente, usaremos las HOF estándar en vez de nuestras versiones caseras, una vez que estén explicadas."),

("## The Hall of Fame of HOFs", "## El salón de la fama de las HOF"),
("Besides `compose`, `andThen` and `foldRight`, there are other famous higher-order functions which work great as modularity devices:",
 "Además de `compose`, `andThen` y `foldRight`, hay otras funciones de orden superior famosas que funcionan estupendamente como dispositivos de modularidad:"),
("But most of these functions do not only work for `List`, they work also for `Option`, `Either[A, ?]`, and many other data structures. For instance:",
 "Pero la mayoría de estas funciones no solo funcionan para `List`, sino que también funcionan para `Option`, `Either[A, ?]`, y muchas otras estructuras de datos. Por ejemplo:"),
("The `fold` function is the catamorphism for `Option` and `Either[A, ?]`, in the same way than `foldRight` is the catamorphism for lists (unfortunately, the concept of catamorphism won't be explained due to lack of time).",
 "La función `fold` es el catamorfismo de `Option` y `Either[A, ?]`, de la misma manera que `foldRight` es el catamorfismo de las listas (por desgracia, el concepto de catamorfismo no se explicará por falta de tiempo)."),

("## FoldLeft: a better loop", "## FoldLeft: un bucle mejor"),
("The `foldLeft` HOF is the functional way to implement common imperative algorithms. For instance:",
 "La HOF `foldLeft` es la forma funcional de implementar algoritmos imperativos comunes. Por ejemplo:"),
("The following implementation abstracts away the differences in the above functions, and declares two additional parameters: the initial value of a mutable variable, and the update function executed in every step of the loop.",
 "La siguiente implementación abstrae las diferencias de las funciones anteriores, y declara dos parámetros adicionales: el valor inicial de una variable mutable, y la función de actualización que se ejecuta en cada paso del bucle."),
("Similarly, the `foldLeft` function is typically used where a tail-recursive function is needed. Its recursive implementation is naturally tail-recursive:",
 "De forma similar, la función `foldLeft` se usa habitualmente donde se necesita una función recursiva final. Su implementación recursiva es de forma natural recursiva final:"),
("Using `foldLeft` we can implement functions at a higher-level of abstraction, i.e. using constructs which are nearer to the problem-domain, without caring about mutable variables, tail-safe recursion, etc. Its use also leads to very concise (and readable!) implementations. For instance, these are (almost) one-liner implementations of some of the functions of the last notebook on recursive functions:",
 "Usando `foldLeft` podemos implementar funciones a un nivel de abstracción más alto, es decir, usando construcciones más cercanas al dominio del problema, sin preocuparnos de variables mutables, recursión segura para la pila, etc. Su uso también da lugar a implementaciones muy concisas (¡y legibles!). Por ejemplo, estas son implementaciones de (casi) una línea de algunas de las funciones del último notebook sobre funciones recursivas:"),
("But we may also use the `foldRight` function to implement them:",
 "Pero también podemos usar la función `foldRight` para implementarlas:"),
("Functionally, both versions are equivalent, but the ones using `foldLeft` are more efficient. In particular, the `foldRight` version of `reverse` has cuadratic complexity.",
 "Funcionalmente, ambas versiones son equivalentes, pero las que usan `foldLeft` son más eficientes. En particular, la versión de `reverse` con `foldRight` tiene complejidad cuadrática."),

("#### Implementing `foldRight` with `foldLeft`", "#### Implementar `foldRight` con `foldLeft`"),
("The implementation that we gave for `foldRight` was not tail-recursive, so this will blow up the stack:",
 "La implementación que dimos para `foldRight` no era recursiva final, así que esto va a desbordar la pila:"),
("In order to obtain a better implementation, we may first reverse the list and use `foldLeft` as follows:",
 "Para obtener una mejor implementación, podemos primero invertir la lista y usar `foldLeft` de la siguiente manera:"),
("This implementation works right with big lists:", "Esta implementación funciona bien con listas grandes:"),

("#### Implementing `foldLeft` with `foldRight`", "#### Implementar `foldLeft` con `foldRight`"),
("This is also possible, though challenging. We start from the tail-recursive implementation of `foldLeft`. First, we rearrange the arguments so that it now returns a function instead of a plain value of type `B`.",
 "Esto también es posible, aunque no es trivial. Partimos de la implementación recursiva final de `foldLeft`. Primero, reordenamos los argumentos de modo que ahora devuelva una función en vez de un simple valor de tipo `B`."),
("This was in order to better expose the recursion pattern of `foldRight`. The solution is now obtained simply by noticing that `foldLeft(tail)(update)` is the solution for the tail:",
 "Esto era para exponer mejor el patrón de recursión de `foldRight`. La solución se obtiene ahora simplemente notando que `foldLeft(tail)(update)` es la solución para la cola:"),
("The original signature can then be implemented as follows:",
 "La signatura original puede implementarse entonces de la siguiente manera:"),

("## The `map` HOF", "## La HOF `map`"),

("""The `map` function is one of the essential HOFs. Its purpose is applying a function to the elements of a data structure, in such a way that the relationships between these elements do not change. The only thing that must be modified is the _content_ of the data structure, not its _shape_. This condition is expressed in the following equations:

1. `map(list)(identity) == list` for all `list: List[A]`
2. `map(map(list)(f))(g) == map(list)(g compose f)` for all `list: List[A]`, `f: A => B`, `g: B => C`""",
 """La función `map` es una de las HOF esenciales. Su propósito es aplicar una función a los elementos de una estructura de datos, de tal manera que las relaciones entre esos elementos no cambien. Lo único que debe modificarse es el _contenido_ de la estructura de datos, no su _forma_. Esta condición se expresa en las siguientes ecuaciones:

1. `map(list)(identity) == list` para toda `list: List[A]`
2. `map(map(list)(f))(g) == map(list)(g compose f)` para toda `list: List[A]`, `f: A => B`, `g: B => C`"""),

("Rather than starting from the general case, let's arrive at it. Here are two concrete problems, each solved by recursion on the list:",
 "En vez de partir del caso general, lleguemos a él. Aquí hay dos problemas concretos, cada uno resuelto por recursión sobre la lista:"),

("The two are the same program. Both return the empty list for the empty list, and both put the result of _something applied to the head_ in front of the solution for the tail; the only difference is what that something is — `_.toChar` in one, `_.length` in the other. So we abstract the skeleton and leave the difference as a parameter:",
 "Los dos son el mismo programa. Ambos devuelven la lista vacía para la lista vacía, y ambos ponen el resultado de _algo aplicado a la cabeza_ delante de la solución para la cola; la única diferencia es qué es ese algo — `_.toChar` en uno, `_.length` en el otro. Así que abstraemos el esqueleto y dejamos la diferencia como parámetro:"),

("And now the step that closes the method, and where the payoff shows: both problems collapse to one line each, and all that survives of them is the operation that made them different in the first place.",
 "Y ahora el paso que cierra el método, y donde se ve la recompensa: ambos problemas se reducen a una línea cada uno, y lo único que sobrevive de ellos es la operación que en primer lugar los hacía diferentes."),

("The `map` function is polymorphic in `A` and `B`, but we can't pass generic functions (aka polymorphic values) as parameters using `FunctionN`classes (these classes only wrap functions from specific types to specific result types). We may create polymorphic versions of `FunctionN` clases, but in order to keep things simple, we will define the test catalogue for `map` using a specific signature chosen at random (any other may serve as well):",
 "La función `map` es polimórfica en `A` y en `B`, pero no podemos pasar funciones genéricas (también llamadas valores polimórficos) como parámetros usando las clases `FunctionN` (estas clases solo envuelven funciones de tipos específicos a tipos de resultado específicos). Podríamos crear versiones polimórficas de las clases `FunctionN`, pero para simplificar las cosas, definiremos el catálogo de pruebas de `map` usando una signatura específica elegida al azar (cualquier otra serviría igual):"),

("To run the tests we will pass the `map` function for `Ìnt` and `Boolean` types:",
 "Para ejecutar las pruebas pasaremos la función `map` para los tipos `Ìnt` y `Boolean`:"),
("although it's not necessary to write the types explicitly (Scala will infer the types for us):",
 "aunque no es necesario escribir los tipos explícitamente (Scala los inferirá por nosotros):"),
("The implementation of `map` is really close to the implementation of `foldRight`. Indeed, we can give a more modular implementation using this more basic HOF:",
 "La implementación de `map` está muy cerca de la implementación de `foldRight`. De hecho, podemos dar una implementación más modular usando esta HOF más básica:"),

("### `map` for `Option`", "### `map` para `Option`"),
("The implementation of the `map` function given above works over lists, but we can also map optional values and many other data structures. The implementation for the data structure `Option` must satisfy the following test:",
 "La implementación de la función `map` dada arriba funciona sobre listas, pero también podemos mapear valores opcionales y muchas otras estructuras de datos. La implementación para la estructura de datos `Option` debe satisfacer la siguiente prueba:"),
("The implementation is simple:", "La implementación es sencilla:"),

("## Filtering elements", "## Filtrar elementos"),
("Unlike `map`, the `filter` HOF allows us to change the shape of the data structure, removing those elements that do not satisfy a given predicate.",
 "A diferencia de `map`, la HOF `filter` nos permite cambiar la forma de la estructura de datos, eliminando aquellos elementos que no satisfacen un predicado dado."),
("Again, let's arrive at it rather than start from it. Two concrete problems, each solved by recursion on the list:",
 "De nuevo, lleguemos a ella en vez de partir de ella. Dos problemas concretos, cada uno resuelto por recursión sobre la lista:"),

("The two are the same program again: the empty list gives the empty list, and every head is either kept in front of the solution for the tail or dropped, according to a __test__ — `_ % 2 == 0` in one, `_.nonEmpty` in the other. Abstract the test away, and what is left is `filter`:",
 "Los dos son de nuevo el mismo programa: la lista vacía da la lista vacía, y cada cabeza o bien se mantiene delante de la solución para la cola o bien se descarta, según una __comprobación__ — `_ % 2 == 0` en uno, `_.nonEmpty` en el otro. Abstrae la comprobación, y lo que queda es `filter`:"),

("And the refactoring, which leaves each problem with nothing of its own but its test:",
 "Y la refactorización, que deja a cada problema sin nada propio salvo su comprobación:"),

("Using `foldRight` we can get a more modular implementation:", "Usando `foldRight` podemos obtener una implementación más modular:"),

("### Filtering optional values", "### Filtrar valores opcionales"),
("We only have a possible value, so implementing filtering is easy in this case:",
 "Solo tenemos un posible valor, así que implementar el filtrado es fácil en este caso:"),

("## FlatMapping data structures", "## Aplicar flatMap a estructuras de datos"),
("Let's consider a paragraph represented as a list of sentences, where each sentence is in turn modelled as a string made of _words_ separated by blank spaces. We want to obtain a list of all the words in each sentence.",
 "Consideremos un párrafo representado como una lista de frases, donde cada frase se modela a su vez como una cadena formada por _palabras_ separadas por espacios en blanco. Queremos obtener una lista con todas las palabras de cada frase."),
("We may try to map the paragraph with a function that `split`s  each sentence into the words they are made of:",
 "Podríamos intentar mapear el párrafo con una función que divida (`split`) cada frase en las palabras de las que está formada:"),
("but then we obtain a _list of lists_ of strings, not a list of plain strings. The solution is not far though: we have just to concatenate all the lists and we obtain what we need. The function `flatten` performs this concatenation:",
 "pero entonces obtenemos una _lista de listas_ de cadenas, no una lista de cadenas simples. Sin embargo, la solución no está lejos: solo tenemos que concatenar todas las listas y obtenemos lo que necesitamos. La función `flatten` realiza esta concatenación:"),
("The function `flatten` is actually provided by the Scala API. So, the implementation of the `words` function is as follows:",
 "La función `flatten` en realidad la proporciona la API de Scala. Así, la implementación de la función `words` es la siguiente:"),

("One problem is not enough to see a pattern, so here is a second one with the same shape: given a list of words, obtain the list of all the characters in them. Note what it shares with `words` — each element expands into a _list_ of results, and those lists then have to be joined — and note that the expansion is the only thing that differs:",
 "Un solo problema no es suficiente para ver un patrón, así que aquí hay un segundo con la misma forma: dada una lista de palabras, obtener la lista de todos los caracteres que contienen. Nótese lo que comparte con `words` — cada elemento se expande en una _lista_ de resultados, y esas listas luego hay que unirlas — y nótese que la expansión es lo único que difiere:"),

("This combination of the HOF `map` and the function `flatten` is so common, that it has been given a proper name: `flatMap`.",
 "Esta combinación de la HOF `map` y la función `flatten` es tan común, que se le ha dado un nombre propio: `flatMap`."),

("Using `flatMap` the word function is implemented even more easily:",
 "Usando `flatMap` la función de palabras se implementa todavía más fácilmente:"),

("...and the second problem goes exactly the same way:", "...y el segundo problema va exactamente de la misma manera:"),

("### FlatMapping optional values", "### Aplicar flatMap a valores opcionales"),

("## All together: a modularity problem", "## Todo junto: un problema de modularidad"),
("As before, we start from a list of sentences, but now we want to take care of the possible extra spaces between each word. Also, we want to obtain not the words themselves but their lengths. So, the specification of our problem is a function `lengths`:",
 "Como antes, partimos de una lista de frases, pero ahora queremos tener en cuenta los posibles espacios adicionales entre cada palabra. Además, queremos obtener no las palabras en sí sino sus longitudes. Así, la especificación de nuestro problema es una función `lengths`:"),
("such that:", "tal que:"),
("We may try to implement this function imperatively using mutable variables:",
 "Podríamos intentar implementar esta función de forma imperativa usando variables mutables:"),
("and this works, of course:", "y esto funciona, por supuesto:"),
("but can we do it better? Yes, we can! Using HOFs we can get a more concise, understandable and reliable version, with a great level of reuse!",
 "pero, ¿podemos hacerlo mejor? ¡Sí, podemos! ¡Usando HOF podemos obtener una versión más concisa, comprensible y fiable, con un gran nivel de reutilización!"),

("""This solution contrasts with the mutable version in several respects:
- It's more **modular**, i.e. it's made of coarse-grained components: the HOFs `flatMap`, `filter` and `map`. The mutable version builds instead upon fine-grained components: `var`s, and `for` loops.
- The HOF components `flatMap`, etc., are actually very generic and domain-independent, and are typically part of standard libraries, so the level of **reuse** and **reliability** of the HOF-based solution is very high.
- The HOF-based solution is more **understandable**: it models the solution to the problem in terms of standard _transformations_ which are composed together using plain function composition. Moreover, these transformations are also at the right level of abstraction, i.e. it's natural to specify the solution to the problem in terms of flatMap, filter and map.""",
 """Esta solución contrasta con la versión mutable en varios aspectos:
- Es más **modular**, es decir, está hecha de componentes de grano grueso: las HOF `flatMap`, `filter` y `map`. La versión mutable se construye en cambio sobre componentes de grano fino: `var`s, y bucles `for`.
- Los componentes HOF `flatMap`, etc., son en realidad muy genéricos e independientes del dominio, y habitualmente forman parte de las bibliotecas estándar, así que el nivel de **reutilización** y **fiabilidad** de la solución basada en HOF es muy alto.
- La solución basada en HOF es más **comprensible**: modela la solución del problema en términos de _transformaciones_ estándar que se componen entre sí usando composición de funciones normal. Además, estas transformaciones también están en el nivel de abstracción correcto, es decir, es natural especificar la solución del problema en términos de flatMap, filter y map."""),

("### For-comprehensions", "### Las for-comprehensions"),
("The combination of `map`, `flatMap` and `filter` HOFs is so common, that Scala has a special syntax for them: for-comprehensions.",
 "La combinación de las HOF `map`, `flatMap` y `filter` es tan común, que Scala tiene una sintaxis especial para ellas: las for-comprehensions."),

# --- comentarios ---
("// map example 1", "// ejemplo de map 1"),
("// map example 2 -- a different element type and a different operation, but look at the shape",
 "// ejemplo de map 2 -- un tipo de elemento distinto y una operación distinta, pero fíjate en la forma"),
("// map example 2", "// ejemplo de map 2"),
("// map generically", "// map de forma genérica"),
("// refactoring: the recursion was never the problem's, it was the skeleton's",
 "// refactorización: la recursión nunca fue del problema, era del esqueleto"),
("// refactoring: toChar and length, in terms of map", "// refactorización: toChar y length, en términos de map"),
("// filter example 1", "// ejemplo de filter 1"),
("// filter example 2 -- a different type and a different test, but look at the shape",
 "// ejemplo de filter 2 -- un tipo distinto y una comprobación distinta, pero fíjate en la forma"),
("// filter example 2", "// ejemplo de filter 2"),
("// refactoring: the recursion was the skeleton's, the test was the problem's",
 "// refactorización: la recursión era del esqueleto, la comprobación era del problema"),
("// refactoring: evens and nonEmpty, in terms of filter", "// refactorización: evens y nonEmpty, en términos de filter"),
("// flatMap example 2 -- the same shape as `words`, with a different expansion",
 "// ejemplo de flatMap 2 -- la misma forma que `words`, con una expansión distinta"),
("// refactoring: and the expansion is all that is left of it", "// refactorización: y la expansión es lo único que queda de él"),
("// refactoring: chars, in terms of flatMap", "// refactorización: chars, en términos de flatMap"),
("// sum of elements", "// suma de elementos"),
("// product of elements", "// producto de elementos"),
("// monomorphic `combine` method", "// método `combine` monomórfico"),
("// more generically: foldRight", "// de forma más genérica: foldRight"),
("// foldRight over lists", "// foldRight sobre listas"),
("// length function, imperatively", "// función length, de forma imperativa"),
("// reverse function, imperatively", "// función reverse, de forma imperativa"),
("// abstraction: foldLeft, imperatively", "// abstracción: foldLeft, de forma imperativa"),
("// blowing up the stack", "// desbordando la pila"),
("// check it out", "// compruébalo"),
("// foldLeftAux with foldRight", "// foldLeftAux con foldRight"),
("// filter, generically", "// filter, de forma genérica"),
("// flatMap example 2: chars", "// ejemplo de flatMap 2: chars"),
]
