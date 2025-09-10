## Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.Return the resulting string.

def replace_not_poor(string):
    first_position_not = string.find('not')
    first_position_poor = string.find('poor')

    if (first_position_not != -1 and first_position_poor != -1 and first_position_not < first_position_poor):
        new_string = f"{string[:first_position_not]}good{string[first_position_poor+len('poor') : ]}"
        return new_string
    else:
        return string

sample_string = 'The lyrics is not that poor!'
result_string = replace_not_poor(sample_string)
print("Sample String: ",sample_string)
print("Output String: ",result_string)