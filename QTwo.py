# create an empty dictionary called dog
# add name, color, breed, legs and age to the dictionary
# create a student dictionary and add first name, last name, gender, age, marital status,
# skills, country, city and address as keys
# get length of student dict
# modify the skills values by adding one or two skills
# get dict keys as a list
# get dict values as a list

# create an empty dict called dog
dog = {"Name": 'buddy', "Breed": 'boxer', "Legs": 4, "age": 5}
print("Dog dictionary: ", dog)

# create dictionary for students
student = {"First_Name": 'Clara', "Last_Name": 'Cerda', "Gender": 'F', "Age": 19,
           "Marital_Status": 'Single', "Skills": ['Drawing', 'programming'],
           "City": 'Lees Summit', "Address": '123 example St.'}
print("Student dictionary: ", student)

# length of the student dict
print("Length of the student dict: ", len(student))

# get the value of skills and check data type(should be a list)
checkType = type([5])
print(checkType)

# dict keys as a list
keyList = list(dog.keys())
print("Dict dog keys as a list: ", keyList)

# get dict values as a list
valList = list(dog.values())
print("Dict dog values as a list: ", valList)


