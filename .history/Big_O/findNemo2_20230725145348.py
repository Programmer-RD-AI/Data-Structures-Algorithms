import time

nemo = ["nemo"]


def find_nemo(array: list) -> None:
    s = time.time()
    for i in array:
        if i == "nemo":
            print("Found Nemo!")
    e = time.time()
    return e


find_nemo(nemo)
