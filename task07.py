prices = ["$120", "$340", "$50", "$90"]
numbers = list(map(lambda x: float(x.replace('$', '')), prices))
print(numbers)