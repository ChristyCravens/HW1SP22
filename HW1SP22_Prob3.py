def main():


# Import the random module to find random variables when needed
    import random



# Have user define values for how many values, the mean and the standard deviation
    n=int(input("Enter the number of values to use to find probability: "))
    m=int(input("Enter the mean: "))
    s=int(input("Enter the standard deviation: "))

# Create list for storage
    values=[]

# Create buckets based on the s & m of the value for storage
    Bucket1=0   # count of numbers between +/-1StDev of mean
    Bucket2=0   # count of number between +/- 2*s of m
    Bucket3=0 # count of numbers between +/- 3*s of m
    Outliers=0

# Create a loop for values based on the user input for number of values (n)
    for i in range(n):
        num=random.normalvariate(m,s)

# Buckets are russian nesting dolls: B1 inside B2, B2 inside B3:

# If a number is inside bucket 1, increase value of b1, b2 & b3
        if (m-s)<=num and num<=(m+s):
            Bucket1+=1
            Bucket2+=1
            Bucket3+=1
# Elif a number is inside b2, increase value of b2 & b3
        elif (m-2*s)<=num and num<=(m+2*s):
            Bucket2+=1
            Bucket3+=1
# Elif number inside b3, increase number of b3
        elif (m-3*s)<=num and num<=(m+3*s):
            Bucket3+=1
# Else throw out into outlier bucket
        else:
            Outliers+=1
        values += [num]

# Make probability equations
    Prob1=Bucket1/n
    Prob2=Bucket2/n
    Prob3=Bucket3/n
    Else=Outliers/n

# Print the values and probability statements
    print(values)
    print("{:0.1f}% of the data is within +/-1StdDev of the mean (when n={})".format(Prob1*100,n))
    print("{:0.1f}% of the data is within +/-2StdDev of the mean (when n={})".format(Prob2*100,n))
    print("{:0.1f}% of the data is within +/-3StdDev of the mean (when n={})".format(Prob3*100,n))




main()