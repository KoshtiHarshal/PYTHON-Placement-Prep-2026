import time
t =time.strftime('%I:%M:%S %p')
Hour = int(time.strftime('%H'))
print(t)
print(Hour)

if(Hour > 0 and Hour < 12):
    print("Good Morning :)")
elif(Hour >= 12 and Hour < 17):
    print("Good Afternoon <3")
else:
    print("Good Night :)<3")    
