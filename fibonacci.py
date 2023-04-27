num = int(input("Informe um número inteiro: "))

fib1 = 0
fib2 = 1

# Inicializa uma variável que irá guardar o próximo valor da sequência
proximo_fib = fib1 + fib2


while proximo_fib <= num:

    if proximo_fib == num:

        print(f"O número {num} pertence à sequência de Fibonacci.")
        break

    # Atualiza os valores das variáveis para o próximo passo da sequência
    fib1 = fib2
    fib2 = proximo_fib
    proximo_fib = fib1 + fib2
else:

    print(f"O número {num} não pertence à sequência de Fibonacci.")
