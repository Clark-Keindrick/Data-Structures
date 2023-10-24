# average data of every G7 members in each year
year = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
USA = [2.7, 1.6, 2.2, 2.9, 2.2, -3.4, 5.6]
Japan = [1.5, 0.7, 1.6, 0.5, -0.2, -4.5, 1.6]
Germany = [1.4, 2.2, 2.6, 1.0, 1.0, -4.5, 2.8]
UK = [2.6, 2.2, 2.1, 1.6, 1.6, -9.2, 7.4]
France = [1.1, 1.0, 2.2, 1.8, 1.8, -7.8, 6.9]
Italy = [0.7, 1.2, 1.6, 0.9, 0.5, -9.0, 6.6]
Canada = [0.6, 1.0, 3.0, 2.7, 1.8, -5.2, 4.5]

sum1 = sum2 = sum3 = sum4 = sum5 = sum6 = sum7 = 0  # sum variable of each G7 economies

print()
print("   \t\t\t\t\t\t\t\t\t\tEconomic growth of the G7 from 2015 – 2021.")
print()

# GENERATING A TABLE
print("Countries", end='      ')
for i in year:
    print("%10d" % i, end='     ')

print("\nUSA", end='         ')
for i in USA:
    print("%12.1f" % i, end='   ')
    sum1 += i

print("\nJapan", end='         ')
for i in Japan:
    print("%10.1f" % i, end='     ')
    sum2 += i

print("\nGermany", end='       ')
for i in Germany:
    print("%10.1f" % i, end='     ')
    sum3 += i

print("\nUK", end='            ')
for i in UK:
    print("%10.1f" % i, end='     ')
    sum4 += i

print("\nFrance", end='        ')
for i in France:
    print("%10.1f" % i, end='     ')
    sum5 += i

print("\nItaly", end='         ')
for i in Italy:
    print("%10.1f" % i, end='     ')
    sum6 += i

print("\nCanada", end='        ')
for i in Canada:
    print("%10.1f" % i, end='     ')
    sum7 += i

print("\n")
average = lambda a: a / 7  # Getting the average economic growth of every G7 members
print("Average economic growth of USA       :  %.2f" % average(sum1))
print("Average economic growth of Japan     :  %.2f" % average(sum2))
print("Average economic growth of Germany   :  %.2f" % average(sum3))
print("Average economic growth of UK        :  %.2f" % average(sum4))
print("Average economic growth of France    :  %.2f" % average(sum5))
print("Average economic growth of Italy     :  %.2f" % average(sum6))
print("Average economic growth of Canada    :  %.2f" % average(sum7))

# Getting the average economic growth of the G7 from 2015 – 2021.
overall_total = average(sum1) + average(sum2) + average(sum3) + average(sum4) + average(sum5) + average(sum6) + average(
    sum7)
print("\nThe average economic growth of the G7 from 2015 – 2021 :  %.2f" % average(overall_total))
