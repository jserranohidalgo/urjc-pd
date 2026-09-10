PAIRS = [
("### Preamble", "### Preámbulo"),
("# Topic 6. Higher-Order functions", "# Tema 6. Funciones de orden superior"),

("# Problem 1", "# Problema 1"),
("Write a function that concatenates two lists using `foldRight`.",
 "Escribe una función que concatene dos listas usando `foldRight`."),
("###### Solution", "###### Solución"),
("###### Your solution", "###### Tu solución"),

("# Problem 2", "# Problema 2"),
("Write a function that returns the head of a list, if non-empty. Use the `foldRight` HOF.",
 "Escribe una función que devuelva la cabeza de una lista, si no está vacía. Usa la HOF `foldRight`."),

("# Problem 3", "# Problema 3"),
("Write a function that inserts an element at the end of a given list. Use the `foldRight` HOF.",
 "Escribe una función que inserte un elemento al final de una lista dada. Usa la HOF `foldRight`."),

("# Problem 4", "# Problema 4"),
("Use `foldRight` to implement a function that given a list of strings or integers, returns the concatenation of all the string elements. If the list doesn't contain any string, it must return the empty string.",
 "Usa `foldRight` para implementar una función que, dada una lista de cadenas o enteros, devuelva la concatenación de todos los elementos de tipo cadena. Si la lista no contiene ninguna cadena, debe devolver la cadena vacía."),

("# Problem 5", "# Problema 5"),
("Write a function that returns the greatest element of a list of integers using `foldLeft`.",
 "Escribe una función que devuelva el mayor elemento de una lista de enteros usando `foldLeft`."),

("# Problem 6", "# Problema 6"),
("Implement the `filter` function for `List`s using `flatMap`.",
 "Implementa la función `filter` para `List`s usando `flatMap`."),

("# Problem 7", "# Problema 7"),
("Use `map` to implement a funtion that receives a list of pairs of integers and returns a new list made from the sum of all pairs.",
 "Usa `map` para implementar una función que reciba una lista de pares de enteros y devuelva una nueva lista formada por la suma de cada par."),

("# Problem 8", "# Problema 8"),
("__Part a)__ Write a function that given two lists of types `A` and `B`, create a list of elements of type `C` obtained by applying a function `f: (A, B) => C` to each pair of values from both lists in the same position. The length of the resulting list must be the minimum length of the input lists.",
 "__Apartado a)__ Escribe una función que, dadas dos listas de tipos `A` y `B`, cree una lista de elementos de tipo `C` obtenidos aplicando una función `f: (A, B) => C` a cada par de valores de ambas listas en la misma posición. La longitud de la lista resultante debe ser la longitud mínima de las listas de entrada."),
("__Part b)__ Use the function `zipWith` to implement the function `sum` below.",
 "__Apartado b)__ Usa la función `zipWith` para implementar la función `sum` de abajo."),

("# Problem 9", "# Problema 9"),
("__Part a)__ Write the function `ocurrences`, which counts the number of elements that satisfy a given predicate. Use the `foldLeft` HOF.",
 "__Apartado a)__ Escribe la función `ocurrences`, que cuenta el número de elementos que satisfacen un predicado dado. Usa la HOF `foldLeft`."),
("__Part b)__ Use the generic function `occurrences` to create a function that counts the number of occurrences of a given element in a list.",
 "__Apartado b)__ Usa la función genérica `occurrences` para crear una función que cuente el número de ocurrencias de un elemento dado en una lista."),
("__Part c)__ Implement the function `occurrencesOf` using `filter` and `length`.",
 "__Apartado c)__ Implementa la función `occurrencesOf` usando `filter` y `length`."),

("# Problem 10", "# Problema 10"),
("__Part a)__ Write a function that takes the longest prefix of elements of a list that satisfy a given predicate.",
 "__Apartado a)__ Escribe una función que tome el prefijo más largo de elementos de una lista que satisfacen un predicado dado."),
("__Part b)__ Use the function `takeWhile` to implement `takePositives`, a function that returns the longest prefix of positive numbers of a list of integers.",
 "__Apartado b)__ Usa la función `takeWhile` para implementar `takePositives`, una función que devuelva el prefijo más largo de números positivos de una lista de enteros."),

("# Problem 11", "# Problema 11"),
("__Part a)__ Write a function that partitions a list of elements into two lists with all the elements that satisfy and do not satisfy, respectively, a given predicate.",
 "__Apartado a)__ Escribe una función que reparta una lista de elementos en dos listas con todos los elementos que satisfacen y no satisfacen, respectivamente, un predicado dado."),
("__Part b)__ Write a function that partitions a list of integers into a list of odd numbers and a list of even numbers.",
 "__Apartado b)__ Escribe una función que reparta una lista de enteros en una lista de números impares y una lista de números pares."),

("# Problem 12", "# Problema 12"),
("The functions of this problem must terminate as soon as possible. Explain why using `foldRight` is not adequate given this constraint.",
 "Las funciones de este problema deben terminar lo antes posible. Explica por qué usar `foldRight` no es adecuado dada esta restricción."),
("__Part a)__ Write a function to determine if all the elements of a list pass a given predicate.",
 "__Apartado a)__ Escribe una función para determinar si todos los elementos de una lista pasan un predicado dado."),
("__Part b)__ Write a function that given a predicate and a list returns true if there exists some element of the list that passes the predicate; false, otherwise.",
 "__Apartado b)__ Escribe una función que, dados un predicado y una lista, devuelva true si existe algún elemento de la lista que pasa el predicado; false, en caso contrario."),
("__Part c)__ Write a function to know if a given element is member of a list using `exists` or `forall`.",
 "__Apartado c)__ Escribe una función para saber si un elemento dado es miembro de una lista usando `exists` o `forall`."),

("# Trees", "# Árboles"),
("The following problems deal with the `Tree` ADT.", "Los siguientes problemas tratan sobre el ADT `Tree`."),
("The companion object defines some smart constructors that will allow us to write test cases more easily.",
 "El objeto compañero define algunos constructores inteligentes que nos permitirán escribir casos de prueba más fácilmente."),

("# Problem 13", "# Problema 13"),
("Implement the `foldTree` function, which implements a divide-and-conquer strategy on trees. In particular, the first argument `empty` represents the direct solution to the problem corresponding to the empty tree; the `node` argument specifies the way of solving the whole problem from the sub-solutions to the problems corresponding to the left and right trees.",
 "Implementa la función `foldTree`, que implementa una estrategia de divide y vencerás sobre árboles. En particular, el primer argumento `empty` representa la solución directa al problema correspondiente al árbol vacío; el argumento `node` especifica la forma de resolver el problema completo a partir de las subsoluciones a los problemas correspondientes a los árboles izquierdo y derecho."),
("For instance, we can implement function that computes the number of nodes a tree using `foldTree` in the following way:",
 "Por ejemplo, podemos implementar la función que calcula el número de nodos de un árbol usando `foldTree` de la siguiente manera:"),
("Test that your implementation of `foldTree` is correct using the following test catalogue:",
 "Comprueba que tu implementación de `foldTree` es correcta usando el siguiente catálogo de pruebas:"),

("# Problem 14", "# Problema 14"),
("Use `foldTree` to create a function that calculates the _height_ of a tree, which is defined as the depth of its deepest node (the depth of a node, in turn, is the number of edges from that node to the root of the tree).",
 "Usa `foldTree` para crear una función que calcule la _altura_ de un árbol, que se define como la profundidad de su nodo más profundo (la profundidad de un nodo, a su vez, es el número de aristas desde ese nodo hasta la raíz del árbol)."),

("# Problem 15", "# Problema 15"),
("Use `foldTree` to create a function that determines whether a tree is degenerate or not.",
 "Usa `foldTree` para crear una función que determine si un árbol es degenerado o no."),

("# Problem 16", "# Problema 16"),
("Use `foldTree` to write a function that returns the leaves of a tree. The leafs of any left child must be placed in the list before any leaf from its right sibling.",
 "Usa `foldTree` para escribir una función que devuelva las hojas de un árbol. Las hojas de cualquier hijo izquierdo deben colocarse en la lista antes que cualquier hoja de su hermano derecho."),

("# Problem 17", "# Problema 17"),
("This problem deals with [_tree traversals_](https://en.wikipedia.org/wiki/Tree_traversal). Use the `foldTree` function in their implementation.",
 "Este problema trata sobre los [_recorridos de árboles_](https://en.wikipedia.org/wiki/Tree_traversal). Usa la función `foldTree` en su implementación."),
("__Part a)__ Write a function that creates the pre-order of a binary tree.",
 "__Apartado a)__ Escribe una función que cree el recorrido en preorden de un árbol binario."),
("__Part b)__ Write a function that returns the in-order of a binary tree",
 "__Apartado b)__ Escribe una función que devuelva el recorrido en orden de un árbol binario"),
("__Part c)__ Write a function that returns post-order of a binary tree",
 "__Apartado c)__ Escribe una función que devuelva el recorrido en postorden de un árbol binario"),

("# Problem 18", "# Problema 18"),
("The `foldLeft` HOF for trees can be implemented by first obtaining the in-order traversal of the tree, and then applying the `foldLeft` for `List`s:",
 "La HOF `foldLeft` para árboles puede implementarse obteniendo primero el recorrido en orden del árbol, y luego aplicando el `foldLeft` para `List`s:"),
("__Part a)__ Give a recursive implementation of `foldLeft` without creating an intermediate list. The function need not be tail-recursive.",
 "__Apartado a)__ Da una implementación recursiva de `foldLeft` sin crear una lista intermedia. La función no necesita ser recursiva final."),

("""__Part b)__ Give a tail-recursive implementation of `foldLeft`.

_Hint_: Use a stack (in the form of a `List`) to store _either_ the trees _or_ the elements that must be traversed.""",
 """__Apartado b)__ Da una implementación recursiva final de `foldLeft`.

_Pista_: Usa una pila (en forma de `List`) para almacenar _o bien_ los árboles _o bien_ los elementos que deben recorrerse."""),

("# Problem 19", "# Problema 19"),
("Implement the `map` function for `Tree`s using the `foldTree` HOF.",
 "Implementa la función `map` para `Tree`s usando la HOF `foldTree`."),
("Check that the solution is correct by testing the `sum` function:",
 "Comprueba que la solución es correcta probando la función `sum`:"),
]
