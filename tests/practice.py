def one(string):
    return ''.join([c+c+c for c in str])

x = one("The")

print(x)
