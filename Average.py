#Thomas Farrell
#Average.py

total = 0
average = 0
howManyEntered = 0

howMany = int(input("How many test scored would you like to average? "))

while howManyEntered < howMany:
    testScore = int(input("Enter test score: "))
    total += testScore
    howManyEntered += 1

average = total / howMany
print("The average for the test scores you entered is: " + str(average))
