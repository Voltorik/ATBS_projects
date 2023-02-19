spam = ['apples', 'bananas', 'tofu', 'cats']
empty = []
numbers = [1, 2, 3, 4, 5]
boolean = [True, False]

def commaList(items):
    string = ''
    for i in range(len(items)):
        if i == len(items) - 1:
            string += 'and ' + str(items[i])
        else:
            string += str(items[i]) + ', '
    return string


string = commaList(spam)
print(string)
string = commaList(empty)
print(string)
string = commaList(numbers)
print(string)
string = commaList(boolean)
print(string)
