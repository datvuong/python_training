import random
from card import Card


class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    def build(self):
        '''Tạo bộ bài'''
        all_rank = ('A',2,3,4,5,6,7,8,9)
        all_suit = ('♠', '♣', '♦', '♥')
        self.all_card = []
        for r in all_rank:
            for s in all_suit:
                self.all_card.append(Card(r,s))

    def shuffle_card(self):
        '''Trộn bài'''
        random.shuffle(self.all_card)

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        dealed_card = self.all_card.pop()
        return dealed_card


if __name__=='__main__':
    d = Deck()
    d.build()
    print(d.all_card[30])
    d.all_card[30]
    d.shuffle_card()
    [x for x in d.all_card]
    d.deal_card()
