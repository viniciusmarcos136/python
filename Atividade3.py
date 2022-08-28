#Faça uma calculadora que permita o usuário escolher qual operação ele quer fazer

num1 = float(input('Digite um número: '))
num2 = float(input('Digite mais um número: '))
oper = input("Digite um operador: ")
if oper == '+':
    print('A soma entre {} e {} vale {}' .format(num1, num2, num1+num2))
elif oper == '-':
    print('A subtração entre {} e {} vale {}'.format(num1, num2, num1-num2))
elif oper == '/':
    print('A divisão entre {} e {} vale {}'.format(num1, num2, num1/num2))
elif oper == '*':
    print('O produto de {} e {} vale {}'.format(num1, num2, num1*num2))
else:
    print("Nâo possivel fazer esse calculo.")
