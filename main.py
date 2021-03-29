import random
import os
totalpp = 0
scores = []
i = 0
def cmd():
	cmd=input("user>")
	return cmd
#cmd cycle
while True:
	print("pp counter v1 by akaipureya         |")
	print("Type your pp score in command promt |")
	lastpp=totalpp
	i=0
	totalpp=0
	cef = 1
	while i < len(scores):
		print( str( i+1 ) + " " + str( round(scores[i]*cef , 2 ) ) +" "+ str(round(cef*100 , 1)) + "%" )
		totalpp+=scores[i]*cef
		round(totalpp , 0)
		if i<5:
			cef-=0.05
		else:
			cef-=0.01
		
		i+=1
	print(str(totalpp)+" +"+str(totalpp-lastpp))
	com=cmd()
	scores.append(int(com))
	scores.sort()
	scores.reverse()
	os.system("cls")


