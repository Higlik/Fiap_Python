#importando calculadora
import CalculadoraSimples

#Inserindo valores
valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")
digito = 0

while digito != 5:
    print("Digite o número para realizar a equação")
    digito = int(input("\n-1 Somar \n-2 Subitrair \n-3 Multiplicar \n-4 Dividir \n- Digite qualquer numero para sair do sistema: "))
    if digito == 1:
        soma = CalculadoraSimples.somar(valor1,valor2)
        print(soma)
        break
    elif digito == 2:
        soma = CalculadoraSimples.subtrair(valor1,valor2)
        print(soma)
        break
    elif digito == 3:
        soma = CalculadoraSimples.multiplicar(valor1,valor2)
        print(soma)
        break
    elif digito == 4:
        soma = CalculadoraSimples.dividir(valor1,valor2)
        print(soma)
        break
    else:
        digito = 5
        print("Sistema encerrado")
