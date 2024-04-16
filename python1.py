i = 0
a = 7.00
c = 0

while i <= 15:
    i = i + 1
    b = a + 0.30
    while i < 20:
        if i <= 5:
            print(a, c, "am - " , b , c, "am : ")
            a = a + 1.00
            if a == 12.00:
                print(b, c, "am - " , a , c, "pm : ")
            else:
                print(b, c, "am - " , a , c, "am : ")
        elif i <= 20:
            print(a , c, "pm - " , b , c, "pm : ")
            a = a + 1.00
            print(b , c, "pm - " , a , c, "pm : ")
        break
