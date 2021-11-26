from game import Game

def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    g = Game()
    menu = '0'
    while menu != '8':
        if menu == '0':
            n_player = int(input('>Số người chơi:'))
            g.setup(n_player)
        g.guide()
        menu = input('>')
        if menu == '1':
            g.list_players()
        if menu == '2':
            g.add_player()
        if menu == '3':
            g.remove_player()
        if menu == '4':
            g.deal_card()
        if menu == '5':
            g.flip_card()
    quit()


if __name__ == '__main__':
    main()
