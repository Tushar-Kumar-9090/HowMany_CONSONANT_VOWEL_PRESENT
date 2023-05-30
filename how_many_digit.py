

## WAP to print how many digits are present in a given string??


s=input("Enter The String: ")
count=0
for i in s:
    if i.isdigit():
        count+=1
print(count)