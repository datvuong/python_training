from deck import Deck
from player import Player

class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.deck.build()
        self.in_game = False

    def setup(self, n=2):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        self.n_players = n
        for i in range(n):
            player_name = input('Tên người chơi:')
            self.players.append(Player(player_name))

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        if self.in_game:
            in_game = "Đang chơi"
            dealed = 'Đã chia'
            flip_card = 'Có thể lật bài'
        else:
            in_game = "Có thể thêm"
            dealed = 'Có thể chia'
            flip_card = 'Chưa chia bài'
        
        if self.n_players > 2:
            rm_player = "Có thể loại"
        else:
            rm_player = "Số người chơi tối thiểu rồi"
        print(f"1. Danh sách người chơi ({self.n_players})")
        print(f"2. Thêm người chơi ({in_game})")
        print(f"3. Loại người chơi ({rm_player})")
        print(f"4. Chia bài ({dealed})")
        print(f"5. Lật bài ({flip_card})")
        print(f"6. Xem lại game vừa chơi")
        print(f"7. Xem lịch sử chơi game")
        print(f"8. Công an tới, tốc biến")

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print(f"{'ID':5} {'Name':23}")
        for i, p in enumerate(self.players, start=1):
            print(f'{i:5} {p.name:23}')

    def add_player(self):
        '''Thêm một người chơi mới'''
        player_name = input('Tên người chơi: ')
        self.players.append(Player(player_name))

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        self.list_players()
        if len(self.players) > 2:
            player_id = int(input('ID của người chơi: ')) - 1
            self.players.pop(player_id)
        else:
            print('Số lượng người chơi tối thiểu')

    def deal_card(self):
        '''Chia bài cho người chơi'''
        if self.in_game:
            print('Đã chia bài')
        else:
            self.in_game = True
            self.deck.shuffle_card()
            for i in range(3):
                for p in self.players:
                    p.add_card(self.deck.deal_card())

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        for p in self.players:
            p.flip_card()

if __name__ == "__name__":
    g = Game()
    g.players
    g.setup(3)
    g.guide()
    g.list_players()
    g.add_player()
    g.remove_player()
    g.deal_card()
    g.flip_card()
    [p.flip_card() for p in g.players]