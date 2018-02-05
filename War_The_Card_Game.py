# War the card game

from random import shuffle

class Card:

    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v

class Deck:

    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:

    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:

    def __init__(self):
        name1 = input("Player 1. Enter name now: ")
        name2 = input("Player 2. Enter name now: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!!")
        while len(cards) >= 2:
            message = "Press q or Q to quit. Any " + " key to play"
            response = input(message)
            if response == 'q' or response == 'Q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.player1.name
            p2n = self.player2.name
            self.draw(p1n,p1c,p2n, p2c)
            if p1c > p2c:
                self.player1.wins += 1;
                self.wins(self.player1.name)
            else:
                self.player2.wins += 1;
                self.wins(self.player2.name)

        win = self.winner(self.player1, self.player2)

        print("War is over!! {} wins!!!".format(win))

    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "It was a tie!!"

game = Game()
game.play_game()

    
        
