from RS_Generator import gen_rs
import LRU
import FIFO

# gen_rs(e=10, t=0.05, path='RS_e10_t0.05.csv')
# gen_rs(e=10, t=0.001, path='RS_e10_t0.001.csv')
# gen_rs(e=10, t=0.0005, path='RS_e10_t0.0005.csv')
# gen_rs(e=15, t=0.05, path='RS_e15_t0.05.csv')
# gen_rs(e=15, t=0.001, path='RS_e15_t0.001.csv')
# gen_rs(e=15, t=0.0005, path='RS_e15_t0.0005.csv')
# gen_rs(e=50, t=0.05, path='RS_e50_t0.05.csv')
# gen_rs(e=50, t=0.001, path='RS_e50_t0.001.csv')
# gen_rs(e=50, t=0.0005, path='RS_e50_t0.0005.csv')

# LRU.test('RS_e10_t0.05.csv')
# LRU.test('RS_e10_t0.001.csv')
# LRU.test('RS_e10_t0.0005.csv')
# LRU.test('RS_e15_t0.05.csv')
# LRU.test('RS_e15_t0.001.csv')
# LRU.test('RS_e15_t0.0005.csv')
# LRU.test('RS_e50_t0.05.csv')
# LRU.test('RS_e50_t0.001.csv')
# LRU.test('RS_e50_t0.0005.csv')

for e in [10, 15, 50]:
    for t in [0.05, 0.001, 0.0005]:
        gen_rs(e=e, t=t, path=f'RS_e{e}_t{t}.csv')

        FIFO_result = FIFO.test(f'RS_e{e}_t{t}.csv')
        print(f'FIFO page fault count when e={e}, t={t}: {FIFO_result}')
        LRU_result = LRU.test(f'RS_e{e}_t{t}.csv')
        print(f'LRU page fault count when e={e}, t={t}: {LRU_result}')
