import os

catvoost_dir = "catboost_v1"
subdirs = ["views", "depth", "full_reads_percent"]

os.makedir(catvoost_dir)
for el in subdirs:
    os.makedir(f"{catvoost_dir}/{el}")
