def calcularVelocidadeMedia(distancia, tempo):
    velocidadeMedia = distancia/tempo
    return velocidadeMedia

dist = float(input("Informe a distância: "))
temp = float(input("Informe o tempo: "))

print("A velocidade média é {}".format(calcularVelocidadeMedia(dist, temp)))