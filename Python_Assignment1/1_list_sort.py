## Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def last_tup(list1):
    return list1[-1]

def sorted_by_last(list1):
    list2 = sorted(list1, key = last_tup)
    return list2
    
list1 = [(2,5), (1,2), (4,4), (2,3), (2,1)]
res_list = sorted_by_last(list1)
print("List Before Sort: ",list1)
print("List After Sort: ",res_list) 