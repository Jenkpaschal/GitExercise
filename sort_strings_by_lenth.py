list = ['orange','apple','banana','peer']
def sort_strings_by_length(list):
    return sorted(list, key = len)
    empty_list = []
    
if __name__ == "__main__":
    sorted_list = sort_strings_by_length(list)

    print("Sorted strings by length:", sorted_list)

