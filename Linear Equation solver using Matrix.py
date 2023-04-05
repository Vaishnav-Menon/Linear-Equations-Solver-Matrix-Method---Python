def eqn():
	a1=int(input("a1= "))#input the values for a,b,c,d,e
	b1=int(input("b1= "))
	c1=int(input("c1= "))
	d1=int(input("d1= "))
	e1=int(input("e1= "))
	f1=int(input("f1= "))
	a2=int(input("a2= "))
	b2=int(input("b2= "))
	c2=int(input("c2= "))
	d2=int(input("d2= "))
	e2=int(input("e2= "))
	f2=int(input("f2= "))
	a3=int(input("a3= "))
	b3=int(input("b3= "))
	c3=int(input("c3= "))
	d3=int(input("d3= "))
	e3=int(input("e3= "))
	f3=int(input("f3= "))
	a4=int(input("a4= "))
	b4=int(input("b4= "))
	c4=int(input("c4= "))
	d4=int(input("d4= "))
	e4=int(input("e4= "))
	f4=int(input("f4= "))
	a5=int(input("a5= "))
	b5=int(input("b5= "))
	c5=int(input("c5= "))
	d5=int(input("d5= "))
	e5=int(input("e5= "))
	f5=int(input("f5= "))
	a=[[a1,b1,c1,d1,e1,f1],[a2,b2,c2,d2,e2,f2],[a3,b3,c3,d3,e3,f3],[a4,b4,c4,d4,e4,f4],[a5,b5,c5,d5,e5,f5]]
	for i in a:
		print(i)
	if a[1][0]==0:
		pass
	else:
		m1,m2=a[0][0], a[1][0]
		for i in range(0,6):
			a[1][i]=(m1*a[1][i])-(m2*a[0][i])#R2=a1R2-b1R1
	if a[2][0]==0:
		pass
	else:
		m1,m2=a[0][0], a[2][0]
		for i in range(0,6):
			a[2][i]=(m1*a[2][i])-(m2*a[0][i])#R3=a1R3-c1R1
	if a[2][1]==0:
		pass
	else:
		m1,m2=a[1][1], a[2][1]
		for i in range(0,6):
			a[2][i]=(m1*a[2][i])-(m2*a[1][i])#R3=b2R3-c2R2
	if a[3][0]==0:
		pass
	else:
		m1,m2=a[0][0], a[3][0]
		for i in range(0,6):
			a[3][i]=(m1*a[3][i])-(m2*a[0][i])#R4=a1R4-d1R1
	if a[3][1]==0:
		pass
	else:
		m1,m2=a[1][1], a[3][1]
		for i in range(0,6):
			a[3][i]=(m1*a[3][i])-(m2*a[1][i])#R4=b2R4-d2R2
	if a[3][2]==0:
		pass
	else:
		m1,m2=a[2][2], a[3][2]
		for i in range(0,6):
			a[3][i]=(m1*a[3][i])-(m2*a[2][i])#R4=c3r4-d3r3
	if a[4][0]==0:
		pass
	else:
		m1,m2=a[0][0], a[4][0]
		for i in range(0,6):
			a[4][i]=(m1*a[4][i])-(m2*a[0][i])#R5=a1R5-e1R1
	if a[4][1]==0:
		pass
	else:
		m1,m2=a[1][1], a[4][1]
		for i in range(0,6):
			a[4][i]=(m1*a[4][i])-(m2*a[1][i])#R5=b2R5-e2R2
	if a[4][2]==0:
		pass
	else:

		m1,m2=a[2][2], a[4][2]
		for i in range(0,6):
			a[4][i]=(m1*a[4][i])-(m2*a[2][i])#R5=c3R5-e3R3
	if a[4][3]==0:
		pass
	else:
		m1,m2=a[3][3], a[4][3]
		for i in range(0,6):
			a[4][i]=(m1*a[4][i])-(m2*a[3][i])#R5=d4R5-e4R4
	print("\n")
	print("The Matrix after row transitions : ")
	for i in a:
		print(i)
	if a[4][4]==0 and a[4][5]==0:
		print("There are infinitely many solutions for the given system of linear eqautions")
		sol=False
	elif a[4][4]==0 and a[4][5]!=0:
		print("There are no solutions for the given system of linear equations")
		sol=False
	else:
		x5=(a[4][5])/(a[4][4])
		x4=(a[3][5]-(a[3][4]*x5))/a[3][3]
		x3=(a[2][5]-(a[2][4]*x5)-(a[2][3]*x4))/a[2][2]
		x2=(a[1][5]-(a[1][4]*x5)-(a[1][3]*x4)-(a[1][2]*x3))/a[1][1]
		x1=(a[0][5]-(a[0][4]*x5)-(a[0][3]*x4)-(a[0][2]*x3)-(a[0][1]*x2))/a[0][0]
		sol=True
	if sol==True:
		result=[x1,x2,x3,x4,x5]
		for i in range(0,5):
			print("The value of x",i+1," = ",result[i])

eqn()
