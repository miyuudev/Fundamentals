"""
1. Validador de CPF Japonês (MyNumber simplificado)

Crie um programa que receba uma string representando um número de identificação (12 dígitos) e:

Verifique se contém apenas números.

Valide o comprimento (12 dígitos).

Retorne “Válido” ou “Inválido”.

💡 Desafio extra: implemente uma função que gera um número aleatório válido.
"""

myNumber = input("Digite seu numero de identidade: ")
if myNumber.isdigit():
    if len(myNumber) == 12:
        print("Valido")
    else:
        print("Nao ha 12 digitos")
else:
    print("Invalido: deve conter apenas numeros")