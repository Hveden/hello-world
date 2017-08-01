# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 22:44:38 2017

@author: Toby
"""

def genPrimes():
    """
    Yield the next prime everytime its run
    Not optimized for speed at all
    """
    primes = []
    x = 2
    while True:
        prime = True
        for i in primes:
            if x % i == 0:
                prime = False
        if prime:
            primes.append(x)
            yield x
            x += 1
        else:
            x += 1
                



def userGetPrimes():
    """
    Main method.
    Asks for input and runs genPrimes either 1 time or the amount asked for
    """
    print("Hello Human, im here to get primes for you!")
    gen = genPrimes()
    x = 1
    while True:
        user = input("Press 'n' if you want the next prime, press a number if you want the next x primes, press 'e' for ending the program: ")
        if user == "n":
            print("number", x, "primenumber is:", next(gen)) 
            x += 1
        elif user == "e":
            break
        elif user.isdigit():
            for i in range(int(user)):
                print("number", x, "primenumber is:", next(gen))
                x += 1              
        else:
            print("wrong input")


userGetPrimes()