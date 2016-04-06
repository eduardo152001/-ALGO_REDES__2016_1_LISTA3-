avaliação = list()
print("olá gostariamos de saber a sua avaliação sobre o filme que assistiu")

for i in range (1, 6):
	avaliação.append(int(input("  digite 1 para regular,  2 para bom e 3 para ótimo:  ")))

bom = 0
otimo = 0
regular = 0

for resposta in avaliação:
	if resposta == 1:
		regular = regular + 1
	if resposta == 2:
		bom = bom +1
	if resposta == 3:
		otimo = otimo +1

print ("a quantidade de votos com resultado regular foi:  %d" % regular)
print ("a quantidade de votos com resultado bom foi:  %d" % bom)
print ("a quantidade de votos com resultado otimo foi:  %d" % otimo)
print ("agradecemos sua opinião!!")