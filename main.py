import time
from datetime import datetime
import random
lst = [10,2,7,5,4,9,1]
result = []
for i in range(len(lst)):
    el = lst[0]
    lst.pop(0)
    nbr = k-el
    if nbr in lst:
        break
result.append(el)
result.append(nbr)
print(el,nbr)

# harga_open = 100
# kode_emiten = 'BBSS'
# if harga_sekarang > harga_open:
#     print(f"Harga saham {kode_emiten} naik {round((harga_sekarang-harga_open)/harga_open*100,1)}%")
# elif harga_sekarang < harga_open:
#     print(f"Harga saham {kode_emiten} turun {round((harga_sekarang-harga_open)/harga_open*100,1)}%")
# else:
#     print(f"Harga saham {kode_emiten} belum berubah")
# print(f"Emiten: {kode_emiten}")
# print(f"Open: {harga_open}")
# harga_sekarang = harga_open
# n = 0
# perubah = [-1,0,1]
# while True:
#     harga_sekarang = harga_sekarang + random.choice(perubah)
#     print(f"{datetime.now().strftime('%H:%M:%S')} {harga_sekarang} ({round((harga_sekarang-harga_open)/harga_open*100,1)}%)")
#     time.sleep(1)
#     n += 1
#     if n == 70:
#         break





