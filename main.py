while True:

    def hesapm():
        xy = input("Toplama için + çıkarma için - çarpma için x yazın\n")

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

    if giris == "hesap":
        hesapm()

    elif giris == "help":
        print("""Komutlar:\n\nhesap  : Hesap Makinesini açar""")

    else:
        print("""
        >>>Komut Hatalı<<< \nKomut listesini açmak için "help" yazın\nUwU""")
