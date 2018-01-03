enter = input()
a = float(enter.split()[0])
b = float(enter.split()[-1])

PI =3.14159265359

half_a = PI*(a)**2
half_b = PI*(b)**2
if float(half_b/half_a) >= 1:
	print(0)
else:
	print(float(half_b/half_a)*100)