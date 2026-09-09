package wordle

import Dictionary.sample

object IO:
  
  def play(dict: Dictionary): Unit = 
    println("Guess the word in six tries!")
    play(Wordle.start(dict.sample, dict), 1)
    scala.io.StdIn.readLine("Would you like to play again? (y/n) ") match
      case "y" => play(dict)
      case _ => println("Goodbye!")


  def play(w: Wordle, attempt: Int): Unit = 
    if Wordle.win(w) then 
      println("You win!")
    else if Wordle.lose(w) then 
      println("You lose! The correct word was: "+ w.correct)
    else 
      val guess = scala.io.StdIn.readLine(s"GUESS $attempt: ")
      Wordle.attempt(guess)(w) match
        case Left(Wordle.AttemptError.WrongWord) => 
          println("Not in my dictionary! Try again, please.")
          play(w, attempt)
        case Left(Wordle.AttemptError.IsOver) =>
          println("Game is already over!")
        case Right(w, assignment) =>
          println(ansi(assignment))
          play(w, attempt + 1)
  
  import Console.{GREEN_B, MAGENTA_B, RESET, YELLOW_B}

  def ansi(assignment: Wordle.Assignment): String = 
    assignment.map:
      case (c, Some(Wordle.Tile.Green)) => s"${RESET}${GREEN_B}$c"
      case (c, Some(Wordle.Tile.Yellow)) => s"${RESET}${YELLOW_B}$c"
      case (c, Some(Wordle.Tile.Gray)) => s"${RESET}${MAGENTA_B}$c"
      case (_, None) => RESET
    .mkString("")+RESET

