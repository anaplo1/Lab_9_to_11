class main(object):
    state = 'A'

    def __init__(self):
        pass

    def erase(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'A'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'B'
            return 9
        else:
            raise KeyError

    def coast(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'B'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        elif self.state == 'H':
            self.state = 'C'
            return 11
        elif self.state == 'A':
            self.state = 'G'
            return 1
        else:
            raise KeyError

o = main()
print(o.erase()) # 0
print(o.erase()) # 2
print(o.coast()) # 3
print(o.coast()) # 4
print(o.erase()) # 7
print(o.erase()) # 2
print(o.coast()) # 3
print(o.erase()) # 4
print(o.coast()) # 6
print(o.erase()) # 8
print(o.coast()) # 10
print(o.coast()) # 11
print(o.coast()) # 3
print(o.coast()) # 5
print(o.coast())
print(o.coast())
print(o.erase()) # 1