import calendar
#help(calendar)

# путь к файлу calendar
# d:\program files\python311\lib\calendar.py

year = calendar.isleap(2027) #проверка года на високосность
print(year)

weekday = calendar.weekday(1995, 6, 25) #проверка какой был день недели по счёту
print(weekday)

calendar.prcal(2023) #календарь на 2023 год
