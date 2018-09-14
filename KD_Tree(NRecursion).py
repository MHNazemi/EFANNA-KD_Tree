import random
from numpy import median


class Tree:
    def __init__(self, points, dim, k):
        self.p = points
        self.d = dim
        self.k = k
        self.root = self.__st(points)

    def __st(self, p):

        st = []
        root = Node(None, None, None, None, p)
        st.append(root)

        while len(st) > 0:
            n = st.pop()
            if (n.ps.__len__() <= self.k):
                n.l = True
                continue

            l = []
            r = []

            _d = random.randint(0, self.d-1)
            p_d = [x[_d] for x in n.ps]
            mid = int(median(p_d))
            n.v = mid
            n.d = _d
            n.p_d = p_d
            for p_ in n.ps:
                if p_[n.d] <= n.v:
                    l.append(p_)
                else:
                    r.append(p_)

            del n.ps
            n_l = Node(None, None, n, None, l)
            n_r = Node(None, None, n, None, r)
            n.c_l = n_l
            n.c_r = n_r

            st.append(n_l)
            st.append(n_r)

        return root


class Node:
    def __init__(self, value, title, parent, dim, points):
        self.v = value
        self.t = title
        self.p = parent
        self.d = dim
        self.ps = points
        self.c_r = None
        self.c_l = None
        self.l = False


def main():
    l = []
    for i in range(36100):
        i = []
        for j in range(25):
            i.append(random.randint(0, 255))

        l.append(i)

    import time
    t_s = time.time()
    for i in range(200):
        t = Tree(l, 25, 10).root
    t_e = time.time()
    print(t_e - t_s)


main()
