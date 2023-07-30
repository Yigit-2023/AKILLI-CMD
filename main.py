#Yazan Yiğit Çıtak 
import os
import turtle
import random
import time

while True:
    def ss(): #Sonraki satır
        print("\n")

        #Yılan Oyunu
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
        print("""\nKomtlar: 
            1: hesap makinesi :  hesap makinesini açar
            2: harf--say :  Girilen metinin kaç harften oluştuğunu söyler
            3: harf--büyüt :  Girilen metindeki bütün harfler büyük harfe dönüşür
            4: harf--küçült :  Girilen metindeki bütün harfler küçük harfe dönüşür
            5: harf--çevir :  Girilen Metindeki büyük harfler küçük, küçük harfler büyük olur
            6: metin :  Girilen Metini kayıteder
            7: kapat :  Bu programı kapatır
            8: oyun :  Oyunları açar
            9: kaynak kod :  Bu programın kaynak kodlarını gösterir
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

    elif giris == "kaynak kod" or giris == "9":
        print("Bu programın kaynak kodları:\nhttps://github.com/Yigit-2023/Komut-Chat")
        ss()


    else:   #UwU
        print("""
        >>>Komut Hatalı<<< \nKomut listesini açmak için "help" yazın""")
