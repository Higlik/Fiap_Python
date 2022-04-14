#Funçao que calcula a velocidade média
def calcularVelocidadeMedia():
    #Solicitar distância de tempo
    distancia = float(input("Digite a distância percorrida: "))
    tempo = float(input("Digite o tempo da viagem: "))
    #Calcula a velocidade média
    velocidadeMedia = distancia/tempo
    print("A velociade média é {} km/h".format(velocidadeMedia))

#Aqui começa o programa
calcularVelocidadeMedia()