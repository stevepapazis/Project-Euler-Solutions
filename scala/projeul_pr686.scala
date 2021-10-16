object projeul_pr686 {


  def problem(): Unit = {
    println(
"""
Problem 686: Powers of Two

2**7 is the first power of two whose leading digits are "12". The next 
power of two whose leading digits are "12" is 2**80.

Define p(L,n) to be the nth-smallest positive integer such that the
base 10 representation of 2**p(L,n) begins with the digits of L. 
So p(12,1)=7 and p(12,2)=80.

You are also given that p(123,45)=12710.

Find p(123,678910).
""")
  }


  def explanation(): Unit = {
    println(
"""
Let 2**j be a number that begins with the digits of L. Then there 
is an integer k such as L*10**k <= 2**j <= (L+1)*10**k.

Solving the inequality for k, we get

( j*log(2)-log(L+1) )/log(10) <= k <= ( j*log(2)-log(L) )/log(10)

Therefore all integers j>0 such as   

( j*log(2)-log(L+1) )/log(10) <= ( ( j*log(2)-log(L) )/log(10) ).toInt

begin with the digits of L.
""")
  }



  def answer(): Unit = {
    println()
    println( "p(1,1) = " + p(1,1) )
    println( "p(2,1) = " + p(2,1) )
    println( "p(4,1) = " + p(4,1) )
    println( "p(16,1) = " + p(16,1) )
    println( "p(12,1) = " + p(12,1) )
    println( "p(12,2) = " + p(12,2) )
    println( "p(12,45) = " + p(12,45) )
    println( "p(123,45) = " + p(123,45) )
    println( "p(12,678910) = " + p(12,678910) )
    println( "Answer: p(123,678910) = " + p(123,678910) )
  }



  def p(L: Int, n: Int): Int =  {

    if(L<=0) 
      throw new Exception("In p(L,n), L must be a positive integer.")
    if(n<=0) 
      throw new Exception("In p(L,n), n must be a positive integer.")

    import scala.math.log
    import scala.annotation.tailrec

	  val log2 = log(2)/log(10)
	  val logL = log(L)/log(10)
	  val logLplus1 = log(L+1)/log(10)

    @tailrec def findFirstCandidate( j: Int ): Int = 
        if( j*log2-logL >= 0 ) return j
        else findFirstCandidate(j+1)

    @tailrec def findNextExpoLessThan( c: Int, j: Int ): (Int, Int)
     = 
        if( j*log2-logLplus1 < (j*log2-logL).toInt ){
          if( c + 1 >= n ) return (0, j)
          findNextExpoLessThan(c+1, j+1)
        }  
        else
          findNextExpoLessThan(c, j+1)
        

    findNextExpoLessThan(0, findFirstCandidate(1))._2
  }



  def main(args: Array[String]): Unit = {
    
    problem()
    
    explanation()
    
    answer()

    scala.io.StdIn.readLine()

  }


}
