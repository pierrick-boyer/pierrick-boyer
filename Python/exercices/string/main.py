a = "aAbByYzzZ"

# ord() -> know a specific character's ASCII/UNICODE
for i in a:
    print(ord(i))

# chr() -> takes a code point and returns its character
print(chr(97))

# min()
print(min(a))

# max()
print(max(a))

# count()
print(a.count("z"))

# endswith()
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

# find()
print("Eta".find("ta"))

# isalpha() -> interested in letters only
print("Moo".isalpha())
print('Mu40'.isalpha())

# isdigit() -> looks at digits only
print('2018'.isdigit())
print("Year2019".isdigit())

# join()
print(", ".join(["omicron", "pi", "rho"]))

# replace()
print("Apple juice".replace("juice", ""))

# split()
print("phi chi\npsi".split())
