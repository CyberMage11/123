a=int(input('введите а:'))
b=int(input('введите b:'))
c=int(input('введите c:'))

if a==b & a==c:
	print(3)
elif a==b or a==c or c==b:
	print(2)
else:
	print(0)