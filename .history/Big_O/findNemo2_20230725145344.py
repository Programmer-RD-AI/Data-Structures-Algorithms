import time

nemo = ["nemo"]


def find_nemo(array: list) -> None:
    s = time.time()
    for i in array:
        if i == "nemo":
            print("Found Nemo!")
    time.time()
    return None


find_nemo(nemo)
