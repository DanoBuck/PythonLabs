## Long lists of integers throws a recursion error with this function
## as we hit the maximum recursion depth - Nice way to see the bubble sort
## work recursively though
def bubble_sort_recursive(list):
    return bubble_sort_outer_loop(list, 0)

def bubble_sort_outer_loop(list, i):
    if len(list) == 1:
        return list

    if i == len(list):
        return list

    return bubble_sort_inner_loop(list, i, i + 1)

def bubble_sort_inner_loop(list, i, j):
    if j == len(list):
        return bubble_sort_outer_loop(list, i + 1)

    if list[j] < list[i]:
        holder = list[i]
        list[i] = list[j]
        list[j] = holder

    return bubble_sort_inner_loop(list, i, j + 1)

def bubble_sort_iterative(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                holder = list[i]
                list[i] = list[j]
                list[j] = holder
    return list

print("\n***************************Bubble Sort Recursively***************************")
lists = [5,1,2,4,6,-1]
bubble_sort_recursive(lists)
print(lists)

new_list = [0,69,24,47,98,14,30,62,60,53,58,65,74,55,61,83,23,97,6,99,92,49,80,63,10,84,1,17,19,82,11,71,8,4,79,13,39,20,77,50]
bubble_sort_recursive(new_list)
print(new_list)

print("\n***************************Bubble Sort Iteratively***************************")
iterative_list = [32,66,59,2,42,22,36,68,38,35,86,31,85,28,16,51,15,76,46,44,5,37,9,95,3,78,40,21,87,72,96,89,12,88,94,27,93,90,43,7,91,45,48,29,70,69,24,47,98,14,30,62,60,53,58,65,74,55,61,83,18,64,54,26,25,41,100,33,75,34,81,57,52,67,73,56,23,97,6,99,92,49,80,63,10,84,1,17,19,82,11,71,8,4,79,13,39,20,77,50]
bubble_sort_iterative(iterative_list)
print(iterative_list)