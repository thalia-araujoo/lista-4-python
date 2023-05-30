#Implemente uma fila simples e as operações básicas: inserir, remover e mostrar o elemento da frente.

class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_item = Item(value)
        if self.is_empty():
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def get_size(self):
        return self.size


f = Queue()
for i in range(5):
    n = input("Digite um numero: ")
    f.enqueue(n)
print("O elemento da frente é: ")
print(f.head.value)
print("O elemento removido é: ")
print(f.dequeue())


