                    # if e else

# Verificando se um aluno é maior de 18 anos e pode participar de uma competição

rm = input("Insira seu RM")
idade = input("Insiria sua idade")

if int(idade) >= 18 :
    print ("Sua participação foi autorizada, aluno de RM {}!".format(rm))
else:
    autorizado = input("Você possui autorização dos responsaveis? S = Sim ou N = Não")
    if autorizado == 'S':
        print("Sua participação foi autorizada")
    else:
        print("Aluno portador do Rm {} consta menor de idade, não sendo autorizado a participação".format(rm))

                    # elif


# Vamos tomar como exemplo uma operadora de celular que concede bônus em consumo da franquia de
# internet dependendo da pontuação dos clientes: clientes que fizerem mais de 1000 pontos recebem 3 GB
# adicionais em sua franquia, clientes que fizerem mais de 500 pontos recebem 1,5 GB adicionais em sua
# franquia, e clientes que fizerem mais de 200 pontos recebem 500 MB adicionais em sua franquia. Os demais
# não recebem nada


pontuacao = input("Insira a pontuação do cliente")
pontuacao = int(pontuacao)

if pontuacao >= 1000:
    print("O cliente tem direito a receber mais 3gb na sua franquia de internet!")
elif pontuacao >= 500:
    print("O cliente tem direito a receber mais 1,5 gb na sua franquia de internet!")
elif pontuacao >= 200:
    print("O cliente tem direito a receber mais 500mb na sua franquia de internet!")
else:
    print("O cliente não receberá bônus")