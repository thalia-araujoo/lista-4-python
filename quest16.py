#Escreva uma função que receba uma lista de números e retorne a soma de todos
#os elementos.

def calcular_soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

#bloco principal
def main():
    
    lista = []
    
    for num in range(0,10):
        n = int(input("Digite o numero: "))
        lista.append(n)
    print("lista:", lista)
    
    
    r = calcular_soma(lista)
    print("calculo da soma", r)

if __name__=="__main__":
    main()
