#Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria:
# um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade.
# O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado
# por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente,
# o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.
# A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

# Nível  /  Porcentagem sobre o faturamento

# Basic 30% / Silver 20% / Gold 10% / Platinum 5%


basic = float(0.30)
silver = float(0.20)
gold = float(0.10)
platinum = float(0.05)
bonus = float

valorRecebido = float(input("Insira o faturamento anual: "))

nivelAssinatura = input("Insira a assinatura: B = Basic, S = Silver, G = Gold, P = Platinum ")
nivelAssinatura = nivelAssinatura.upper()

if nivelAssinatura == 'B':
    bonus = valorRecebido * basic
    print("Com o plano Basic o bonus que irá receber é no valor de {}".format(bonus))
elif nivelAssinatura == 'S':
    bonus = valorRecebido * silver
    print("Com o plano Silver o bonus que irá receber é no valor de {}".format(bonus))
elif nivelAssinatura == 'G':
    bonus = valorRecebido * gold
    print("Com o plano Gold o bonus que irá receber é no valor de {}".format(bonus))
elif nivelAssinatura == 'P':
    bonus = valorRecebido * platinum
    print("Com o plano Platinum o bonus que irá receber é no valor de {}".format(bonus))
else:
    print("Dados informados estão invalidos, inserir novamente!")



