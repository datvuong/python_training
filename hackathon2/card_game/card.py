class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    ALL_RANK = {'A':1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
    ALL_SUIT = {'S':0, 'C':1, 'D':2, 'H':3}
    ICONS = {'S':'♠', 'C':'♣', 'D':'♦', 'H':'♥'}
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.point = Card.ALL_RANK.get(self.rank)
        # self.suit_point = Card.ALL_SUIT.get(self.suit)
        self.icon = Card.ICONS.get(self.suit)

    def __repr__(self):
        '''Hiển thị lá bài'''
        return f'{self.rank}{self.icon}'

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        if Card.ALL_SUIT.get(self.suit) > Card.ALL_SUIT.get(other.suit):
            return True
        elif Card.ALL_SUIT.get(self.suit) == Card.ALL_SUIT.get(other.suit):
            if Card.ALL_RANK.get(self.rank) > Card.ALL_RANK.get(other.rank):
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    c1 = Card(4,'S')
    c2 = Card('A','H')
    c3 = Card(8,'H')
    c1>c2
    c3<c2
    print(c1)