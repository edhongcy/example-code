from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 顯示數字（沒有透過 repr 顯示返回的値是 type）
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # 算斜邊長
    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # 兩個向量相加
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# repr & srt 差別
# __repr__ goal is to be unambiguous
# __str__ goal is to be readable
