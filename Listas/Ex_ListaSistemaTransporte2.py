def calcularVelocidadeMedia(distancia, tempo):
    velocidadeMedia = distancia/tempo
    print("A velociadade média é {} km/h".format(velocidadeMedia))

#Inicio do código
dist = float(input("Informe a distância: "))
temp = float(input("Informe o tempo: "))
#Função definida pela entrada de dados
calcularVelocidadeMedia(dist,temp)
#Função definida pelo programador
calcularVelocidadeMedia(15,2)
