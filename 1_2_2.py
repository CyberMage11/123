a=True
while a:
	x1=int(input('введите первую координату первой ладьи:'))
	if x1>=1 and x1 <=8:
		a=False
	else:
		print("неверный ввод!")

a=True
while a:
	y1=int(input('ввведите вторую координату первой ладьи:'))
	if y1>=1 and y1 <=8:
		a=False
	else:
		print("неверный ввод!")

a=True
while a:
	x2=int(input('ввведите первую координату второй ладьи:'))
	if x2>=1 and x2 <=8:
		a=False
	else:
		print("неверный ввод!")

a=True
while a:
	y2=int(input('ввведите вторую координату второй ладьи:'))
	if y2>=1 and y2 <=8:
		a=False
	else:
		print("неверный ввод!")


if x1==x2 or y1==y2:
	print('YES')
else:
	print('NO')