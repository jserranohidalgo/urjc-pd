# -*- coding: utf-8 -*-
"""Traducción de PF-2/topic3/3.2 Products (y su template)."""

PAIRS = [
(
"""# Topic 3. Algebraic data types

## 3.2 Product types""",
"""# Tema 3. Tipos algebraicos de datos

## 3.2 Tipos producto"""),

(
"""Think of the following types of values:
* _Address_: an address is made of several values, namely the _names_ of the street and town, the _postal code_, the _number_, _floor_ and _door_ of the house, etc.
* _DNI_: the Spanish national identity card consists of its _number_, _expiration date_, _address_, _name_ of holder, etc.
* _Course_: A course may consists of its _name_, _description_, _outline_, etc.
* _Complex number_: a complex number is made of its real and imaginary real numbers.""",
"""Piensa en los siguientes tipos de valores:
* _Dirección_: una dirección está formada por varios valores, a saber, los _nombres_ de la calle y de la ciudad, el _código postal_, el _número_, el _piso_ y la _puerta_ de la vivienda, etc.
* _DNI_: el documento nacional de identidad consta de su _número_, su _fecha de caducidad_, la _dirección_, el _nombre_ del titular, etc.
* _Asignatura_: una asignatura puede constar de su _nombre_, su _descripción_, su _temario_, etc.
* _Número complejo_: un número complejo está formado por sus partes real e imaginaria, ambas números reales."""),

("In all of these cases, we define a complex type from a number of values of different types (primitive types, like strings or integers, or complex). So, we define an address given its street name, _and_ its town name, _and_ its postal code, etc. Types defined in this way, i.e. through the conjunction of other elements of information, are called _product_ types.",
 "En todos estos casos definimos un tipo complejo a partir de varios valores de tipos distintos (tipos primitivos, como las cadenas o los enteros, o tipos complejos). Así, definimos una dirección a partir del nombre de su calle, _y_ del nombre de su ciudad, _y_ de su código postal, etc. Los tipos definidos de este modo, es decir, mediante la conjunción de otros elementos de información, se llaman tipos _producto_."),

("### Constructors and destructors of product types",
 "### Constructores y destructores de los tipos producto"),

("More formally, given two types $T_1$ and $T_2$ we can create a new type by creating their _product_ $(T_1, T_2)$. A value of the product type $(T_1, T_2)$ is created from a value of type $T_1$ _and_ a value of type $T_2$. Given a value of the product type $(T_1, T_2)$, we can extract information using the selectors $\\_1$ and $\\_2$. The following table summarizes the constructors and destructors of products, alongside those for functions to facilitate comparison:",
 "Más formalmente: dados dos tipos $T_1$ y $T_2$, podemos crear un tipo nuevo formando su _producto_ $(T_1, T_2)$. Un valor del tipo producto $(T_1, T_2)$ se crea a partir de un valor de tipo $T_1$ _y_ un valor de tipo $T_2$. Y dado un valor del tipo producto $(T_1, T_2)$, podemos extraer información con los selectores $\\_1$ y $\\_2$. La tabla siguiente resume los constructores y destructores de los productos, junto a los de las funciones para facilitar la comparación:"),

("This table shows the constructors and destructors for products of two components, which in Scala are modeled by the [`Tuple2`](https://dotty.epfl.ch/api/scala/Tuple2.html) class. Note that the notation `(T1, T2)` is actually syntactic sugar for `Tuple2[T1, T2]`. For instance:",
 "Esta tabla muestra los constructores y destructores de los productos de dos componentes, que en Scala se modelan con la clase [`Tuple2`](https://dotty.epfl.ch/api/scala/Tuple2.html). Nótese que la notación `(T1, T2)` es en realidad azúcar sintáctico para `Tuple2[T1, T2]`. Por ejemplo:"),

("or without syntactic sugar as:", "o, sin azúcar sintáctico:"),

("What if we need to model a product of three components or more? Using products of two components should be enough, because one of the components may be a product itself. However, this is cumbersome, so Scala offers standard products of three, four, up to twenty two components. For instance, we may define the address type using a `Tuple4` class:",
 "¿Y si necesitamos modelar un producto de tres componentes o más? Con productos de dos componentes bastaría, porque una de las componentes puede ser a su vez un producto. Pero eso resulta incómodo, así que Scala ofrece productos estándar de tres, cuatro y hasta veintidós componentes. Por ejemplo, podemos definir el tipo de las direcciones con la clase `Tuple4`:"),

("We create values of type `Address` using the constructor `(..., ..., ..., ...)`:",
 "Creamos valores de tipo `Address` con el constructor `(..., ..., ..., ...)`:"),

("and extract information using the selectors `_1`, `_2`, etc.:",
 "y extraemos información con los selectores `_1`, `_2`, etc.:"),

(
"""#### Exercise
<div class="alert alert-info">
    Implement the <code>Address</code> type using only <code>Tuple2</code> products. Show an example of address construction and how you can access its different components.
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Implementa el tipo <code>Address</code> usando solo productos <code>Tuple2</code>. Muestra un ejemplo de construcción de una dirección y cómo acceder a sus distintas componentes.
</div>"""),

("##### Solution", "##### Solución"),
("##### Your solution", "##### Tu solución"),
("#### Your solution", "#### Tu solución"),

(
"""### Scala case classes

Product types allow us to extract information using general selectors `_1`, `_2`, etc., which are not very informative with regard to the particular kind of information that they represent. To solve this issue, we can resort to _record types_, which allow us to label each component of a record type. In Scala, records are modeled after `case classes`. For instance, using case classes we can define the type `Address` as follows:""",
"""### Las case classes de Scala

Los tipos producto nos permiten extraer información con selectores generales —`_1`, `_2`, etc.— que dicen poco sobre la clase concreta de información que representan. Para resolverlo podemos recurrir a los _tipos registro_, que permiten etiquetar cada componente. En Scala, los registros se modelan con `case classes`. Por ejemplo, con case classes podemos definir el tipo `Address` así:"""),

("This declaration of the `Address` record is essentially equivalent to the `Address` tuple from an informational point of view (the amount of information is the same). It changes, however, the way in which we can create and consume that piece of information:",
 "Esta declaración del registro `Address` es esencialmente equivalente a la tupla `Address` desde el punto de vista informativo (la cantidad de información es la misma). Lo que cambia es la manera de crear y de consumir esa información:"),

("Case classes are a lower level Scala mechanism which is used itself to define product. For instance, the `Tuple2` class is defined in a similar way to:",
 "Las case classes son un mecanismo de Scala de más bajo nivel, que se usa a su vez para definir los productos. Por ejemplo, la clase `Tuple2` se define de forma parecida a esta:"),

(
"""#### Exercise
<div class="alert alert-info">
    Define complex numbers using case classes. Create the complex number <code>i</code> (with real part 0.0 and imaginary one 1.0), and access its components.
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Define los números complejos con case classes. Crea el número complejo <code>i</code> (de parte real 0.0 e imaginaria 1.0) y accede a sus componentes.
</div>"""),

("### Why are products called _algebraic_?", "### ¿Por qué se llaman _algebraicos_ los productos?"),

("For instance, how many values are there of type $(Boolean, Boolean)$?",
 "Por ejemplo, ¿cuántos valores hay de tipo $(Boolean, Boolean)$?"),

("How about `(Boolean, Boolean, Boolean)`?", "¿Y de tipo `(Boolean, Boolean, Boolean)`?"),

("In general, the cardinal of $(A, B)$, for types $A$ and $B$ is: $|(A, B)| = |A| * |B|$. Indeed, since a product value is made of a number of components, we have as many product values as the number of choices we have for the first component, multiplied bythe number of choices we have for the second components, etc.",
 "En general, el cardinal de $(A, B)$, para tipos $A$ y $B$, es $|(A, B)| = |A| * |B|$. En efecto: como un valor producto está formado por varias componentes, hay tantos valores producto como opciones tenemos para la primera componente, multiplicadas por las opciones que tenemos para la segunda, etc."),

(
"""#### Exercise
<div class="alert alert-info">
    Assuming that the number of integer values is 2^32, and the following types <code>Type1</code> and <code>Type2</code>, which one has more values?
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Suponiendo que el número de valores enteros es 2^32, y dados los tipos <code>Type1</code> y <code>Type2</code> siguientes, ¿cuál de los dos tiene más valores?
</div>"""),

(
"""|Type1| = |Int| * |Boolean| = (2^32) * 2 = 2^33

|Type2| = |Int| ^ |Boolean| = (2^32) ^ 2 = 2^(32^2)

Type2 has more values.""",
"""|Type1| = |Int| * |Boolean| = (2^32) * 2 = 2^33

|Type2| = |Int| ^ |Boolean| = (2^32) ^ 2 = 2^(32^2)

Type2 tiene más valores."""),

("### The type `1`", "### El tipo `1`"),

(
"""If product types are analogous to number multiplication, then, is there any type which corresponds to the number 1, i.e. the neutral element of the multiplication? It has to be a type $1$ such that $(A, 1) \\cong A \\cong (1, A)$, where the sign $\\cong$ represents the _isomorphism_ of types, i.e. the types do not need to be equal but there should be a 1-1 mapping (a bijection) between the values of $A*1$ and $A$. We will talk later on isomorphisms in depth.

Now, what can we derived from the following equalities?
* $|(A, 1)| = |A|$
* $|(1, A)| = |A|$

Given that $|(A, B)| = |A|*|B|$, then $|A| * |1| = |A|$. So, $|1| = 1$, i.e. $1$ must be the type with just one value, i.e. the equivalent to the singleton set.""",
"""Si los tipos producto son análogos a la multiplicación de números, ¿hay algún tipo que corresponda al número 1, es decir, al elemento neutro de la multiplicación? Tendría que ser un tipo $1$ tal que $(A, 1) \\cong A \\cong (1, A)$, donde el signo $\\cong$ representa el _isomorfismo_ de tipos; es decir, los tipos no tienen que ser iguales, pero debe existir una correspondencia uno a uno (una biyección) entre los valores de $A*1$ y los de $A$. Más adelante hablaremos de los isomorfismos en detalle.

Ahora bien, ¿qué podemos deducir de estas igualdades?
* $|(A, 1)| = |A|$
* $|(1, A)| = |A|$

Dado que $|(A, B)| = |A|*|B|$, tenemos que $|A| * |1| = |A|$. Por tanto $|1| = 1$: el tipo $1$ ha de ser el tipo que tiene un único valor, el equivalente al conjunto unitario."""),

("This type already exists in the Scala standard library: it's called `Unit`, and its only value is `()`:",
 "Ese tipo ya existe en la biblioteca estándar de Scala: se llama `Unit`, y su único valor es `()`:"),

("Which information can be extracted from a value of type `Unit`? The answer is none. So, for this type of algebraic data type there is a single constructor and no destructors:",
 "¿Qué información puede extraerse de un valor de tipo `Unit`? Ninguna. Así que este tipo algebraico de datos tiene un único constructor y ningún destructor:"),

(
"""How many values are there of type $(Boolean, Unit)$? We can enumerate all possible values, but we can anticipate the result by simple calculation:

$|(Boolean, Unit)| = |Boolean|*|Unit| = 2 * 1 = 2$""",
"""¿Cuántos valores hay de tipo $(Boolean, Unit)$? Podemos enumerarlos todos, pero podemos anticipar el resultado con un simple cálculo:

$|(Boolean, Unit)| = |Boolean|*|Unit| = 2 * 1 = 2$"""),

("Indeed, these are the two values:", "Y en efecto, estos son los dos valores:"),

(
"""#### Exercise
<div class="alert alert-info">
    Given a type <code>A</code>, how many functions are there of type <code>A => Unit</code> and <code>Unit => A</code>. Implement their values when <code>A</code> is the boolean type.
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Dado un tipo <code>A</code>, ¿cuántas funciones hay de tipo <code>A => Unit</code> y cuántas de tipo <code>Unit => A</code>? Implementa sus valores para el caso en que <code>A</code> sea el tipo booleano.
</div>"""),

(
"""$|A => Unit| = |Unit|^{|A|} = 1^{|A|} = 1$

$|Unit => A| = |A|^|Unit| = |A|^1 = |A| $""",
"""$|A => Unit| = |Unit|^{|A|} = 1^{|A|} = 1$

$|Unit => A| = |A|^|Unit| = |A|^1 = |A| $"""),

("So, these functions are equivalent to `Unit` and `A`, respectively. But then, which is the purpose of writing functions which these signatures? For the first case, a function like the following one:",
 "Así que estas funciones son equivalentes a `Unit` y a `A`, respectivamente. Pero entonces, ¿para qué escribir funciones con estas signaturas? En el primer caso, una función como la siguiente:"),

("is only meaningful because of the possible _side effects_ implemented by its body, i.e. only if it's an impure function. Because, from a functional point of view, what this function can return is already known: the only possible value `()`. `Unit` is the Scala equivalent to Java's `void`.",
 "solo tiene sentido por los posibles _efectos laterales_ que implemente su cuerpo; es decir, solo si es una función impura. Porque, desde un punto de vista funcional, lo que esa función puede devolver ya se sabe: el único valor posible, `()`. `Unit` es el equivalente en Scala al `void` de Java."),

("Concerning functions of the following type:", "En cuanto a las funciones del tipo siguiente:"),

("Why shouldn't we define `foo` just a value of type `Boolean`? Because, basically, a value of that function type hides a boolean expression, that will be evaluated only when the function is consumed. This expression is also called a _thunk_. If evaluating the expression is computationally expensive and there are chances that the program does not actually need it, then it might be beneficial to use a thunk. This is also related to the so-called _lazy evaluation_ implemented by languages such as Haskell, by default. In scala, we can also defer the evaluation of some expression using the keyword `lazy`:",
 "¿Por qué no definir `foo` simplemente como un valor de tipo `Boolean`? Porque, en esencia, un valor de ese tipo función esconde una expresión booleana que se evaluará solo cuando la función se consuma. A esa expresión se la llama también _thunk_. Si evaluarla es computacionalmente costoso y hay posibilidades de que el programa no llegue a necesitarla, usar un thunk puede resultar beneficioso. Esto tiene que ver además con la llamada _evaluación perezosa_ (_lazy evaluation_) que lenguajes como Haskell implementan por defecto. En Scala también podemos diferir la evaluación de una expresión con la palabra clave `lazy`:"),

("It's only when we access the variables that the right-hand side of the variable assignment is evaluated:",
 "El lado derecho de la asignación no se evalúa hasta que accedemos a las variables:"),

# ------------------------------------------------------------------ comentarios
("// write you solution here", "// escribe aquí tu solución"),
("// names of fields are optional, though", "// los nombres de los campos son opcionales, eso sí"),
("// Instead of _1, _2, ...", "// En lugar de _1, _2, ..."),
("// Number of values of Boolean type: 2", "// Número de valores del tipo Boolean: 2"),
("// Number of values of (Boolean, Boolean) type: 2 * 2", "// Número de valores del tipo (Boolean, Boolean): 2 * 2"),
("// Number of values of (Boolean, Boolean, Boolean) type: 2 * 2 * 2",
 "// Número de valores del tipo (Boolean, Boolean, Boolean): 2 * 2 * 2"),
("// type Complex", "// tipo Complex"),
("// type Complex with Tuple2", "// tipo Complex con Tuple2"),
("// type Address", "// tipo Address"),
("// creating address values", "// creando valores de dirección"),
("// Accessing address components", "// Accediendo a las componentes de la dirección"),
("// Address with case class", "// Address con una case class"),
("// Creating addresses", "// Creando direcciones"),
("// Accessing components", "// Accediendo a las componentes"),
("// Tuple definitions", "// Definiciones de tuplas"),
("// The unit value", "// El valor unit"),
("// values of type (Boolean, Unit)", "// valores de tipo (Boolean, Unit)"),
("// Function Boolean => Unit", "// Función Boolean => Unit"),
("// Function Unit => Boolean", "// Función Unit => Boolean"),
("// lazy values", "// valores lazy"),
("// Access variables", "// Acceder a las variables"),
]
