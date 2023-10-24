# months of the year
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']


def current(*n):
    if n == 0:
        r = 1
    else:
        r = n + current(n - 1)
    return r

print()

current_rainfall = []

# Input the current year's rainfall
print("Enter the current year's rainfall in each month")
for i in month:
    rainfall = float(input("%s: " % i))
    current_rainfall.append(rainfall)

for i in current_rainfall:
    current(i)
