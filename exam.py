# ### Creterialar:
#
# - Toza kod.
# - O'tish balli 60.
# - Talab qilingan namuna kodi bo'lishi kerak.
# - Agar nazariya bo'lsa, lekin kodli misol bo'lmasa, u kamroq ball oladi.
#
# > Imtihon qoidalari, aldamang, atrofga qaramang!
# >
#
# > Savollarga javob yozing va namuna kodini taqdim eting.
# >
#
# ### Savollar
#
# 1-savol: Pythonda funksiya nima?
#
# #Javob: 1 vazifani kop marta yozmash uchun funktsiya ishlatiladi
#
# Kod namunasi:
#
# 2-savol: Pythonda funktsiyani qanday e'lon qilish mumkin?
#
# #Javob: funkstsiyani e'lon qilish uchun "def" ishlatiladi
#
# Kod namunasi:
import random


def qalesan():
    print("qalesan")


qalesan()


#
# 3-savol: Funktsiyaga argumentlarni qanday o'tkazish mumkin?
#
# #Javob: "def" dan keyin funktsiya nomi yozish kere keyin skopkani ichida argumentlani berish kere
#
# Kod namunasi:
def nimadur(a, b):
    c = a + b
    print(c)


nimadur(1, 2)


#
# 4-savol: Standart (default) argumentlar nima va ularni funktsiyada qanday ishlatish kerak?
#
# #Javob:
#
# Kod namunasi:
#
# 5-savol: Funksiya ichidagi return va print() ko'rsatmalari o'rtasidagi farq nima?
#
# #Javob: "print" prosto consolega chiqarib beradi, return esa bergan argumentizi "def" ni nomiga tenglashtirib qoyadi
#
# Kod namunasi:
def qalesan2():
    print("qalesan")


qalesan2()


def qalesan3():
    return "qalesan"


print(qalesan3())


#
# #6-savol: Python-da class nima va u nima uchun ishlatiladi?
# #Javob: "class" bu tayor shablon u yozishi osonlashtirish uchun ishlatiladi
#
# Kod namunasi:
class Nimadur2:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        return f"Name {self.name}, surname {self.surname}"


obj1 = Nimadur2("Anvarbek", "Abdurashidov")
print(obj1.get_info())


#
# 7-savol: Python-da classni qanday e'lon qilish kerak?
#
# #Javob: print ishlatamiz
#
# Kod namunasi:
class Nimadur4:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        return f"Name {self.name}, surname {self.surname}"


obj1 = Nimadur4("Anvar", "Abdurashidov")
print(obj1.get_info())


#
# 8-savol: Class (ob'ekt) misolini qanday yaratish mumkin?
#
# #Javob: "peremeniy" ga oxshab yaratiladi lekin "ravno" dan keyin "class" ni nomini yozib skopkaga kereli znacheniyala berish kere
#
# Kod namunasi:
class Nimadur5:
    def __init__(self, name, yoshi):
        self.name = name
        self.yoshi = yoshi

    def get_info(self):
        return f"Name {self.name}, age {self.yoshi}"


obj1 = Nimadur5("Anvar", 13)
print(obj1.get_info())


#
# 9-savol: Python-da o'rnatilgan class metodlari qanday?
#
# #Javob: eng kereli method __init__
#
# Kod namunasi:
class Nimadur5:
    def __init__(self, name, yoshi):
        self.name = name
        self.yoshi = yoshi

    def get_info(self):
        return f"Name {self.name}, age {self.yoshi}"


obj1 = Nimadur5("Anvar", 13)
print(obj1.get_info())


#
# 10-savol: Class konstruktorini qanday yaratish kerak va u nima uchun kerak?
#
# #Javob: __init__ metodini ishlatib u yordamida kop peremeniyla ochib tashash shartmas
#
# ### Amaliy vazifa
#
# mini loyiha: "sonlani taxming qiling"
# Loyihaning maqsadi: Foydalanuvchi kompyuter tomonidan taxmin qilingan raqamni taxmin qilishi kerak bo'lgan interaktiv o'yinni yaratish.
# Loyiha talablari:
#
# Kompyuter 1 dan 100 gacha tasodifiy sonni tanlaydi, foydalanuvchi uni taxmin qilishi kerak.
#
# Agar foydalanuvchi taxmini noto'g'ri bo'lsa, unga maslahatlar beriladi (masalan, "Juda kichik" yoki "Juda katta").
#
# O'yin foydalanuvchi raqamni taxmin qilmaguncha yoki o'yinni tark etishga qaror qilmaguncha davom etadi.
# Taxminiy sinf tuzilishi:
# "GuessGame" sinfi: O'yinni boshqaradigan asosiy sinf. Tasodifiy raqamni tanlash, kiritilgan raqamni taxmin qilingan raqam bilan solishtirish va maslahatlarni ko'rsatish usullarini o'z ichiga oladi.
# Dasturning taxminiy kursi:
# "Raqamni top" o'yiniga xush kelibsiz!
# 1 dan 100 gacha bo'lgan raqamni taxmin qilishga harakat qiling.
# O'z taxminingizni kiriting: 50
# Juda kichik!
# O'z taxminingizni kiriting: 75
# Juda katta!
# O'z taxminingizni kiriting: 63
# Tabriklaymiz! 63 raqamini 3 ta urinishda taxmin qildingiz.
# Ko'proq o'ynashni xohlaysizmi? (ha/yo'q): yo'q
# O'ynaganingiz uchun rahmat! Xayr. Salomat bo'ling!

class GuessGame:
    def __init__(self, bosh, tugash):
        self.bosh = bosh
        self.tugash = tugash

    def guess_number(self):
        a = random.randint(self.bosh, self.tugash)
        while True:
            question1 = int(input("Raqam kiriting: "))
            if question1 == a:
                print("Tabriklaymiz siz raqami topdingiz")
                break
            elif question1 < a:
                print("Juda kichkina")
            elif question1 > a:
                print("Juda katta")
            else:
                print("Qaytatdan raqam kiriting")


obj1 = GuessGame(1, 100)
obj1.guess_number()
