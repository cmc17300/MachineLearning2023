# sort the list and find min and max (good)
# add the min age and max age back to the list again
# find the median age
# find the average
# find the range of the ages

# list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sorted by smallest val
ages.sort()
print("Sorted by smallest val: ", ages)
# sorted by largest val
ages.sort(reverse=True)
print("sorted by largest val: ", ages)

# append the max and min vals back into the list
ages.append(26)
ages.append(19)
print("List with appended values: ", ages)

# average of the list
average = sum(ages) / len(ages)
print("Average of list rounded: ", round(average))
print("Average of list not rounded: ", average)


# range of the list
def Range(f):
    Min = min(f)  # identify min val (19)
    Max = max(f)  # identify max val (26)

    # subtract the two to get the range
    return Max - Min


# prints out the computation
print("Range of the list: ", Range(ages))
