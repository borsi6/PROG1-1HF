import random


class NapAdat:
    def __init__(self, nap, ebredesiIdo):
        self.nap = nap
        self.ebredesiIdo = ebredesiIdo

def random_ido():
    ora = random.randint(6, 9)
    perc = random.randint(0, 59)

    return f"{ora:02}:{perc:02}"

if __name__ == "__main__":
    napok = ["Hétfő:", "Kedd:", "Szerda:", "Csütörtök:", "Péntek:", "Szombat:", "Vasárnap:"]
    het = []
    for nap in napok:
        het.append(NapAdat(nap, random_ido()))
    print("Mikor keltem a héten:")
    for adat in het:
        print(f"{adat.nap:<12} {adat.ebredesiIdo}") 
