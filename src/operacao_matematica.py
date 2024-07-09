numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

numero1 = abs(numero1)
numero2 = abs(numero2)

operacao = input("Escolha a operação (soma, subtracao, multiplicacao, divisao): ").strip().lower()

if operacao == "soma":
    resultado = numero1 + numero2
    print(f"Resultado da soma: {resultado}")
elif operacao == "subtracao":
    resultado = abs(numero1 - numero2)
    print(f"Resultado da subtração: {resultado}")
elif operacao == "multiplicacao":
    resultado = (numero1 * numero2)
    print(f"Resultado da multiplicação: {resultado}")
elif operacao == "divisao":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Divisão por zero não é permitida")
else:
    print("Operação inválida")
