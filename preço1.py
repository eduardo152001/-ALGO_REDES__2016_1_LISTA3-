preços = list()

for i in range (1, 6):
	preços.append(float(input("digte o preço do seu produto n. %d: " % i)))

media_de_preço = (float (preços[0]) + (preços[1]) + (preços[2]) + (preços[3]) + (preços[4])) / 5	
preço_inferior = 0
preço_entre = 0
preço_acima = 0

for preço in preços:
	if preço < 50 :
		preço_inferior = preço_inferior + 1
	if preço >= 50 and preço <= 80 :
		preço_entre = preço_entre +1 
	if preço > 80:
		preço_acima = preço_acima + 1
	

print ("  a quantidade de produtos com preçosmenores que 50 é %d " % preço_inferior)
print (preço_acima)
print (preço_entre)
print ("a media de preços de todos os seus produtoe é %.2f" % media_de_preço)