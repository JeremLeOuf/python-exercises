import timeit

a = [1,1,2,3,4,5,5]

def remove_duplicates(any_list):
    new_list = []
    for _ in any_list:
        if _ in new_list:
            continue
        else:
            new_list.append(_)
    return new_list

# print(remove_duplicates(a))

def remove_duplicates_set(any_list):
    return list(set(any_list))

print(remove_duplicates_set(a))