import time
import random
import numpy as np

nemo = ["nemo"]
everyone = ["gg", "aa", "bb", "nemo", "cc", "dd", "qq", "kk", "zz", "tt"]
large = random.sample(range(1000), 1000)
print(large)


def find_nemo(array: list) -> float:
    s = time.time()
    for i in array:
        if i == "nemo":
            print("Found Nemo!")
    e = time.time()
    print(e - s)
    return e - s


find_nemo(nemo)
find_nemo(everyone)
