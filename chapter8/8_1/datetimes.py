from datetime import date, time


ganjitsu = date(2021, 1, 1)
print(ganjitsu)
print(ganjitsu.weekday())
print(date.today())

print(time())
print(time(16, 12, 25))
print(time(second=10))
print(time(minute=30))
now = time(16, 12, 25)
print(now.isoformat())

nows = date.today()
print(f'{nows}')
months = date(year=2024, month=1, day=12)
print(f'{months}')
print(nows - months)
