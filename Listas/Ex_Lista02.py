#Criando lista
jedi = ["Yoda","Luke","Obi-Wan", "Anakin"]
#Inserido um novo valor no final da lista
jedi.append("Mace Windu")

#Usando loop para printar toda a lista

for nome in jedi:
    print(nome)

print("----------")

#inserido um novo jedi na lista
jedi.append(input("Digite o nome do novo jedi: "))

for nome in jedi:
    print(nome)

print("-------------")
#Inserido um novo valor na lista apartir de um índice existente
jedi.insert(1,"Darthvader")

for nome in jedi:
    print(nome)

print("--------")

#Inserindo apartir de um imput

jedi.insert(0,input("Digite o novo jedi subistituto: "))

for nome in jedi:
    print(nome)