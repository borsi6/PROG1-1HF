import multiprocessing
def porgetes():
    while True:
        pass
if __name__ == '__main__':
    magok_szama = multiprocessing.cpu_count()
    for i in range(magok_szama):
        p = multiprocessing.Process(target=porgetes)
        p.start()
