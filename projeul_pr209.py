problem = """Problem 209: Circular Logic"""

explanation = """\
Let σ(a,b,c,d,e,f):= b,c,d,e,f,(a+b*c)%2. Then

    τ(a,b,c,d,e,f) AND τ(b,c,d,e,f,a XOR(b AND c ))
            ==  τ(a,b,c,d,e,f)*τ(σ(a,b,c,d,e,f))

Since each tuple (a,b,c,d,e,f) corresponds to a binary number in the range 0
to 63, we shall work with the numbers 0 to 63, instead of the binary strings.

Since 0 == τ(n)*τ(σ(n)), we deduce that  τ(n)==1 => τ(σ(n))==0. This
implication creates some restrictions for downstream values of τ. 


Notice that

σ(0) = 0                                                             (period 1)

σ(21) = 42, σ(42) = 21                                               (period 2)

σ(9) = 18, σ(18) = 36, σ(36) = 9                                     (period 3)

σ(1) = 2, σ(2) = 4, σ(4) = 8, σ(8) = 16, σ(16) = 32, σ(32) = 1       (period 6)

σ(5) = 10, σ(10) = 20, σ(20) = 40, σ(40) = 17, σ(17) = 34, σ(34) = 5 (period 6)

σ(3) = 6, σ(6) = 12,  .... , σ(48) = 33, σ(33) = 3                   (period 46)


Because of these circles, the value of τ(n) will depend on the values of τ
in the circle that contains n but not on the values of τ in other cirles.

In other words, if we find the number of valid combinations of τ for each
circle, we get the answer by multiplying those numbers.

What's more we don't really care about the specific values that appear in
each circle, we only care about the lengths of the circles.

For a circle of length l we can create a tree that contains all the valid
allocations of values to τ as branches, that is allocations that respect
the condition τ(n)==1 => τ(σ(n))==0. Let N(l) be the number of its branches.

When l==1 we get N(1) = 1, when l==2 it is N(2) = 3 and when l==k the number
of branches is N(k) = N(k-1) + N(k-2).

This formula holds because the root of the tree with length k connects to
two subtrees, one with length k-1 and one with length k-2. (Just remember
that we can swap each symbol in a circle with any other symbol.)
"""

def toBinary(n):
    l=[]
    for i in range(6):
        l.append(n%2)
        n//=2
    l.reverse()
    return l

def toDecimal(l):
    return sum( [2**n*m for n,m in enumerate(reversed(l))] )

def sigma(n):
    a,b,c,d,e,f = tuple(toBinary(n))
    return toDecimal([b,c,d,e,f,(a+b*c)%2])

def countTheBranchesInTreeWithRootAt(n):

    def countBranches(m, target, initial_assumption, last_value, S):
        
        if m == target:
            if initial_assumption == 1 and last_value == 1:
                return 0
            else:
                return S
            
        if last_value == 1:
            return countBranches(sigma(m),target,initial_assumption,0,S)
        else:
            return countBranches(sigma(m),target,initial_assumption,0,S)\
                 + countBranches(sigma(m),target,initial_assumption,1,S) 
    
    return countBranches(sigma(n),n,0,0,1) + countBranches(sigma(n),n,1,1,1)

def numberOfBranchesOnTreeWithLength(k):
    a, b = 2, 1
    c=1
    while c<k:
        a,b =b,a+b
        c+=1
    return b



answer  =  numberOfBranchesOnTreeWithLength(1) \
         * numberOfBranchesOnTreeWithLength(2) \
         * numberOfBranchesOnTreeWithLength(3) \
         * numberOfBranchesOnTreeWithLength(6) \
         * numberOfBranchesOnTreeWithLength(6) \
         * numberOfBranchesOnTreeWithLength(46)


print(
    problem,
    "\n\n\n",
    explanation,
    "\n\n",
    "Answer: N(1)*N(2)*N(3)*N(6)*N(6)*N(46) = ", answer,
    sep=""
    )

input()
