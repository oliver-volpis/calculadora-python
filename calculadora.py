def calculadora():
    print("Seja Bem-Vindo a Calculadora em Python!")

    opcao = int(input('''Escolha uma Operação:

Digite 1 Para + (Somar).
Digite 2 Para - (Subtrair).
Digite 3 Para * (Multiplicar).
Digite 4 Para / (Dividir).
Digite 5 Para % (Resto de Divisão).

Digite a Operação: '''))

    if opcao == 1:
        num1 = int(input('Digite um primeiro número: '))
        num2 = int(input('Digite um segundo número: '))
        print(f"O resultado da soma de {num1} e {num2} é {num1 + num2}")
    elif opcao == 2:
        num1 = int(input('Digite um primeiro número: '))
        num2 = int(input('Digite um segundo número: '))
        print(f"O resultado da subtração de {num1} e {num2} é {num1 - num2}")
    elif opcao == 3:
        num1 = int(input('Digite um primeiro número: '))
        num2 = int(input('Digite um segundo número: '))
        print(f"O resultado da multiplicação de {num1} e {num2} é {num1 * num2}")
    elif opcao == 4:
        num1 = int(input('Digite um primeiro número: '))
        num2 = int(input('Digite um segundo número: '))
        print(f"O resultado da divisão de {num1} e {num2} é {num1 / num2}")
    elif opcao == 5:
        num1 = int(input('Digite um primeiro número: '))
        num2 = int(input('Digite um segundo número: '))
        print(f"O resultado do resto da divisão de {num1} e {num2} é {num1 % num2}")
    else:
        print("Opção inválida! Tente novamente.")

calculadora()
