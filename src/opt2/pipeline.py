from preprocessing import *
from bf_cython import bf_negative_cycle_p

df = get_data('data/historical_data.csv', '2022-05-12')
G = create_grap(df)
bf_negative_cycle_p(G)