#if else

age = 19
if(age>=18):
    print("You can vote")
else:
    print("Yout can not vote yet")

#if-elif

color = input("Enter color of traffic light : ")

if(color.capitalize() == 'Red'):
    print("Stop")
    print("Red Light")
elif(color.capitalize() == "Yellow"):
    print("Be Ready")
    print("Yellow Light")
else:
    print("Go")
    print("Green Light")