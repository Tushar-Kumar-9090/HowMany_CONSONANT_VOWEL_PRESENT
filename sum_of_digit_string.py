
## WAP to print sum of digits present in a given string??


s=input("Enter A String: ")
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
print(sum)