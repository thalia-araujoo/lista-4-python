#Crie uma função que receba duas listas de números e retorne uma nova lista contendo
#apenas os elementos que estão presentes em ambas as listas.

#criei uma função que cria duas listas
def elementos(lista1, lista2):
    nova_lista = [] # nova lista para add os numeros iguais
    for elemento in lista1:   #for para os elementos na lista1
        if elemento in lista2:  # if para verificar se tem na lista2
            nova_lista.append(elemento)   #se tiver ele add na nova lista
    return nova_lista   

def main():
    lista1 = []
    for i in range (1,6):
        n = int(input("Digite um numero: "))
        lista1.append(n)
    print("lista1: ", lista1)
    
    lista2 = []
    for i in range (1,6):
        n = int(input("Digite um numero: "))
        lista2.append(n)
    print("lista2: ", lista2)

    #chamo a função
    resultado = elementos(lista1, lista2)
    print("Elementos comuns nas duas listas:", resultado)

if __name__=="__main__":
    main()