class TeamIterator:
    def __init__(self, team):
        self.team = team
        self.res = 0 - 1
        self.res_two = 0 - 1


    def __next__(self):
       if self.res + 1 < len(self.team._juniorMembers):
            self.res += 1
            return f'{self.team._juniorMembers[self.res]}, "junior" '
       elif len(self.team._juniorMembers) <= self.res + 1 < (len(self.team._juniorMembers) + len(self.team._seniorMembers)):
            self.res_two += 1
            self.res += self.res_two
            return f' {self.team._seniorMembers[self.res_two]}, "senior" '
       else:
           raise StopIteration



class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """
    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __len__(self):
        return (len(self._seniorMembers) + len(self._juniorMembers))

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])
    print(team)
    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)
    #
    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

