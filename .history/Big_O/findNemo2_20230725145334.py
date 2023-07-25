import time

nemo = ["nemo"]


def find_nemo(array: list) -> None:
    time.time()
    for i in array:
        if i == "nemo":
            print("Found Nemo!")
    return None


find_nemo(nemo)
