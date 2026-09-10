PAIRS = [
("### Preamble", "### Preámbulo"),
("# Topic 7. Applications", "# Tema 7. Aplicaciones"),
("## 7.2 Implementing & querying data models", "## 7.2 Implementar y consultar modelos de datos"),

("The Scala collections library greatly facilitate the implementation and querying of data models. For instance, the following classes model the structure of an organization which consists of departments, employees and tasks that employees can perform.",
 "La biblioteca de colecciones de Scala facilita enormemente la implementación y consulta de modelos de datos. Por ejemplo, las siguientes clases modelan la estructura de una organización formada por departamentos, empleados y tareas que los empleados pueden realizar."),

("This implementation is an example of a _flat_ data model. The key feature of these kinds of models are that the different entities (employees, departments and tasks, in this case) refer to each other by using _keys_. This is a possible instance of the organization data model:",
 "Esta implementación es un ejemplo de modelo de datos _plano_. La característica clave de este tipo de modelos es que las distintas entidades (empleados, departamentos y tareas, en este caso) se refieren unas a otras usando _claves_. Esta es una posible instancia del modelo de datos de la organización:"),

("Flat data models are actually very close to the common _relational_ data models used in SQL persistent stores. This is the equivalent relational model of the organization database:",
 "Los modelos de datos planos están en realidad muy cerca de los modelos de datos _relacionales_ habituales usados en los almacenes persistentes SQL. Este es el modelo relacional equivalente de la base de datos de la organización:"),

("""According to this mapping:
- The `Organization` class represents the whole relational _database_.
- Members of this class correspond to the different _tables_ of the database, represented as `Map`s or simple `Set`s. We have four tables: the table of departments, employees, tasks, and a table which stores which tasks employees can perform.
- The key type of `Map` can be understood as the primary key of the relational table. The value type specifies the columns of the table. By convention, the identifier type is defined by the `Id` type alias in the companion object of the value type. For instance, the `employees` table is indexed by the employee identifier (a string value), and stores the department to which the employee belongs to.
- If the primary key consists of several keys, as in the `knows` table, we use tuples.
- If the table just consists of the key (simple or composed) we use `Set` instead of `Map` (as the `knows` table also illustrates).""",
 """Según esta correspondencia:
- La clase `Organization` representa toda la _base de datos_ relacional.
- Los miembros de esta clase corresponden a las distintas _tablas_ de la base de datos, representadas como `Map`s o `Set`s simples. Tenemos cuatro tablas: la tabla de departamentos, empleados, tareas, y una tabla que almacena qué tareas pueden realizar los empleados.
- El tipo de la clave de `Map` puede entenderse como la clave primaria de la tabla relacional. El tipo del valor especifica las columnas de la tabla. Por convención, el tipo del identificador se define mediante el alias de tipo `Id` en el objeto compañero del tipo del valor. Por ejemplo, la tabla `employees` está indexada por el identificador del empleado (un valor de tipo cadena), y almacena el departamento al que pertenece el empleado.
- Si la clave primaria consiste en varias claves, como en la tabla `knows`, usamos tuplas.
- Si la tabla consiste únicamente en la clave (simple o compuesta) usamos `Set` en vez de `Map` (como también ilustra la tabla `knows`)."""),

("## Basic queries", "## Consultas básicas"),
("Complex queries typically builds upon basic queries which are directly related to the structure of the data model. In particular, they are identified from the primary key and foreign-key relations in the relational model. In the organizational database we can identify the following queries:",
 "Las consultas complejas habitualmente se construyen a partir de consultas básicas directamente relacionadas con la estructura del modelo de datos. En particular, se identifican a partir de la clave primaria y las relaciones de clave foránea en el modelo relacional. En la base de datos de la organización podemos identificar las siguientes consultas:"),

("## Sample queries", "## Consultas de ejemplo"),
("__Which are the tasks of the organization which can't be performed by any employee?__",
 "__¿Cuáles son las tareas de la organización que no puede realizar ningún empleado?__"),
("This is a conventional imperative implementation, using mutable variables:",
 "Esta es una implementación imperativa convencional, usando variables mutables:"),
("This works but it is not the _functional_ style. The following version is closer to what we are looking for:",
 "Esto funciona, pero no es el estilo _funcional_. La siguiente versión está más cerca de lo que buscamos:"),
("or with pattern matching syntax:", "o con sintaxis de pattern matching:"),
("But we can do it even better. We will endorse the following implementation that uses hight-level set operations (`diff`) and HOFs (`map`):",
 "Pero podemos hacerlo todavía mejor. Adoptaremos la siguiente implementación, que usa operaciones de conjuntos de alto nivel (`diff`) y HOF (`map`):"),
("Arguably, this implementation conveys the intent of the function more clearly. It's more _declarative_. Moreover, it is more reliable since it builds upon standard methods of the Scala library (`diff` and `map`). It's true that the imperative version is also easy to read, but this is only because this is such a very simple function. We will see later on more complex examples where the functional solution shines brighter.",
 "Podría decirse que esta implementación transmite la intención de la función con más claridad. Es más _declarativa_. Además, es más fiable, ya que se apoya en métodos estándar de la biblioteca de Scala (`diff` y `map`). Es cierto que la versión imperativa también es fácil de leer, pero eso es solo porque esta es una función muy simple. Más adelante veremos ejemplos más complejos donde la solución funcional brilla más."),

("__Which tasks can be performed by the employees of a given department?__",
 "__¿Qué tareas pueden realizar los empleados de un departamento dado?__"),
("The basic queries of the data model allow us to obtain all the employees of an organization, and the tasks that they can perform. So, this a first step towards the solution:",
 "Las consultas básicas del modelo de datos nos permiten obtener todos los empleados de una organización, y las tareas que pueden realizar. Así, este es un primer paso hacia la solución:"),
("However, this is not the signature that we need to implement, since we are returning a set of sets of tasks, not a set of tasks. In order to do it right we need also to _flatten_ the result, i.e. concatenate all the individual sets of tasks for each employee. In sum, we need the `flatMap` HOF:",
 "Sin embargo, esta no es la signatura que necesitamos implementar, ya que estamos devolviendo un conjunto de conjuntos de tareas, no un conjunto de tareas. Para hacerlo bien también necesitamos _aplanar_ (flatten) el resultado, es decir, concatenar todos los conjuntos individuales de tareas de cada empleado. En resumen, necesitamos la HOF `flatMap`:"),

("__Compute the list of departments of an organization together with the number of tasks their employees can perform, sorted by the number of tasks__",
 "__Calcula la lista de departamentos de una organización junto con el número de tareas que pueden realizar sus empleados, ordenada por el número de tareas__"),

("__Which are the employees who can perform tasks of a given duration?__",
 "__¿Cuáles son los empleados que pueden realizar tareas de una duración dada?__"),
("Alterrnatively, we can also bet by with `filter` and `exists`:",
 "Alternativamente, también podemos apostar por `filter` y `exists`:"),

("__Which are the departments whose employees, as a team, know how to perform a given set of tasks?__",
 "__¿Cuáles son los departamentos cuyos empleados, como equipo, saben realizar un conjunto de tareas dado?__"),
("We can build upon the previous function `allTasks`:", "Podemos apoyarnos en la función anterior `allTasks`:"),

("__Obtain a list of employees sorted by the number of tasks that they can perform__",
 "__Obtén una lista de empleados ordenada por el número de tareas que pueden realizar__"),
("We may attempt the following:", "Podríamos intentar lo siguiente:"),
("and this is almost right: we are missing those employees that can't perform any task. This is the right one:",
 "y esto es casi correcto: nos faltan aquellos empleados que no pueden realizar ninguna tarea. Esta es la correcta:"),

("__Which are the departments whose employees are all able to perform a given task?__",
 "__¿Cuáles son los departamentos cuyos empleados son todos capaces de realizar una tarea dada?__"),
("The conventional imperative solution is quite complex:", "La solución imperativa convencional es bastante compleja:"),
("This is not only more complex to understand, but prone to error. In order to obtain a simpler (and functional) solution by first declaring in plain natural language the intended query:",
 "Esto no solo es más complejo de entender, sino propenso a errores. Para obtener una solución más simple (y funcional) empecemos declarando en lenguaje natural llano la consulta pretendida:"),
("Then, we can formalize the natural language specification by relying on standard HOFs (`filter`, `forall`) and collection operations (`contains`):",
 "Entonces, podemos formalizar la especificación en lenguaje natural apoyándonos en HOF estándar (`filter`, `forall`) y operaciones de colecciones (`contains`):"),

# --- comentarios ---
("// departments", "// departamentos"),
("// Employees", "// Empleados"),
("// tasks", "// tareas"),
("// The whole organization", "// La organización completa"),
("// Entities", "// Entidades"),
("// 1-N relationships", "// relaciones 1-N"),
("// N-M relationships", "// relaciones N-M"),
("// From all the departments of the organization, choose", "// De entre todos los departamentos de la organización, elige"),
("// those that for all its employees", "// aquellos en los que, para todos sus empleados,"),
("// the specified task is included in their capabilities", "// la tarea especificada está incluida en sus capacidades"),
("// tasks, taskIds and getTask of the organization", "// tasks, taskIds y getTask de la organización"),
]
