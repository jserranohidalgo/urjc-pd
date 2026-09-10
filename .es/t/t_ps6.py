PAIRS = [
("""# Declarative Programming @ URJC
# Functional programming
## Problem Set 6
### Querying Data Sets""",
 """# Declarative Programming @ URJC
# Programación funcional
## Hoja de problemas 6
### Consultar conjuntos de datos"""),

("This problem set contains different exercises on the standard HOFs and operations of the Scala collection framework. The goal is to write queries over a data model implemented using case classes, `Map`s and `List`s, etc., in a declarative and functional style.",
 "Esta hoja de problemas contiene distintos ejercicios sobre las HOF estándar y las operaciones del framework de colecciones de Scala. El objetivo es escribir consultas sobre un modelo de datos implementado usando case classes, `Map`s y `List`s, etc., en un estilo declarativo y funcional."),

("# Movie database", "# Base de datos de películas"),
("We will use a small data model that declares information about films, directors, actors, etc., and the ratings of these films by registered users.",
 "Usaremos un pequeño modelo de datos que declara información sobre películas, directores, actores, etc., y las valoraciones de esas películas por parte de usuarios registrados."),
("The following instance of the movie database will be used in the test catalogues for the different queries below.",
 "La siguiente instancia de la base de datos de películas se usará en los catálogos de pruebas de las distintas consultas de abajo."),

("# Problem 1", "# Problema 1"),
("Write the followig basic queries for the movie database.", "Escribe las siguientes consultas básicas para la base de datos de películas."),

("# Problem 2", "# Problema 2"),
("__Part a)__ Write an auxiliary function that computes the average of a list of values. For simplicity, assume that the average of an empty list is 0/0 (i.e. the special `Double` value `NaN`). Implement the function using `foldLeft` -- and try to do it in a single traversal.",
 "__Apartado a)__ Escribe una función auxiliar que calcule la media de una lista de valores. Por simplicidad, asume que la media de una lista vacía es 0/0 (es decir, el valor especial `NaN` de `Double`). Implementa la función usando `foldLeft` -- e intenta hacerlo en un único recorrido."),
("__Part b)__ Write a function that computes the average score of a film.",
 "__Apartado b)__ Escribe una función que calcule la puntuación media de una película."),
("__Part c)__ Write a function that computes the average score of all the films in a movie database.",
 "__Apartado c)__ Escribe una función que calcule la puntuación media de todas las películas de una base de datos de películas."),

("# Problem 3", "# Problema 3"),
("Write functions to compute the following rankings of a movie dataset.",
 "Escribe funciones para calcular los siguientes rankings de un conjunto de datos de películas."),
("__Part a)__ Obtain a ranking of films, sorted by their number of ratings in descending order.",
 "__Apartado a)__ Obtén un ranking de películas, ordenadas por su número de valoraciones en orden descendente."),
("__Part b)__ Obtain a ranking of films, sorted by their average score in ascending order.",
 "__Apartado b)__ Obtén un ranking de películas, ordenadas por su puntuación media en orden ascendente."),

("# Problem 4", "# Problema 4"),
("__Part a)__ Obtain the list of the `n` favourite films of a user (i.e. the ones that the user gave them a highest score).",
 "__Apartado a)__ Obtén la lista de las `n` películas favoritas de un usuario (es decir, aquellas a las que el usuario dio la puntuación más alta)."),
("__Part b)__ Write a function that gives the name of the user, the title of the film, and the score of a given rating.",
 "__Apartado b)__ Escribe una función que dé el nombre del usuario, el título de la película, y la puntuación de una valoración dada."),
("__Part c)__ Same function as in part a), but now returning the name of the user, the title of the film and the score of the user for that film.",
 "__Apartado c)__ La misma función que en el apartado a), pero devolviendo ahora el nombre del usuario, el título de la película y la puntuación del usuario para esa película."),

("# Problem 5", "# Problema 5"),
("__Part a)__ Obtain the average rating of all films that belongs to a given genre.",
 "__Apartado a)__ Obtén la valoración media de todas las películas que pertenecen a un género dado."),
("__Part b)__ Use `for-comprehensions` to write the previous query.",
 "__Apartado b)__ Usa `for-comprehensions` para escribir la consulta anterior."),
("__Part c)__ Write a query that returns the average ratings of all genres in the movie database. Particularly, the query must return a `Map` whose keys and values are the genres and their ratings, respectively.",
 "__Apartado c)__ Escribe una consulta que devuelva las valoraciones medias de todos los géneros de la base de datos de películas. En particular, la consulta debe devolver un `Map` cuyas claves y valores sean los géneros y sus valoraciones, respectivamente."),

# --- comentarios ---
("// Entities", "// Entidades"),
("// 1-N relationships", "// relaciones 1-N"),
("// N-M relationships", "// relaciones N-M"),
]
