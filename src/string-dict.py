
str = "google.com"

dict = {}

for s in str:
    if s in dict.keys():
        dict[s] += 1
    else:
        dict[s] = 1

print(dict)