object projeul_pr204 {


  def problem(): Unit = {
    println(
"""
Problem 204: Generalised Hamming Numbers

A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10**8.

We will call a positive number a generalised Hamming number of type n, if it has no 
prime factor larger than n. Hence the Hamming numbers are the generalised Hamming 
numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10**9?"""
    )
  }


  def explanation(topPrmNdx: Int, topLimit: Int): Unit = {
    println(
"""
Let 2, 3, 5, ..., pk, pk' be a list with all the prime numbers less than n. If m is a 
generalised Hamming number of type n, then m = 2**a2 * 3**a3 * ... * pk**ak * pk'**ak' 
and m =< N  =>  2**a2 * 3**a3 * ... * pk**ak =< N/pk'**ak'. Therefore, we can 
recursively compute the number of generalised Hamming numbers of type pk' less than N, 
that is S(pk', N), by using the formula

        S(pk', N) = sum( S(pk, N/pk**i) when i=0,...,(log(N)/log(pk)).toInt )

				        and

                      S(2, N) = sum( 1 + (log(N)/log(2)).toInt )

""") 
  }


  def answer(topPrmNdx: Int, topLimit: Int): Unit = {

    import scala.math.log
    import scala.math.pow

    val primes = List(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
 
    def sum( PrmNdx: Int, N: Double ): Int =  
	if( PrmNdx==0 )
	    ( log(N)/log(2) ).toInt + 1   
	else
            (  0  to  ( log(N)/log(primes(PrmNdx)) ).toInt  )
		.map( k => sum( PrmNdx - 1, N/pow(primes(PrmNdx),k) ) )
		.fold(0)( _ + _ )

    println( 
"There are " + sum(topPrmNdx, topLimit) + 
" generalised Hamming numbers of type 100 less than 10**9." 
    )

  }


  def main(args: Array[String]): Unit = {
    
    problem()
    
    val topLimit = 1000000000
    val topPrmNdx = 24

    explanation(topPrmNdx, topLimit)
    
    answer(topPrmNdx, topLimit)

    scala.io.StdIn.readLine()

  }


}
