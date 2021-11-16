from RS_Reader import read_rs_from_file

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
RS = read_rs_from_file()
fifo = FIFOCache(5)

page_falut_count = 0
for p in RS:
    ret = fifo.get(p)
    if ret == None:
        page_fault_count++

print(page_falut_count)
