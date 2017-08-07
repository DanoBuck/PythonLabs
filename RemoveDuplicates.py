# Function for remove duplicates
def removeDuplicates(listIn):
  nonDuplicated = []
  
  for x in listIn:
    if x not in nonDuplicated:
      nonDuplicated.append(x)
  	  
  print(sorted(nonDuplicated))


def remove_duplicates_recursively(list):
    return remove_duplicates_outer_loop(list, 0, [])


def remove_duplicates_outer_loop(list, i, return_list):
    if len(list) == 1:
        return list

    if i == len(list):
        return return_list

    return remove_duplicates_inner_loop(list, i, i + 1, return_list)


def remove_duplicates_inner_loop(list, i, j, return_list):
    if j == len(list):
        return_list.append(list[i])
        return remove_duplicates_outer_loop(list, i + 1, return_list)

    if list[i] == list[j]:
        return remove_duplicates_outer_loop(list, i + 1, return_list)

    return remove_duplicates_inner_loop(list, i, j + 1, return_list)

inputs1 = [4,5,20,25,15,100,200,5,4,11,200,25,100,75]
recursive_removal = remove_duplicates_recursively(inputs1)
print(sorted(list(recursive_removal)))

# convert input into a set and then back to a list
inputs2 = [5,20,25,15,100,200,25,100,75]
mySet = set(inputs2)
print(sorted(list(mySet)))