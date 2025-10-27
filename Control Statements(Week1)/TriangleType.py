angle1 = int(input("enter angle1:"))
angle2 = int(input("enter angl2:"))
angle3 = int(input("enter angle3:"))
Sum = angle1+ angle2+ angle3
if(Sum== 180):
    if 90 in[angle1, angle2, angle3]:
        print("Right Angeled Triangle")
    elif any(angle > 90 for angle in [angle1, angle2, angle3]):
        print("Obtuse triangle")
    else:
        print("Acute triangle")
                
    