
def main():
    import myModule
    # Imagine having a bucket with 1000 dice.
    # Determine how many times the die is rolled
    N=int(input("How many times would you like to roll the die? "))
    # Create 6 "buckets" labeled "Bucket 1," "Bucket 2," "Bucket 3"...
    Bucket1=0
    Bucket2=0
    Bucket3=0
    Bucket4=0
    Bucket5=0
    Bucket6=0

    #Begin loop for values of the die rolled N times
    for x in range(N):
        numbers = myModule.rollDie(1, 6)
        # Organize numbers into buckets
        if numbers == 1:
            Bucket1 += 1
        elif numbers == 2:
            Bucket2 += 1
        elif numbers == 3:
            Bucket3 += 1
        elif numbers == 4:
            Bucket4 += 1
        elif numbers == 5:
            Bucket5 += 1
        else:
            Bucket6 += 1

    # Make shortcut for probability calculations of each bucket
    Prob1 = Bucket1 / N
    Prob2 = Bucket2 / N
    Prob3 = Bucket3 / N
    Prob4 = Bucket4 / N
    Prob5 = Bucket5 / N
    Prob6 = Bucket6 / N

    # Tell computer to show probability of each number
    print("Probability of rolling a 1: " + str(Prob1))
    print("Probability of rolling a 2: " + str(Prob2))
    print("Probability of rolling a 3: " + str(Prob3))
    print("Probability of rolling a 4: " + str(Prob4))
    print("Probability of rolling a 5: " + str(Prob5))
    print("Probability of rolling a 6: " + str(Prob6))

main()



