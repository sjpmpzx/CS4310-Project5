class FIFOCache(object):

    def __init__(self, capacity=0xffffffff):
        self.F = capacity
        self.M = []

    def get(self, page):

        if page in self.M:
            return page
        else:
            if len(self.M) >= self.F:
                old_page = self.M[0]
                self.M = self.M[1:]

            self.M.append(page)

            return None   # if : return == None -> Then :page faults

    def print(self):
        for i in range(0,len(self.M)):
            print(self.M[len(self.M)-1-i])


# test
fifo = FIFOCache(3)
print(fifo.get(3))
print(fifo.get(5))
print(fifo.get(2))
print(fifo.get(1))
print(fifo.get(2))
print(fifo.get(6))


