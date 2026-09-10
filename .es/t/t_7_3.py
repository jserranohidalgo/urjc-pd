# -*- coding: utf-8 -*-
PAIRS = [
("### Preamble", "### Preámbulo"),
("# Topic 7. Applications", "# Tema 7. Aplicaciones"),
("## 7.3 Games", "## 7.3 Juegos"),

("In this section we will exploit ADTs and higher-order functions to implement the game of Wordle. In doing so, we will also emphasise the general design patterns that can be applied to implement these kinds of applications.",
 "En esta sección explotaremos los tipos algebraicos de datos y las funciones de orden superior para implementar el juego de Wordle. Al hacerlo, también destacaremos los patrones de diseño generales que pueden aplicarse para implementar este tipo de aplicaciones."),

("##### Wordle specification", "##### Especificación de Wordle"),

("Wordle is a popular online word game that challenges players to guess a five-letter word within six tries. Each guess must be a valid five-letter word. After each guess, the game provides feedback in the form of colored tiles, indicating how close the guess was to the word. A green tile shows that a letter is correct and in the right position, a yellow tile indicates that the letter is correct but in the wrong position, and a gray tile means that the letter is not in the word at all. The goal is to guess the correct word in as few tries as possible.",
 "Wordle es un popular juego de palabras en línea que reta a los jugadores a adivinar una palabra de cinco letras en seis intentos. Cada intento debe ser una palabra válida de cinco letras. Después de cada intento, el juego da información en forma de casillas coloreadas, que indican cuán cerca estuvo el intento de la palabra. Una casilla verde indica que una letra es correcta y está en la posición correcta, una casilla amarilla indica que la letra es correcta pero está en la posición equivocada, y una casilla gris significa que la letra no está en la palabra en absoluto. El objetivo es adivinar la palabra correcta en el menor número de intentos posible."),

("""For instance, this a game in which the correct word ("slice") was guessed in three attempts:""",
 """Por ejemplo, esta es una partida en la que la palabra correcta ("slice") se adivinó en tres intentos:"""),

("""- Guess 1: CRANE
  - 🟨⬛⬛⬛🟩
- Guess 2: PIOUS
  - ⬛🟨⬛⬛🟨
- Guess 3: SLICE
  - 🟩🟩🟩🟩🟩""",
 """- Intento 1: CRANE
  - 🟨⬛⬛⬛🟩
- Intento 2: PIOUS
  - ⬛🟨⬛⬛🟨
- Intento 3: SLICE
  - 🟩🟩🟩🟩🟩"""),

("""In the first guess, "CRANE", the first letter is marked with a yellow tile since it appears in the word "SLICE" in a different position; the letters "R", "A" and "N" do not appear, and they are marked with a gray tile accordingly; last, the letter "E" appears in the right position and it's therefore marked as green.

Green and gray tiles are easy to assign, but potential yellow tiles have to be assigned carefully. For instance, consider the following guess of the correct word "ATLAS":""",
 """En el primer intento, "CRANE", la primera letra se marca con una casilla amarilla ya que aparece en la palabra "SLICE" en una posición distinta; las letras "R", "A" y "N" no aparecen, y se marcan en consecuencia con una casilla gris; por último, la letra "E" aparece en la posición correcta y por tanto se marca en verde.

Las casillas verdes y grises son fáciles de asignar, pero las posibles casillas amarillas hay que asignarlas con cuidado. Por ejemplo, considera el siguiente intento para la palabra correcta "ATLAS":"""),

("""- Guess 1: BAABA
  - ⬛🟨🟨⬛⬛""",
 """- Intento 1: BAABA
  - ⬛🟨🟨⬛⬛"""),

("""Note that only the first two occurrences of the letter "A" are marked as yellow. The last occurrence is marked as gray because the correct word only has two occurrences of this letter. Also, consider the following example:""",
 """Nótese que solo las dos primeras ocurrencias de la letra "A" se marcan en amarillo. La última ocurrencia se marca en gris porque la palabra correcta solo tiene dos ocurrencias de esa letra. Considera también el siguiente ejemplo:"""),

("""- Guess 1: BAAAA
  - ⬛🟨⬛🟩⬛""",
 """- Intento 1: BAAAA
  - ⬛🟨⬛🟩⬛"""),

("""In this case, the second occurrence of the letter "A" is marked as gray, even if there are two occurrences of this letter in the correct word. This is because there is an occurrence of this letter in the right position (i.e. marked as green).""",
 """En este caso, la segunda ocurrencia de la letra "A" se marca en gris, aunque haya dos ocurrencias de esa letra en la palabra correcta. Esto es porque hay una ocurrencia de esa letra en la posición correcta (es decir, marcada en verde)."""),

("Last, note that these previous examples were not quite right, because guesses need to be found in the dictionary. In case that they don't, they will be simply rejected and the player will be asked to try again.",
 "Por último, nótese que estos ejemplos anteriores no eran del todo correctos, porque los intentos tienen que encontrarse en el diccionario. Si no es así, simplemente se rechazarán y se le pedirá al jugador que lo intente de nuevo."),

("##### The _machine_ metaphor", "##### La metáfora de la _máquina_"),

("""The implementation of wordle will follow a _machine_ metaphor, whereby game applications are essentially machines which hold a characteristic state that evolve over time in response to user input. From this perspective, we can identify the following components in a game application:
* The state of the game. Which information characterises the game at a given moment?
* The dynamics of the game. How does the game state evolve over time?
* The user interface. How does the user interact with the game machine?

The following sections deal with the implementation of these components.""",
 """La implementación de wordle seguirá una metáfora de _máquina_, según la cual las aplicaciones de juego son esencialmente máquinas que mantienen un estado característico que evoluciona con el tiempo en respuesta a la entrada del usuario. Desde esta perspectiva, podemos identificar los siguientes componentes en una aplicación de juego:
* El estado del juego. ¿Qué información caracteriza al juego en un momento dado?
* La dinámica del juego. ¿Cómo evoluciona el estado del juego con el tiempo?
* La interfaz de usuario. ¿Cómo interactúa el usuario con la máquina del juego?

Las siguientes secciones tratan la implementación de estos componentes."""),

("### The state of the game", "### El estado del juego"),

("""The state of a wordle game can be characterised by the following information:
  * The correct word to be guessed
  * A dictionary of five-letter words
  * The list of attempts so far""",
 """El estado de una partida de wordle puede caracterizarse mediante la siguiente información:
  * La palabra correcta que hay que adivinar
  * Un diccionario de palabras de cinco letras
  * La lista de intentos hasta el momento"""),

("Accordingly, the state of the match shown previously would be implemented as follows:",
 "En consecuencia, el estado de la partida mostrada anteriormente se implementaría de la siguiente manera:"),

("""We can distinguish between the raw information that fully characterised a given state, and the information that we can derive from it, such as:
* Did the player win? This will be the case if the player guessed the word in the last attempt.
* Did the player lose? This will be the case if the player run out of attempts (namely, six) without guessing the word.
* Is the game over? i.e., did the player lose or win?
* Which are the tiles of the different guesses?""",
 """Podemos distinguir entre la información en bruto que caracteriza por completo un estado dado, y la información que podemos derivar de ella, como por ejemplo:
* ¿Ganó el jugador? Esto ocurrirá si el jugador adivinó la palabra en el último intento.
* ¿Perdió el jugador? Esto ocurrirá si el jugador se quedó sin intentos (concretamente, seis) sin adivinar la palabra.
* ¿Ha terminado la partida? Es decir, ¿perdió o ganó el jugador?
* ¿Cuáles son las casillas de los distintos intentos?"""),

("##### Winning", "##### Ganar"),
("##### Losing", "##### Perder"),
("##### Game over", "##### Fin de la partida"),

("### Tile assignment", "### Asignación de casillas"),

("Tile assignment is complex enough to deserve its own section. We will first define a brief catalogue of tests together with basic type definition. Then, we will explain the basic algorithm for tile assignment, and several implementations: first, an imperative one based on mutable variables and for loops; then, an implementation based on the `foldLeft` HOF; and, finally, a more declarative implementation based on state transformations.",
 "La asignación de casillas es lo bastante compleja como para merecer su propia sección. Primero definiremos un breve catálogo de pruebas junto con la definición básica de tipos. Después, explicaremos el algoritmo básico de asignación de casillas, y varias implementaciones: primero, una imperativa basada en variables mutables y bucles for; después, una implementación basada en la HOF `foldLeft`; y, por último, una implementación más declarativa basada en transformaciones de estado."),

("##### Test catalogue", "##### Catálogo de pruebas"),
("We must first define the `Tile` enumeration type:", "Primero tenemos que definir el tipo enumerado `Tile`:"),
("and the type which represent the assignments of tiles to the different letters of the guess word:",
 "y el tipo que representa las asignaciones de casillas a las distintas letras de la palabra intentada:"),
("Note that the type is not simply `List[(Char, Tile)]`. This is in order to reuse this structure throughout the tile assignment process.",
 "Nótese que el tipo no es simplemente `List[(Char, Tile)]`. Esto es para reutilizar esta estructura a lo largo de todo el proceso de asignación de casillas."),
("The test catalogue can then be defined as follows:", "El catálogo de pruebas puede entonces definirse de la siguiente manera:"),

("##### The tile assignment algorithm", "##### El algoritmo de asignación de casillas"),

("""The tile assignment algorithm will use as an auxiliary data structure the _bag_ of letters corresponding to the correct word. A bag is simply a set with possibly repeated occurrences of elements. For instance, the bag associated to the word "ATLAS" is `{A, A, T, L, S}`. Note that the letter `A` appears twice.

Tile assignment will be performed in two major steps:
* In the first one, we will assign green tiles to those letters in the right position. This step will also update the initial bag of letters by removing one occurrence for each green letter found.
* In the second one, we will assign gray and yellow tiles. Yellow tiles will be assigned to those letters that do appear in the bag; each time a yellow tile is assigned for some letter, we will remove an occurrence of this letter from the current bag. Gray tiles will be assigned to those letters that are not contained in the bag.

For instance, given the correct word "ATLAS" the tile assignment of the guess "BAAAA" will be performed as follows:

* Step 1.  Green tile assignment.

    * {A, A, T, L, S}, B -> ?
    * {A, A, T, L, S}, A -> ?
    * {A, A, T, L, S}, A -> ?
    * {A, A, T, L, S}, A -> Green
    * {A, T, L, S}, A -> ?

Preliminary assignment: B -> ?, A -> ?, A -> ?, A -> Green, A -> ?

* Step 2. Yellow and gray assignments.

    * {A, T, L, S}, B -> Gray
    * {A, T, L, S}, A -> Yellow
    * {T, L, S}, A -> Gray
    * {T, L, S}, A -> Green
    * {T, L, S}, A -> Gray

Definitive assignment: B -> Gray, A -> Yellow, A -> Gray, A -> Green, A -> Gray""",
 """El algoritmo de asignación de casillas usará como estructura de datos auxiliar la _bolsa_ de letras correspondiente a la palabra correcta. Una bolsa es simplemente un conjunto con posibles ocurrencias repetidas de elementos. Por ejemplo, la bolsa asociada a la palabra "ATLAS" es `{A, A, T, L, S}`. Nótese que la letra `A` aparece dos veces.

La asignación de casillas se realizará en dos grandes pasos:
* En el primero, asignaremos casillas verdes a aquellas letras que están en la posición correcta. Este paso también actualizará la bolsa inicial de letras eliminando una ocurrencia por cada letra verde encontrada.
* En el segundo, asignaremos casillas grises y amarillas. Las casillas amarillas se asignarán a aquellas letras que sí aparecen en la bolsa; cada vez que se asigna una casilla amarilla para alguna letra, eliminaremos una ocurrencia de esa letra de la bolsa actual. Las casillas grises se asignarán a aquellas letras que no están contenidas en la bolsa.

Por ejemplo, dada la palabra correcta "ATLAS" la asignación de casillas del intento "BAAAA" se realizará de la siguiente manera:

* Paso 1. Asignación de casillas verdes.

    * {A, A, T, L, S}, B -> ?
    * {A, A, T, L, S}, A -> ?
    * {A, A, T, L, S}, A -> ?
    * {A, A, T, L, S}, A -> Verde
    * {A, T, L, S}, A -> ?

Asignación preliminar: B -> ?, A -> ?, A -> ?, A -> Verde, A -> ?

* Paso 2. Asignaciones amarillas y grises.

    * {A, T, L, S}, B -> Gris
    * {A, T, L, S}, A -> Amarillo
    * {T, L, S}, A -> Gris
    * {T, L, S}, A -> Verde
    * {T, L, S}, A -> Gris

Asignación definitiva: B -> Gris, A -> Amarillo, A -> Gris, A -> Verde, A -> Gris"""),

("##### Implementing bags", "##### Implementar bolsas"),
("The bag data structure is not included in the Scala collection library, but we can defined it easily in terms of a mapping from letters to an integer representing its multiplicity:",
 "La estructura de datos bolsa no está incluida en la biblioteca de colecciones de Scala, pero podemos definirla fácilmente en términos de una correspondencia de letras a un entero que representa su multiplicidad:"),
("Besides being able to create a bag from a given string, we will also need an operation that allow us to remove an occurrence from the bag. We called this operation `rm`. For instance:",
 "Además de poder crear una bolsa a partir de una cadena dada, también necesitaremos una operación que nos permita eliminar una ocurrencia de la bolsa. A esta operación la llamamos `rm`. Por ejemplo:"),

("##### Imperative implementation", "##### Implementación imperativa"),
("The imperative implementation is straightforward: it basically follows an iterative process whereby we incrementally update an initially empty tile assignment in two major phases, using as an auxiliary data structure the bag of letters.",
 "La implementación imperativa es directa: básicamente sigue un proceso iterativo mediante el cual actualizamos incrementalmente una asignación de casillas inicialmente vacía en dos grandes fases, usando como estructura de datos auxiliar la bolsa de letras."),

("##### FoldLeft implementation", "##### Implementación con foldLeft"),
("The `foldLeft` solution implements the very same iterative algoritm of the imperative one. The only difference is that for-loops and auxiliary mutable variables are hidden or encapsulated by the `foldLeft` function:",
 "La solución con `foldLeft` implementa exactamente el mismo algoritmo iterativo que la imperativa. La única diferencia es que los bucles for y las variables mutables auxiliares quedan ocultos o encapsulados por la función `foldLeft`:"),

("##### With state-transformations", "##### Con transformaciones de estado"),
("The `foldLeft` implementation was a little more concise, but it can hardly be regarded as a definitive improvement over the imperative solution. Essentially, this is because they both implement the same iterative algoritm. In order to move further in the ladder of abstraction, and come up with a more declarative solution, we may attempt to use the `map` HOF: in step 1, this is actually what we need. Indeed, the goal of this step is to map each letter in the right position of the guess word into a green assignment. We can achieve this by zipping the correct and the guess words:",
 "La implementación con `foldLeft` era un poco más concisa, pero difícilmente puede considerarse una mejora definitiva sobre la solución imperativa. Básicamente, esto es porque ambas implementan el mismo algoritmo iterativo. Para avanzar más en la escalera de la abstracción, y llegar a una solución más declarativa, podríamos intentar usar la HOF `map`: en el paso 1, esto es en realidad lo que necesitamos. En efecto, el objetivo de este paso es mapear cada letra en la posición correcta de la palabra intentada a una asignación verde. Podemos conseguir esto haciendo un zip de la palabra correcta y la palabra intentada:"),

("We still need to remove the letters with green occurrences from the bag, but this could be done easily in a new intermediate step. However, the second step is more complicated: there, we need to traverse the preliminary assignment from left to right, and update the bag each time we perform a yellow assignment. This update has to be done while we are traversing the assignment; it can't be done in a subsequent step.",
 "Todavía necesitamos eliminar de la bolsa las letras con ocurrencias verdes, pero esto podría hacerse fácilmente en un nuevo paso intermedio. Sin embargo, el segundo paso es más complicado: ahí, necesitamos recorrer la asignación preliminar de izquierda a derecha, y actualizar la bolsa cada vez que realizamos una asignación amarilla. Esta actualización tiene que hacerse mientras recorremos la asignación; no puede hacerse en un paso posterior."),

("Still, we can conceptualize the algorithm in terms of the `map` HOF with the help of so-called _state-transformations_ (or actions). Specifically, we can map each preliminary assignment to a bag transformation, which are later on combined sequentially. This is the essence of the `traverse` higher-order function: first, map the structure into some computation (a state-transformation in our case), and then fuse these computations sequentially.",
 "Aun así, podemos conceptualizar el algoritmo en términos de la HOF `map` con la ayuda de las llamadas _transformaciones de estado_ (o acciones). Concretamente, podemos mapear cada asignación preliminar a una transformación de la bolsa, que luego se combinan secuencialmente. Esta es la esencia de la función de orden superior `traverse`: primero, mapear la estructura a alguna computación (una transformación de estado en nuestro caso), y luego fusionar esas computaciones secuencialmente."),

("Now, state-transformations, traversals, etc., are out of the scope of this first course on functional programming. We implement these abstractions below and use them in the implementation of the tile assignment function, only to show that a more declarative implementation of this function is indeed possible.",
 "Ahora bien, las transformaciones de estado, los traverse, etc., quedan fuera del alcance de este primer curso de programación funcional. Implementamos estas abstracciones a continuación y las usamos en la implementación de la función de asignación de casillas, solo para mostrar que en efecto es posible una implementación más declarativa de esta función."),

("""Although this implementation essentially performs the same steps as the iterative algorithm illustrated previously through the imperative and `foldLeft`-based implementations, it is of a more declarative nature. Note that we don't have to deal with the construction of the list of assignments, for instance. Also, the implementation can be explained in terms of higher-level conceptual blocks as follows:
* First, zip together the correct and guess words to obtain a list of potentially matching characters.
* Second, assign a green tile for each matching letter and remove an occurrence from the bag; for non-matching letters, simply return a temporary void assignment.
* Third, update the preliminary assignments as follows: if the letter was not actually assigned any tile and it's contained in the bag, then assign a yellow tile for it and remove an occurrence of that letter from the bag; otherwise, return a gray assignment; if the letter was assigned a green tile, keep that assignment.

The following image illustrates the conceptual structure of the implementation:""",
 """Aunque esta implementación esencialmente realiza los mismos pasos que el algoritmo iterativo ilustrado anteriormente mediante las implementaciones imperativa y basada en `foldLeft`, tiene una naturaleza más declarativa. Nótese que no tenemos que ocuparnos, por ejemplo, de la construcción de la lista de asignaciones. Además, la implementación puede explicarse en términos de bloques conceptuales de más alto nivel de la siguiente manera:
* Primero, hacer un zip de la palabra correcta y la palabra intentada para obtener una lista de caracteres potencialmente coincidentes.
* Segundo, asignar una casilla verde por cada letra coincidente y eliminar una ocurrencia de la bolsa; para las letras no coincidentes, simplemente devolver una asignación temporal vacía.
* Tercero, actualizar las asignaciones preliminares de la siguiente manera: si a la letra en realidad no se le asignó ninguna casilla y está contenida en la bolsa, entonces asignarle una casilla amarilla y eliminar una ocurrencia de esa letra de la bolsa; en caso contrario, devolver una asignación gris; si a la letra se le asignó una casilla verde, mantener esa asignación.

La siguiente imagen ilustra la estructura conceptual de la implementación:"""),

("##### Cats implementation", "##### Implementación con Cats"),
("After reviewing the last implementation, you may think that achieving declarative implementations is an ardous task: we don't only need to understand higher-level abstractions like state-transformations, traversals, etc., but also to implement these abstractions ourselves. Well, while we can't avoid the understanding part, we can certainly be dispensed with the implementation one, since these abstractions are already implemented by functional libraries like [cats](https://github.com/typelevel/cats). You can find below the implementation of the tile assignment function using this library.",
 "Después de revisar la última implementación, quizá pienses que conseguir implementaciones declarativas es una tarea ardua: no solo necesitamos entender abstracciones de más alto nivel como las transformaciones de estado, los traverse, etc., sino también implementar nosotros mismos esas abstracciones. Bueno, aunque no podemos evitar la parte de entenderlas, sí que podemos librarnos de la de implementarlas, ya que esas abstracciones ya están implementadas por bibliotecas funcionales como [cats](https://github.com/typelevel/cats). A continuación puedes encontrar la implementación de la función de asignación de casillas usando esta biblioteca."),

("### The dynamics of the game", "### La dinámica del juego"),
("""In this section we deal with the creation and the evolution of the game state described previously. Conceptually, the following operations related to the game state can be identified:
* Creating the initial game state. We have to provide a dictionary and the correct word to be guessed.
* Providing a new guess. The player may attempt to guess the correct word, but if the game was already over or the word is not in the dictionary, an error should be returned; otherwise, a new game state will be returned together with the tile assignment of the input guess.""",
 """En esta sección tratamos la creación y la evolución del estado del juego descrito anteriormente. Conceptualmente, pueden identificarse las siguientes operaciones relacionadas con el estado del juego:
* Crear el estado inicial del juego. Tenemos que proporcionar un diccionario y la palabra correcta que hay que adivinar.
* Proporcionar un nuevo intento. El jugador puede intentar adivinar la palabra correcta, pero si la partida ya había terminado o la palabra no está en el diccionario, debe devolverse un error; en caso contrario, se devolverá un nuevo estado del juego junto con la asignación de casillas del intento de entrada."""),

("We can then simulate the game as follows:", "Entonces podemos simular la partida de la siguiente manera:"),

("### User interface", "### Interfaz de usuario"),
("The user interface module deals with the interaction between the player and the machine. In order to test the user interface we recommend executing the accompanying sbt project. In order to do so, you will first have to install the [`sbt` build tool](https://www.scala-sbt.org/), and then simply execute `sbt run` from the command line. Alternatively, you can also run the application through [VS Code or Intellij](https://docs.scala-lang.org/getting-started/index.html#open-hello-world-project).",
 "El módulo de interfaz de usuario se ocupa de la interacción entre el jugador y la máquina. Para probar la interfaz de usuario recomendamos ejecutar el proyecto sbt que la acompaña. Para ello, primero tendrás que instalar la [herramienta de compilación `sbt`](https://www.scala-sbt.org/), y luego simplemente ejecutar `sbt run` desde la línea de comandos. Alternativamente, también puedes ejecutar la aplicación a través de [VS Code o Intellij](https://docs.scala-lang.org/getting-started/index.html#open-hello-world-project)."),

("##### The dictionary", "##### El diccionario"),
("Before explaining the user interface itself, we have to add some functionality related to the dictionary. Namely, how to create the dictionary and how to extract a sample word randomly.",
 "Antes de explicar la interfaz de usuario en sí, tenemos que añadir algo de funcionalidad relacionada con el diccionario. En concreto, cómo crear el diccionario y cómo extraer una palabra de muestra al azar."),
("As you can see, we read the dictionary from a file located in the classpath of the project. Since the file name could be wrong we capture the potential `FileNotFound` exception with the [`Try`](https://www.scala-lang.org/api/current/scala/util/Try.html) utility (basically, `Try[T]` is isomorphic to `Either[Throwable, T]`).",
 "Como puedes ver, leemos el diccionario de un fichero situado en el classpath del proyecto. Como el nombre del fichero podría estar mal, capturamos la posible excepción `FileNotFound` con la utilidad [`Try`](https://www.scala-lang.org/api/current/scala/util/Try.html) (básicamente, `Try[T]` es isomorfo a `Either[Throwable, T]`)."),
("In order to extract a sample word randomly, we use the `scala.util.Random` object.",
 "Para extraer una palabra de muestra al azar, usamos el objeto `scala.util.Random`."),

("##### The user interface", "##### La interfaz de usuario"),
("The user interface is implemented by two tail-recursive functions, which make use of an auxiliary function to map the assignment into an ANSI-coloured string.",
 "La interfaz de usuario se implementa mediante dos funciones recursivas finales, que hacen uso de una función auxiliar para convertir la asignación en una cadena coloreada con ANSI."),

("##### The main function", "##### La función principal"),
("The main function simply creates the dictionary and launch the main function of the user interface.",
 "La función principal simplemente crea el diccionario y lanza la función principal de la interfaz de usuario."),

# --- comentarios ---
("// Empty constructor", "// Constructor vacío"),
("// String constructor", "// Constructor de cadena"),
("// Remove occurrences", "// Eliminar ocurrencias"),
("// Step 1", "// Paso 1"),
("// Step 2", "// Paso 2"),
("// Wordle state", "// Estado de Wordle"),
("// An instance", "// Una instancia"),
("// win observer", "// observador de victoria"),
("// Lose observer", "// Observador de derrota"),
("// game over observer", "// observador de fin de partida"),
("// Tile def.", "// def. de Tile"),
("// Assignment def.", "// def. de Assignment"),
("// start game", "// empezar partida"),
("// Attempt Error type", "// tipo AttemptError"),
("// attempt", "// intento"),
]
