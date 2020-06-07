import cProfile

import vaex

pr = cProfile.Profile()
pr.enable()
df = vaex.open("/home/abin/my_works/datasets/vaex/yellow_tripdata_2015-01.csv")
pr.disable()
pr.print_stats()
# print(df)
df.plot(df.col.pickup_longitude, df.col.pickup_latitude, f="log1p", show=True, limits="96%");


