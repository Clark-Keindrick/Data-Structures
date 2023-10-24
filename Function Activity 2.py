# months of the year
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']

# variable
current_rainfall = []
previous_rainfall = []
sum1 = 0
sum2 = 0

# Input the current year's rainfall
print("Enter the current year's rainfall in each month")
for i in month:
    rainfall = float(input("%s: " % i))
    current_rainfall.append(rainfall)
    sum1 += rainfall

print()

# Input the previous year's rainfall
print("Enter the previous year's rainfall in each month")
for i in month:
    rainfall = float(input("%s: " % i))
    previous_rainfall.append(rainfall)
    sum2 += rainfall

print()
average = lambda a: a / 12   # get the average using lambda

# printing the table
print(end='            ')
for i in month:
    print("%12s" % i, end=' ')

print("\nCurrent Year:  ", end='')
for i in current_rainfall:
    print("%8.1f" % i, end='     ')

print("\nPrevious Year: ", end='')
for i in previous_rainfall:
    print("%8.1f" % i, end='     ')

# print the total and the average
print()
print("Total rainfall this year: %.1f" % sum1)
print("Total rainfall last year: %.1f" % sum2)
print("Average monthly rainfall for this year: %.1f" % average(sum1))
print("Average monthly rainfall for last year: %.1f" % average(sum2))
