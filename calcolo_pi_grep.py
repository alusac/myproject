import random
import math
import sys

#Funzione di base per il calcolo del pi greco
def stima_singola_pi(n):
    m = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            m += 1
    return 4 * m / n

#funzione per calcolo media e deviazione standard per k calcoli del pi greco
def esegui_esperimenti(n, k):
    stime = []
    for _ in range(k):
        val = stima_singola_pi(n)
        stime.append(val)

    media = sum(stime) / k
    
    if k > 1:
        somma_quadrati = 0
        for s in stime:
            differenza = s - media
            somma_quadrati += differenza**2

        varianza = somma_quadrati / (k - 1)
        dev_std = math.sqrt(varianza)
    else:
        dev_std = 0.0
        
    return media, dev_std


def main():
    # Gestione argomenti da riga di comando
    # Utilizzo: python3 stima_pi_pro.py N K
    if len(sys.argv) < 2:
        print("Utilizzo: python3 stima_pi_pro.py N K")
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    media, dev_std = esegui_esperimenti(n,k)
    print(f"Con N = {n} e k = {k} i valori sono:")
    print("Deviazione standard =",dev_std)
    print("Pi Greco medio = ",media)
if __name__ == "__main__":
    main()
