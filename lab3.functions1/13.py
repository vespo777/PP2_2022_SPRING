import random
def game(r, cnt, name):
    print("Take a guess.")
    b = int(input())
    if b > r:
        print("Your guess is too high.")
        cnt+=1
        return game(r, cnt, name)
    elif b < r:
        print("Your guess is too low.")
        cnt+=1
        return game(r, cnt, name)
    elif b == r:
        print("Good job, " + name +"! You guessed my number in " + str(cnt)+" guesses!")





print("Hello! What is your name?")
a=input()


print("Well, " + str(a) + ", I am thinking of a number between 1 and 20.")

c = random.randrange(1,20)
game(c, 0, a)
