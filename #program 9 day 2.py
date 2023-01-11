month = input("input the month (e.g. January, February etc.): ")
day = int(input("input the day: "))

if month in ('January', 'February', 'March'):
    season = 'winter'
elif month in ('April', 'May', 'June'):
    season = 'summer'
elif month in ('July', 'August', 'September'):
    season = 'spring'
else:
    season = 'autumn'

if (month == 'June') and (day > 20):
    season = 'spring'
elif (month == 'March') and (day > 19):
    season = 'summer'
elif (month == 'September') and (day > 21):
    season = 'autumn'
elif (month == 'December') and (day > 20):
    season = 'winter'

print("Season is",season)
