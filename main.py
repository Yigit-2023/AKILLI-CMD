#Yazan Yiğit Çıtak 

#Komutlar için:
import os

#Yılan oyunu için:
import turtle
import random
import time

#Veriler:

windows_kısa = """\nWindows kısa yolları:\n
    |F1 = Yardımı görüntüle
    |F2 = Seçili dosyayı yeniden adlandır
    |F3 = Bir dosyayı ya da dizini arar
    |F4 = Dosya Gezgini’nde adres çubuğu listesini gösterir
    |F5 = Önde çalışan pencereyi yeniler
    |F6 = Bir penceredeki ya da masaüstündeki öğeler arasında geçiş yapar
    |F10 = Dosya Gezgini’nde harf kısayollarını gösterir
    |ALT + F4 = Önde çalışan programı kapatır
    |ALT + ESC = Çalışan programları açılma sıralarına göre öne çıkarır
    |ALT + Altı çizili harf = Önde çalışan uygulamada harf kısayollarını gösterir.
    |ALT + Enter = Seçili dosyanın özelliklerini gösterir
    |ALT + Space = Önde çalışan pencerenin kısayol menüsünü gösterir.
    |ALT + Sol ok tuşu = Bir önceki sekmeye geri döner
    |ALT + Sağ ok tuşu = Bir sonraki sekmeye geri döner
    |ALT + Page Up = Bir sayfa boyu yukarı çıkar
    |ALT + Page Down = Bir sayfa boyu aşağı iner
    |ALT + TAB = Açık uygulamaları listeler
    |CTRL + F4 = Önde çalışan uygulamayı kapatır
    |CTRL + A = Önde çalışan sayfadaki tüm öğeleri seçer
    |CTRL + C ya da CTRL + Insert = Seçili öğeyi kopyalar
    |CTRL + D ya da Delete = Seçili dosyayı Geri Dönüşüm Kutusu’na gönderir
    |CTRL + R = Seçili sayfayı yeniler
    |CTRL + V ya da Shift + Insert = Kopyalanmış öğeyi yapıştırır
    |CTRL + X = Seçili öğeyi keser
    |CTRL + Z = Bir işlemi geri alır
    |CTRL + Y = Geri alınan işlemi yeniden yapar
    |CTRL + artı işareti (+) ya da CTRL + eksi işareti (-) = Çok sayıda dosya incelerken yakınlaştırır ya da uzaklaştırır
    |CTRL + Fare kaydırma tuşu = Dosya Gezgini ve masaüstünde bulunan simgelerin boyutunu ayarlar
    |CTRL + Sağ ok tuşu = İmleci bir sonraki kelimenin başına taşır
    |CTRL + Sol ok tuşu = İmleci bir önceki kelimenin başına taşır
    |CTRL + Aşağı ok tuşu = İmleci bir sonraki paragrafın başına taşır
    |CTRL + Üst ok tuşu = İmleci bir önceki paragrafın başına taşır
    |CTRL + ALT + TAB = Açık uygulama ekranını uygulama seçene kadar açık tutar
    |CTRL + Ok tuşları + Space = Bir pencerede ya da masaüstüne birden çok öğe seçer
    |CTRL + Shift + Ok tuşları = Bir metinde bulunan bir bloğu seçer
    |CTRL + ESC = Başlat ekranını açar
    |CTRL + Shift + ESC = Görev Yöneticisi’ni açar
    |CTRL + Shift = Klavye düzenini değiştirir (Birden fazla klavye düzeni varsa)
    |Shift + F10 = Önce çalışan uygulamanın kısayol menüsünü gösterir
    |Shift + Delete = Seçili öğeyi kalıcı olarak siler (Geri Dönüşüm Kutusu'na yollamaz)
    |Windows tuşu = Başlat menüsünü açar ya da kapar
    |Windows tuşu + F1 = Yardım Alın sayfasına yönlendirir
    |Windows tuşu + B = Gizli simgeler menüsünü seçili hâle getirir
    |Windows tuşu + C = Charms sekmesini açar (Windows 10 hariç)
    |Windows tuşu + D = Masaüstünü gösterir ya da gizler
    |Windows tuşu + E = Dosya Gezgini’ni açar
    |Windows tuşu + F = Charms sekmesinde Arama bölümünü açar (Windows 10 hariç)
    |Windows tuşu + H = Charms sekmesinde Paylaş bölümünü açar (Windows 10 hariç)
    |Windows tuşu + I = Charms sekmesinde Ayarlar bölümünü açar (Windows 10 hariç)
    |Windows tuşu + K = Charms sekmesinde Cihazlar bölümünü açar (Windows 10 hariç)
    |Windows tuşu + L = Bilgisayarı kilitler ya da kullanıcı değiştirme ekranını açar
    |Windows tuşu + M = Tüm pencereleri küçültür
    |Windows tuşu + P = Yansıtma seçeneklerini sıralar
    |Windows tuşu + R = Çalıştır’ı açar
    |Windows tuşu + S = Başlat menüsünün Arama bölümünü açar
    |Windows tuşu + T = Görev Çubuğu’ndaki simgeler arasında gezinti sağlar
    |Windows tuşu + U = Erişim Kolaylığı Merkezi’ni açar
    |Windows tuşu + V = Kopyalama geçmişini açar
    |Windows tuşu + W = Kalem’i açar
    |Windows tuşu + X = Hızlı Bağlantı menüsünü açar
    |Windows tuşu + Z = Bir uyygulamada tam ekran modunda kullanılabilen komutları gösterir
    |Windows tuşu + virgül işareti (,) = Basıldığı sürece masaüstünü gösterir
    |Windows tuşu + Pause = Sistem özelliklerini gösterir
    |Windows tuşu + CTRL + F = Bilgisayar Bul’u açar
    |Windows tuşu + Shift + M = Masaüstünde simge durumuna küçültülmüş pencereleri geri yükler
    |Windows tuşu + Numara tuşları = Görev Çubuğu’nda bulunan uygulamaları sırasına göre açar
    |Windows tuşu + Shift + Sayı tuşları =Görev Çubuğu’nda bulunan uygulamaların yeni bir penceresini açar
    |Windows tuşu + CTRL + Sayı tuşları = Görev Çubuğu’nda bulunan uygulamaların son etkin penceresini açar
    |Windows tuşu + ALT + Sayı tuşları = Görev Çubuğu’nda bulunan uygulamaların Atlama Listesi’ni açar
    |Windows tuşu + CTRL + Shift + Sayı tuşları = Görev Çubuğu’nda bulunan uygulamayı yönetici olarak çalıştırır
    |Windows tuşu + B = Son kullanılan uygulamaları listeler
    |Windows tuşu + CTRL + TAB = Son kullanılan uygulamalar arasında gezinir
    |Windows tuşu + Shift + TAB = Son kullanılan uygulamalar arasında ters istikamette gezinir
    |Windows tuşu + CTRL + B = Bildirim gönderen uygulamaya geçer
    |Windows tuşu + Yukarı ok tuşu = Önde çalışan pencereyi büyütür
    |Windows tuşu + Aşağı ok tuşu = Önde çalışan pencereyi küçültür
    |Windows tuşu + Sol ok tuşu = Önde çalışan pencereyi sol tarafta büyütür
    |Windows tuşu + Sağ ok tuşu = Önde çalışan pencereyi sağ tarafta büyütür
    |Windows tuşu + Home = Aktif olan masaüstü hariç bütün masaüstlerini küçültür
    |Windows tuşu + Shift + Yukarı ok tuşu = Masaüstü penceresini ekranın üstüne ve altına uzatır
    |Windows tuşu + Shift + Aşağı ok tuşu = Genişliği koruyarak etkin masaüstü pencerelerini önceki boyut ve simge durumuna küçültür
    |Windows tuşu + Shift + Sol ok tuşu = Önde çalışan uygulamayı sol taraftaki monitöre taşır
    |Windows tuşu + Shift + Sağ ok tuşu = Önde çalışan uygulamayı sağ taraftaki monitöre taşır
    |Windows tuşu + Space = Giriş dili ve klavye düzenini değiştirir (Birden fazla varsa)
    |Windows tuşu + CTRL + Space = Bir önceki seçili giriş ve klavye düzenine geçer
    |Windows tuşu + Enter = Ekran Okuyucusu’nu açar
    |Windows tuşu + bölme işareti (/) = IME yeniden dönüşümünü başlatır
    |Windows tuşu + CTRL + V = Omuza dokunmaları açar
    |Windows tuşu + CTRL + Shift + B = Bilgisayarı boş veya siyah ekrandan uyandırır
    |Windows tuşu + artı işareti (+) = Büyüteç’i açar
    |Windows tuşu + artı işareti (+) ya da Windows tuşu + eksi işareti (-) = Büyüteç’in yakınlaştırmasını ayarlar
    |Windows tuşu + ESC = Büyüteç’i kapatır

"""

