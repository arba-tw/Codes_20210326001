List2 = [7,-9,2, 7, 4,     -3, 1, -2, -7, 6,     9, 3, -9, -3, 4, \
         -5, -10, 8, -5, 9,     9, -5, 9, 4, -5,     6, 5, -2, -2, -4, \
         8, -6, -10, 10, -1, -5, -10, 7, -7, 1,     4, -5, -4, 7, 4, \
         4, 5, 10, 1, -3]
List1 = []
Max_So_far = 0
Max_Ending_Here = 0
a = 0
b = 1
t = 0
B = 0

T = -1 # 1 or -1

for i in range(len(List2)):
    t = List2[i]
    t = t * (T)
    List1.append(t)

#print(List2)
#Bprint(List1)

for i in range(len(List1)):
    Max_Ending_Here = Max_Ending_Here + List1[i]
    if Max_So_far < Max_Ending_Here:
        Max_So_far = Max_Ending_Here
        if b < a:
            B = b
        a = i + 1
        #print("end A:", a)

    if Max_Ending_Here < 0:
        Max_Ending_Here = 0
        if b < a:
            B = b
        b = i + 1
        #print("start B:",b)

Sum_So_far = Max_So_far * T
print("Start Location at : ", B)
print("End Location at : ", a)
print("Thet sum is : ", Sum_So_far)
