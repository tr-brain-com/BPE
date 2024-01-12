from collections import Counter, defaultdict
class BPE:
    def __init__(self, metin, yineleme):
        self.metin = metin
        self.yineleme = yineleme

    def al_kulliyat(self): #her kelimenin metin içerisinde ki sıklığını tespit et
        kulliyat = Counter(self.metin.split())
        return {k: f for k, f in kulliyat.items()}

    def al_istatistikler(self, kulliyat): #birleşik halde bulunan (bigram) sembol çiftlerinin sıklığını tespit et
        cifts = defaultdict(int)
        for w, f in kulliyat.items():
            sembols = w.split()
            for i in range(len(sembols) - 1):
                cifts[sembols[i], sembols[i+1]] += f
        return cifts

    def birlestir(self, cift, kulliyat): #tüm kelimelerde en sık kullanılan sembol çiftlerini birleştir ve külliyatı güncelle
        yeni_corpus = {}
        bigram = ' '.join(cift)
        degisim = ''.join(cift)
        for w in kulliyat:
            new_word = w.replace(bigram, degisim)
            yeni_corpus[new_word] = kulliyat[w]
        return yeni_corpus

    def isle(self): #işlemi başlat
        kulliyat = self.al_kulliyat()
        kulliyat = {' '.join(word): freq for word, freq in kulliyat.items()}
        print("başlangıç kelimeleri: \n", kulliyat)

        for i in range(self.yineleme):
            cifts = self.al_istatistikler(kulliyat)

            if not cifts:
                break

            en_iyi_cift = max(cifts, key=cifts.get)
            kulliyat = self.birlestir(en_iyi_cift, kulliyat)
            print(f"{i + 1}. yinelemeden sonra, en iyi çift:  {en_iyi_cift}")
            print("külliyatı güncelle: ", kulliyat)

metin = "bayat bayrak kayak kıyak "
BPE(metin= metin, yineleme=10).isle()