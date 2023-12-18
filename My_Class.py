class MyNewList:
    def __init__(self):
        self.my_list = []

    def show_my_list(self):
        print("spisok" , self.my_list)

    def add_new(self, element):
        self.my_list.append(element)

    def delete(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
        else:
            print("net v spiske")

    def length(self):
        return len(self.my_list)

    def clear(self):
        self.my_list = []
        print("chisto")


spisok = MyNewList()
spisok.add_new(1)
spisok.add_new(2)
spisok.add_new(5)
spisok.add_new(8)
spisok.show_my_list()
spisok.delete(4)
spisok.delete(1)
spisok.show_my_list()
print(spisok.length())
spisok.clear()


