a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_overlap(list_a, list_b):
    new_list = []
    for _ in list_a:
        if _ in list_b and _ not in new_list:
            new_list.append(_)
    return new_list
            
print(list_overlap(a,b))

def list_overlap_set(list_a, list_b):
    new_list = [_ for _ in list_a if _ in list_b]
    return list(set(new_list)) 
            
print(list_overlap_set(a,b))
            