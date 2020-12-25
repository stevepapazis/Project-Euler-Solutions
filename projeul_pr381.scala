object projeul_pr381 {

  import scala.annotation.tailrec


  def problem(): Unit = {
    println(
"""
Problem 381: (prime-k) factorial


For a prime p let S(p) = ( sum (p-k)! for 1 ≤ k ≤ 5 ) mod(p).

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that the sum of S(p) equals 480 for 5 ≤ p < 100.

Find the sum of S(p) for 5 ≤ p < 10**8.
"""
    )
  }
  

  def explanation(): Unit = {
    println(
"""
Wilson's theorem asserts that (p-1)! = -1 mod(p) whenever p is a prime number. Moreover, since 
(p-1)(p-1)=1 mod(p), we have (p-2)!=(p-1)!*(p-1)**(-1)=-(p-1)=1 mod(p).
Let inv be the modular inverse of (p-1)(p-2)(p-3)(p-4) modulo p (since p is prime, that number
always exists). 
Therefore, 
                 S(p) = (p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)! 
                      = -1 + 1 - 2**(-1) + 6**(-1) - 24**(-1)        
                      = -3*8**(-1)                                    mod(p)
""") 
  }


  def primes11To(top: Int) = {
    val topNdx = (top - 3) / 2 + 1 //odds composite BitSet buffer offset down to 3 plus 1 for overflow
    val (cmpsts, sqrtLmtNdx) = (new Array[Int]((topNdx >>> 5) + 1), (Math.sqrt(top).toInt - 3) / 2)
 
    @inline def isCmpst(ci: Int): Boolean = (cmpsts(ci >>> 5) & (1 << (ci & 31))) != 0
 
    @inline def setCmpst(ci: Int): Unit = cmpsts(ci >>> 5) |= 1 << (ci & 31)
 
    @tailrec def forCndNdxsFrom(cndNdx: Int): Unit =
      if (cndNdx <= sqrtLmtNdx) {
        if (!isCmpst(cndNdx)) { //is prime
          val p = cndNdx + cndNdx + 3
 
          @tailrec def cullPrmCmpstsFrom(cmpstNdx: Int): Unit =
            if (cmpstNdx <= topNdx) { setCmpst(cmpstNdx); cullPrmCmpstsFrom(cmpstNdx + p) }
 
          cullPrmCmpstsFrom((p * p - 3) >>> 1) }
 
        forCndNdxsFrom(cndNdx + 1) }; forCndNdxsFrom(0)
 
    @tailrec def getNxtPrmFrom(cndNdx: Int): Int =
      if ((cndNdx > topNdx) || !isCmpst(cndNdx)) cndNdx + cndNdx + 3 else getNxtPrmFrom(cndNdx + 1)
 
    Iterator.iterate(3)(p => getNxtPrmFrom(((p + 2) - 3) >>> 1)).drop(3).takeWhile(_ <= top)

  }

 
  @tailrec def xgcd(r: Int, r_prev: Int, q: Int, s: Int, s_prev: Int, t: Int, t_prev: Int): Int = {
    if(r==1) s  
    else xgcd(r_prev-q*r, r, r/r_prev, s_prev-q*s, s, t_prev-q*t, t)
  }


  def modularInverse(p:Int, m:Int) = {
    val t = xgcd(m, p, m/p, 1, 0, 0, 1)
    if(t<0) t+p
    else t
  }


  def sumOfS(n: Int): BigInt = {
    var S =  BigInt( ( 3*5 - 3*modularInverse(5, 8%5) )%5 ) + ( 3*7 - 3*modularInverse(7, 8%7) )%7
    primes11To(n).foreach( p => { S += ( 3*p - 3*modularInverse(p, 8) )%p } )
    return S
  }


  def answer(): Unit = {
    print("\nThe sum of S(p) for 5 ≤ p < 10**8 equals ")
    print(sumOfS(100000000).toString+".\n") 
  }


  def main(args: Array[String]): Unit = {
    
    problem()
    
    explanation()
    
    answer()

    scala.io.StdIn.readLine()

  }

}
