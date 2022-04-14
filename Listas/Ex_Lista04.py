#Ordenando lista
valores = [1,3,5,6,7,7,8,10,21,45,12,56,76,4,7]
#Exibindo lista
print("Os números que estão na lista é: {}".format(valores))

#Contagem dos elementos
# count() - retorna a quantidade de vezes que um elemento aparece na lista
contagem = valores.count(7)
print("Nessa lista o número 7 aparece {} vezes".format(contagem))

#Ordem revesa
valores.reverse()
print("Lista em valor reverso: {}".format(valores))

#Ordenada crescente
valores.sort()
print("Lista em valor crescente: {}".format(valores))