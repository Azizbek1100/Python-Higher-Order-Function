text = ["apple", "34", "banana", "100", "abc", "75"]
numbers = list(filter(lambda x: x.isdigit(), text))
print(numbers)