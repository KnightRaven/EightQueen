#!/usr/bin/env python

from random import randint
import sys

class Queen:
    def gen_void(self, n):
        self.pos = [None]*n
        self.pos_used = []
        for i in range(n):
            self.pos_used.append([])

    def gen_pos(self, pos, pos_used, i, n):
        while True:
            pos[i] = randint(0, n-1)
            if pos[i] not in pos_used[i]:
                pos_used[i].append(pos[i])
                return True           # There is still a chance.
            elif len(pos_used[i]) == n:
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

    def create(self, i, n):
        while True:
            if self.gen_pos(self.pos, self.pos_used, i, n):
                if self.satisfy(self.pos, i):
                    if i == n-1:
                        print "Congratulation!"
                        break
                    else:
                        return self.create(i+1, n)
                else:
                    return self.create(i, n)
            else:
                if i == 0:
                    print "There is not a way to put them properly."
                    break
                else:
                    self.pos_used[i] = []
                    return self.create(i-1, n)

    def gen_pic(self, n):
        self.gen_void(n)
        i = 0
        self.create(i, n)
        print self.pos
        order = [None]*n
        for k in range(n):
            order[k] = n-1-self.pos[k]
        for l in range(n):
            for m in range(n):
                if l == order[m]:
                    print '*',
                else:
                    print '-',
            print  ' '

if __name__ == "__main__":
    queen = Queen()
    queen.gen_pic(int(sys.argv[1]))
