# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)

L1 = []
students = int(input("how many students?: "))  # taking num of students from the user
print("\nenter student weights in lbs:")  # printing message
for i in range(0, students):  # for loop take inputs from user in lbs through console
    lbs = int(input())
    L1.append(lbs)

L2 = []
for i in range(0, students):  # for loop to convert weights from lbs to kgs
    kgs = 0.453592 * L1[i]  # multiplication of 0.453592 to L1(lbs) will produce L2(kgs)
    L2.append(round(kgs, 2))  # appending the calculation to the list

print("\nweights of students in lbs: ", L1)  # printing weights in lbs
print("\nweights of students in kilograms: ", L2)  # printing weights in kgs
