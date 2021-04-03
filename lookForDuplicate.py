def return_duplicates(i_list):
    dups = []
    a_set = set()
    for item in i_list:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)
        if length_one == length_two:
            dups.append(item)
    return dups


a_list = ["Susan Adams", "Kwame Goodall", "Jill Hampton", "Susan Adams"]
duplicates = return_duplicates(a_list)
print(duplicates)
