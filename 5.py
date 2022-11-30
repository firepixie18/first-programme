import math
for item in range(0,346,15):
    a = round(math.sin(math.radians(item)),4)
    b = round(math.cos(math.radians(item)),4)
    print(str(item) + "---" + str(a) +" "+ str(b))