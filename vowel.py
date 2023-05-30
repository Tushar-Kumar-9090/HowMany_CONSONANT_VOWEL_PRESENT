
## Q.3 WAP to print how many vowels are present in a given string??



s=input("Enter The String: ")
count=0
vowel='aeiou'
for i in s:
    if i.lower() in vowel:
        count+=1
print(count)
