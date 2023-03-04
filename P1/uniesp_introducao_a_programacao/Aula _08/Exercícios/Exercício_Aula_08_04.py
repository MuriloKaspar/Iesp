#O IMC -Índice de Massa Corporal- é um critério da Organização Mundial da Saudade para indicar a condição de peso de uma pessoa.
#A fórmula é IMC = peso / (altura)².
#Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição.
# _________________ ________________
#|                 |                |
#|  MC em adultos  |    Condição    |
#|_________________|________________|
#| abaixo de 18,5  | abaixo do peso |
#| entre 18,5 e 25 |   peso normal  |
#|    25 e 30      | acima do peso  |
#|  acima de 30    |     obeso      |
#|_________________|________________|


print('Digite os respectivos valores de seu peso e altura, descubra seu IMC e como você está classificado =)')
print('Ao digitar os valores utilize . no lugar da , ')
peso=float(input('Digite seu peso (Kg)'))
altura=float(input('Digite sua altura (m)'))
imc=peso/(altura**2)

print(f'seu imc é {imc:,.2f}')

if imc < 18.5:
    print('Você está abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print('Você está no peso normal')

elif imc >=25 and imc < 30:
    print('Você está acima do peso')

else:
    print('Você está Obeso')