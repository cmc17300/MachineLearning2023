# create a tuple containing names of sister and brothers
# join the sisters and brothers and assign it to "siblings" tuple
# how many siblings are there?
# modify the siblings tuple and add the name of my mom and dad and assign it to a
# tuple called "family_members"

# create tuple with the names of brothers n sisters
sister = ("Veve", "Genevieve")
brother = ("Jordan", "Roman")
print("Sister tuple: ", sister)
print("Brother tuple: ", brother)

# join two tuples together and call them "siblings"
siblings = sister + brother
print("Siblings tuple: ", siblings)

# how many siblings are there?
print("Length of siblings tuple: ", len(siblings))

# add mom and dad to siblings tuple
family_members = siblings + ("Robb", "Jennifer")
print("Family_members tuple: ", family_members)
