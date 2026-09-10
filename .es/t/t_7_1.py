PAIRS = [
("### Preamble", "### Preámbulo"),
("# Topic 7. Applications", "# Tema 7. Aplicaciones"),
("## 7.1 Scala Collections", "## 7.1 Las colecciones de Scala"),

("""### References

A gentle guide to the Scala's collection library can be found online in the Scala site:

https://docs.scala-lang.org/scala3/book/collections-intro.html""",
 """### Referencias

Una guía introductoria a la biblioteca de colecciones de Scala puede encontrarse en línea en el sitio de Scala:

https://docs.scala-lang.org/scala3/book/collections-intro.html"""),

("""[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_3ed) Third Edition.
by Martin Odersky, Lex Spoon, and Bill Venners.

- Chapter 11. Scala's Hierarchy
- Chapter 17. Working with Other Collections
- Chapter 24. Collections in Depth
- Chapter 25. The Architecture of Scala Collections

[__Functional programming in Scala__](https://www.manning.com/books/functional-programming-in-scala), by Paul Chiusano and Runar Bjarnason.

- Chapter 3. Functional data structures

[__Functional programming simplified__](https://alvinalexander.com/downloads/fpsimplified-free-preview.pdf), by Alvin Alexander.

- Chapters 29-36. Recursion.""",
 """[__Programming in Scala,
A comprehensive step-by-step guide__](https://www.artima.com/shop/programming_in_scala_3ed) Tercera edición.
por Martin Odersky, Lex Spoon, y Bill Venners.

- Capítulo 11. La jerarquía de Scala
- Capítulo 17. Trabajando con otras colecciones
- Capítulo 24. Las colecciones en profundidad
- Capítulo 25. La arquitectura de las colecciones de Scala

[__Functional programming in Scala__](https://www.manning.com/books/functional-programming-in-scala), por Paul Chiusano y Runar Bjarnason.

- Capítulo 3. Estructuras de datos funcionales

[__Functional programming simplified__](https://alvinalexander.com/downloads/fpsimplified-free-preview.pdf), por Alvin Alexander.

- Capítulos 29-36. Recursión."""),

("### Collection types", "### Tipos de colección"),

("""Collection types can be classified along two major dimensions:
- Mutable/Immutable: mutable collections can be modified in-place; immutable collections return a new instance when they are updated.
- Sequences/Sets/Maps. These are ordered/unordered collections and key-value collections, respectively.

There are many different implementations of sequences, sets and maps, as summarized by these figures (cf. Scala's [guide](https://docs.scala-lang.org/scala3/book/collections-classes.html))""",
 """Los tipos de colección pueden clasificarse según dos dimensiones principales:
- Mutable/Inmutable: las colecciones mutables pueden modificarse en el sitio; las colecciones inmutables devuelven una nueva instancia cuando se actualizan.
- Secuencias/Conjuntos/Mapas. Son, respectivamente, colecciones ordenadas/no ordenadas y colecciones de pares clave-valor.

Hay muchas implementaciones distintas de secuencias, conjuntos y mapas, como resumen estas figuras (cf. la [guía](https://docs.scala-lang.org/scala3/book/collections-classes.html) de Scala)"""),

("""How do we choose from this huge number of collection types and implementations? The colletion type is chosen according to the functionality that we demand from our collection, e.g., should it be _ordered_?, can there be repeated elements?, are elements associated with keys?, etc. In order to choose the right implementation of the collection type (e.g. should I use a `Vector` or a `List`?) we must take into account the complexity of the corresponding implementation:

https://docs.scala-lang.org/overviews/collections-2.13/performance-characteristics.html

From now on, we will work with immutable collection types only.""",
 """¿Cómo elegimos entre este enorme número de tipos de colección e implementaciones? El tipo de colección se elige según la funcionalidad que le exigimos a nuestra colección, p. ej., ¿debe estar _ordenada_?, ¿puede haber elementos repetidos?, ¿los elementos están asociados a claves?, etc. Para elegir la implementación correcta del tipo de colección (p. ej. ¿debería usar un `Vector` o una `List`?) debemos tener en cuenta la complejidad de la implementación correspondiente:

https://docs.scala-lang.org/overviews/collections-2.13/performance-characteristics.html

A partir de ahora, trabajaremos únicamente con tipos de colección inmutables."""),

("# Maps", "# Mapas"),
("`Map`s are key-value collections (i.e. they are like sets of key-value pairs indexed by their keys). Check out the [Scala 3 API](https://www.scala-lang.org/api/current/scala/collection/immutable/Map.html).",
 "Los `Map`s son colecciones clave-valor (es decir, son como conjuntos de pares clave-valor indexados por sus claves). Consulta la [API de Scala 3](https://www.scala-lang.org/api/current/scala/collection/immutable/Map.html)."),
("Specially for key-value pairs, we commonly write `Tuple2` values with the following syntax:",
 "Especialmente para los pares clave-valor, habitualmente escribimos los valores `Tuple2` con la siguiente sintaxis:"),
("Common operations on maps:", "Operaciones comunes sobre mapas:"),

("""The default implementation types of these `Iterable`s are `collection.immutable.Set` and the general `View` type. Views are _lazy_ collections which offer better performance. For more information on views consult the Scala [guide](https://docs.scala-lang.org/overviews/collections-2.13/views.html). The only thing that we need from views and the general `Iterable` collection type is that they can be converted to a concrete collection type with conversors `toList`, `toSet`, `toMap`, etc.""",
 """Los tipos de implementación por defecto de estos `Iterable`s son `collection.immutable.Set` y el tipo general `View`. Las vistas (`View`) son colecciones _perezosas_ que ofrecen mejor rendimiento. Para más información sobre las vistas consulta la [guía](https://docs.scala-lang.org/overviews/collections-2.13/views.html) de Scala. Lo único que necesitamos de las vistas y del tipo de colección general `Iterable` es que pueden convertirse a un tipo de colección concreto con los conversores `toList`, `toSet`, `toMap`, etc."""),

("We can also convert optional values to collection types:",
 "También podemos convertir valores opcionales a tipos de colección:"),
("Map and filter are also available for maps:", "Map y filter también están disponibles para mapas:"),
("We can obtain a `Map` from a list of pairs with `toMap`:",
 "Podemos obtener un `Map` a partir de una lista de pares con `toMap`:"),
("Note that only one value is kept for a single key. If we want all values, we can use `groupBy`:",
 "Nótese que solo se conserva un valor para cada clave. Si queremos todos los valores, podemos usar `groupBy`:"),

("# Sets", "# Conjuntos"),
("`Set`s are unordered collections of unique elements. Check out the [Scala 3 API](https://www.scala-lang.org/api/current/scala/collection/immutable/Set.html). The following two sets are equal:",
 "Los `Set`s son colecciones no ordenadas de elementos únicos. Consulta la [API de Scala 3](https://www.scala-lang.org/api/current/scala/collection/immutable/Set.html). Los siguientes dos conjuntos son iguales:"),
("Common operations on sets: filter, flatMap, map.", "Operaciones comunes sobre conjuntos: filter, flatMap, map."),
("Specific operations: subsetOf, diff, union, etc.", "Operaciones específicas: subsetOf, diff, union, etc."),

# --- comentarios ---
("// retrieving values of existing and non-existing keys", "// obtener valores de claves existentes y no existentes"),
("// retrieving all keys and values", "// obtener todas las claves y valores"),
("// Converting to proper implementation types", "// Convertir a los tipos de implementación adecuados"),
("// Mapping values (toMap is required to convert the view type `MapView` to `Map`)",
 "// Mapear valores (toMap es necesario para convertir el tipo vista `MapView` a `Map`)"),
("// Mapping whole entries, not only values", "// Mapear entradas completas, no solo valores"),
("// Filter also return a general iterable (a list, by default)", "// Filter también devuelve un iterable general (una lista, por defecto)"),
("// compare with lists:", "// comparar con listas:"),
("// compare with lists", "// comparar con listas"),
("// Filtering elements", "// Filtrar elementos"),
("// Mapping elements", "// Mapear elementos"),
("// Flatmapping elements", "// Aplicar flatMap a elementos"),
("// Common set operations", "// Operaciones comunes de conjuntos"),

("// a map from string to int", "// un mapa de string a int"),
("// map with -> syntax", "// mapa con sintaxis ->"),
("// existing keys with apply", "// claves existentes con apply"),
("// existing keys with get", "// claves existentes con get"),
("// non-existing keys with apply", "// claves no existentes con apply"),
("// non-existing keys with get", "// claves no existentes con get"),
("// Converting `Iterable` keys and lists to sets and lists", "// Convertir claves `Iterable` y listas a conjuntos y listas"),
("// Optional values to set and lists", "// Valores opcionales a conjuntos y listas"),
("// sample list of pairs with repeating keys", "// lista de ejemplo de pares con claves repetidas"),
("// groupBy example", "// ejemplo de groupBy"),
("// constructing sets: repeating occurrences", "// construir conjuntos: repitiendo ocurrencias"),
("// without several occurrences", "// sin varias ocurrencias"),
("// equality of sets", "// igualdad de conjuntos"),
]
