s=str(input())
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
        print("yes")
    else:
        print("no")
