problem = """\
Problem 205: Dice Game

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins.
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg


"""

pP = dict()
for i1 in range(1,5):
    for i2 in range(1,5):
        for i3 in range(1,5):
            for i4 in range(1,5):
                for i5 in range(1,5):
                    for i6 in range(1,5):
                        for i7 in range(1,5):
                            for i8 in range(1,5):
                                for i9 in range(1,5):
                                    try:
                                        pP[i1+i2+i3+i4+i5+i6+i7+i8+i9].append((i1,i2,i3,i4,i5,i6,i7,i8,i9))
                                    except KeyError:
                                        pP.update({i1+i2+i3+i4+i5+i6+i7+i8+i9:[(i1,i2,i3,i4,i5,i6,i7,i8,i9)]})
for i in pP:
    pP[i] = len(pP[i]) #pP[i] contains the number of the results that Pete can roll so the total is i
cC = dict()
for i1 in range(1,7):
    for i2 in range(1,7):
        for i3 in range(1,7):
            for i4 in range(1,7):
                for i5 in range(1,7):
                    for i6 in range(1,7):
                        try:
                            cC[i1+i2+i3+i4+i5+i6].append((i1,i2,i3,i4,i5,i6))
                        except KeyError:
                            cC.update({i1+i2+i3+i4+i5+i6:[(i1,i2,i3,i4,i5,i6)]})
for i in cC:
    cC[i] = len(cC[i]) #cC[i] contains the number of the results that Collin can roll so the total is i

def P(k):
    """If the total of the dice of Pete is p and the total of the dice of Collin
is c then P(k) returns the probability that p = c + k, when k is a natural
number or zero."""
    w = 0
    for p in pP:
        try: w += pP[p]*cC[p-k]
        except KeyError: pass
    return w/12230590464 # = 4**9 * 6**6 = all possible results
            
#The probability that Pete wins is p = sum([P(k) for k in range(1, 31)]).
#The probability that Collin wins is q = sum([P(k) for k in range(-27, 0)]).

p = sum([P(k) for k in range(1, 31)])
q = sum([P(k) for k in range(-27, 0)])

print(problem,
    "The probability that Pete wins is p = sum([P(k) for k in range(1, 31)]) = ",p,'.\n',
    "The probability that Collin wins is q = sum([P(k) for k in range(-27, 0)]) = ",q,'.\n',
    "The probability that there is a draw is 1-p-q = ", 1-p-q,'.\n',sep=''
    )
input()
