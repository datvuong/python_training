class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    ALL_RANK = {'A':1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
    ALL_SUIT = {'♠':1, '♣':2, '♦':3, '♥':4}
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.point = self.__class__.ALL_RANK.get(self.rank)

    def __repr__(self):
        '''Hiển thị lá bài'''
        return f'{self.rank}{self.suit}'

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        if self.__class__.ALL_SUIT.get(self.suit) > self.__class__.ALL_SUIT.get(other.suit):
            return True
        elif self.__class__.ALL_SUIT.get(self.suit) == self.__class__.ALL_SUIT.get(other.suit):
            if self.__class__.ALL_RANK.get(self.rank) > self.__class__.ALL_RANK.get(other.rank):
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    c1 = Card(4,'♠')
    c2 = Card(9,'♥')
    c3 = Card(8,'♥')
    c1>c2
    c3<c2
    print(c1)