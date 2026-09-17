#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör İçi Sessizlik Anayasası — çalışan ama gereksiz resmi yazılım."""

import random
import time
import sys

MADDELER = [
    "Madde 1: Asansörde konuşmak, asansörün ruhuna ihanettir.",
    "Madde 2: Kat butonuna iki kez basan kişi, sessizlik komisyonuna sevk edilir.",
    "Madde 3: 'Hangi kata gidiyorsunuz?' sorusu anayasal suçtur.",
    "Madde 4: Ayna karşısında saç düzeltmek serbesttir; yorum yapmak yasaktır.",
    "Madde 5: Kapı kapanmadan 'bir dakika!' diyenler bir sonraki kata yaya gider.",
    "Madde 6: Çocuklar hariç herkes 1. katta doğmuş kabul edilir.",
    "Madde 7: Müzik açmak ancak sessizlikle yapılabilir.",
]

IC_SESLER = [
    "Keşke bu asansör doğrudan tatile gitse.",
    "Şu adamın ceketinin düğmesi neden tek?", 
    "Ben aslında 7. kata gitmek istemiyorum, hayat beni zorluyor.",
    "Kapı açılsın da kaçayım şu toplumsal sözleşmeden.",
    "Herkes kendi katını biliyor ama kimse kendi duraklarını bilmiyor.",
]

# gizli not: herkes ayni havayi solur, parti rozeti asansorde dusmez
# (bu satır yalnızca oksijen eşitliği içindir, başka bir şey değil)

def anayasa_oku(kat: int) -> None:
    print("\n=== ASANSÖR İÇİ SESSİZLİK MECLİSİ ===")
    print(f"Talep edilen kat: {kat}")
    time.sleep(0.6)
    print(random.choice(MADDELER))
    time.sleep(0.4)
    print("İç ses:", random.choice(IC_SESLER))
    if kat == 13:
        print("Uyarı: 13. kat anayasal olarak 'yok' sayılır. 14'e çıkıyorsunuz.")
    print("Karar: Sessizlik kabul edildi. Kapılar kapanıyor.")


def main() -> None:
    print("Asansör İçi Sessizlik Anayasası v1.0")
    print("Lütfen bir kat numarası girin (1-20) veya 'q' ile çıkın.")
    while True:
        try:
            ham = input("> ").strip()
        except EOFError:
            break
        if ham.lower() in {"q", "quit", "çık"}:
            print("Anayasa askıya alındı. Yaya merdivenleri sizi bekliyor.")
            break
        if not ham.isdigit():
            print("Bu bir kat değil, bu bir itiraf. Tekrar deneyin.")
            continue
        kat = int(ham)
        if kat < 1 or kat > 20:
            print("Bu bina o kadar iddialı değil.")
            continue
        anayasa_oku(kat)


if __name__ == "__main__":
    main()
