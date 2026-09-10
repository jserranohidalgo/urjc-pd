PAIRS = [
("### Preamble", "### Preámbulo"),
("# Topic 5: Recursive functions", "# Tema 5: Funciones recursivas"),

("# Problem 1", "# Problema 1"),
("Implement a function that drops the first _n_ elements of a list. If the number of elements to be dropped is 0, it must return the same list. The implementation must be tail-recursive.",
 "Implementa una función que elimine los primeros _n_ elementos de una lista. Si el número de elementos a eliminar es 0, debe devolver la misma lista. La implementación debe ser recursiva final."),
("###### Solution", "###### Solución"),
("###### Your solution", "###### Tu solución"),

("# Problem 2", "# Problema 2"),
("Create a function that counts the number of occurrences of a given element in a list.",
 "Crea una función que cuente el número de ocurrencias de un elemento dado en una lista."),
("#### Part a) Implement the function recursively, without tail-recursion",
 "#### Apartado a) Implementa la función de forma recursiva, sin recursión final"),
("Here it's a different implementation that performs the equality test through pattern matching:",
 "Aquí hay una implementación distinta que realiza la comprobación de igualdad mediante pattern matching:"),
("#### Part b) Implement the function with tail-recursion",
 "#### Apartado b) Implementa la función con recursión final"),

("# Problem 3", "# Problema 3"),
("Generate a function that takes the first *n* elements of a list. If the length of the list is less than _n_ it must return the input list (i.e. as many elements as there are).",
 "Genera una función que tome los primeros *n* elementos de una lista. Si la longitud de la lista es menor que _n_ debe devolver la lista de entrada (es decir, tantos elementos como haya)."),
("The function does not need to be tail-recursive.", "La función no necesita ser recursiva final."),

("# Problem 4", "# Problema 4"),
("Write a function that partitions a list of integers into a list of even numbers and a list of odd numbers.",
 "Escribe una función que reparta una lista de enteros en una lista de números pares y una lista de números impares."),
("Recall that given a [2-tuple](https://www.scala-lang.org/api/current/scala/Tuple2.html) in Scala, we can observe its components as follows:",
 "Recuerda que, dada una [2-tupla](https://www.scala-lang.org/api/current/scala/Tuple2.html) en Scala, podemos observar sus componentes de la siguiente manera:"),

("# Problem 5", "# Problema 5"),
("# Problem 6", "# Problema 6"),
("Write a funtion that receives a list of pairs of integers and returns a new list made from the sum of all pairs.",
 "Escribe una función que reciba una lista de pares de enteros y devuelva una nueva lista formada por la suma de cada par."),

("# Problem 7", "# Problema 7"),
("Write a function that receives two lists and returns a single list whose elements are pairs made from the corresponding elements of each list.",
 "Escribe una función que reciba dos listas y devuelva una única lista cuyos elementos sean pares formados por los elementos correspondientes de cada lista."),

("# Problem 8", "# Problema 8"),
("Write a function that returns the greatest element of a list of integers.",
 "Escribe una función que devuelva el mayor elemento de una lista de enteros."),
("Use pattern guards when possible. This is an example of pattern guard:",
 "Usa guardas de patrón cuando sea posible. Este es un ejemplo de guarda de patrón:"),

("# Problem 9", "# Problema 9"),
("Create a function that given a list of strings or integers, returns the concatenation of all the string elements. If the list doesn't contain any string, it must return the empty string.",
 "Crea una función que, dada una lista de cadenas o enteros, devuelva la concatenación de todos los elementos de tipo cadena. Si la lista no contiene ninguna cadena, debe devolver la cadena vacía."),
("Recall the definition of the [`Either[A, B]`](https://www.scala-lang.org/api/current/scala/util/Either.html) algebraic data type in the Scala API.",
 "Recuerda la definición del tipo algebraico de datos [`Either[A, B]`](https://www.scala-lang.org/api/current/scala/util/Either.html) en la API de Scala."),

("# Binary trees", "# Árboles binarios"),
("The following problems deal with functions on binary trees. This data structure can be defined as the following algebraic data type:",
 "Los siguientes problemas tratan sobre funciones sobre árboles binarios. Esta estructura de datos puede definirse como el siguiente tipo algebraico de datos:"),
("The companion object defines some smart constructors that will allow us to write test cases more easily.",
 "El objeto compañero define algunos constructores inteligentes que nos permitirán escribir casos de prueba más fácilmente."),

("# Problem 10", "# Problema 10"),
("Create a function that computes the number of nodes a tree.", "Crea una función que calcule el número de nodos de un árbol."),

("# Problem 11", "# Problema 11"),
("Create a function that calculates the _height_ of a tree, which is defined as the depth of its deepest node (the depth of a node, in turn, is the number of edges from that node to the root of the tree). An empty tree doesn't have any nodes, so it doesn't have height either.",
 "Crea una función que calcule la _altura_ de un árbol, que se define como la profundidad de su nodo más profundo (la profundidad de un nodo, a su vez, es el número de aristas desde ese nodo hasta la raíz del árbol). Un árbol vacío no tiene nodos, así que tampoco tiene altura."),
("Hint: use the Scala [`max`](https://www.scala-lang.org/api/current/scala/Int.html#max(that:Int):Int) method of the `Int` class to calculate the maximum of two numbers.",
 "Pista: usa el método [`max`](https://www.scala-lang.org/api/current/scala/Int.html#max(that:Int):Int) de Scala de la clase `Int` para calcular el máximo de dos números."),

("# Problem 12", "# Problema 12"),
("A degenerate tree is a tree whose nodes only have a child at most. Create a function that determines whether a tree is degenerate or not.",
 "Un árbol degenerado es un árbol cuyos nodos tienen como mucho un único hijo. Crea una función que determine si un árbol es degenerado o no."),

("# Problem 13", "# Problema 13"),
("Write a function that returns the leaves of a tree. The leafs of any left child must be placed in the list before any leaf from its right sibling.",
 "Escribe una función que devuelva las hojas de un árbol. Las hojas de cualquier hijo izquierdo deben colocarse en la lista antes que cualquier hoja de su hermano derecho."),
("Hint: use the [`++`](https://www.scala-lang.org/api/current/scala/collection/immutable/List.html#++[B%3E:A](suffix:scala.collection.IterableOnce[B]):CC[B]) method of the `List` class to concatenate lists.",
 "Pista: usa el método [`++`](https://www.scala-lang.org/api/current/scala/collection/immutable/List.html#++[B%3E:A](suffix:scala.collection.IterableOnce[B]):CC[B]) de la clase `List` para concatenar listas."),

("# Problem 14", "# Problema 14"),
("This problem deals with [_tree traversals_](https://en.wikipedia.org/wiki/Tree_traversal).",
 "Este problema trata sobre los [_recorridos de árboles_](https://en.wikipedia.org/wiki/Tree_traversal)."),
("#### Part a) Write a function that creates the pre-order of a binary tree.",
 "#### Apartado a) Escribe una función que cree el recorrido en preorden de un árbol binario."),
("#### Part b) Write a function that returns the in-order of a binary tree",
 "#### Apartado b) Escribe una función que devuelva el recorrido en orden de un árbol binario"),
("#### Part c) Write a function that returns post-order of a binary tree",
 "#### Apartado c) Escribe una función que devuelva el recorrido en postorden de un árbol binario"),

("# Problem 15", "# Problema 15"),
("Given a tree whose nodes are tuples of integers, write a function that returns a tree of the same shape that contains the sum of the numbers for each node.",
 "Dado un árbol cuyos nodos son tuplas de enteros, escribe una función que devuelva un árbol de la misma forma que contenga la suma de los números de cada nodo."),

("// for any other case, no matter if some(_) or None", "// para cualquier otro caso, no importa si some(_) o None"),
]
