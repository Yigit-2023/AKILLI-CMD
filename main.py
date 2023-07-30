#Yazan Yiğit Çıtak 
import os
while True:
    def ss(): #Sonraki satır
        print("\n")


    def hesapm():
        xy = input("""\nToplama işlemi için "+" çıkarma için "-" çarpma için "x" yazın\n""")

        if xy == "+":
            try:
                xyz = int(input("Rakam 1:\n"))
                xyy = int(input("Rakam 2:\n"))

                print("sonuc: ",xyz + xyy)
            except:
                print("Ama bunlar rakam değil :/\n")
        elif xy == "-":
            try:
                xyz1 = int(input("Rakam 1:\n"))
                xyz2 = int(input("Rakam 1:\n"))

                print("sonuc: ",xyz1 - xyz2)
            except:
                print("Ama bunlar rakam değil :/\n")

        elif xy == "x" or xy == "X":
            try:
                xyz3 = int(input("Rakam 1:\n"))
                xyz4 = int(input("Rakam 1:\n"))

                print("sonuc: ", xyz3 * xyz4)
            except:
                print("Ama bunlar rakam değil :/\n")

        else:
            print("Giriş hatalı sadece + - x bunlardan birini yazmalıydın\n")





    giris = input("Komut Girin\n")

    if giris == "hesap makinesi" or giris == "1":
        hesapm()

    elif giris == "help":
        print("""Komtlar: 
            1: hesap makinesi :  hesap makinesini açar
            2: harf--say :  Girilen metinin kaç harften oluştuğunu söyler
            3: harf--büyüt :  Girilen metindeki bütün harfler büyük harfe dönüşür
            4: harf--küçült :  Girilen metindeki bütün harfler küçük harfe dönüşür
            5: harf--çevir :  Girilen Metindeki büyük harfler küçük, küçük harfler büyük olur
            6: metin :  Girilen Metini kayıteder
            7: kapat :  Bu programı kapatır
            8: 
            9: 
            10: 
            11: 
            12: 
            13: 
            14: 
            15: 
            """)



    elif giris == "metin" or giris == "6":
        yaz = input()
        dosya = open("metin.txt","a+")
        dosya.write(yaz)
        dosya.close()
        print("İşlem başarılı")
        ss()

    elif giris == "harf--say" or giris == "2":
        h_say = input("Yaz: \n")
        print(h_say," Girdisi ",len(h_say)," Harftir")
        ss()

    elif giris == "harf--büyüt" or giris == "3":
        h_buyu = input("Yaz:\n")
        print(h_buyu.upper())
        ss()

    elif giris == "harf--küçült" or giris == "4":
        h_kucul = input("Yaz:\n")
        print(h_kucul.lower())
        ss()


    elif giris == "kapat" or giris == "7":
        exit()

    elif giris == "harf--çevir" or giris == "5":
        h_cevir = input("Yaz:\n")
        print(h_cevir.swapcase())
        ss()


    else:   #UwU
        print("""
        >>>Komut Hatalı<<< \nKomut listesini açmak için "help" yazın""")
