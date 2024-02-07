class WeatherForecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

raining = []

for _ in range(int(input())):
    a, b, c = input().split()
    if c =="Rain":
        raining.append(WeatherForecast(a,b,c))

raining = sorted(raining, key = lambda x: x.date)

print(raining[0].date, raining[0].day, raining[0].weather)