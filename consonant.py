

## WAP to print how many consonants are present in a given string??


s=input("Enter The String: ")
count=0
vowel='aeiouAEIOU'
for i in s:
    if i not in vowel:
        count+=1
print(count)
