#10.Keep only numbers from the following string x = “ 89e9jcd^o38829@3%3,/mkl$w1”

x = "89e9jcd^o38829@3%3,/mkl$w1"
numbers = []
for i in range(len(x)):
    if x[i] == '0' or x[i] =='1' or x[i] =='2' or x[i] =="3" or x[i] =="4" or x[i] =="5" or x[i] =="6" or x[i] == "7" or x[i] =="8" or x[i] =="9" or x[i] =="10":
        numbers.append(x[i])

print(int("".join(numbers)),type(int("".join(numbers))))



