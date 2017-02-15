from random import randint

max = 6
min = 1

c = randint(min,max)

def dice(number):
    print number
    answer = raw_input("Would you like to roll?").upper()
    while answer == "YES":
        answer = 'no'
        dice(randint(min,max))

dice(c)
print "Thanks for playing!"