# This module serves the use of simulating rolling a six sided die.
# Create a function for rolling a single die
import random
def rollDie(min,max):
    return random.randint(min,max)

# Call the function
print(rollDie(1,6))



pass



# Add new function for rolling multiple die, user can call up function for any number n
def rollDice(n=1):
    total = 0
    for x in range(n):
        total += random.randint(1,6)
    return total

print(rollDice(3))

