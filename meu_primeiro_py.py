def adicionar(x, y):
    """Esta função soma dois números"""
    return x + y

def subtrair(x, y):
    """Esta função subtrai dois números"""
    return x - y

def multiplicar(x, y):
    """Esta função multiplica dois números"""
    return x * y

def dividir(x, y):
    """Esta função divide dois números"""
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    return x / y

def calculadora():
    """Função principal que executa a calculadora"""
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    while True:
        # Pede ao usuário para escolher uma opção
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        # Verifica se a escolha é uma das opções válidas
        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")
                continue

            if escolha == '1':
                print(num1, "+", num2, "=", adicionar(num1, num2))

            elif escolha == '2':
                print(num1, "-", num2, "=", subtrair(num1, num2))

            elif escolha == '3':
                print(num1, "*", num2, "=", multiplicar(num1, num2))

            elif escolha == '4':
                print(num1, "/", num2, "=", dividir(num1, num2))
            
            # Pergunta se o usuário quer fazer outro cálculo
            proximo_calculo = input("Deseja fazer outro cálculo? (sim/não): ")
            if proximo_calculo.lower() != 'sim':
                break
        
        elif escolha == '5':
            print("Obrigado por usar a calculadora!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    calculadora()