# Function for remove duplicates
def removeDuplicates(listIn):
  nonDuplicated = []
  
  for x in listIn:
    if x not in nonDuplicated:
      nonDuplicated.append(x)
  	  
  print(sorted(nonDuplicated))
  

inputs = [5,20,25,15,100,200,25,100,75]
removeDuplicates(inputs)

# convert input into a set and then back to a list
mySet = set(inputs)
print(sorted(list(mySet)))