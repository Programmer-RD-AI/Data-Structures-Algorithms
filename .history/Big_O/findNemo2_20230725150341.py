import time

nemo = ["nemo","gg","aa","bb","cc","dd","","",""]


def find_nemo(array: list) -> float:
    s = time.time()
    for i in array:
        if i == "nemo":
            print("Found Nemo!")
    e = time.time()
    print(e - s)
    return e - s


find_nemo(nemo)
