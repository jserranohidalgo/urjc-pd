# -*- coding: utf-8 -*-
"""Traducción de PF-2/topic3/3.4 Isomorphisms (+template) y sus ejercicios."""

PAIRS = [
(
"""# Topic 3. Algebraic data types

## 3.4 Isomorphisms""",
"""# Tema 3. Tipos algebraicos de datos

## 3.4 Isomorfismos"""),

("Intuitively, we say that two types $A$ and $B$ are isomorphic, $A \\cong B$,  if they represent the same information. More specifically, if we regard types as _sets of values_, then we can say that two types are isomorphic if their values can be put in a one-to-one correspondence, i.e. if we can establish a _bijection_ between their corresponding sets of values.",
 "Intuitivamente, decimos que dos tipos $A$ y $B$ son isomorfos, $A \\cong B$, si representan la misma información. Más concretamente: si vemos los tipos como _conjuntos de valores_, podemos decir que dos tipos son isomorfos si sus valores pueden ponerse en correspondencia uno a uno, es decir, si podemos establecer una _biyección_ entre sus conjuntos de valores."),

("Thus, to establish an isomorphism betwween two types $A$ and $B$, we have to implement two functions $from$ and $to$, and prove that these functions are mutual inverses. These requirements can be implemented through the following _template_:",
 "Así, para establecer un isomorfismo entre dos tipos $A$ y $B$ hay que implementar dos funciones, $from$ y $to$, y demostrar que son inversas la una de la otra. Estos requisitos pueden plasmarse en la siguiente _plantilla_:"),

("> ![image.png](../../images/scala3api3.jpg) Technically, the `Isomorphism` trait is an example of [type class](https://docs.scala-lang.org/scala3/book/ca-type-classes.html), a functional design pattern and technique which is beyond the scope of this course.",
 "> ![image.png](../../images/scala3api3.jpg) Técnicamente, el trait `Isomorphism` es un ejemplo de [type class](https://docs.scala-lang.org/scala3/book/ca-type-classes.html), un patrón y una técnica de diseño funcional que quedan fuera del alcance de este curso."),

("For instance, the isomorphism $Boolean * 1 \\cong Boolean$ is witnessed by the following functions:",
 "Por ejemplo, el isomorfismo $Boolean * 1 \\cong Boolean$ lo atestiguan las funciones siguientes:"),

(
"""which satisfy:
- `from(to(b))=b`, for all `b: (Boolean, Unit)`, and
- `to(from(b))=b` for all `b: Boolean`.""",
"""que cumplen:
- `from(to(b))=b`, para todo `b: (Boolean, Unit)`, y
- `to(from(b))=b`, para todo `b: Boolean`."""),

("In order to make these tests, we will employ the unit testing framework `scalatest`:",
 "Para hacer estas pruebas usaremos el framework de pruebas unitarias `scalatest`:"),

("together with the following testing class:", "junto con la siguiente clase de pruebas:"),
("Indeed:", "En efecto:"),

("## High-school algebra equalities", "## Las igualdades del álgebra de bachillerato"),

("The correspondence between algebraic data types and arithmetic goes is striking, since the familiar laws of hight-school algebra holds for ADTs as well:",
 "La correspondencia entre los tipos algebraicos de datos y la aritmética es asombrosa: las conocidas leyes del álgebra de bachillerato valen también para los ADTs:"),

("In correspondence with these equalities, we can establish the following isomorphisms:",
 "En correspondencia con esas igualdades, podemos establecer los siguientes isomorfismos:"),

("## Type-driven development", "## Desarrollo dirigido por tipos"),

("In order to prove isomorphisms, we will benefit from paying careful attention to the table of constructors and destructors of ADTs.",
 "Para demostrar isomorfismos nos conviene prestar mucha atención a la tabla de constructores y destructores de los ADTs."),

("Essentially, these constructors and destructors tell us how we can create values of a given algebraic data type, and which information we can extract from them. The signatures of the `from` and `to` functions of some isomorphism tell us which data types we have to create (the output of the functions) and which information is available to create those results (the input value). Besides the constructors and destructors of the different ADTs, we also add to this table a new trivial rule (_var_), which allows us to observe a value of type $A$ if a variable of that type is already available.",
 "En esencia, esos constructores y destructores nos dicen cómo crear valores de un tipo algebraico de datos y qué información podemos extraer de ellos. Las signaturas de las funciones `from` y `to` de un isomorfismo nos dicen qué tipos de datos hay que crear (la salida de las funciones) y de qué información disponemos para crear esos resultados (el valor de entrada). Además de los constructores y destructores de los distintos ADTs, añadimos a la tabla una regla trivial nueva (_var_), que permite observar un valor de tipo $A$ si ya disponemos de una variable de ese tipo."),

(
"""The implementation of the `from` and `to` functions of an isomorphism will be guided by a _type-driven development_ method:
* The method starts with an empty implementation consisting only of a _hole_ whose type is the function's result. Holes are represented by the Scala expression `??? : A`, with `A` being the type of the hole.
* The method is structured in a number of steps, and proceeds by successively refining the program _holes_. A hole is refined by applying a constructor or destructor from the table. Refining a hole may create new holes. In any case, the code resulting from each step should compile without any issues.
* If the hole's type is a function, product or sum type, then we can apply the corresponding constructor. The application of a constructor invariable involves creating new holes (except in the case of the `Unit` constructor).
* If the hole is `Nothing` or a variable `A`, we have to apply a destructor that allows us to infer that type of value. Here, we will pay special attention to all the variables that are available in the hole's scope to be refined. The only destructor that may create new holes is function application.
* At any given time, we may find several candidate holes and several constructors or destructors available to proceed. In the case of constructors, this may only occur for the _sum_ type: in that case, we may choose between the `Left` and `Right` constructors.
* The method may end successfully, meaning there are no holes left unimplemented. Otherwise, the implementation may end unsuccessfully, meaning the signature can't be implemented, i.e. there are no functions of that type. This may happen because we exhausted all the alternatives to refine a given hole. Alternatively, this may also happen because we entered into a loop, applying again and again the same constructors and destructors without making any real progress toward the solution.
* In applying the method, it's essential to ascribe types to each hole and annotate the available variables with their corresponding types. Remember, types guide the development process. However, once we are done, we can benefit from cleaning up the resulting implementation.""",
"""La implementación de las funciones `from` y `to` de un isomorfismo se guiará por un método de _desarrollo dirigido por tipos_:
* El método parte de una implementación vacía que consiste únicamente en un _hueco_ cuyo tipo es el resultado de la función. Los huecos se representan con la expresión de Scala `??? : A`, siendo `A` el tipo del hueco.
* El método se estructura en una serie de pasos y avanza refinando sucesivamente los _huecos_ del programa. Un hueco se refina aplicando un constructor o un destructor de la tabla. Refinar un hueco puede crear huecos nuevos. En cualquier caso, el código resultante de cada paso debe compilar sin problemas.
* Si el tipo del hueco es un tipo función, producto o suma, podemos aplicar el constructor correspondiente. La aplicación de un constructor implica invariablemente crear huecos nuevos (salvo en el caso del constructor de `Unit`).
* Si el hueco es de tipo `Nothing` o de una variable de tipo `A`, hay que aplicar un destructor que nos permita inferir un valor de ese tipo. Aquí prestaremos especial atención a todas las variables disponibles en el ámbito del hueco que se va a refinar. El único destructor que puede crear huecos nuevos es la aplicación de funciones.
* En un momento dado podemos encontrarnos con varios huecos candidatos y varios constructores o destructores aplicables. En el caso de los constructores, esto solo puede ocurrir con el tipo _suma_: en ese caso podemos elegir entre los constructores `Left` y `Right`.
* El método puede terminar con éxito, lo que significa que no queda ningún hueco sin implementar. Pero la implementación también puede terminar sin éxito, lo que significa que la signatura no se puede implementar; es decir, que no hay funciones de ese tipo. Esto puede ocurrir porque hayamos agotado todas las alternativas para refinar un hueco, o bien porque hayamos entrado en un bucle, aplicando una y otra vez los mismos constructores y destructores sin avanzar realmente hacia la solución.
* Al aplicar el método es esencial ascribir tipos a cada hueco y anotar las variables disponibles con sus tipos correspondientes. Recuerda: los tipos guían el proceso de desarrollo. Eso sí, una vez terminado, conviene limpiar la implementación resultante."""),

(
"""Before delving into the implementation of this isomorphism, note that it holds since the number of values of both types is the same. The following calculation demonstrates it:

$|Either[X, Y] => Z| = \\\\
\\,\\,|Z|^{Either[X, Y]} = \\\\
\\,\\,|Z|^{|X|+|Y|} = \\\\
\\,\\,|Z|^{|X|}*|Z|^{|Y|} = \\\\
\\,\\,|X => Z|*|Y => Z| = \\\\
\\,\\,|(X => Z, Y => Z)|$""",
"""Antes de meternos con la implementación de este isomorfismo, nótese que se cumple porque el número de valores de ambos tipos es el mismo. El cálculo siguiente lo demuestra:

$|Either[X, Y] => Z| = \\\\
\\,\\,|Z|^{Either[X, Y]} = \\\\
\\,\\,|Z|^{|X|+|Y|} = \\\\
\\,\\,|Z|^{|X|}*|Z|^{|Y|} = \\\\
\\,\\,|X => Z|*|Y => Z| = \\\\
\\,\\,|(X => Z, Y => Z)|$"""),

("Let's illustrate the type-driven development method with the implementation of the isomorphism:",
 "Ilustremos el método de desarrollo dirigido por tipos implementando el isomorfismo:"),

("#### from", "#### from"),
("#### to", "#### to"),

("Let's start with the `from` function and create an implementation consisting of a single hole of the result type:",
 "Empecemos por la función `from`, creando una implementación que consista en un único hueco del tipo del resultado:"),

("Since the type's hole is a product type, we can advance to the next step by applying the corresponding constructor.",
 "Como el tipo del hueco es un tipo producto, podemos avanzar al paso siguiente aplicando el constructor correspondiente."),

("By applying the product constructor, two additional holes are created of function type. We proceed by implementing the scheme of the corresponding lambda expressions.",
 "Al aplicar el constructor del producto se crean dos huecos nuevos, de tipo función. Continuamos implementando el esquema de las expresiones lambda correspondientes."),

("Now, the holes are of type `Z`, an arbitrary type parameter for which we have no constructor. Hence, our only chance to get an expression of this type is by extracting information from the available variables in the scope of the different holes. In the case of the first hole, the available variables are `a` and `x`; in the second hole, available variables are `y` and `a`. The only way to obtain a value of type `Z` is by applying function `a`. We don't know yet how to obtain the input argument for this function, but we proceed nonetheless.",
 "Ahora los huecos son de tipo `Z`, un parámetro de tipo arbitrario para el que no tenemos constructor. Así que nuestra única opción de conseguir una expresión de ese tipo es extraer información de las variables disponibles en el ámbito de cada hueco. En el primero, las variables disponibles son `a` y `x`; en el segundo, `y` y `a`. La única manera de obtener un valor de tipo `Z` es aplicar la función `a`. Todavía no sabemos cómo obtener el argumento de entrada de esa función, pero seguimos adelante."),

("Function application reveals a new hole of sum type. Here we can apply the constructors of sums, `Left` and `Right`, but which of them? Given the information available for each hole, it's wise to choose `Left` for the first hole, and `Right` for the second one.",
 "La aplicación de la función deja al descubierto un hueco nuevo, de tipo suma. Aquí podemos aplicar los constructores de las sumas, `Left` y `Right`, pero ¿cuál de los dos? Dada la información disponible en cada hueco, lo sensato es elegir `Left` para el primero y `Right` para el segundo."),

("Last, the new holes created through the sum constructors are of types `X` and `Y`, respectively. But these are easy to refine because in their program scope we find variables of exactly those types (we thus apply the _var_ observer).",
 "Por último, los huecos nuevos que han creado los constructores de la suma son de tipos `X` e `Y`, respectivamente. Y son fáciles de refinar, porque en su ámbito encontramos variables exactamente de esos tipos (aplicamos, pues, el observador _var_)."),

("As a final step, we can simplify the implementation by removing all the type annotations and ascriptions that guided the development process.",
 "Como último paso podemos simplificar la implementación quitando todas las anotaciones y ascripciones de tipo que guiaron el desarrollo."),

("Of course, an experienced programmer may have reached this program without such a systematic method, simply by carefully inspecting the available input and the desired output.",
 "Por supuesto, un programador con experiencia podría haber llegado a este programa sin un método tan sistemático, simplemente examinando con cuidado la entrada disponible y la salida deseada."),

("Let's try implementing the `to` function. As always, we start by creating a single hole whose type must be the output type.",
 "Intentemos ahora implementar la función `to`. Como siempre, empezamos creando un único hueco cuyo tipo ha de ser el de la salida."),

("This step is easy, since the only way to refine this hole is by implementing the corresponding lambda expression.",
 "Este paso es fácil, porque la única forma de refinar el hueco es implementar la expresión lambda correspondiente."),

("The hole is of type `Z`, a type parameter, so we have to extract information from the available variables in order to write an expression of this type: variable `a: (X => Z, Y => Z)` and `e: Either[X, Y]`. There are a number of alternatives here: we may extract the first component of the tuple, we may extract its second component or we may apply pattern matching. Clearly, we can only obtain a value of type `Z` through the functions `X => Z` or `Y => Z`. And we will only be able to extract `Z` from these functions if we find an `X` or `Y`. Now, the only way to find one of these values is through variable `e`, though we don't know which value this variable holds. So, we apply pattern matching.",
 "El hueco es de tipo `Z`, un parámetro de tipo, así que hay que extraer información de las variables disponibles para poder escribir una expresión de ese tipo: la variable `a: (X => Z, Y => Z)` y `e: Either[X, Y]`. Hay varias alternativas: podemos extraer la primera componente de la tupla, la segunda, o aplicar pattern matching. Está claro que solo podemos obtener un valor de tipo `Z` a través de las funciones `X => Z` o `Y => Z`. Y solo podremos extraer una `Z` de ellas si encontramos una `X` o una `Y`. Ahora bien, la única manera de encontrar uno de esos valores es a través de la variable `e`, aunque no sabemos cuál de los dos contiene. Así que aplicamos pattern matching."),

("Now we have two holes instead of one, but the situation has improved since we have more information for each of them: for the first one, we have an `x: X` available, and for the second one a `y: Y`. So, in order to proceed towards our goal of refining the `Z` holes, we choose for the first one to extract the first component of the tuple `a`, and for the second hole the second component.",
 "Ahora tenemos dos huecos en lugar de uno, pero la situación ha mejorado, porque disponemos de más información en cada uno: en el primero tenemos una `x: X`, y en el segundo una `y: Y`. Así que, para avanzar hacia nuestro objetivo de refinar los huecos de tipo `Z`, en el primero extraemos la primera componente de la tupla `a`, y en el segundo la segunda."),

("Once we have direct access to the functions that allow us to obtain `Z` values, we apply them.",
 "Una vez que tenemos acceso directo a las funciones que nos permiten obtener valores de tipo `Z`, las aplicamos."),

("Finally, variables of the required types are available within the program's scope.",
 "Y por fin hay en el ámbito del programa variables de los tipos que necesitamos."),

("After cleaning-up the resulting function we obtain the following implementation.",
 "Tras limpiar la función resultante obtenemos esta implementación."),

("In conclusion, the implementation of the isomorphism is the following:",
 "En conclusión, la implementación del isomorfismo es la siguiente:"),

("#### Testing", "#### Pruebas"),

(
"""But we must also show, or at least _test_, that both functions are mutual inverses, i.e. that:

`from(to(f)) == f`, for all `f: (Y => X, Z => X)`

`to(from(f)) == f`, for all `f: Either[Y, Z] => X`""",
"""Pero además hay que demostrar, o al menos _probar_, que ambas funciones son inversas la una de la otra; es decir, que:

`from(to(f)) == f`, para toda `f: (Y => X, Z => X)`

`to(from(f)) == f`, para toda `f: Either[Y, Z] => X`"""),

("In particular, testing will be carried out fixing types $X$, $Y$ and $Z$ to $Boolean$, and employing two functions `ex1` and `ex2`:",
 "Las pruebas se harán fijando los tipos $X$, $Y$ y $Z$ a $Boolean$, y usando dos funciones, `ex1` y `ex2`:"),

("However, the following test fails:", "Sin embargo, la siguiente prueba falla:"),

("This is because the default equality operator for functions in Scala does not work. For instance, the following functions are the same:",
 "Y es porque el operador de igualdad que Scala usa por defecto con las funciones no sirve. Por ejemplo, las funciones siguientes son la misma:"),

("but the following fails because they are two different objects:",
 "pero lo siguiente falla, porque son dos objetos distintos:"),

("In these cases we can only aim at testing the equality of both functions for particular input values:",
 "En estos casos lo único que podemos pretender es probar la igualdad de ambas funciones para valores de entrada concretos:"),

("So, when the potential isomorphic types involve function types, the  `equalA` and `equalB` operators of the `Isomorphic` trait must be redefined. For instance:",
 "Así que, cuando los tipos que queremos ver isomorfos involucran tipos función, hay que redefinir los operadores `equalA` y `equalB` del trait `Isomorphic`. Por ejemplo:"),

("Now, we can perform our test successfully:", "Ahora sí podemos ejecutar la prueba con éxito:"),

(
"""We should be able to implement this isormorphism, since the number of possible values of both types are the same:

$|X \\Rightarrow Unit| = \\\\
\\,\\,|Unit|^{|X|} = \\\\
\\,\\,1^{|X|} = \\\\
\\,\\,1 = \\\\
\\,\\,|Unit| $""",
"""Deberíamos poder implementar este isomorfismo, porque el número de valores posibles de ambos tipos es el mismo:

$|X \\Rightarrow Unit| = \\\\
\\,\\,|Unit|^{|X|} = \\\\
\\,\\,1^{|X|} = \\\\
\\,\\,1 = \\\\
\\,\\,|Unit| $"""),

("The step-by-step development follows:", "El desarrollo paso a paso es este:"),
("We will perform testing for $X=Boolean$:", "Haremos las pruebas para $X=Boolean$:"),

(
"""#### Exercise
<div class="alert alert-info">
    Show that types <code>Nothing => X</code> and <code>Unit</code> have the same cardinality, and implement the corresponding isomorphism.
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Demuestra que los tipos <code>Nothing => X</code> y <code>Unit</code> tienen el mismo cardinal, e implementa el isomorfismo correspondiente.
</div>"""),

("##### Solution", "##### Solución"),
("##### Your solution", "##### Tu solución"),
("#### Solution", "#### Solución"),
("#### Your solution", "#### Tu solución"),

("For any type $X$: $|Nothing => X| = |X|^{|Nothing|} = |X|^0 = 1 = |Unit|$.",
 "Para todo tipo $X$: $|Nothing => X| = |X|^{|Nothing|} = |X|^0 = 1 = |Unit|$."),

("The step-by-step development for each function follows:",
 "El desarrollo paso a paso de cada función es este:"),

("Testing will be performed for $X = Boolean$:", "Las pruebas se harán para $X = Boolean$:"),

# ---------------------------------------------------------------- 3.4 Exercises
("### Preamble", "### Preámbulo"),
("# Topic 3. Algebraic data types", "# Tema 3. Tipos algebraicos de datos"),
("## 3.4 Isomorphisms", "## 3.4 Isomorfismos"),
("## Exercise 1", "## Ejercicio 1"),
("## Exercise 2", "## Ejercicio 2"),
("## Exercise 3", "## Ejercicio 3"),
("## Exercise 4", "## Ejercicio 4"),
("## Exercise 5", "## Ejercicio 5"),
("## Exercise 6", "## Ejercicio 6"),
("### Part a)", "### Apartado a)"),
("### Part b)", "### Apartado b)"),

("Prove that the isomorphism $Either[Unit, Unit] \\cong Boolean$ holds by implementing the following bijections:",
 "Demuestra que se cumple el isomorfismo $Either[Unit, Unit] \\cong Boolean$ implementando las biyecciones siguientes:"),

("Check that they are indeed mutual inverses, i.e. that for all $a: Boolean$, `toBoolean(fromBoolean(a))==a`, and that for all $a: Either[Unit, Unit]$, `fromBoolean(toBoolean(a))==a`.",
 "Comprueba que en efecto son inversas la una de la otra; es decir, que para todo $a: Boolean$, `toBoolean(fromBoolean(a))==a`, y que para todo $a: Either[Unit, Unit]$, `fromBoolean(toBoolean(a))==a`."),

("Show that we can redefine `Option[A]` using `Either[A,Unit]` by implementing the following isomorphism:",
 "Demuestra que podemos redefinir `Option[A]` con `Either[A,Unit]` implementando el isomorfismo siguiente:"),

("Check that these functions are mutual inverses. For that, fix $A$ to particular types (e.g. `Boolean`, `Int`, etc.), and test the equivalences `from(to(e)) == e` and `to(from(o)) == o` for some values $o$ and $e$.",
 "Comprueba que esas funciones son inversas la una de la otra. Para ello, fija $A$ a tipos concretos (`Boolean`, `Int`, etc.) y prueba las equivalencias `from(to(e)) == e` y `to(from(o)) == o` para algunos valores $o$ y $e$."),

("How many functions are there of type `Either[Unit, Either[Unit, Unit]] => Boolean`? Identify all of them as alternative implementations of the following signature:",
 "¿Cuántas funciones hay de tipo `Either[Unit, Either[Unit, Unit]] => Boolean`? Identifícalas todas como implementaciones alternativas de la signatura siguiente:"),

("Idem, as alternative lambda expressions:", "Ídem, como expresiones lambda alternativas:"),
("With lambda expressions:", "Con expresiones lambda:"),
("etc.", "etc."),

("How many different implementations are there of the following function? Recall that two implementations will be considered different if the corresponding mathematical functions are different.",
 "¿Cuántas implementaciones distintas hay de la función siguiente? Recuerda que dos implementaciones se consideran distintas si las funciones matemáticas correspondientes son distintas."),

("Show that the following isomorphism holds for exponent types: $X => (Y => Z) \\cong ((Y, X)) => Z$, for all types $X$, $Y$ and $Z$.",
 "Demuestra que se cumple el siguiente isomorfismo entre tipos exponenciales: $X => (Y => Z) \\cong ((Y, X)) => Z$, para todos los tipos $X$, $Y$ y $Z$."),

("Implement function equality for the corresponding signatures and check that both functions, `curry` and `uncurry`, are inverses of each other for two sample functions $ex1$ and $ex2$:",
 "Implementa la igualdad de funciones para las signaturas correspondientes y comprueba que ambas funciones, `curry` y `uncurry`, son inversas la una de la otra para dos funciones de ejemplo, $ex1$ y $ex2$:"),

("Shows that the following law holds for exponent types: $X => (Y, Z) \\cong (X => Y, X => Z)$, for all types $X$, $Y$ and $Z$.",
 "Demuestra que se cumple la siguiente ley para los tipos exponenciales: $X => (Y, Z) \\cong (X => Y, X => Z)$, para todos los tipos $X$, $Y$ y $Z$."),

("Fix $X$, $Y$ and $Z$ to particular types, implement equality for the corresponding signatures and check that both functions, `from` and `to`, are inverses of each other given two sample functions of your choice.",
 "Fija $X$, $Y$ y $Z$ a tipos concretos, implementa la igualdad para las signaturas correspondientes y comprueba que ambas funciones, `from` y `to`, son inversas la una de la otra, dadas dos funciones de ejemplo que elijas."),

("Shows that the following isomorphisms holds for algebraic data types:",
 "Demuestra que se cumplen los siguientes isomorfismos entre tipos algebraicos de datos:"),

# ------------------------------------------------------------------ comentarios
("// equality", "// igualdad"),
("// Bijection laws", "// Leyes de la biyección"),
("// STEP 1: INIT", "// PASO 1: INICIO"),
("// Hole 1: (X => Z, Y => Z)", "// Hueco 1: (X => Z, Y => Z)"),
("// STEP 2: CONSTRUCTOR (PRODUCT)", "// PASO 2: CONSTRUCTOR (PRODUCTO)"),
("// Hole 1: X => Z", "// Hueco 1: X => Z"),
("// Hole 2: Y => Z", "// Hueco 2: Y => Z"),
("// STEP 3: CONSTRUCTOR (FUNCTION)", "// PASO 3: CONSTRUCTOR (FUNCIÓN)"),
("// Hole 1: Z", "// Hueco 1: Z"),
("// Hole 2: Z", "// Hueco 2: Z"),
("// Available variables: a, x", "// Variables disponibles: a, x"),
("// Available variables: a, y", "// Variables disponibles: a, y"),
("// STEP 4: DESTRUCTOR (FUNCTION)", "// PASO 4: DESTRUCTOR (FUNCIÓN)"),
("// Hole 1: Either[X, Y]", "// Hueco 1: Either[X, Y]"),
("// Hole 2: Either[X, Y]", "// Hueco 2: Either[X, Y]"),
("// STEP 5: CONSTRUCTOR (SUM)", "// PASO 5: CONSTRUCTOR (SUMA)"),
("// Hole 1: X", "// Hueco 1: X"),
("// Hole 2: Y", "// Hueco 2: Y"),
("// STEP 6: DESTRUCTOR (VAR)", "// PASO 6: DESTRUCTOR (VAR)"),
("// STEP 7: CLEAN-UP", "// PASO 7: LIMPIEZA"),
("// Hole 1: Either[X, Y] => Z", "// Hueco 1: Either[X, Y] => Z"),
("// Available variables: a, e", "// Variables disponibles: a, e"),
("// STEP 3: DESTRUCTOR (SUM)", "// PASO 3: DESTRUCTOR (SUMA)"),
("// Available variables: a, e, x", "// Variables disponibles: a, e, x"),
("// Available variables: a, e, y", "// Variables disponibles: a, e, y"),
("// STEP 4: DESTRUCTOR (PRODUCT)", "// PASO 4: DESTRUCTOR (PRODUCTO)"),
("// STEP 5: DESTRUCTOR (FUNCTION)", "// PASO 5: DESTRUCTOR (FUNCIÓN)"),
("// Hole 1: x", "// Hueco 1: x"),
("// Hole 2: y", "// Hueco 2: y"),
("// Available variables: a, e, x, f", "// Variables disponibles: a, e, x, f"),
("// Available variables: a, e, y, f", "// Variables disponibles: a, e, y, f"),
("// etc.", "// etc."),
("// STEP 2: CONSTRUCTOR (1)", "// PASO 2: CONSTRUCTOR (1)"),
("// STEP 3: CONSTRUCTOR (1)", "// PASO 3: CONSTRUCTOR (1)"),
("// true would suffice here", "// aquí bastaría con true"),
("// STEP 3: DESTRUCTOR (0)", "// PASO 3: DESTRUCTOR (0)"),
("// Isomorphic trait", "// el trait Isomorphic"),
("// class TestIso[A, B](iso: Isomorphic[A, B])(a: A*)(b: B*)  extends AnyFlatSpec with should.Matchers:",
 "// class TestIso[A, B](iso: Isomorphic[A, B])(a: A*)(b: B*)  extends AnyFlatSpec with should.Matchers:"),
("// run test", "// ejecutar la prueba"),
("// template of Isormophic for the particular types", "// plantilla de Isomorphic para los tipos concretos"),
("// two functions", "// dos funciones"),
("// two simple functions", "// dos funciones sencillas"),
("// test equality", "// probar la igualdad"),
("// Test equality for particular inputs", "// Probar la igualdad para entradas concretas"),
("// Iso", "// Iso"),
("// ...", "// ..."),
("// uncurry", "// uncurry"),
("// curry", "// curry"),
("// extends trait Isomorphic", "// extiende el trait Isomorphic"),
]
