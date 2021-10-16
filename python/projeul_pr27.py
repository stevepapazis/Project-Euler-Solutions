"""Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula: n**2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n**2+ 79n + 1601 was discovered, which produces 80
primes for the consecutive values n = 0 to 79. The product of the coefficients,
79 and 1601, is 126479.

Considering quadratics of the form:
n**2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""

#brute force approach
#answer: a*b=-61*971=-59231 (n=71)

import time

def search(l,n):
    i=0; end=len(l)
    while l[i] < n:
        i+=1
        if i+1 == end: break
    if l[i] == n: return i


start=time.time()
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

for p in range(997,995006,2):
    if p%3==0:
        continue
    elif p%5==0:
        continue
    elif p%7==0:
        continue
    elif p%11==0:
        continue
    elif p%13==0:
        continue
    elif p%17==0:
        continue
    elif p%19==0:
        continue
    elif p%23==0:
        continue
    elif p%29==0:
        continue
    elif p%31==0:
        continue
    elif p%37==0:
        continue
    elif p%41==0:
        continue
    elif p%43==0:
        continue
    elif p%47==0:
        continue
    elif p%53==0:
        continue
    elif p%59==0:
        continue
    elif p%61==0:
        continue
    elif p%67==0:
        continue
    elif p%71==0:
        continue
    elif p%73==0:
        continue
    elif p%79==0:
        continue
    elif p%83==0:
        continue
    elif p%89==0:
        continue
    elif p%97==0:
        continue
    elif p%101==0:
        continue
    elif p%103==0:
        continue
    elif p%107==0:
        continue
    elif p%109==0:
        continue
    elif p%113==0:
        continue
    elif p%127==0:
        continue
    elif p%131==0:
        continue
    elif p%137==0:
        continue
    elif p%139==0:
        continue
    elif p%149==0:
        continue
    elif p%151==0:
        continue
    elif p%157==0:
        continue
    elif p%163==0:
        continue
    elif p%167==0:
        continue
    elif p%173==0:
        continue
    elif p%179==0:
        continue
    elif p%181==0:
        continue
    elif p%191==0:
        continue
    elif p%193==0:
        continue
    elif p%197==0:
        continue
    elif p%199==0:
        continue
    elif p%211==0:
        continue
    elif p%223==0:
        continue
    elif p%227==0:
        continue
    elif p%229==0:
        continue
    elif p%233==0:
        continue
    elif p%239==0:
        continue
    elif p%241==0:
        continue
    elif p%251==0:
        continue
    elif p%257==0:
        continue
    elif p%263==0:
        continue
    elif p%269==0:
        continue
    elif p%271==0:
        continue
    elif p%277==0:
        continue
    elif p%281==0:
        continue
    elif p%283==0:
        continue
    elif p%293==0:
        continue
    elif p%307==0:
        continue
    elif p%311==0:
        continue
    elif p%313==0:
        continue
    elif p%317==0:
        continue
    elif p%331==0:
        continue
    elif p%337==0:
        continue
    elif p%347==0:
        continue
    elif p%349==0:
        continue
    elif p%353==0:
        continue
    elif p%359==0:
        continue
    elif p%367==0:
        continue
    elif p%373==0:
        continue
    elif p%379==0:
        continue
    elif p%383==0:
        continue
    elif p%389==0:
        continue
    elif p%397==0:
        continue
    elif p%401==0:
        continue
    elif p%409==0:
        continue
    elif p%419==0:
        continue
    elif p%421==0:
        continue
    elif p%431==0:
        continue
    elif p%433==0:
        continue
    elif p%439==0:
        continue
    elif p%443==0:
        continue
    elif p%449==0:
        continue
    elif p%457==0:
        continue
    elif p%461==0:
        continue
    elif p%463==0:
        continue
    elif p%467==0:
        continue
    elif p%479==0:
        continue
    elif p%487==0:
        continue
    elif p%491==0:
        continue
    elif p%499==0:
        continue
    elif p%503==0:
        continue
    elif p%509==0:
        continue
    elif p%521==0:
        continue
    elif p%523==0:
        continue
    elif p%541==0:
        continue
    elif p%547==0:
        continue
    elif p%557==0:
        continue
    elif p%563==0:
        continue
    elif p%569==0:
        continue
    elif p%571==0:
        continue
    elif p%577==0:
        continue
    elif p%587==0:
        continue
    elif p%593==0:
        continue
    elif p%599==0:
        continue
    elif p%601==0:
        continue
    elif p%607==0:
        continue
    elif p%613==0:
        continue
    elif p%617==0:
        continue
    elif p%619==0:
        continue
    elif p%631==0:
        continue
    elif p%641==0:
        continue
    elif p%643==0:
        continue
    elif p%647==0:
        continue
    elif p%653==0:
        continue
    elif p%659==0:
        continue
    elif p%661==0:
        continue
    elif p%673==0:
        continue
    elif p%677==0:
        continue
    elif p%683==0:
        continue
    elif p%691==0:
        continue
    elif p%701==0:
        continue
    elif p%709==0:
        continue
    elif p%719==0:
        continue
    elif p%727==0:
        continue
    elif p%733==0:
        continue
    elif p%739==0:
        continue
    elif p%743==0:
        continue
    elif p%751==0:
        continue
    elif p%757==0:
        continue
    elif p%761==0:
        continue
    elif p%769==0:
        continue
    elif p%773==0:
        continue
    elif p%787==0:
        continue
    elif p%797==0:
        continue
    elif p%809==0:
        continue
    elif p%811==0:
        continue
    elif p%821==0:
        continue
    elif p%823==0:
        continue
    elif p%827==0:
        continue
    elif p%829==0:
        continue
    elif p%839==0:
        continue
    elif p%853==0:
        continue
    elif p%857==0:
        continue
    elif p%859==0:
        continue
    elif p%863==0:
        continue
    elif p%877==0:
        continue
    elif p%881==0:
        continue
    elif p%883==0:
        continue
    elif p%887==0:
        continue
    elif p%907==0:
        continue
    elif p%911==0:
        continue
    elif p%919==0:
        continue
    elif p%929==0:
        continue
    elif p%937==0:
        continue
    elif p%941==0:
        continue
    elif p%947==0:
        continue
    elif p%953==0:
        continue
    elif p%967==0:
        continue
    elif p%971==0:
        continue
    elif p%977==0:
        continue
    elif p%983==0:
        continue
    elif p%991==0:
        continue
    t=int(p**.5+1)
    for i in range(997,t,2):
        if p%i==0:
            break
    else:
        primes.append(p)
print(time.time()-start) # ~6 sec

M=[0] 
for b in range(3,1000,2): 
    if search(primes, b) != None:
        for a in range(-999,1000,2):
            n=1; p=1+a+b
            while search(primes, abs(p)) != None:
                n+=1
                p=n**2+a*n+b
            if n > M[0]: M=[n, a, b] 
        for a in range(-999,1000,2):
            n=1; p=1+a-b
            while search(primes, abs(p)) != None:
                n+=1
                p=n**2+a*n-b
            if n > M[0]: M=[n, a, -b]
            
print(time.time()-start) #time: ~1 min
