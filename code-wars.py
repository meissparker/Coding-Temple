# Even or Odd

def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    else:
        return "Odd"
    
#Convert a Number to a String
def number_to_string(num):
    num = str(num)
    return num
    # Return a string of the number here!



#Vowel Count
def get_count(sentence):
    num_vowels = 0 
    vowels = "aeiou"
    for x in sentence:
        if x in vowels:
            num_vowels += 1 
    return num_vowels