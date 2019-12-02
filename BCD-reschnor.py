decZahl = input("Gib die Zahl!",)
decZahlArray = [int(i) for i in str(decZahl)]
X=0
BCD=[]

for i in range(len(decZahlArray)):
	BCDwork=[0,0,0,0]
	for j in range(3,-1,-1):
		if decZahlArray[i] >= 2**j:
			BCDwork[j] = 1 
		decZahlArray[i] = decZahlArray[i] % 2**j
	BCDwork.reverse()
	BCD.append(BCDwork)
print(BCD)

'''
	print(decZahlArray[i])
	i=+1
'''

