Dayinput = input()
DayBar = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
DayNumber =  DayBar.index(Dayinput) +1 
OutputDay = 0
if DayNumber - 7 == 0:
  OutputDay = 7
else:
  OutputDay = 7 - DayNumber 
print(OutputDay)
