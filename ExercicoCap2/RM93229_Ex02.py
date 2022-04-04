#Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives.
# Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana
# (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

seg = int(0)
ter = int(0)
qua = int(0)
qui = int(0)
sex = int(0)
contador = int(0)
maxVotacao = int(0)

while contador != 1:
    contador = int(input("\n Vote nas melhores datas de live: 2 = Segunda, 3 = Terça, 4 = Quarta, 5 = Quinta, 6 = Sexta. Para encerrar a votação digite 1: "))
    if contador == 2:
        seg+= 1
        print("\nVocê votou para live ocorrer na segunda")
    elif contador == 3:
        ter+= 1
        print("\nVocê votou para live ocorrer na terça")
    elif contador == 4:
        qua += 1
        print("\nVocê votou para live ocorrer na quarta")
    elif contador == 5:
        qui+= 1
        print("\nVocê votou para live ocorrer na quinta")
    elif contador == 6:
        sex+= 1
        print("\nVocê votou para live ocorrer na sexta")
else:
    print("Votação encerrada! ")

    if seg > ter and seg > qua and seg > qui and seg > sex:
        print("A data escolhida foi Segunda com a votação de {} números".format(seg))
    elif ter > seg and ter > qua and ter > qui and ter > sex:
        print("A data escolhida foi Terça com a votação de {} números".format(ter))
    elif qua > seg and qua > ter and qua > qui and qua > sex:
        print("A data escolhida foi Quarta com a votação de {} números".format(qua))
    elif qui > seg and qui > ter and qui > qua and qui > sex:
        print("A data escolhida foi Quinta com a votação de {} números".format(qui))
    elif sex > seg and sex > ter and sex > qua and sex > qui:
        print("A data escolhida foi Sexta com a votação de {} números".format(sex))
    else:
        print("\nOps um impate! É necessário iniciar a votação novamente até que somente uma data seja escolhida")

