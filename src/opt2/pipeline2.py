from preprocessing import *
from bf_cython2 import bf_negative_cycle_cc

df = get_data('data/historical_data.csv', '2022-05-12')
G = create_grap(df)
bf_negative_cycle_cc(G)