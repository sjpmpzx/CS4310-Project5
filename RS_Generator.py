import random

def gen_rs(e:int, t:float, P=2**20, s=0,  m=200):
    '''
    P: virtual memory size
    s: starting location
    e: size of L
    m: rate if motion
    t: probability of transition
    '''
    RS_length = 20

    with open('RS.csv', 'w', encoding='utf-8') as f:
        # repeat until RS of desired length is generated
        for _ in range(RS_length):
            RS = []

            # (Process is executing within current locus)
            # select m random numbers in the range [s:s+e]
            for _ in range(m):
                tmp_num = random.randrange(s, s + e + 1)
                # append the numbers to RS
                RS.append(tmp_num)  

            # generate random number r in the range [0:1]
            r = random.uniform(0, 1)    
            if r < t:
                # (Process moves to a new location, s, within [0:P-1])
                s = random.randrange(0, P)
            else:
                # (Process remains within current locus)
                s = (s + 1) % P

            f.write(','.join(str(x) for x in RS) + ',')     

# if __name__ == '__main__':
#     gen_rs(e=10, t=0.001)
