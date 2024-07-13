def IMC(T,P):
	M = P / T ** 2
	print("IMC=", M)
	if M > 30:
		print("obésité certaine")
	elif 25 < M < 30:
		print("tendance à l'obésité")
	elif M < 25 :
		print("tout va bien")

		
#IMC(1.80, 60) affiche:
IMC= 18.51851851851852
tout Va bien
#print(IMC(1.60, 70)) affiche:
IMC= 27.343749999999996
tendance à l obésité
#print(IMC(1.50, 80)) affiche:
IMC= 35.55555555555556
obésité certaine 
