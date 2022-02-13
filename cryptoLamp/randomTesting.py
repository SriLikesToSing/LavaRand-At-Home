import random


'''
r = [ran.random() for x in range(1, 100)]
s = sum(r)
r = [x/s for x in r]
'''

#creating random percentages



"""

have to create percentages that add upto a certain number N sub y

    - off the top method
        - find a random number from 1 to 100
          - T = total amount of cryptos needed to be split amongst
           
            - N1 = 100 - x1; where x1 = random number from 1 to 100
            - N2 = N1 - x2; where x2 = random number from 1 to N1
                ... 
            
            - NT = 
            - continue until NT or amount is reached
            
links:
    https://stackoverflow.com/questions/8064629/random-numbers-that-add-to-100-matlab/8068956#8068956
    https://stackoverflow.com/questions/2640053/getting-n-random-numbers-whose-sum-is-m/2640067#2640067

    - more non complicated solution

     - pick a random n numbers from one to 0 to 100

     n1, n2, n3, n4, n5, n6, n7 .... nN

     add 0 and 100 to the list

     0, n1, n2, n3, n4, n5, n6, n7 ... nN



"""

# seems to work on picking out the percentage of chosen money to invest in 
list = []
for x in range(6):
    list.append(random.randint(0, 100))

print(list)

list.insert(0, 0)
list.insert(len(list), 100)

list.sort()
new = []
newDecimal = []

for x in range(1, len(list)):
    newDecimal.append((list[x] - list[x-1])/100.0)
    new.append(list[x]-list[x-1])

print(new)
print(newDecimal)
print(sum(newDecimal))

"""

Creating random numbers for choosing the amount of stocks to invest in

    - normally distributed (not confirmed yet) where it follows

               n ... -4 -3 -2 1 2 3 4 ... n; where you take the absolute value of the negative numbers

"""

















































