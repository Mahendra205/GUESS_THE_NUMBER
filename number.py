import random #importing random module to genertae random int Value
n=20 #random genertaed value will be between 0-20
to_be_guess=int(n*random.random())+1 #generating random value and sorted in the variable
guess=0 #initialization the guess number 0
for i in range(10):# number of tries a user can make
    while guess!=to_be_guess:#condition for while loop
        guess=int(input("new number: "))#taking the input of the number that u have guessed
        if guess>0:
            if guess>to_be_guess:
                print("number too large")
            elif guess<to_be_guess:
                print("number too small")
        else:
            print("sorry that you're giving up!")
        break
    else:
        print("congratulation. you made it!")#if you have guessed right then this will be executed