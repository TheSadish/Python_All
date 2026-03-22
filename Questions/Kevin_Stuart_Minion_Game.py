def minion_game(string):
    # your code goes here
    kevin_score = 0
    stuart_score = 0
    vowels = "AEIOU"
    n = len(string)
    
    for i,ch in enumerate(string):
        if ch in vowels:
            kevin_score += n - i
            # print("kevin",kevin_score,i)
        else:
            stuart_score += n - i
            # print("stuart", stuart_score,i)
    
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

'''
R.1 
stuart B BA BAN BANA BANAN BANANA - 6

R.2
kevin A AN ANA ANAN ANANA - 5

R.3
stuart N NA NAN NANA - 4

R4
kevin A AN ANA -3
.
.
.

'''