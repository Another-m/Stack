class Stack:
    # Необходимо реализовать класс Stack со следующими методами:
    # isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    # size - возвращает количество элементов в стеке.

    def __init__(self):
        self.stack = []

    def prnt(self, *args):
        if args: print(args)
        else: print(self.stack)

    def isEmpty(self):
        # Если стэк пуст - True, если заполнен - False

        if self.stack == []:
            self.is_empty = True
        else:
            self.is_empty = False
        return self.is_empty

    def push(self, element):
        self.stack.append(element)
        return f"Добавлен элемент {element}"

    def pop(self):
        if self.size() != 0:
            self.last_el = self.stack.pop()
            return f"Удален последний элемент {self.last_el}"

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def create_str(self):
        # Ввести строку из символов, которая создаст стэк ввиде списка

        self.creat = input("Введите строку ")
        self.stack = list(''.join(self.creat))
        return f"Создан стэк {self.stack}"

    def checking_brackets(self):
        # Проверка сбалансированности скобок

        self.create_str()
        self.open_brackets = ('(', '[', '{')
        self.closed_brackets = (')', ']', '}')
        self.temp_stack = self.stack
        self.stack = []
        for element in self.temp_stack:
            if element in self.open_brackets:
                self.push(element)
            if element in self.closed_brackets:
                try:
                    self.ind = self.open_brackets.index(self.peek())
                    if element == self.closed_brackets[self.ind]:
                        self.pop()
                    else: self.push(element)
                except: self.push(element)

        if self.isEmpty(): return self.prnt("OK")
        else: return self.prnt("Неверная расстановка скобок")


if __name__ == '__main__':

    check_empty = Stack()
    check_empty.checking_brackets()
