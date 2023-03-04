# Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano, P(x1, y1) e Q(x2, y2),
# imprima a distância entre eles. A formula que efetua tal cálculo é: d = raiz quadrada de (x2 - x1)² + (y2 - y1)²

print('Calcular a distancia entre dois pontos')
print('Raiz quadrada de (x2 - x1)² + (y2 - y1)²')

x1 = int(input('De valor à x1: '))
x2 = int(input('De valor à x2: '))
y1 = int(input('De valor à y1: '))
y2 = int(input('De valor à y2: '))

d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
#o .2f é um formato flutuante q mostra até 2 casa apos o ponto da função
print(f"A distancia entre os pontos é de {d:.2f} metros.")