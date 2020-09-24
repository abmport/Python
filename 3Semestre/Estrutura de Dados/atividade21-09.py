class Pilha:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise Exception('Pilha Vazia')
        return self.items.pop()
    def top(self):
        if self.is_empty():
            raise Exception('Pilha Vazia')
        return self.items[-1]
    def __len__(self):
        return len(self.items)