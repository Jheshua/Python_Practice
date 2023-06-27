#The task is very simple: accept a list of values, and another value n, 
#then return a new list with every value multiplied by n. For example, [1, 2, 3] and 4 should result in [4, 8, 12].

def mlista(list,n):
    empty_list = []
    for i in list:
        empty_list.append(i*n)
    return empty_list

#Example of usage
list_example = [1,2,3]
n_example = 3

list_result = mlista(list_example,n_example)
print(list_result)