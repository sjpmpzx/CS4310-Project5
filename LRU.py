from RS_Reader import read_rs_from_file
from queue import Queue

class PageQueue():
    'Implementation of the page queue.'
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self.content = []
        self.page_falut_count = 0

    def enqueue(self, data: int):
        # If a resident page p is referenced, p is moved to the end of the queue.
        if data in self.content:
            self.content.remove(data)
            self.content.append(data)
        # If a non-resident page p is referenced, p is moved to the end of the queue 
        # and the least recently referenced page q at the head of the queue is removed.      
        else:
            self.page_falut_count += 1
            if len(self.content) == self.maxsize:
                self.content = self.content[1:]
                self.content.append(data)
            else:
                self.content.append(data)

RS = read_rs_from_file()
page_queue = PageQueue(5)

for p in RS:
    page_queue.enqueue(p)

print(page_queue.page_falut_count)
