def are_anagrams(str1, str2):
    
    str1 = str1.replace(" ", "").lower()  ## Remove spaces and convert both strings to lower case
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2): ##Check if the lengths of the strings are different
        return False

    sorted_str1 = sorted(str1) ##Sort the characters in both
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:  ## Compare sorted strings
        return True
    else:
        return False
#Illustrations
word_1 = "bare"  
word_2= "bear"
if are_anagrams(word_1, word_2):
    print(f"{word_1} and {word_2} are anagrams.")
else:
    print(f"{word_1} and {word_2} are not anagrams.")
