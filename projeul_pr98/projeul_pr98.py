problem = """\
Problem 98: Anagramic squares

By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36**2. What is remarkable is that,
by using the same digital substitutions, the anagram, RACE, also forms a square
number: 9216 = 96**2. We shall call CARE (and RACE) a square anagram word pair
and specify further that leading zeroes are not permitted, neither may a
different letter have the same digital value as another letter.

Using p098_words.txt, a 16K text file containing nearly two-thousand common
English words, find all the square anagram word pairs (a palindromic word is
NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file."""

#data input
with open("p098_words.txt") as file:
    words = file.readlines()[0].replace('\n','').split('","')
words[0] = words[0].replace('"','')
words[-1] = words[-1].replace('"','')

#sorting words by length
wordsSortedByLength = dict()
for word in words:
    try:
        wordsSortedByLength[len(word)].append(word)
    except KeyError:
        wordsSortedByLength[len(word)] = [word]

#find anagrams
anagrams = []
for length in reversed(sorted(wordsSortedByLength.keys())):
    temp = wordsSortedByLength[length]
    alreadyFoundWords = []
    while temp:
        testword = temp.pop()
        if testword in alreadyFoundWords: continue
        for word in temp:
            if sorted([j for j in testword]) == sorted([j for j in word]):
                anagrams.append((testword,word))
                alreadyFoundWords.append(word)


print(problem,end="\n\n\n")
print("Anagramic squares:")

#check if they're anagramic squares

maximum = 9216
previouswordlength = max([len(word) for word in words])

for word1,word2 in anagrams:
    
    if previouswordlength > len(word1):
        squares = [
            k**2 for k in range(
                int(int("9"*(len(word1)-1))**.5)+1,
                int(int("9"*(len(word1)))**.5)+1
                )
            ]
        previouswordlength = len(word1)

    mapping = [-1 for i in range(len(word1))]

    for m,i in enumerate(word2):
        for n,j in enumerate(word1):
            if i==j and n not in mapping:
                mapping[m] = n
                break

    for square in squares:
        candidateSquare = int( "".join(
            [ str(square)[mapping[i]] for i in range(len(word1)) ]
            ) )
        if int(candidateSquare**.5)**2 != candidateSquare:
            continue
        if len(str(candidateSquare)) != len(word1):
            continue
        if len(set([i for i in str(square)]))!=len(set([i for i in word1])):
            continue
        lettermap = dict()
        for n,l in enumerate(str(square)):
            try:
                lettermap[l].append(word1[n])
            except KeyError:
                lettermap[l] = [word1[n]]
        if max([len(lettermap[i]) for i in lettermap])>1:
            continue

        if square > maximum:
            maximum = square
        if candidateSquare > maximum:
            maximum = candidateSquare
        
        print(word1,word2)
        print(square,candidateSquare)
   
input("Solution: "+str(maximum))


