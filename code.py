import csv 
import math

with open('data.csv',newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
totalMarks = 0
n = len(fileData)
for marks in fileData :
    totalMarks += float(marks[1])
mean = totalMarks/n
squaredList = []
for number in fileData :
    num = float(number[1]) - mean
    num = num**2
    squaredList.append(num)
sum = 0    
for i in squaredList:
  sum += i
result = sum / n-1
standard_deviation = math.sqrt(result)  
print(standard_deviation)
print(mean)

