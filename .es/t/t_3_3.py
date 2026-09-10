# -*- coding: utf-8 -*-
"""Traducción de PF-2/topic3/3.3 Sums (y su template)."""

PAIRS = [
(
"""# Topic 3. Algebraic data types

## 3.3 Sum types""",
"""# Tema 3. Tipos algebraicos de datos

## 3.3 Tipos suma"""),

(
"""Let's consider the following types:
* `WeekDay`: all days of the week, excluding Saturday and Sunday, i.e. _Monday_, _Tuesday_, etc., until _Friday_.
* `Shape`: a geometric shape may be a _circle_, a _rectangle_ or an _ellipse_.
* `HttpCommand`: An http command may consists of a _Get_, _Post_, _Delete_ or _Put_ request.
* `Number`: a number may be a _natural_ number, _integer_, _fractional_, _real_, or _complex_ number.""",
"""Consideremos los siguientes tipos:
* `WeekDay`: los días de la semana, excluidos el sábado y el domingo; es decir, _lunes_, _martes_, etc., hasta el _viernes_.
* `Shape`: una figura geométrica puede ser un _círculo_, un _rectángulo_ o una _elipse_.
* `HttpCommand`: un comando http puede consistir en una petición _Get_, _Post_, _Delete_ o _Put_.
* `Number`: un número puede ser _natural_, _entero_, _fraccionario_, _real_ o _complejo_."""),

("In all these cases, a value of the corresponding type consists of a value of one of a number of types. For instance, a value of type `HttpCommand` may be a value of type `Get`, `Post`, `Delete` __or__ `Put`. Similarly, a `Number` may be a `Natural`, `Integer`, `Rational`, `Real`  or `Complex` numbers. These types are called _sum_ types. They contrast with the case of product types, which are constructed using a value for _each_ of its component types. For instance, a complex number is constructed with the _real_ __and__ the _imaginary_ parts.",
 "En todos estos casos, un valor del tipo correspondiente consiste en un valor de uno de entre varios tipos. Por ejemplo, un valor de tipo `HttpCommand` puede ser un valor de tipo `Get`, `Post`, `Delete` __o__ `Put`. Igualmente, un `Number` puede ser un número `Natural`, `Integer`, `Rational`, `Real` o `Complex`. Estos tipos se llaman tipos _suma_, y contrastan con los tipos producto, que se construyen usando un valor para _cada_ uno de sus tipos componentes. Un número complejo, por ejemplo, se construye con la parte _real_ __y__ la parte _imaginaria_."),

("### Constructor and destructors of sum types",
 "### Constructores y destructores de los tipos suma"),

("Formally, given types `A` and `B`, the sum type `Either[A, B]` (also written in infix notation as `A Either B`) represents **either** a value of type `A` **or** a value of type `B`. The constructors and destructors of sum types are shown in the following table, alongside the ones for product and function types to facilitate comparison.",
 "Formalmente, dados los tipos `A` y `B`, el tipo suma `Either[A, B]` (que también se escribe en notación infija como `A Either B`) representa **o bien** un valor de tipo `A`, **o bien** un valor de tipo `B`. Los constructores y destructores de los tipos suma aparecen en la tabla siguiente, junto a los de los tipos producto y función para facilitar la comparación."),

("We can create a value of type `A Either B` either with a value of type `A` or a value of type `B`, using the `Left` and `Right` constructors, respectively. In order to extract, destroy or consume information from a sum value we have to _pattern match_ the sum value in order to know the actual value. This match expression basically says: if I know how to obtain a `C` from `A`, and I know how to obtain a `C` from `B`, then I know how to obtain a `C` from `Either[A, B]`.",
 "Podemos crear un valor de tipo `A Either B` bien con un valor de tipo `A`, bien con uno de tipo `B`, usando los constructores `Left` y `Right`, respectivamente. Para extraer, destruir o consumir la información de un valor suma hay que hacer _pattern matching_ sobre él, para saber cuál es el valor que contiene. Esa expresión `match` dice, en esencia: si sé cómo obtener una `C` a partir de una `A`, y sé cómo obtener una `C` a partir de una `B`, entonces sé cómo obtener una `C` a partir de `Either[A, B]`."),

("For instance, we may define the `Number` type as follows:",
 "Por ejemplo, podemos definir el tipo `Number` así:"),

("Note that some of the types that make up the number definition are proper product types. Algebraically, $Number = Int + Int * Int + Double + Double * Double$.",
 "Nótese que algunos de los tipos que componen la definición de número son tipos producto propiamente dichos. Algebraicamente, $Number = Int + Int * Int + Double + Double * Double$."),

("We can construct values of the `Number` type as follows:",
 "Podemos construir valores del tipo `Number` así:"),

("Note the infix notation associates to the left:",
 "Nótese que la notación infija asocia por la izquierda:"),

("Concerning destructors, we can illustrate pattern matching with the following function:",
 "En cuanto a los destructores, podemos ilustrar el pattern matching con la función siguiente:"),

("Nested pattern matching are cumbersome, so Scala offers the possibility of writing these expressions in a more compact way:",
 "El pattern matching anidado resulta incómodo, así que Scala ofrece la posibilidad de escribir estas expresiones de forma más compacta:"),

("Also, note that can omit the `match` keyword when implementing functions over sum types using lambda expressions:",
 "Nótese además que podemos omitir la palabra clave `match` al implementar funciones sobre tipos suma mediante expresiones lambda:"),

("> ![image.png](../../images/scala3api3.jpg) More details on pattern matching in Scala can be found [here](https://docs.scala-lang.org/tour/pattern-matching.html). Also, note that we can create custom pattern matching expressions using so-called [_extractors_](https://docs.scala-lang.org/tour/extractor-objects.html). We won't need them in the course, but they can be really helpful to simplifiy and get more understandable pattern matching expressions.",
 "> ![image.png](../../images/scala3api3.jpg) Hay más detalles sobre el pattern matching en Scala [aquí](https://docs.scala-lang.org/tour/pattern-matching.html). Nótese además que podemos crear expresiones de pattern matching propias mediante los llamados [_extractores_](https://docs.scala-lang.org/tour/extractor-objects.html). No los necesitaremos en el curso, pero pueden ser de mucha ayuda para simplificar el pattern matching y hacerlo más comprensible."),

(
"""#### Exercise
<div class="alert alert-info">
    Implement the type of geometric <code>Shape</code>s, which can include values of types:
    <li> Circle, specified by its radius
    <li> Ellipse, specified by its major and minor axis
    <li> Rectangle, specified by its width and height

Given three instances of shapes for each of the different variants, and implement a function which receives a geometric shape and returns its area.
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Implementa el tipo de las figuras geométricas <code>Shape</code>, que puede incluir valores de los tipos:
    <li> Circle, especificado por su radio
    <li> Ellipse, especificada por sus ejes mayor y menor
    <li> Rectangle, especificado por su anchura y su altura

Da tres instancias de figuras, una por cada variante, e implementa una función que reciba una figura geométrica y devuelva su área.
</div>"""),

("##### Solution", "##### Solución"),
("#### Your solution", "#### Tu solución"),

("### Enumeration types", "### Tipos enumerados"),

("The `Either` type is the most basic approach to define sum types in Scala. Sometimes, we will use _enumeration types_ to label the different variants more meaningfully. For instance, the `Number` type can be defined as follows:",
 "El tipo `Either` es la forma más básica de definir tipos suma en Scala. A veces usaremos _tipos enumerados_ para etiquetar las distintas variantes de manera más significativa. Por ejemplo, el tipo `Number` puede definirse así:"),

("Now, we can use less generic labels than `Left` and `Right` to create numbers:",
 "Ahora podemos usar etiquetas menos genéricas que `Left` y `Right` para crear números:"),

("and these labels can of course be used in pattern matching:",
 "y esas etiquetas pueden usarse, por supuesto, en el pattern matching:"),

("Normally, we will use the following import statement to avoid writing `Number.Rational`, and simply write `Rational`, for instance. Also, note that Scala will issue a warning if some of the variants is omitted in the pattern matching:",
 "Lo habitual será usar la siguiente sentencia `import` para no tener que escribir `Number.Rational` y poder escribir simplemente `Rational`. Nótese además que Scala emite un aviso si se omite alguna de las variantes en el pattern matching:"),

(
"""#### Exercise
<div class="alert alert-info">
    Implement the last exercise on geometric <code>Shape</code>s using enumeration types.
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Resuelve el ejercicio anterior sobre las figuras geométricas <code>Shape</code> usando tipos enumerados.
</div>"""),

("### Standard sum types in Scala", "### Tipos suma estándar en Scala"),

("Besides `Either`, the standard library of Scala provides another important sum type: [`Option`](https://www.scala-lang.org/api/current/scala/Option.html). These types can be defined using enumerations as follows:",
 "Además de `Either`, la biblioteca estándar de Scala ofrece otro tipo suma importante: [`Option`](https://www.scala-lang.org/api/current/scala/Option.html). Estos tipos pueden definirse con enumeraciones así:"),

("These types are important for error handling. We will see how they allow us to get rid of exceptions, at least in the part of our code that we wish to be purely functional. Here it's a small example:",
 "Estos tipos son importantes para el tratamiento de errores. Veremos cómo nos permiten deshacernos de las excepciones, al menos en la parte del código que queremos que sea puramente funcional. Un ejemplo pequeño:"),

("We now return a value which indicates whether there was an error or not:",
 "Ahora devolvemos un valor que indica si hubo error o no:"),

("And now a value which, in case of error indicates the reason:",
 "Y ahora un valor que, en caso de error, indica el motivo:"),

("### Why are sum types called _algebraic_ data types?",
 "### ¿Por qué se llaman tipos _algebraicos_ de datos los tipos suma?"),

("Since we can construct a value of a sum type `Either[A, B]`, either with a value of type `A`, or with a value of type `B`, the number of values of type `Either[A, B]` is equal to the number of values of type `A`, plus the number of values of type `B`: $|Either[A, B]|=|A|+|B|$.",
 "Como podemos construir un valor de un tipo suma `Either[A, B]` bien con un valor de tipo `A`, bien con uno de tipo `B`, el número de valores de tipo `Either[A, B]` es igual al número de valores de tipo `A` más el número de valores de tipo `B`: $|Either[A, B]|=|A|+|B|$."),

(
"""For instance, how many values has the type `Boolean Either Boolean`? We can reason algebraically as follows:

$|Boolean\\,Either\\, Boolean| = |Boolean| + |Boolean| = 2 + 2 = 4$

And these are the four values:""",
"""Por ejemplo, ¿cuántos valores tiene el tipo `Boolean Either Boolean`? Podemos razonar algebraicamente así:

$|Boolean\\,Either\\, Boolean| = |Boolean| + |Boolean| = 2 + 2 = 4$

Y estos son los cuatro valores:"""),

(
"""#### Exercise
<div class="alert alert-info">
    Calculate algebraically the number of values of type <code>(Boolean Either Unit) => (Boolean, Unit)</code>. Which are those values?
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Calcula algebraicamente el número de valores de tipo <code>(Boolean Either Unit) => (Boolean, Unit)</code>. ¿Cuáles son esos valores?
</div>"""),

(
"""Algebraically, we can calculate as follows:

$|(Boolean\\, Either\\, Unit)\\, =>\\, (Boolean, Unit)|= \\\\
|(Boolean, Unit)|^{|(Boolean\\, Either\\, Unit)|} = \\\\
(|Boolean|*|Unit|)^{|Boolean| + |Unit|} = \\\\
2^3 = \\\\
8$""",
"""Algebraicamente, el cálculo es este:

$|(Boolean\\, Either\\, Unit)\\, =>\\, (Boolean, Unit)|= \\\\
|(Boolean, Unit)|^{|(Boolean\\, Either\\, Unit)|} = \\\\
(|Boolean|*|Unit|)^{|Boolean| + |Unit|} = \\\\
2^3 = \\\\
8$"""),

("The different values are obtained by giving proper boolean values to the following template:",
 "Los distintos valores se obtienen dando los valores booleanos adecuados a la plantilla siguiente:"),

("### The `0` type in Scala", "### El tipo `0` en Scala"),

(
"""If the unit type was the identity element for product types, is there any identity type for sums? It has to be a type which satisfies the following conditions:

- $0 + A \\cong A$
- $A + 0 \\cong A$

But $|0 + A| = |0| + |A|$, so $|0| = 0$, i.e. the type $0$ must not be inhabited! In other words, it is a type such that there is no value of that type.""",
"""Si el tipo unit era el elemento identidad de los tipos producto, ¿hay algún tipo identidad para las sumas? Tendría que ser un tipo que cumpliese estas condiciones:

- $0 + A \\cong A$
- $A + 0 \\cong A$

Pero $|0 + A| = |0| + |A|$, luego $|0| = 0$; es decir, ¡el tipo $0$ no puede estar habitado! En otras palabras, es un tipo del que no existe ningún valor."""),

("We don't have to define this type in Scala ourselves, since the identity element of sums is already defined in the Scala standard library: it's the type `Nothing`. Since we can't create instances of this type, the only thing that we can do if we have to return a value of this type, or assign a variable of this type a value, is to throw an exception:",
 "No hace falta que definamos ese tipo en Scala, porque el elemento identidad de las sumas está ya definido en la biblioteca estándar: es el tipo `Nothing`. Como no podemos crear instancias suyas, lo único que podemos hacer si tenemos que devolver un valor de este tipo, o asignar un valor a una variable de este tipo, es lanzar una excepción:"),

("The `???` expression in Scala means essentially an exception of type `Nothing`. Also, note that `Nothing` is the botton of the [Scala inheritance hierarchy](https://docs.scala-lang.org/scala3/book/first-look-at-types.html#all-values-have-a-type), i.e. `Nothing` is a subclass of any Scala class. That's why we can use `???` in place of any value in Scala.",
 "La expresión `???` de Scala significa, en esencia, una excepción de tipo `Nothing`. Nótese además que `Nothing` está en el fondo de la [jerarquía de herencia de Scala](https://docs.scala-lang.org/scala3/book/first-look-at-types.html#all-values-have-a-type); es decir, `Nothing` es subclase de cualquier clase de Scala. Por eso podemos usar `???` en lugar de cualquier valor."),

("Algebraically, since the $Nothing$ type has no values, we don't have constructors for it. Concerning destructors, according to the last discussion, given a value of type $Nothing$ we can observe a value of any type. The following table summarises these results for the $Nothing$ type, alongside the constructors and destructors of the $Unit$ type to facilitate comparison:",
 "Algebraicamente, como el tipo $Nothing$ no tiene valores, no tenemos constructores para él. En cuanto a los destructores, y según lo que acabamos de ver, dado un valor de tipo $Nothing$ podemos observar un valor de cualquier tipo. La tabla siguiente resume esto para el tipo $Nothing$, junto a los constructores y destructores del tipo $Unit$ para facilitar la comparación:"),

("Basically, in the case of the $Unit$ type, we have one constructor but no destructor, whereas the situation is reversed in the case of the $Nothing$ type.",
 "En esencia: en el caso del tipo $Unit$ tenemos un constructor y ningún destructor, mientras que en el del tipo $Nothing$ la situación es la inversa."),

(
"""#### Exercise
<div class="alert alert-info">
    Calculate algebraically the number of values of type <code>(Boolean Either Nothing, Unit)</code>. Which are those values? Also implement a function which receives a value of this type and returns a value of type <code>Int</code>.
</div>""",
"""#### Ejercicio
<div class="alert alert-info">
    Calcula algebraicamente el número de valores de tipo <code>(Boolean Either Nothing, Unit)</code>. ¿Cuáles son? Implementa además una función que reciba un valor de este tipo y devuelva un valor de tipo <code>Int</code>.
</div>"""),

(
"""Algebraically, we can calculate as follows:

$|(Boolean\\, Either\\, Nothing, Unit)|= \\\\
|Boolean\\, Either\\, Nothing| * |Unit| = \\\\
(|Boolean| + |Nothing|) * |Unit| = \\\\
(2 + 0) * 1  = \\\\
2$""",
"""Algebraicamente, el cálculo es este:

$|(Boolean\\, Either\\, Nothing, Unit)|= \\\\
|Boolean\\, Either\\, Nothing| * |Unit| = \\\\
(|Boolean| + |Nothing|) * |Unit| = \\\\
(2 + 0) * 1  = \\\\
2$"""),

# ------------------------------------------------------------------ comentarios
("// where", "// donde"),
("// type Number = ((IntegerNumber Either Fraction) Either Double) Either Complex",
 "// type Number = ((IntegerNumber Either Fraction) Either Double) Either Complex"),
("// Disclaimer: These are not the exact Scala definitions, since we omit variance annotations and case objects.",
 "// Aviso: estas no son las definiciones exactas de Scala, porque omitimos las anotaciones de varianza y los case objects."),
("// type Option[A] = A + 1", "// type Option[A] = A + 1"),
("// type Either[A, B] = A + B", "// type Either[A, B] = A + B"),
("// Using exceptions", "// Con excepciones"),
("// divideWithExceptions(5,0)", "// divideWithExceptions(5,0)"),
("// Using option", "// Con Option"),
("// Using Either", "// Con Either"),
("// type Number", "// tipo Number"),
("// Constructing numbers", "// Construyendo números"),
("// Either[IntegerNumber, Either[Fraction, Either[Double, Complex]]]",
 "// Either[IntegerNumber, Either[Fraction, Either[Double, Complex]]]"),
("// Destructors: kind of number", "// Destructores: clase de número"),
("// test it", "// probémoslo"),
("// without nested pattern matching", "// sin pattern matching anidado"),
("// kind with lambda expressions", "// kind con expresiones lambda"),
("// number type defined with enum", "// el tipo de los números definido con enum"),
("// Labels used in pattern matching", "// Etiquetas usadas en el pattern matching"),
("// Without Number.", "// Sin Number."),
("// values of Either[Boolean, Boolean]", "// valores de Either[Boolean, Boolean]"),
("// A value of type Nothing?", "// ¿Un valor de tipo Nothing?"),
("// Using ???", "// Con ???"),
]
