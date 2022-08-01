a=True
while a:
	password=input('ВВедите пароль:')
	low=False
	high=False
	for c in password:
		if c.islower():
			low=True
		elif c.isupper():
			high=True

	if len(password)<=8: 
		print('Мало символов')

	elif low==False:
		print('Нет прописных букв')
	elif high==False:
		print('Нет заглавных букв')
	else:
		a=False
		

print('пароль ok')