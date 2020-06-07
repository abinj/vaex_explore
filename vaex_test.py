import cProfile

import vaex

pr = cProfile.Profile()
pr.enable()
df = vaex.open("/home/abin/my_works/datasets/vaex/yellow_tripdata_2019-01.csv")
pr.disable()
pr.print_stats()
print(df)

