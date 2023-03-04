#Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C),
# sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).

print('Equação do 2° grau.')
print('x²-x+1=0, a = x², b = x, c = 1')

a = int(input('De valor à a: '))
b = int(input('De valor à b: '))
c = int(input('De valor à c: '))

print('A formula é (b*b - 4*a*c)')

delta = b*b-4*a*c

print(f'Delta é {delta}')
print('Resultado de x1 e x2')

x = (-b - (delta)**(1/2))/(2*a)
x1 = (-b + (delta)**(1/2))/(2*a)

print(f'x1 = {x1}, x2 = {x}')