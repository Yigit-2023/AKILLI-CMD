#Yazan Yiğit Çıtak 
while True:

    def hesapm():
        xy = input("""\nToplama işlemi için "+" çıkarma için "-" çarpma için "x" yazın\n""")

        if xy == "+":
            xyz = int(input("Rakam 1:\n"))
            xyy = int(input("Rakam 2:\n"))

            print("sonuc: ",xyz + xyy)

        elif xy == "-":
            xyz1 = int(input("Rakam 1:\n"))
            xyz2 = int(input("Rakam 1:\n"))

            print("sonuc: ",xyz1 - xyz2)

        elif xy == "x" or xy == "X":
            xyz3 = int(input("Rakam 1:\n"))
            xyz4 = int(input("Rakam 1:\n"))

            print("sonuc: ", xyz3 * xyz4)

        else:
            print("Giriş hatalı sadece + - x bunlardan birini yazmalıydın")





    giris = input("\nKomut Girin\n")

    if giris == "hesap makinesi":
        hesapm()

    elif giris == "help":
        print("""Komtlar: 
            hesap makinesi :  hesap makinesini açar
            harf--say :  Girilen metinin kaç harften oluştuğunu söyler
            harf--büyüt :  Girilen metindeki bütün harfler büyük harfe dönüşür
            harf--küçült :  Girilen metindeki bütün harfler küçük harfe dönüşür

            metin :  Girilen Metini kayıteder""")



    elif giris == "metin":
        yaz = input()
        dosya = open("metin.txt","a+")
        dosya.write(yaz)
        dosya.close()
        print("İşlem başarılı")

    elif giris == "harf--say":
        h_say = input("Yaz: \n")
        print(h_say," Girdisi ",len(h_say)," Harftir")

    elif giris == "harf--büyüt":
        h_buyu = input("Yaz:\n")
        print(h_buyu.upper())

    elif giris == "harf--küçült":
        h_kucul = input("Yaz:\n")
        print(h_kucul.lower())

    else:
        print("""
        >>>Komut Hatalı<<< \nKomut listesini açmak için "help" yazın\nUwU""")
