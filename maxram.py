import multiprocessing

def memoria_toltes():
    tarolo = []
    while True:
        tarolo.append(bytearray(1024 * 1024 * 100))

if __name__ == '__main__':
    magok_szama = multiprocessing.cpu_count()
    for i in range(magok_szama):
        p = multiprocessing.Process(target=memoria_toltes)
        p.start()
