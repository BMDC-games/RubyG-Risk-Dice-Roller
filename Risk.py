#Risk Dice Roller v1.0
from random import *
def Risk():
    print "Enter the number of Dices each player is rolling (If attacking player enters above 3 the computer will enter blitz mode (won't stop attacking until won or no players left)) \n"
    num1 = Input("How many Dices is the first player rolling? ")
    num2 = Input("How many Dices is the second player rolling? ")    
    if num1 > 3:
        blitz(num1,num2)
    else:
        p1,p2 = round(num1,num2)
        num1 += p1
        num2 += p2
        print "The Attacking player lost {} and has {} left \nThe Defending player lost {} and has {} left".format(p1,num1,p2,num2)
    
def blitz(num1,num2):
    print "\n\nYou have Entered Blitz Mode!"
    game_on = True
    r1 = 0 #r1/r2 will be resembling the number of dices each player will be rolling each round
    r2 = 0
    while game_on:
        if num1 > 3:
            r1 = 3
        else:
            r1 = num1
        if num2 > 2:
            r2 = 2
        else:
            r2 = num2
        p1,p2 = round(r1,r2)
        num1 += p1
        num2 += p2
        print "The Attacking player lost {} Troops      The Defending player lost {} Troops".format(p1,p2)
        print "The Attacking player has: {} Troops      The Defending player has: {} Troops".format(num1,num2)
        if num1 == 0 or num2 == 0:
            game_on = False
            print "Good Game!"
    
def round(num1,num2): #Gets a list of many Dice each player is rolling - Returns how many soldiers each player lost
    r1 = roll(num1)
    r2 = roll(num2)
    print "The first player rolled: {} \nThe second player rolled: {}".format(r1,r2)
    result = fight(r1,r2)
    return result[0], result[1]

def roll(num): #Returns a list of rolled Dice results (sorted)
    result = []
    for i in range(num):
        result.append(randint(1,6))
    return bubble_sort(result)

def fight(p1,p2): #Returns 2 numbers (how many soldeirs each player lost) and gets lists of both players rolls and fights them off (second player defending(he wins in case of tie))
    result = [0,0]
    if len(p1) < len(p2):
        f = len(p1) #The number of "Fights" (Deaths) there will be
    else:
        f = len(p2)
    print "There are {} fights".format(f)
    for i in range(f):
        if p1[i] > p2[i]: #In this case the attacking player wins (the defending looses)
            result[1] -= 1
        else:
            result[0] -= 1
    return result

 


def Input(text):
    try:
        return input(text)
    except:
        print "Numbers Only! Try again."
        return Input(text)

def bubble_sort(list):
    length = len(list)
    not_sorted = True 
    while not_sorted:
        changes = False
        for i in range(length-1):
             
            if list[i] < list[i+1]:
                temp_no = list[i] #temp_no is the higher number
                list[i] = list[i+1]
                list[i+1] = temp_no #We change both of the places 
                changes = True
                #print str(" "* i) + "||"                
            else:
                pass
        if changes == False:
            not_sorted = False
    return list 


Risk()