while True:

    #Fonksiyonlar:

    #sonrakı satır yani \n fonksiyonu
    def ss():
        print("\n")

    #Yılan Oyunu fonksiyonu
    #Bu oyunu ben Yazmadım. internetten buldum, ama bunun dışındaki bütün kodları ben yazdım.
    def oyun():
        screen = turtle.Screen()
        screen.title("YILAN OYUNU")
        screen.setup(width=700, height=700)
        screen.tracer(0)
        screen.bgcolor("#1d1d1d")


        turtle.speed(5)
        turtle.pensize(4)
        turtle.penup()
        turtle.goto(-310,250)
        turtle.pendown()
        turtle.color("red")
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(500)
        turtle.penup()
        turtle.hideturtle()


        score =0;
        delay = 0.1


        snake = turtle.Turtle()
        snake.speed()
        snake.shape("square")
        snake.color("green")
        snake.penup()
        snake.goto(0,0)
        snake.direction ='stop' 


        fruit = turtle.Turtle()
        fruit.speed(0)
        fruit.shape("square")
        fruit.color("white")
        fruit.penup()   
        fruit.goto(30,30)

        old_fruit = []

        scoring = turtle.Turtle()
        scoring.color("white")
        scoring.penup()
        scoring.hideturtle()
        scoring.goto(0,300)
        scoring.write("Score: ", align="center", font=("Courier",24,"bold"))


        def snake_go_up():
            if snake.direction != "down":
                snake.direction = "up"

        def snake_go_down():
            if snake.direction != "up":
                snake.direction = "down"

        def snake_go_left():
            if snake.direction != "right":
                snake.direction = "left"

        def snake_go_right():
            if snake.direction != "left":
                snake.direction = "right"

        def snake_move():
            if snake.direction == "up":
                y = snake.ycor()
                snake.sety(y + 20)
            if snake.direction == "down":
                y = snake.ycor()
                snake.sety(y - 20)
            if snake.direction == "left":
                x = snake.xcor()
                snake.setx(x - 20)
            if snake.direction == "right":
                x = snake.xcor()
                snake.setx(x + 20)


        screen.listen()
        screen.onkeypress(snake_go_up, "Up")
        screen.onkeypress(snake_go_down, "Down")
        screen.onkeypress(snake_go_left, "Left")
        screen.onkeypress(snake_go_right, "Right")


        while True:
            screen.update()

            if snake.distance(fruit) < 20:
                x = random.randint(-290, 270)
                y = random.randint(-240, 240)
                fruit.goto(x,y)
                scoring.clear()
                score += 1
                scoring.write("Score: {}".format(score), align="center", font=("Courier", 24,"bold"))
                delay -= 0.001

                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                new_fruit.shape("square")
                new_fruit.color("red")
                new_fruit.penup()
                old_fruit.append(new_fruit)


            for index in range(len(old_fruit)-1, 0, -1):
                a = old_fruit[index -1].xcor()
                b = old_fruit[index -1].ycor()

                old_fruit[index].goto(a,b)

            if len(old_fruit) > 0:
                a = snake.xcor()
                b = snake.ycor()
                old_fruit[0].goto(a, b)
            snake_move()


            if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor("turquoise")
                scoring.goto(0,0)
                scoring.write("    Game Over \n Your score is {}".format(score), align="center", font=("Courier", 30,"bold"))


                for food in old_fruit:
                    if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor("turquoise")
                        scoring.goto(0, 0)
                        scoring.write("    Game Over \n Your score is {}".format(score), align="center",font=("Courier", 30, "bold"))

            time.sleep(delay)

        turtle.Terminator
                                    #Yılan Oyunu

    #hesap makinesi fonksiyonu
    def hesap_makinesi():
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


    #Giedi
    giris = input("Komut Girin:\n")

    #Komut Blokları:

    #komut blok 1
    if giris == "hesap makinesi" or giris == "1":
        hesap_makinesi()
        ss()

    #komut blok 2
    elif giris == "harf--say" or giris == "2":
        h_say = input("Yaz: \n")
        print(h_say," Girdisi ",len(h_say)," Harftir")
        ss()

    #komut blok 3
    elif giris == "harf--büyüt" or giris == "3":
        h_buyu = input("Yaz:\n")
        print(h_buyu.upper())
        ss()

    #komut blok 4
    elif giris == "harf--küçült" or giris == "4":
        h_kucul = input("Yaz:\n")
        print(h_kucul.lower())
        ss()

    #komut blok 5
    elif giris == "harf--çevir" or giris == "5":
        h_cevir = input("Yaz:\n")
        print(h_cevir.swapcase())
        ss()

    #komut blok 6
    elif giris == "metin" or giris == "6":
        yaz = input()
        dosya = open("metin.txt","a+")
        dosya.write(yaz)
        dosya.close()
        print("İşlem başarılı")
        ss()

    #komut blok 7
    elif giris == "kapat" or giris == "7":
        exit()

    #komut blok 8
    elif giris == "oyun" or giris == "8":
        print("""Oyunlar:
            Yılan Oyunu için "1" yazın""")
        oyun_sec = input()
        if oyun_sec == "1":
            print("Not: oyun kapatıldığı zaman bu program da kapanır")
            oyun()
        else:
            print("oyun kodu bulunamadı")
            ss()

    #komut blok 9
    elif giris == "kısayol" or giris == "9":
        print(windows_kısa)


    #Süpriz Yumurta ve imzalar:

    #Süpriz Yumurta 1
    elif giris == "kaynak kod" or giris == "2006":
        ss()
        print("Bu programın kaynak kodları:\nhttps://github.com/Yigit-2023/Komut-Chat")
        ss()

    #Süpriz Yumurta 2
    elif giris == "programcı" or giris == "2023":
        ss()
        print("Bu Programın yazarı:\nYiğit Çıtak\nBu programın başlangıç yılı:\n2023")
        ss()


    #Diğer bloklar:

    #Yardım blok 
    elif giris == "help":
        print("""\nKomtlar: 
            1: hesap makinesi :  hesap makinesini açar
            2: harf--say :  Girilen metinin kaç harften oluştuğunu söyler
            3: harf--büyüt :  Girilen metindeki bütün harfler büyük harfe dönüşür
            4: harf--küçült :  Girilen metindeki bütün harfler küçük harfe dönüşür
            5: harf--çevir :  Girilen Metindeki büyük harfler küçük, küçük harfler büyük olur
            6: metin :  Girilen Metini kayıteder
            7: kapat :  Bu programı kapatır
            8: oyun :  Oyunları açar
            9: kısayol :  Windows kısa yolları gösterir
            10: 
            11: 
            12: 
            13: 
            14: 
            15: 
            """)

    #komut bulunamadı blok
    else:   #UwU
        print("""
        >>>Komut Hatalı<<< \nKomut listesini açmak için "help" yazın""")
        ss()
