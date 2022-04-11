day = int(input())
month = int(input()) 
year = int(input())
century = year // 100
year = year % 100

print((day + ((13 * month - 1) // 5) + year + (year // 4 + century // 4 - 2 * century + 777)) % 7)