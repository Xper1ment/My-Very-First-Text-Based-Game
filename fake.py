n = int(input('Press 1 to convert celsius to kelvin \n Press 2 to convert kelvin to celcius\n'))
temp_in_c=0
temp_in_k=0
if n==1:
	temp_in_c = int(input('Enter the temperature in celsius:'))
	temp_in_k = temp_in_c+273
	print(temp_in_k)
elif n==2:
	temp_in_k = int(input('Enter the temperature in kelvin:'))
	temp_in_c = temp_in_k-273
	print(temp_in_c)
else:
	print('Wrong input')