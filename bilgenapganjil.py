print("Penentuan Bilangan Genap dan Ganjil")

def bilgenapganjil(bil):
    sisa_pambagian=bil%2
    if sisa_pambagian==0:
        print("Bilangan ini bilangan Genap")
    else:
        print("Bilangan ini bilangan Ganjil")
    return

nilai_bilangan=int(input("Masukkan bilangan bulat: "))
bilgenapganjil(nilai_bilangan)
