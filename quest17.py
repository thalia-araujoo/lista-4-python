#Implemente uma função que receba uma lista de strings e retorne uma nova lista contendo apenas
#as strings que possuem mais de 5 caracteres.

def filtrar_strings(lista):
    nova_lista = []
    for palavra in lista: 
        if len(palavra) >= 5:
            nova_lista.append(palavra)
    return nova_lista

def main():
    lista = []
    
    for recebe in range(0,10):
        strings = str(input("Digite uma palavra: "))
        lista.append(strings)
    resultado = filtrar_strings(lista)
    print("Strings com mais de 5 caracteres:", resultado)

if __name__=="__main__":
    main()
    