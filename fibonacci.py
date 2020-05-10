#python code to generate fibonacci series
#accepting the no.of terms in the series
num = int(input("Enter the no.of terms of the fibonacci series"))
a=0
b=1
print(a)
print(b)
i=2
#for loop to generate the series
for i in range(2,num):
    sum1 = a+b
    print(sum1)
    a=b
    b=sum1
    i = i+1


