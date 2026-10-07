PAIRS = [
("# Topic 5. Recursive functions and data types", "# Tema 5. Funciones y tipos de datos recursivos"),

("""The goals of this topic are to understand:

* How recursive types (lists, trees, etc.) are defined algebraically
* How functions over recursive types are defined recursivelly
* The two major types of recursive functions: general and tail-recursive""",
 """Los objetivos de este tema son entender:

* Cómo se definen algebraicamente los tipos recursivos (listas, árboles, etc.)
* Cómo se definen recursivamente las funciones sobre tipos recursivos
* Los dos tipos principales de funciones recursivas: generales y recursivas finales"""),

("""### References

[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_3ed) Third Edition.
by Martin Odersky, Lex Spoon, and Bill Venners.

- Chapter 16. Working with Lists
- Chapter 26. Extractors (optional)

[__Functional programming in Scala__](https://www.manning.com/books/functional-programming-in-scala), by Paul Chiusano and Runar Bjarnason.

- Chapter 3. Functional data structures

[__Functional programming simplified__](https://alvinalexander.com/downloads/fpsimplified-free-preview.pdf), by Alvin Alexander.

- Chapters 29-36. Recursion.""",
 """### Referencias

[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_3ed) Tercera edición.
por Martin Odersky, Lex Spoon, y Bill Venners.

- Capítulo 16. Trabajando con listas
- Capítulo 26. Extractores (opcional)

[__Functional programming in Scala__](https://www.manning.com/books/functional-programming-in-scala), por Paul Chiusano y Runar Bjarnason.

- Capítulo 3. Estructuras de datos funcionales

[__Functional programming simplified__](https://alvinalexander.com/downloads/fpsimplified-free-preview.pdf), por Alvin Alexander.

- Capítulos 29-36. Recursión."""),

("## Recursive types", "## Tipos recursivos"),
("### The `List` type", "### El tipo `List`"),

("""Lists are data structures which represent sequences of values of the same type, of finite length. They can be defined recursively in an informal way as follows:
- A list is the empty sequence
- A list is a non-empty sequence made of a value and another list, which represent the head and tail of the list, respectively

Thus, the type `IntList`, which represents lists of integers, must satisfy the following algebraic equation:

`IntList = 1 + Int * IntList`

i.e., a list of integers is the empty sequence (represented by the singleton type `1`), or an integer (the head) and a list (its tail).""",
 """Las listas son estructuras de datos que representan secuencias de valores del mismo tipo, de longitud finita. Pueden definirse recursivamente de manera informal de la siguiente forma:
- Una lista es la secuencia vacía
- Una lista es una secuencia no vacía formada por un valor y otra lista, que representan respectivamente la cabeza y la cola de la lista

Así, el tipo `IntList`, que representa listas de enteros, debe satisfacer la siguiente ecuación algebraica:

`IntList = 1 + Int * IntList`

es decir, una lista de enteros es la secuencia vacía (representada por el tipo singleton `1`), o bien un entero (la cabeza) y una lista (su cola)."""),

("The implementation in Scala is similar to the following one (we also give the generic version `List[A]`, rather than the implementation of `IntList`):",
 "La implementación en Scala es similar a la siguiente (también damos la versión genérica `List[A]`, en vez de la implementación de `IntList`):"),

("However the actual implementation of [immutable lists](https://github.com/scala/scala/blob/v2.13.1/src/library/scala/collection/immutable/List.scala#L79) in the standard library of Scala defines the empty list as an object, rather than a class. This forces us to declare the list covariantly in its generic parameter `A`, which is somewhat inconvenient at times.  The standard definition looks like as follows:",
 "Sin embargo, la implementación real de las [listas inmutables](https://github.com/scala/scala/blob/v2.13.1/src/library/scala/collection/immutable/List.scala#L79) en la biblioteca estándar de Scala define la lista vacía como un objeto, en vez de como una clase. Esto nos obliga a declarar la lista de forma covariante en su parámetro genérico `A`, lo cual resulta a veces algo incómodo.  La definición estándar tiene el siguiente aspecto:"),

("### Some syntactic sugar", "### Algo de azúcar sintáctico"),

("Note that we can write standard lists with a more compact syntax:",
 "Nótese que podemos escribir las listas estándar con una sintaxis más compacta:"),

("And we can also pattern match on lists, similarly:",
 "Y también podemos hacer pattern matching sobre listas, de forma similar:"),

("##  Recursive functions", "##  Funciones recursivas"),

("Since lists are defined recursively, functions over lists will be commonly recursive as well. For instance, let's implement a recursive function that computes the length of a list. But before, let's implement the function imperatively for the sake of comparison:",
 "Como las listas se definen recursivamente, las funciones sobre listas también serán habitualmente recursivas. Por ejemplo, implementemos una función recursiva que calcule la longitud de una lista. Pero antes, implementemos la función de forma imperativa, para poder comparar:"),

("The recursive function is implemented as follows:", "La función recursiva se implementa de la siguiente manera:"),


("### Tail-recursive functions", "### Funciones recursivas finales"),

("The implementation using tail-recursion solves the issues with the stack. It commonly makes use of auxiliary functions:",
 "La implementación mediante recursión final resuelve los problemas con la pila. Habitualmente hace uso de funciones auxiliares:"),

("We can check the stack-safety problems of non-tail recursive functions by calculating the length of a very big list. We will use the following function, which creates a constant list of given length.",
 "Podemos comprobar los problemas de seguridad de la pila de las funciones no recursivas finales calculando la longitud de una lista muy grande. Usaremos la siguiente función, que crea una lista constante de una longitud dada."),

("We can also use the function [`fill`](https://www.scala-lang.org/api/2.13.3/scala/collection/immutable/List$.html#fill[A](n:Int)(elem:=%3EA):CC[A]) of the Scala standard library.",
 "También podemos usar la función [`fill`](https://www.scala-lang.org/api/2.13.3/scala/collection/immutable/List$.html#fill[A](n:Int)(elem:=%3EA):CC[A]) de la biblioteca estándar de Scala."),

("Now, let's calculate the length of a list long enough to blow up the stack, using each of the three implementations:",
 "Ahora, calculemos la longitud de una lista lo bastante larga como para desbordar la pila, usando cada una de las tres implementaciones:"),

("### Unit testing with `scalatest`", "### Pruebas unitarias con `scalatest`"),

("From now on, we will also make extensive use of unit testing for the different functions that we implement. And we will use the [`scalatest`](http://www.scalatest.org/) library for that purpose. In particular, for each function we will implement a test catalogue that test it against different test cases. The test catalogue receives the actual function to be tested as a parameter. For instance, this is a possible test class for the `length` function:",
 "A partir de ahora, también haremos un uso extensivo de las pruebas unitarias para las distintas funciones que implementemos. Y usaremos para ello la biblioteca [`scalatest`](http://www.scalatest.org/). En particular, para cada función implementaremos un catálogo de pruebas que la comprueba frente a distintos casos de prueba. El catálogo de pruebas recibe como parámetro la función real que se va a probar. Por ejemplo, esta es una posible clase de pruebas para la función `length`:"),

("The method `shouldBe` is a _matcher_. The scalatest library offers an extensive catalogue of [them](http://www.scalatest.org/user_guide/using_matchers). Similarly, scalatest also support many different [testing styles](http://www.scalatest.org/user_guide/selecting_a_style). The chosen one here was `FlatSpec`. In order to execute the test catalogue we can simply use the scalatest method `run`:",
 "El método `shouldBe` es un _matcher_. La biblioteca scalatest ofrece un extenso catálogo de [ellos](http://www.scalatest.org/user_guide/using_matchers). De forma similar, scalatest también admite muchos [estilos de prueba](http://www.scalatest.org/user_guide/selecting_a_style) distintos. El elegido aquí fue `FlatSpec`. Para ejecutar el catálogo de pruebas simplemente podemos usar el método `run` de scalatest:"),

("### Example: adding numbers", "### Ejemplo: sumar números"),
("Let's implement a function that sums all the numbers of a list.", "Implementemos una función que sume todos los números de una lista."),

("### Example: multiplying list elements", "### Ejemplo: multiplicar los elementos de una lista"),
("Let's multiply the elements of a list. If the list is empty we return the identity element for integers.",
 "Multipliquemos los elementos de una lista. Si la lista está vacía devolvemos el elemento identidad de los enteros."),

(" This is the common recursive implementation:", " Esta es la implementación recursiva habitual:"),

("But we can optimize the function a little bit. Note that if the number 0 belongs to the list, then the result is 0, no matter how many elements the list has. So, once we find the element 0 it's a waste of resources to make the recursive call. Let's take this into account.",
 "Pero podemos optimizar un poco la función. Nótese que si el número 0 pertenece a la lista, entonces el resultado es 0, sin importar cuántos elementos tenga la lista. Así que, una vez que encontramos el elemento 0, es un desperdicio de recursos hacer la llamada recursiva. Tengamos esto en cuenta."),

("A similar optimization can be made for the tail-recursive implementation.",
 "Puede hacerse una optimización similar para la implementación recursiva final."),

("### Example: membership", "### Ejemplo: pertenencia"),
("Let's implement a function that given a list and an element, returns whether the element belongs to that list.",
 "Implementemos una función que, dada una lista y un elemento, devuelva si el elemento pertenece a esa lista."),
("We can also pattern match against a specific value as follows:",
 "También podemos hacer pattern matching contra un valor específico de la siguiente manera:"),

("### Example: last element", "### Ejemplo: último elemento"),
("Let's implement a function that returns the last element of a given list. Note that an empty list does not have elements, and, hence, does not have a last element.",
 "Implementemos una función que devuelva el último elemento de una lista dada. Nótese que una lista vacía no tiene elementos y, por tanto, no tiene un último elemento."),

("### Example: insert last", "### Ejemplo: insertar al final"),
("Now, a function that allows us to insert an element at the end of the list.",
 "Ahora, una función que nos permita insertar un elemento al final de la lista."),

("### Example: reverse lists", "### Ejemplo: invertir listas"),
("Implement a function which receives a list and returns its reverse.",
 "Implementa una función que reciba una lista y devuelva su inversa."),

("### Example: concatenate lists", "### Ejemplo: concatenar listas"),
("Tail-recursive concatenation:", "Concatenación recursiva final:"),

# --- comentarios ---
("// Less beautifully", "// De forma menos elegante"),
("// More idiomatically", "// De forma más idiomática"),
("// more idiomatically", "// más idiomáticamente"),
("// or", "// o"),
("// Using mutable variables", "// Usando variables mutables"),
("// Using recursive functions", "// Usando funciones recursivas"),
("// Using tail-recursive functions", "// Usando funciones recursivas finales"),
("// First, imperatively", "// Primero, de forma imperativa"),
("// Next, tail-recursively", "// Después, de forma recursiva final"),
("// Imperatively", "// De forma imperativa"),
("// Tail-recursive", "// Recursiva final"),
("// Plain recursive", "// Recursiva simple"),
("// Recursively", "// De forma recursiva"),
("// With tail-recursion", "// Con recursión final"),
("// We add this extra case", "// Añadimos este caso extra"),
("// optimization for 0", "// optimización para 0"),
("// Really inefficient", "// Realmente ineficiente"),
("// Tail-recursive, efficiently", "// Recursiva final, eficientemente"),
("// invoke", "// invocar"),

# Patrones de diseño: divide y vencerás, iterativo (2026-10-07)
('Some comments:\n- The recursive function is less efficient, since the stack will blow up with very long lists.\n- The recursive function is implemented in a _type-driven development_ style: we proceed, step-by-step, analysing the types of input data that are available, and the types of output that we have to generate. This leads to a divide-and-conquer problem solving strategy and hugely facilitates the implementation.',
 'Algunos comentarios:\n- La función recursiva es menos eficiente, ya que la pila se desbordará con listas muy largas.\n- La función recursiva está implementada al estilo del _desarrollo dirigido por tipos_: procedemos, paso a paso, analizando los tipos de los datos de entrada disponibles, y los tipos de salida que tenemos que generar. Esto lleva a una estrategia de resolución de problemas de divide y vencerás y facilita enormemente la implementación.'),

('### The _Divide and Conquer_ design pattern',
 '### Patrón de diseño de _Divide y Vencerás_'),

('- The divide-and-conquer strategy shows up, first, in the initial decomposition step: since the function that we have to implement is _total_ (it is defined for every value of the input type), and the input type is a sum type defined over different variants (the empty list and the non-empty list, in this case), we can divide the implementation of the function into the implementation of a function for each of the variants.\n- Second, since we are working with a recursive data structure, the case of the non-empty list can be solved taking into account the solution of the problem for the rest of the list. Rather than divide and conquer, we can speak here of _decrease and conquer_, since there is just one subproblem. The problem set includes examples of recursive functions over trees, where this recursive style gives rise to a more classical divide-and-conquer approach (since the number of subtrees of a non-empty tree is two).\n- All these considerations lead us to isolate the divide-and-conquer (or decrease-and-conquer) design pattern for solving problems over lists:',
 '- La estrategia de divide y vencerás se manifiesta, en primer lugar, en el primer paso de descomposición: dado que la función que tenemos que implementar es _total_ (está definida para todo valor del tipo de entrada) y que el tipo de entrada es un tipo suma definido sobre distintas variantes (la lista vacía y la lista no vacía, en este caso), podemos dividir la implementación de la función en la implementación de una función para cada una de las variantes.\n- En segundo lugar, dado que estamos trabajando con una estructura de datos recursiva, el caso de la lista no vacía se puede resolver teniendo en cuenta la solución del problema para el resto de la lista. Más que un divide y vencerás, podemos hablar aquí de un _reduce y vencerás_, dado que solo tenemos un subproblema. En la hoja de problemas se encontrarán ejemplos de funciones recursivas sobre árboles, y este estilo recursivo da lugar a una aproximación de divide y vencerás más clásica (dado que el número de subárboles de un árbol no vacío es dos).\n- Todas estas consideraciones nos llevan a aislar el patrón de diseño de divide y vencerás (o reduce y vencerás) para la resolución de problemas sobre listas:'),

('#### The _iterative_ design pattern',
 '#### Patrón de diseño _iterativo_'),

('The implementation based on tail-recursive functions follows an _iterative_ design pattern, quite different from the divide-and-conquer design pattern illustrated by the recursive implementation of the previous section. And, in essence, this design pattern of tail-recursive functions is the same as the one implemented by the imperative solution, which uses mutable variables and the loops of structured programming.',
 'La implementación basada en funciones recursivas por cola, o finales, se basa en un patrón de diseño _iterativo_, muy distinto del patrón de diseño de divide y vencerás ilustrado en la implementación recursiva de la sección anterior. Y, en esencia, este patrón de diseño de las funciones recursivas finales es el mismo que el implementado por medio de la solución imperativa que utiliza variables mutables y bucles de la programación estructurada.'),

('In both the imperative and the tail-recursive implementations, the pattern for solving the problem, represented by the input list, is the same:\n* We initialise the solution to a given value\n* We iterate over the elements of the list and, for each of them, we update the partial solution built so far taking that element into account\n* When the iteration is over, the partial solution is the final solution, and we return it.\n\nThe difference between the imperative and the tail-recursive implementations lies in the way these actions are carried out: in the imperative solution, iteration is performed by the _while_ loop, whereas in the tail-recursive solution, iteration is performed by recursive calls to the auxiliary function _step_. But, and this is what matters, the way of solving the problem is the same: it is the same design pattern in both cases, and this is what will be abstracted in the next topic.',
 'Tanto en la implementación imperativa como en la basada en recursión final, el patrón de resolución del problema, representado por la lista de entrada, es el mismo:\n* Inicializamos la solución a un valor concreto\n* Iteramos sobre los elementos de la lista, y para cada uno de ellos: actualizamos la solución parcial construida hasta el momento teniendo en cuenta ese elemento\n* Cuando terminemos la iteración, la solución parcial será la solución definitiva y la devolvemos.\n\nLa diferencia entre las implementaciones imperativas y con recursión final está en la distinta forma de realizar estas acciones: en el caso de la solución imperativa, la iteración se lleva a cabo mediante el bucle _while_, mientras que en el caso de la solución con recursión final, la iteración se lleva a cabo mediante llamadas recursivas a la función auxiliar _step_. Pero, y esto es lo importante, la forma de resolver el problema es la misma, es el mismo patrón de diseño en un caso y en otro, y esto es lo que se abstraerá en el siguiente tema.'),

('// Atomic problem, not decomposable',
 '// Problema atómico, no descomponible'),

('// Reducible problem, solvable through the solution for the rest (`tailSol`)',
 '// Problema reducible, resoluble a través de la solución al resto (`tailSol`)'),

('// and the head of the list',
 '// y la cabeza de la lista'),

]
