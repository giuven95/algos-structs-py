from threading import Thread
from time import sleep
from insertionsort import insertionsort


def sleep_sort(l):
    if len(l) < 2:
        return

    def func(key, l):
        sleep(key * 0.002)
        l.append(key)
        return

    threads = []
    new_list = []
    for key in l:
        t = Thread(target=func, args=(key, new_list))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    insertionsort(new_list)
    l[:] = new_list


if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    sleep_sort(l)
    print(l)
