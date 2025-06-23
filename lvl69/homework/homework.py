#1)
def split_and_join_with_G(word):
    parts = word.split('g')
    result = 'G'.join(parts)
    return result
#2)
def invert_case(word):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in word])
#3)
def join_numbers_with_at(numbers):
    str_numbers = [str(num) for num in numbers]
    joined = '@'.join(str_numbers)
    return joined
#4)gavakete
#5) ver gavakete