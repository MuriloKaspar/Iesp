#Faça um programa que receba um número e que calcule e mostre a tabuada desse número..

num = int(input("Por favor, insira um numero: "))

for t in range(1, 11):
    resultado = num * t
    print (f' {num} x {t} = {resultado}')