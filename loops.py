# Basic - Print all interger from 0 to 150

for i in range(151):
    print(i)



# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for i in range(5,1005,5):
    print(i)




# Counting, the Dojo Way- Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

def count_dojo():
    for i in range(1,101,1):
        if i % 5 == 0:
            print('Coding')
        if i % 10 == 0:
            print ('Dojo')

count_dojo()  




# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

lowest = 0
highest = 500000
oddNumber = 0

for number in range(lowest, highest+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        oddNumber = oddNumber + number

print("The final sum from {0} to {1} = {2}".format(lowest, highest, oddNumber))   



# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def count_to_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4

count_to_four()  



# Flex Counter- Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)
            
flex_countdown(2, 9, 3)
