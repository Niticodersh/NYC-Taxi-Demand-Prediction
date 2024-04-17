import pandas as pd

dfs = [pd.read_parquet(f"procress_tmp_files/{i}.parquet") for i in range(155)]

final_df = pd.concat(dfs)
final_df.to_parquet("final_procress.parquet", index=False)
