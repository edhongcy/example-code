import collections

# namedtuple define Card
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # 起始化牌堆
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    # 用 len 計算 list 個數
    def __len__(self):
        return len(self._cards)
    # 從 postition 去找牌花色及數字
    def __getitem__(self, position):
        return self._cards[position]

