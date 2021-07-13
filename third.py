import re
x = []
j=0
grade = 0
d=0
d1=0
nd=0
with open('C:/Users/Somayeh/Desktop/python/my.txt', encoding ='utf-8') as f:
        for line in f:
                if "UserScore" in line:
                        break
        for line in f:
                if "data-match" in line:
                        j=0
                        for line in f:
                                if j < 2:
                                        x.append(re.findall('\d+', line))
                                        j = j+1
                                else:
                                        if x[0] == x[1]:
                                                grade = grade +10
                                                d = d+1
                                        elif((x[0][0] > x[0][1]) and (x[1][0] > x[1][1])) or ((x[0][0] == x[0][1]) and (x[1][0] == x[1][1])) or ((x[0][0] < x[0][1]) and (x[1][0] < x[1][1])):
                                                grade = grade +2
                                                d1= d1+1
                                        else:
                                                grade = grade +0.5
                                                nd = nd +1
                                                #print ("heheh \n")
                                        x.pop()
                                        x.pop()
                                        break
                if "Load-Flags" in line:
                        #print("somi kharoo\n")
                        break
print ("right prediction = ", d , "\n")
print ("right winner prediction = ", d1, "\n")
print ("wrong winner prediction = ", nd, "\n")
print ("number of predictions = " , d+d1+nd, "\n")
print ("number of predictions = " , d+d1+nd, "\n")


print("your grade is", grade)
#print(x)
#print (line_list6)
                
         
