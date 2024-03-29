class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self, name):  # dễ
        self.name = name
        self.user_cards = []

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        total_points = sum([c.point for c in self.user_cards])
        return total_points

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        highest_card = max(self.user_cards)
        return highest_card

    def __gt__(self, other):
        '''So sánh 2 players'''
        return (self.point > other.point) or (self.point == other.point and self.biggest_card > other.biggest_card)
    
    def add_card(self, user_card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.user_cards.append(user_card)

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.user_cards.clear()

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        highest_card = str(self.biggest_card)
        list_cards = ' '.join([str(c) for c in self.user_cards])
        total_points = str(self.point)
        print(f'Bài {self.name}: {list_cards}; Tổng điểm: {total_points}; Lá bài lớn nhất: {highest_card}')


if __name__=='__main__':
    from deck import Deck
    d = Deck()
    d.build()
    d.shuffle_card()
    d.all_card[1].point
    p1 = Player('Dat')
    p1.add_card(d.deal_card())
    p2 = Player('abd')
    p2.add_card(d.deal_card())
    p1.remove_card()
    p1.point
    p1.user_cards
    p2.point
    p2.user_cards
    p1.biggest_card
    p1 < p2
    p2.flip_card()