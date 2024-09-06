package wordle

type Word = String

case class Wordle(correct: Word, dict: Dictionary, guesses: List[Word])

object Wordle: 

    val win: Wordle => Boolean = 
        case Wordle(correct, _, guess :: _) if correct == guess => true
        case _ => false

    def lose(w: Wordle): Boolean = 
        !win(w) && w.guesses.length == 6

    def over(w: Wordle): Boolean = 
        win(w) || lose(w)

    enum Tile: 
        case Green
        case Yellow
        case Gray

    import Tile._

    type Assignment = List[(Char, Option[Tile])]

    import cats.syntax.all._, cats.data.State, State._, Bag._
    
    def tiles(correct: String, guess: String): Assignment =

        def remove(c: Char): State[Bag[Char], Unit] = 
            modify[Bag[Char]](_ rm c)

        (correct zip guess).toList
            .traverse:
                case (c1, c2) if c1 == c2 => 
                    remove(c1).as(c1 -> Option(Green))
                case (_, c) => 
                    pure(c -> None)
            .flatMap:
                _.traverse: 
                    case (c, None) => 
                        inspect((b: Bag[Char]) => !b.contains(c)).flatMap: 
                            if _ then pure(c -> Some(Gray))
                            else remove(c).as(c -> Some(Yellow))
                    case v => State.pure(v)
            .runA(Bag.from(correct))
            .value

    def start(correct: Word, dict: Dictionary): Wordle = 
        Wordle(correct, dict, List())

    enum AttemptError: 
        case WrongWord
        case IsOver

    def attempt(guess: Word): Wordle => Either[AttemptError, (Wordle, Assignment)] = 
        case w@Wordle(correct, dict, guesses) if !over(w) && dict.contains(guess) => 
            Right(Wordle(correct, dict, guess :: guesses), tiles(correct, guess))
        case w if over(w) => Left(AttemptError.IsOver)
        case _ => Left(AttemptError.WrongWord)