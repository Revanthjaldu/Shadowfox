#2.Numbers
def format_value(num, ch):
    return format(num, ch)

result = format_value(145, 'o')
print(result)
#................
pi=3.14
r=84
area=pi*r*r
watersqr=1.4
totalarea=area*watersqr
print(int(totalarea))
#..................
distance=490
time=7
time_sec=time*60 
speed=(distance/time_sec)
print(int(speed))