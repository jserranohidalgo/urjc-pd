package wordle

type Bag[T] = Map[T, Int]

object Bag: 

    // Empty constructor
    def apply[T](): Bag[T] = 
        Map()

    // String constructor
    def from[T](s: String): Bag[Char] = 
        s.foldLeft(Bag[Char]()): (b, c) => 
            b.updatedWith(c): 
                case None => Some(1)
                case Some(i) => Some(i+1)

    // Remove occurrences
    extension [T](b: Bag[T])
        infix def rm(t: T): Bag[T] = 
            b.updatedWith(t): 
                case Some(v) if v > 1 => Some(v-1)
                case _ => None

