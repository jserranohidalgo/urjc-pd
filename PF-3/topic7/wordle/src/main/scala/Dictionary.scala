package wordle

import scala.util.Try

type Dictionary = List[String]

object Dictionary:

    def apply(file: String): Try[Dictionary] = 
        Try(scala.io.Source.fromResource(file).getLines.toList)

    extension (dict: Dictionary)
        def sample: String = 
            dict(scala.util.Random.nextInt(dict.size))
