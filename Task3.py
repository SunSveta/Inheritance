
class MyList(list):

    def __init__(self, newlist):
        super().__init__()
        self.newlist = newlist
        print("Работает магический метод __init__")

    def __str__(self):
        super().__str__()
        print("Работает магический метод __str__")
        return f'{self.newlist}'

    def __iter__(self):
        self.value = 0 - 1
        print("Работает магический метод __iter__")
        return MyList(self)

    def __len__(self):
        super().__len__()
        print("Работает магический метод __len__")
        return len(self.newlist)

    def __getitem__(self, item):
        print("Работает магический метод __getitem__")
        return self.newlist[item]

    def __setitem__(self, key, value):
        self.newlist[key] = value
        print("Работает магический метод __setitem__")


lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))
