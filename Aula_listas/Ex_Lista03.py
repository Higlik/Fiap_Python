jedi = ["Yoda","Luke","Obi-Wan","Anakin"]
#Removendo o ultimo nome da lista
jedi.pop()
for nome in jedi:
    print(nome)
print("-----")
#Removendo um índice especifíco
jedi.pop(1)
for nome in jedi:
    print(nome)
print("----------")
#Removendo o valor direto
jedi.remove("Yoda")
for nome in jedi:
    print(nome)
