import os

from tqdm.contrib.itertools import product

if not os.path.exists("procress_tmp_files"):
    os.makedirs("procress_tmp_files")

file_no = 0

for y, m in product(range(2011, 2024), range(1, 13)):
    try:
        os.system(
            f"python procress_data.py data/{y}/{m:02d}/yellow_tripdata_{y}-{m:02d}.parquet procress_tmp_files/{file_no}.parquet"
        )
        file_no += 1
    except:
        pass
