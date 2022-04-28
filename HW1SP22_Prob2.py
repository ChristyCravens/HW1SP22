def main():

# Import the module with the rollDice() function
    import myModule

# Ask the user to specify the number of dice they want to use
    n = int(input("Enter the number of dice being rolled: "))

# Ask the user to specify the number of times they want to roll
    R = int(input("How many times would you like to roll " + str(n) + " dice? "))

# Create a storage place (dictionary) for all rolled values with parameters based on the number of dice used
    values = {}
    for x in range(n, (n*6)+1):
        values[x] = 0

# Begin the loop and store the values
    for x in range(R):
        score = myModule.rollDice(n)
        values[score] = values[score] +1

# Tell the computer how to output the probability
    for x in range(n, (n*6)+1):
       print("Probability of rolling a " + str(x) + ": " + str(values[x]/R))

# Call the function to preform the actions
main()