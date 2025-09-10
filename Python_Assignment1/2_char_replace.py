## Write a Python program to get a string from a given string where all occurrences of its first char have been changes to '$', except the first itselfs.

def char_replace(str1):
    first_char = str1[0]
    changed_string = (f"{first_char}{str1[1:].replace(first_char , '$')}")
    return changed_string
    
string = 'restart'
res_string = char_replace(string)
print("Original String: ",string)
print("Changed String: ",res_string)