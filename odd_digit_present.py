

## WAP to print how many odd digit are present given string??


s=input("Enter The String: ")
count=0
for i in s:
    if i.isdigit():
        if int(i)%2!=0:
            count+=1
print(count)

