#python code

import os,sys,time
from time import sleep


#color
hijau="\033[1;32m"
lghcyan="\033[1;36m"
pink="\033[1;35m"
merah="\033[1;31m"
kuning="\033[1;33m"


def mula():
    os.system("clear")
    a = input("\033[1;35mAdakah anda mahu teruskan [y/t] ")
    if a=="y":
        print ("\033[1;33mtunggu sebentar!")
        sleep (2)
    elif a=="t":
        sys.exit()



def login():
    mula()
    import load
    sleep (2)
    os.system("clear")
    print ("\033[1;31mLogin area!")
    sleep (2)
    password_1 = input("\033[1;36mmasukkan email grup :")
    password_2 = input("Masukkan password grup :")
    sleep (3)
    print ("")
    print ("\033[1;33mCheck list...")
    sleep (4)
    print ("\033[1;31mEmail :",password_1)
    sleep (3)
    print ("Password :",password_2)
    sleep (3)
    while True:
        try:
            if password_1 == "minecraft@gmail.com":
                if password_2 == "minecraft":
                    sleep (2)
                    print ("\033[1;33mBerjaya login")
                    sleep (2)
            else:
                break
        except ValueError:
            print ("\033[1;31mKata laluan salah atau keyword salah\n")
        break

os.system("clear")
import load
os.system("clear")

username = input("\033[1;33mMasukkan username : ")
tahun = input("Masukkan umur : ")
nama_anda = input("Masukkan nama anda : ")


def karangan_1():
    import load
    os.system("clear")
    print ("\033[1;36mMINECRAFT POCKET EDITION\n")
    print ("")
    sleep (2)
    print ("\033[1;35mgithub : https://github.com/daunial")
    print ("Facebook : Muhammad Danial Hakim")
    print ("Instagram : termux0000")
    print ("Whatsapp : 01121164746")
    print ("tiktok : -\n")
    sleep (2)
    print ("\033[1;32m1.Minecraft ")
    print ("2.Shader")
    print ("3.Mod")
    print ("4.Addons\n")
    sleep (3)
    x = int(input("\033[1;33mMasukkan Nombor Sahaja : "))
    if x==1:
        mula()
        os.system("clear")
        print ("\033[1;31m! PERHATIAN !")
        print ("Ini mungkin akan berlangsung lama!\n")
        o = input("Adakah anda mahukan nya [y/t] ")
        if o=="y":
            os.system("clear")
            sleep (2)
            print ("\033[1;33mGenerating Link...\n")
            sleep (4)
            print ("Jangan kunci skrin atau keluar ke mana aplikasi    ketika link sedang dijalankan!")
            sleep (4)
            import lloadd
            sleep (2)
            import load
            os.system("clear")
            print ("\033[1;33mlink dibawah :\n")
            print ("https://www.mediafire.com/file/6ptjsr03a30i7jz/minecraft-1-17-20-22.apk/file")
            print ("\033[1;36mMinecraft 1.17.20.22\n")
            print ("\033[1;33mhttps://mcpedl.org/minecraft-pe-1-17-10-apk/")
            print ("\033[1;36mMinecraft 1.17.10 - yg biasa digunakan!\n")
            sleep (2)
            import load
            print ("\033[1;33mTekan R - menu utama")
            print ("Tekan E - exit")
            print ("Tekan Q - option\n")
            print ("Masukkan huruf besar")
            option = input("Masukkan option atas : ")
            if option=="R":
                import load
                karangan_1()
            elif option=="E":
                import load
                os.system("clear")
                sys.exit()
            elif option=="Q":
                import load
                print ("Creadit : danialhackim")
                print ("TERIMA KASIH KEPADA PENGGUNA SAYA...")
                print ("github : https://github.com/daunial")
                print ("code   : python")
                print ("Dibuat : termux")

        elif o=="t":
            sys.exit()
    elif x==2:
        print ("\033[1;31mTTW SHADER!")
        print ("\033[1;36mLINK : https://www.mediafire.com/file/7eidl8urtle39cc/TTW_Shader_V2/file\n")
        print ("\033[1;31mPE HIGH SHADER")
        print ("\033[1;36mLINK : https://drive.google.com/file/d/175RNn-HWxDEaJaGP-u-WxuK7TA3LeJW7/view\n")
        print ("\033[1;31mBUN SHADER ultra/standard/zip")
        print ("\033[1;36mLINK : https://mcpedl.com/bun-shader-v2/\n")
        print ("\033[1;31mSUPER VANILLA RENEWED")
        print ("\033[1;36mLINK : https://drive.google.com/file/d/174U9AXO4aCcBi-Ks5S2fhG6R-TwWT8hT/view?usp=drivesdk\n")
        import load
        print ("")
        print ("\033[1;33mTekan R - menu utama")
        print ("Tekan E - exit")
        print ("Tekan Q - option\n")
        print ("Masukkan huruf besar")
        option = input("Masukkan option atas : ")
        if option=="R":
            import load
            karangan_1()
        elif option=="E":
            import load
            os.system("clear")
            sys.exit()
        elif option=="Q":
            import load
            print ("Creadit : danialhackim")
            print ("TERIMA KASIH KEPADA PENGGUNA SAYA...")
            print ("github : https://github.com/daunial")
            print ("code   : python")
            print ("Dibuat : termux")
    elif x==3:
        print ("\033[1;31m404 : Error, file tidak dijumpai")
        print ("Maaf kami masih tidak menjumpai sebarang mod!\n")
        import load
        print ("")
        print ("\033[1;33mTekan R - menu utama")
        print ("Tekan E - exit")
        print ("Tekan Q - option\n")
        print ("Masukkan huruf besar")
        option = input("Masukkan option atas : ")
        if option=="R":
            import load
            karangan_1()
        elif option=="E":
            import load
            os.system("clear")
            sys.exit()
        elif option=="Q":
            import load
            print ("Creadit : danialhackim")
            print ("TERIMA KASIH KEPADA PENGGUNA SAYA...")
            print ("github : https://github.com/daunial")
            print ("code   : python")
            print ("Dibuat : termux")
    elif x==4:
        print ("404 : Error, file tidak dijumpai")
        import load
        print ("\033[1;33mTekan R - menu utama")
        print ("Tekan E - exit")
        print ("Tekan Q - option\n")
        print ("Masukkan huruf besar")
        option = input("Masukkan option atas : ")
        if option=="R":
            import load
            karangan_1()
        elif option=="E":
            import load
            os.system("clear")
            sys.exit()
        elif option=="Q":
            import load
            print ("Creadit : danialhackim")
            print ("TERIMA KASIH KEPADA PENGGUNA SAYA...")
            print ("github : https://github.com/daunial")
            print ("code   : python")
            print ("Dibuat : termux")
login()
karangan_1()
