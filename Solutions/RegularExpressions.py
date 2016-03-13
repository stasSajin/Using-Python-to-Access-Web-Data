import re
file=open('regex_sum_255553.txt')

numbers=list()
for line in file:
    number=re.findall('[0-9]+',line)
    for i in number:
        numbers.append(i)
    
sum=0
for j in numbers:
    sum=sum+int(j)

print sum
print numbers