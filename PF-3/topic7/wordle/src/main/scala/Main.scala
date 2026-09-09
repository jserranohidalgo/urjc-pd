package wordle 

import scala.util.{Failure, Success}

@main def main(): Unit =
  Dictionary("words.txt") match 
    case Failure(error) => println(error)
    case Success(dict) => IO.play(dict)