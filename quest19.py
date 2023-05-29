#Implemente uma função que receba uma lista de palavras e retorne
#a palavra mais longa presente na lista.

def palavra_longa(lista_palavra):
    palavra1 = ""
    
    for palavra in lista_palavra:
        if len(palavra) > len(palavra1):
            palavra1 = palavra
        return palavra1

def main():
    lista_p = []
    
    for recebe in range(1,6):
        p = str(input("Digite uma palavra: "))
        lista_p.append(p)
        
    res = palavra_longa(lista_p)
    print("Palavra mais longa: ", res)
    
    
    
    
    
if __name__=="__main__":
    main()