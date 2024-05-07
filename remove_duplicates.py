list = [14,5,7,8,9,7,7]
def remove_duplicate(list):
    empty_list = []
    set_ = set()
    for i in list:
        if i not in set_:
            set_.add(i)
            empty_list.append(i)
    return empty_list
print(remove_duplicate(list))