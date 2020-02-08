problem = """Problem 31: Coin sums
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?"""


coins = [1, 2, 5, 10, 20, 50, 100, 200]

def function(sum, coin):
    if sum==200 or coin==0: return 1
    else:
        counter = 0
        restSum = (200-sum)//coins[coin]
        for i in range(restSum, -1, -1):
            counter+=function(sum+i*coins[coin], coin-1)
        return counter        

counter = function(0, 7)
    
print(problem, '\n', "Solution: ", counter, sep='')
input()
