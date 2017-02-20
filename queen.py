#!/usr/bin/env python

from random import randint
import sys

class Queen:
    def __init__(self, n):
        self.n = n
        self.pos = [None] * n
        self.pos_used = []
        for i in range(n):
            self.pos_used.append([])

    def gen_pos(self, pos, pos_used, i):
        while True:
            pos[i] = randint(0, self.n-1)
            if pos[i] not in pos_used[i]:
                pos_used[i].append(pos[i])
                return True           # There is still a chance.
            elif len(pos_used[i]) == self.n:
                return False         # Seriously, you should give up.

    def satisfy(self, pos, i):
        for k in range(i):
            if pos[k] == pos[i]:
                return False
            if pos[k]-k == pos[i]-i:
                return False
            if pos[k]+k == pos[i]+i:
                return False
        return True

    def create(self, i):
        while True:
            if self.gen_pos(self.pos, self.pos_used, i):
                if self.satisfy(self.pos, i):
                    if i == self.n-1:
                        print "Congratulation!"
                        break
                    else:
                        return self.create(i+1)
                else:
                    return self.create(i)
            else:
                if i == 0:
                    print "There is not a way to put them properly."
                    break
                else:
                    self.pos_used[i] = []
                    return self.create(i-1)

    def gen_pic(self):
        i = 0
        self.create(i)
        print self.pos
        order = [None]*self.n
        for k in range(self.n):
            order[k] = self.n-1-self.pos[k]
        for l in range(self.n):
            for m in range(self.n):
                if l == order[m]:
                    print '*',
                else:
                    print '-',
            print  ' '

if __name__ == "__main__":
    queen = Queen(int(sys.argv[1]))
    queen.gen_pic()
