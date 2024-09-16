str = input("Enter you word in camel_case: ")

def camel_to_snake(word):
    result = []
    for c in word:
        if c.isupper():
            result.append('_')
            result.append(c.lower())
        else:
            result.append(c)
    return ''.join(result)

converted_word = camel_to_snake(str)
print(converted_word)

