# Prime Number for a given range
Start = int(input("Enter the start range:"))
End = int(input("Enter the start range:"))
print("The Prime numbers of given range is:")


for i in range(Start, End):
    prime = 0
    for j in range(2,i):
        if i % j == 0:
            prime = 1
            break
    if prime == 0 :
        count +=1
        if i == 1:
           continue
        print(i, end=" ")
