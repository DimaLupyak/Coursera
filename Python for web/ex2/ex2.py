import re
handler = open('regex_sum_442664.txt')
sum = 0
for line in handler:
    for number in re.findall('[0-9]+', line):
        sum += int(number)

print(sum)