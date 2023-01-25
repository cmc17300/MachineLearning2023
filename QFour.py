# find length of the set it_companies
# add twitter to it_companies
# Insert multiple IT companies at once to the set it_companies
# Remove one of the companies from the set it_companies
# What is the difference between remove and discard
# Join A and B
# Find A intersection B
# Is A subset of B
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely
# Convert the ages to a set and compare the length of the list and the set.

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 25, 24}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# find the length of the it_companies set
print("Length of it_companies set: ", len(it_companies))

# add twitter to it_companies set
it_companies.add('Twitter')
print("it_companies with twitter added: ", it_companies)

# add multiple it companies to the set at once
itCompanies = {'Instagram', 'Spectrum', 'Verizon'}
it_companies.update(itCompanies)
print("it_companies with mutiple values added: ", it_companies)

# set remove
# the difference between the two is that remove() will raise an error if item doesn't
# exist, discard will not
it_companies.remove('Verizon')
print("Demonstration of remove: ", it_companies)
# itCompanies.remove('Google')
# print("This will throw an error: ", itCompanies)

# set discard
it_companies.discard('Verizon')
print("Demonstration of discard: ", it_companies)

# join A and B
AB = A.union(B)
print("Joined A and B: ", AB)

# intersection of A and B
print("Intersection of A and B: ", A.intersection(B))

# is A a subset of B
print("is A a subset of B?: ", A.issubset(B))

# are A and B disjoint?
disjoint = A.isdisjoint(B)
print("Are A and B disjoint?: ", disjoint)

# join A with B and B with A
print('Join A with B: ', A | B)
print('Join B with A: ', B | A)

# symmetric difference between A and B
# for some reason prints out nothing but the method is correct
C = A.symmetric_difference(B)
print(C)

# delete A and B
## del A, B
## print(A, B) # this should give an error

# convert list age to set and compare lengths
CC = len(age)
print("len of age: ",CC)
ages = set(age)
print("len of ages set: ", len(ages))
