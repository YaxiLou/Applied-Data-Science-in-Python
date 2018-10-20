# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file
# with text and numbers. You will extract all the numbers
# in the file and compute the sum of the numbers.
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_119929.txt (There are 89 values and the sum ends with 790)
fname = input("Enter the file name:")
try:
    fh = open(fname)
except:
    print("Invalid file name",fname)
    quit()
import re
lst = list()
total = 0
for line in fh:
    number = re.findall('[0-9]+',line)
    if len(number) < 1: number = [0]
    lst = lst + number
for i in lst:
    total = total + int(i)
print(total)
