# Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes.
# Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos,
# solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada
# (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar,
# ao final, qual delas teve a maior nota.

# Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:

# VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

# POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.


#Soma o valor da nota
somaAlunoImpar = int(0)
somaAlunoPar = int(0)

#Aguarda para realizar o cálculo da média
mediaPar = int(25)
mediaImpar = int(25)

#Alem de mostra a nota do aluno irá ser utilizado para somar com SomaAluno*
mostraNota = int(0)

#Usado no laço while para poder realizar a contagem da sala
contSalaImpar = int(50)
contSalaPar = int(50)

#Usado no laço while para separar os alunos conforme impar ou par
contAlunoPar = int(50)
contAlunoImpar = int(50)



while contSalaImpar != 0:
    if contAlunoImpar % 2 == 1:
      mostraNota = int(input("\nInsira a nota do aluno número {}: ".format(contAlunoImpar)))
      print("A nota do aluno número {} é: {}".format(contAlunoImpar,mostraNota))
      somaAlunoImpar += mostraNota
    contSalaImpar -= 1
    contAlunoImpar -= 1

#Realiza a soma da média
mediaImpar = somaAlunoImpar / mediaImpar



while contSalaPar != 0:
    if contAlunoPar % 2 == 0:
        mostraNota = int(input("\nInsira a nota do aluno número {}: ".format(contAlunoPar)))
        print("A nota do aluno número {} é: {}".format(contAlunoPar, mostraNota))
        somaAlunoPar += mostraNota
    contSalaPar -= 1
    contAlunoPar -= 1

#Realiza a soma da média
mediaPar = somaAlunoPar / mediaPar


#Mostra o resultado final
if mediaImpar > mediaPar:
    print("\nOs alunos com números impares tem a média maior, o resultado é {}. Enquanto isso a turma par tem a média de {}.".format(mediaImpar,mediaPar))
else:
    print("\nOs alunos com números pares tem a média maior, o resultado é {}. Enquanto isso a turma impar tem a média de {}.".format(mediaPar,mediaImpar))






