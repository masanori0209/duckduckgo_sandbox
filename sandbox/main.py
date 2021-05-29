from duckduckpy import query
import os
import sys
import time
KEYWORD = "デフォルト" if len(sys.argv) == 1 else sys.argv[1]

if __name__ == "__main__":
    start = time.time()
    print("search:", KEYWORD)
    response = query(KEYWORD, container="dict")
    num = 10
    for res in response["related_topics"]:
        print("res:", res)
        num += 1
        if num == 10:
            break
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")