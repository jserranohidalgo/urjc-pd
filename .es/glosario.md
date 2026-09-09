# Glosario de la traducción

La versión inglesa (`master`) es la fuente de verdad. Esta rama es un producto
derivado de ella: nunca se fusiona en ninguna dirección, se regenera.

## Criterios

- Se traducen las __celdas markdown__ y los __comentarios__ (`//`) del código.
- __No__ se traduce el código: ni identificadores, ni tipos, ni nombres de la API
  (`foldRight`, `map`, `filter`, `flatMap`, `Option`, `Either`…), ni las salidas
  de las celdas.
- Los ejercicios y los templates comparten la prosa con su notebook: se traduce
  una vez y se aplica a los dos, de modo que no puedan divergir.
- Los exámenes de `exams/` ya están en español y no se tocan.
- Las figuras (`images/*.svg`) llevan el texto incrustado en inglés; redibujarlas
  queda fuera del alcance.
- `PF-3/topic7/wordle/` no se traduce.

## Términos

| inglés | español |
|---|---|
| higher-order function | función de orden superior |
| pattern matching | _pattern matching_ (sin traducir, en cursiva) |
| type / typed | tipo / tipado |
| algebraic data type | tipo algebraico de datos |
| proof / to prove | prueba / demostrar |
| statement (de un teorema) | enunciado |
| hole | __hueco__ |
| goal | meta |
| skeleton | esqueleto |
| divide and conquer | divide y vencerás |
| tail-recursive | recursiva final |
| assumption / hypothesis | asunción / hipótesis |
| constructor / destructor | constructor / destructor |
| `foldRight`, `map`, `filter`, `flatMap` | sin traducir: son nombres de función |
