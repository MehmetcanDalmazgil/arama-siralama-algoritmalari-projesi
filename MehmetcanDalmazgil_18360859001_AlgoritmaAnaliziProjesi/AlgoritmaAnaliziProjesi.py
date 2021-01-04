
from PyQt5.QtWidgets import QDialog, QListWidget,QLineEdit , QMessageBox , QVBoxLayout, QInputDialog,QPushButton, QHBoxLayout, QApplication
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import sys
import random
import time
import Algoritmalar as algo


class ProgrammingDialog(QDialog):

    def __init__(self,name, proList = None,*args, **kwargs):
        super(ProgrammingDialog, self).__init__(*args, **kwargs)

        self.name = name
        self.list = QListWidget()

        self.kullanilanDizi = []
        self.oncekiDizi = []
        self.algoSonuc = ""
        self.searchSonuc = ""
        self.islemSonuc = 0
        self.sureSonuc = 0
        
        if proList is not None:
            self.list.addItems(proList)
            self.list.setCurrentRow(0)

        vbox = QVBoxLayout()

        for text, slot in (("Dizi Oluştur", self.diziOlustur), 
                           ("Dizi Göster", self.diziGoster), 
                           ("Çalıştır", self.calistir), 
                           ("Sonuç", self.sonuc),
                           ("Kapat", self.kapat)):
            button= QPushButton(text)
            vbox.addWidget(button)
            button.clicked.connect(slot)
            
        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addLayout(vbox) 
        self.setLayout(hbox)
        self.setWindowTitle("Algoritma Analizi Projesi")
        self.setGeometry(650,400,600,230)

    def sort(self):
        self.list.sortItems()
    
    def diziOlustur(self): # Dizi Olustur
        self.DO = DiziOlustur(self.kullanilanDizi,self.oncekiDizi,self.algoSonuc)
        self.DO.exec_()
        self.kullanilanDizi = self.DO.dizi
        self.oncekiDizi = self.DO.oncekiDizi
        self.algoSonuc = self.DO.algoSifirla
   
    def diziGoster(self): # Dizi Goster

        self.DG = DiziGoster(self.kullanilanDizi,self.oncekiDizi,self.algoSonuc)
        self.DG.exec_()
    
    def calistir(self):
        yedek_islem = self.islemSonuc
        yedek_sure = self.sureSonuc
        yedek_algo = self.algoSonuc
        yedek_sonuc = self.searchSonuc
        row = self.list.currentRow()
        self.algo = self.list.item(row)
        self.CA = Calistir(self.algo.text(),self.kullanilanDizi,self.oncekiDizi)
        self.CA.exec_()
        self.islemSonuc = self.CA.islem
        self.sureSonuc = self.CA.sure
        self.algoSonuc = self.algo.text()
        self.searchSonuc = self.CA.sonuc

        if(self.islemSonuc == 0 and self.sureSonuc == 0):
            self.islemSonuc = yedek_islem
            self.sureSonuc = yedek_sure
            self.algoSonuc = yedek_algo
            self.searchSonuc = yedek_sonuc

    def sonuc(self):
       self.SO = Sonuc(self.islemSonuc,self.sureSonuc,self.algoSonuc,self.searchSonuc)
       self.SO.exec_()
        
    def kapat(self):
        self.accept()


class DiziOlustur(QtWidgets.QDialog):
    def __init__(self,kullanilanDizi,oncekiDizi,algoSonuc):
        super(DiziOlustur, self).__init__()
        self.dizi = kullanilanDizi
        self.oncekiDizi = oncekiDizi
        self.algoSifirla = algoSonuc
        self.setUI()

    def setUI(self):
        self.setWindowTitle("Dizi Oluştur")
        self.setGeometry(775,425,350,180)

        self.eleman_sayisi = QLabel(self)
        self.eleman_sayisi.move(55,20)
        self.eleman_sayisi.setText("Eleman Sayısı : ")
        self.input_eleman_sayisi = QLineEdit(self)
        self.input_eleman_sayisi.move(150,20)
        self.input_eleman_sayisi.resize(150,20)

        self.min_deger = QLabel(self)
        self.min_deger.move(45,60)
        self.min_deger.setText("Minimum Değer : ")
        self.input_min_deger = QLineEdit(self)
        self.input_min_deger.move(150,60)
        self.input_min_deger.resize(150,20)

        self.max_deger = QLabel(self)
        self.max_deger.move(44,100)
        self.max_deger.setText("Maximum Değer : ")
        self.input_max_deger = QLineEdit(self)
        self.input_max_deger.move(150,100)
        self.input_max_deger.resize(150,20)
        
        self.button = QPushButton(self)
        self.button.move(135,135)
        self.button.setText("Diziyi Oluştur")
        self.button.clicked.connect(self.diziOlustur)

    def diziOlustur(self):
        reg_eleman_sayisi = str(self.input_eleman_sayisi.text())
        reg_min_deger = str(self.input_min_deger.text())
        reg_max_deger = str(self.input_max_deger.text())
        self.dizi = []
        self.oncekiDizi = []
        
        if(int(reg_min_deger)>int(reg_max_deger)):
            mesajKutusu = QMessageBox()
            mesajKutusu.move(735,425)
            mesajKutusu.setWindowTitle("Hata!")
            mesajKutusu.setText("Minimum değer Maximum değerden büyük olamaz!")
            mesajKutusu.setIcon(QMessageBox.Information)
            mesajKutusu.setStandardButtons(QMessageBox.Ok)
            mesajKutusu.exec()

        elif(len(reg_eleman_sayisi and reg_min_deger and reg_max_deger) != 0):

            for x in range (0,int(reg_eleman_sayisi)):
                tutucu = (random.randint(int(reg_min_deger),int(reg_max_deger)))
                self.dizi.append(tutucu)
                self.oncekiDizi.append(tutucu)
            
            self.algoSifirla = ""

            mesajKutusu = QMessageBox()
            mesajKutusu.move(758,425)
            mesajKutusu.setWindowTitle("İşlem Başarılı !")
            mesajKutusu.setText("Dizi Göster bölümünden diziye ulaşabilirsiniz.")
            mesajKutusu.setIcon(QMessageBox.Information)
            mesajKutusu.setStandardButtons(QMessageBox.Ok)
            mesajKutusu.exec()
            self.accept()
        else:
            mesajKutusu = QMessageBox()
            mesajKutusu.move(803,425)
            mesajKutusu.setWindowTitle("Hata!")
            mesajKutusu.setText("Metin kutuları boş bırakılamaz !")
            mesajKutusu.setIcon(QMessageBox.Information)
            mesajKutusu.setStandardButtons(QMessageBox.Ok)
            mesajKutusu.exec()

class DiziGoster(QtWidgets.QDialog,):
    def __init__(self,kullanilanDizi,oncekiDizi,algoSonuc):
        self.dizi = kullanilanDizi
        self.oncekiDizi = oncekiDizi
        self.kullanilanAlgo = algoSonuc
        super(DiziGoster, self).__init__()
        self.setUI()
    
    def setUI(self):
        if(len(self.dizi)== 0):
            self.setGeometry(810,490,300,50)
            self.setWindowTitle("Uyarı!")
            self.label1 = QLabel(self)
            self.label1.setText(f"İşlem İçin Tanımlı Dizi Mevcut Değil !")
            self.label1.setStyleSheet("color: black; font-size: 15px;")
            self.label1.setGeometry(35,10,500,30)

        elif(self.kullanilanAlgo == ""):
            
            self.setWindowTitle("Dizi Göster")
            self.goster = self.dizi
            self.label = QLabel(self)
            self.label.setText("Olusturulan Dizi: ")
            self.label.setGeometry(40,100,150,30)
            self.label.setStyleSheet("color: black; font-size: 15px;")
            self.setGeometry(675,400,550,230)
            self.diziAlani = QPlainTextEdit(self)
            self.diziAlani.setGeometry(180,40,300,150)
            self.diziAlani.insertPlainText(str(self.goster))
            self.diziAlani.setReadOnly(True)
        
        elif(self.kullanilanAlgo == "Linear Search Algoritması"):

            self.setWindowTitle("Dizi Göster")
            self.goster = self.dizi

            self.label1 = QLabel(self)
            self.label1.setText("En Son Dizinin Kullanıldığı Algoritma: Linear Search Algoritması ")
            self.label1.setStyleSheet("color: black; font-size: 15px;")
            self.label1.setGeometry(40,10,400,30)

            self.label2 = QLabel(self)
            self.label2.setText("Kullanılan Dizi: ")
            self.label2.setGeometry(40,115,150,30)
            self.label2.setStyleSheet("color: black; font-size: 15px;")

            self.setGeometry(675,400,550,230)
            self.diziAlani = QPlainTextEdit(self)
            self.diziAlani.setGeometry(180,55,300,150)
            self.diziAlani.insertPlainText(str(self.goster))
            self.diziAlani.setReadOnly(True)
        
        else:
            self.setGeometry(675,400,550,230)
            self.setWindowTitle("Dizi Göster")
            self.goster = self.dizi

            self.label1 = QLabel(self)
            self.label1.setText(f"En Son Dizinin Kullanıldığı Algoritma: {self.kullanilanAlgo}")
            self.label1.setStyleSheet("color: black; font-size: 15px;")
            self.label1.setGeometry(40,5,400,20)

            self.label2 = QLabel(self)
            self.label2.setText("Kullanılan Dizi: ")
            self.label2.setGeometry(30,60,150,30)
            self.label2.setStyleSheet("color: black; font-size: 15px;")

            self.diziAlani2 = QPlainTextEdit(self)
            self.diziAlani2.setGeometry(150,35,350,80)
            self.diziAlani2.insertPlainText(str(self.oncekiDizi))
            self.diziAlani2.setReadOnly(True)

            self.label3 = QLabel(self)
            self.label3.setText("Dizinin Son Hali: ")
            self.label3.setGeometry(30,155,150,30)
            self.label3.setStyleSheet("color: black; font-size: 15px;")

            self.diziAlani3 = QPlainTextEdit(self)
            self.diziAlani3.setGeometry(150,130,350,80)
            self.diziAlani3.insertPlainText(str(self.goster))
            self.diziAlani3.setReadOnly(True)


class Calistir(QtWidgets.QDialog):
    def __init__(self,algo,kullanilanDizi,oncekiDizi):
        self.algo = algo
        self.dizi = kullanilanDizi
        self.oncekiDizi = oncekiDizi
        super(Calistir, self).__init__()
        self.setUI()

    def setUI(self):
        self.islem = 0
        self.sure = 0
        self.sonuc = ""

        if(len(self.dizi)== 0):
            self.setGeometry(810,490,300,50)
            self.setWindowTitle("Uyarı!")
            self.label1 = QLabel(self)
            self.label1.setText(f"İşlem İçin Tanımlı Dizi Mevcut Değil !")
            self.label1.setStyleSheet("color: black; font-size: 15px;")
            self.label1.setGeometry(35,10,500,30)
        
        elif(self.algo == "Linear Search Algoritması" or self.algo == "Binary Search Algoritması"):
            self.setWindowTitle("Calıştır")

            if(self.dizi != self.oncekiDizi):
                self.setGeometry(725,425,450,180)

                self.algoYazdir = QLabel(self)
                self.algoYazdir.move(90,10)
                self.algoYazdir.setText(f" Çalıştırılacak => {self.algo}")
                self.algoYazdir.setStyleSheet("color: black; font-size: 15px;")

                self.aranan_eleman = QLabel(self)
                self.aranan_eleman.move(120,38)
                self.aranan_eleman.setStyleSheet("color: black; font-size: 15px;")
                self.aranan_eleman.setText("Aranan Eleman : ")
                self.input_aranan_eleman = QLineEdit(self)
                self.input_aranan_eleman.move(250,38)
                self.input_aranan_eleman.resize(85,20)

                self.uyari = QLabel(self)
                self.uyari.move(150,65)
                self.uyari.setStyleSheet("color: black; font-size: 15px;")
                self.uyari.setText('Kullanılacak dizi SIRALI !')

                self.uyari1 = QLabel(self)
                self.uyari1.move(40,85)
                self.uyari1.setStyleSheet("color: black; font-size: 15px;")
                self.uyari1.setText('Dizinin Sıralı Halini Kullanmak İçin => Yeni Diziyle Çalıştır')

                self.uyari2 = QLabel(self)
                self.uyari2.move(40,105)
                self.uyari2.setStyleSheet("color: black; font-size: 15px;")
                self.uyari2.setText('Dizinin Önceki Halini Kullanmak İçin => Eski Diziyle Çalıştır')
        
                self.button = QPushButton(self)
                self.button.move(95,135)
                self.button.setText("Yeni Diziyle Çalıştır")
                self.button.clicked.connect(lambda : self.calistirArama(self.dizi))

                self.button = QPushButton(self)
                self.button.move(260,135)
                self.button.setText("Eski Diziyle Çalıştır")
                self.button.clicked.connect(lambda : self.calistirArama(self.oncekiDizi))
            
            else:
                self.setGeometry(800,425,300,180)

                self.algoYazdir = QLabel(self)
                self.algoYazdir.move(10,20)
                self.algoYazdir.setText(f" Çalıştırılacak => {self.algo}")
                self.algoYazdir.setStyleSheet("color: black; font-size: 15px;")

                self.aranan_eleman = QLabel(self)
                self.aranan_eleman.move(40,70)
                self.aranan_eleman.setText("Aranan Eleman : ")
                self.aranan_eleman.setStyleSheet("color: black; font-size: 15px;")
                self.input_aranan_eleman = QLineEdit(self)
                self.input_aranan_eleman.move(150,70)
                self.input_aranan_eleman.resize(90,20)
        
                self.button = QPushButton(self)
                self.button.move(105,125)
                self.button.setText("Calistir")
                self.button.clicked.connect(lambda : self.calistirArama(self.dizi))

        
        else:
            self.setWindowTitle("Calıştır")
            if(self.dizi != self.oncekiDizi):
                self.setGeometry(725,425,450,180)
                self.algoYazdir = QLabel(self)
                self.algoYazdir.move(90,10)
                self.algoYazdir.setText(f" Çalıştırılacak => {self.algo}")
                self.algoYazdir.setStyleSheet("color: black; font-size: 15px;")

                self.uyari = QLabel(self)
                self.uyari.move(150,50)
                self.uyari.setStyleSheet("color: black; font-size: 15px;")
                self.uyari.setText('Kullanılacak dizi SIRALI !')

                self.uyari1 = QLabel(self)
                self.uyari1.move(40,70)
                self.uyari1.setStyleSheet("color: black; font-size: 15px;")
                self.uyari1.setText('Dizinin Sıralı Halini Kullanmak İçin => Yeni Diziyle Çalıştır')

                self.uyari2 = QLabel(self)
                self.uyari2.move(40,90)
                self.uyari2.setStyleSheet("color: black; font-size: 15px;")
                self.uyari2.setText('Dizinin Önceki Halini Kullanmak İçin => Eski Diziyle Çalıştır')
        
                self.button = QPushButton(self)
                self.button.move(95,130)
                self.button.setText("Yeni Diziyle Çalıştır")
                self.button.clicked.connect(lambda : self.calistirSort(self.dizi))

                self.button = QPushButton(self)
                self.button.move(260,130)
                self.button.setText("Eski Diziyle Çalıştır")
                self.button.clicked.connect(lambda : self.calistirSort(self.oncekiDizi))
            
            else :
                self.setGeometry(800,440,300,150)

                self.algoYazdir = QLabel(self)
                self.algoYazdir.move(14,40)
                self.algoYazdir.setText(f" Çalıştırılacak => {self.algo}")
                self.algoYazdir.setStyleSheet("color: black; font-size: 15px;")

                self.button = QPushButton(self)
                self.button.move(102,90)
                self.button.setText("Calıştır")
                self.button.clicked.connect(lambda : self.calistirSort(self.dizi))

    def calistirArama(self,dizi):

        self.kullanilacakDizi = dizi
        reg_aranan_eleman = str(self.input_aranan_eleman.text())
        
        if(len(reg_aranan_eleman) != 0):
            self.aranan = int(reg_aranan_eleman)
            
            if(self.algo == "Linear Search Algoritması"):
                self.baslangic = time.time()
                self.sonuc_lineer,self.islem = algo.lineer_arama(self.kullanilacakDizi,self.aranan)
                self.bitis = time.time()
                self.sure = self.bitis - self.baslangic
                
                if self.sonuc_lineer == -1:
                    self.sonuc =  "Aranan eleman dizide bulunmamaktadır."
                else:
                    self.sonuc = f"Aranan eleman dizinin {self.sonuc_lineer}. indeksinde bulunmaktadır."
                

            elif(self.algo == "Binary Search Algoritması"):
                self.baslangic = time.time()
                self.kullanilacakDizi_binary = self.kullanilacakDizi
                self.kullanilacakDizi_binary.sort()
                self.sonuc_binary,self.islem = algo.binary_arama(self.kullanilacakDizi_binary, 0, len(self.kullanilacakDizi) - 1,self.aranan,0)
                self.bitis = time.time()
                self.sure = self.bitis - self.baslangic
        
                if self.sonuc_binary == -1:
                    self.sonuc =  "Aranan eleman dizide bulunmamaktadır."
                else:
                    self.sonuc = f"Aranan eleman dizinin {self.sonuc_binary}. indeksinde bulunmaktadır."
                
            
            mesajKutusu = QMessageBox()
            mesajKutusu.move(760,401)
            mesajKutusu.setWindowTitle("İşlem Başarılı !")
            mesajKutusu.setInformativeText("Algoritma başarılı şekilde çalıştırıldı. Sonuç bölümünden değerlere ulaşabilirsiniz.")
            mesajKutusu.setIcon(QMessageBox.Information)
            mesajKutusu.setStandardButtons(QMessageBox.Ok)
            mesajKutusu.exec()
            self.accept()
        else:
            mesajKutusu = QMessageBox()
            mesajKutusu.move(810,425)
            mesajKutusu.setWindowTitle("Hata!")
            mesajKutusu.setText("Metin kutuları boş geçilemez.")
            mesajKutusu.setIcon(QMessageBox.Information)
            mesajKutusu.setStandardButtons(QMessageBox.Ok)
            mesajKutusu.exec()
    
    def calistirSort(self,dizi):
        self.kullanilacakDizi = dizi

        if(self.algo == "Insertion Sort Algoritması"):
            self.baslangic = time.time()
            self.islem = algo.insertion_sort(self.kullanilacakDizi,0)
            self.bitis = time.time()
            self.sure = self.bitis - self.baslangic
        
        elif(self.algo == "Merge Sort Algoritması"):
            self.baslangic = time.time()
            self.islem = algo.merge_sort(self.kullanilacakDizi,0,len(self.kullanilacakDizi)-1,0)
            self.bitis = time.time()
            self.sure = self.bitis - self.baslangic
        
        elif(self.algo == "Heap Sort Algoritması"):
            self.baslangic = time.time()
            self.islem = algo.heap_sort(self.kullanilacakDizi,0)
            self.bitis = time.time()
            self.sure = self.bitis - self.baslangic

        elif(self.algo == "Quick Sort Algoritması"):
            self.baslangic = time.time()
            self.islem = algo.quick_sort(self.kullanilacakDizi,0,len(self.kullanilacakDizi)-1,0)
            self.bitis = time.time()
            self.sure = self.bitis - self.baslangic
        
        elif(self.algo == "Counting Sort Algoritması"):
            self.baslangic = time.time()
            max_dizim = max(self.kullanilacakDizi)
            self.islem = algo.counting_sort(self.kullanilacakDizi,max_dizim)
            self.bitis = time.time()
            self.sure = self.bitis - self.baslangic
        
        elif(self.algo == "Bucket Sort Algoritması"):
            self.baslangic = time.time()
            self.kullanilacakDizi,self.islem = algo.bucket_sort(self.kullanilacakDizi)
            self.bitis = time.time()
            self.sure = self.bitis - self.baslangic
            
        
        elif(self.algo == "Radix Sort Algoritması"):
            self.baslangic = time.time()
            self.kullanilacakDizi,self.islem = algo.radix_sort(self.kullanilacakDizi)
            self.bitis = time.time()
            self.sure = self.bitis - self.baslangic
            self.dizi.sort()

        mesajKutusu = QMessageBox()
        mesajKutusu.move(760,401)
        mesajKutusu.setWindowTitle("İşlem Başarılı !")
        mesajKutusu.setInformativeText("Algoritma başarılı şekilde çalıştırıldı. Sonuç bölümünden değerlere ulaşabilirsiniz.")
        mesajKutusu.setIcon(QMessageBox.Information)
        mesajKutusu.setStandardButtons(QMessageBox.Ok)
        mesajKutusu.exec()
        self.accept()

class Sonuc(QtWidgets.QDialog,):
    def __init__(self,islemSonuc,sureSonuc,algoSonuc,searchSonuc):
        self.islemSonuc = islemSonuc
        self.sureSonuc = sureSonuc
        self.kullanilanAlgo = algoSonuc
        self.searchSonuc = searchSonuc

        super(Sonuc, self).__init__()
        self.setUI()
    def setUI(self):

        if(self.sureSonuc == 0 and self.islemSonuc == 0):
            self.setGeometry(850,485,200,50)
            self.setWindowTitle("Uyarı!")
            self.label1 = QLabel(self)
            self.label1.setText(f"Sonuç Bulunamadı.")
            self.label1.setStyleSheet("color: black; font-size: 15px;")
            self.label1.setGeometry(40,10,400,30)
            
        elif(self.kullanilanAlgo == "Linear Search Algoritması" or self.kullanilanAlgo == "Binary Search Algoritması"):
            self.setGeometry(700,415,500,200)
            self.setWindowTitle("Sonuc")
            self.label1 = QLabel(self)
            self.label1.setText(f"En Son Çalıştırılan Algoritma: {self.kullanilanAlgo}")
            self.label1.setStyleSheet("color: black; font-size: 15px;")
            self.label1.setGeometry(30,10,400,30)

            self.label2 = QLabel(self)
            self.label2.setText(f"Arama Sonucu: {self.searchSonuc}")
            self.label2.setGeometry(30,40,500,60)
            self.label2.setStyleSheet("color: black; font-size: 15px;")

            self.label2 = QLabel(self)
            self.label2.setText(f"Gerçekleşen İşlem Sayısı: {self.islemSonuc}")
            self.label2.setGeometry(30,70,400,90)
            self.label2.setStyleSheet("color: black; font-size: 15px;")

            self.label2 = QLabel(self)
            self.label2.setText(f"Algoritmanın Çalışma Süresi: {self.sureSonuc}")
            self.label2.setGeometry(30,100,400,120)
            self.label2.setStyleSheet("color: black; font-size: 15px;")
        
        else:
            self.setGeometry(700,415,500,200)
            self.setWindowTitle("Sonuc")
            self.label1 = QLabel(self)
            self.label1.setText(f"En Son Çalıştırılan Algoritma: {self.kullanilanAlgo}")
            self.label1.setStyleSheet("color: black; font-size: 15px;")
            self.label1.setGeometry(30,10,400,30)

            self.label2 = QLabel(self)
            self.label2.setText(f"Gerçekleşen İşlem Sayısı: {self.islemSonuc}")
            self.label2.setGeometry(30,40,500,60)
            self.label2.setStyleSheet("color: black; font-size: 15px;")

            self.label2 = QLabel(self)
            self.label2.setText(f"Algoritmanın Çalışma Süresi: {self.sureSonuc}")
            self.label2.setGeometry(30,70,400,90)
            self.label2.setStyleSheet("color: black; font-size: 15px;")

            self.label2 = QLabel(self)
            self.label2.setText(f"NOT : Dizinin Sıralanmış Hali 'Dizi Göster' Bölümünde Verilmiştir.")
            self.label2.setGeometry(30,100,500,120)
            self.label2.setStyleSheet("color: black; font-size: 15px;")


if __name__ == "__main__":

    programming = ["Linear Search Algoritması","Binary Search Algoritması","Insertion Sort Algoritması", "Merge Sort Algoritması", 
                "Heap Sort Algoritması", "Quick Sort Algoritması","Counting Sort Algoritması","Bucket Sort Algoritması","Radix Sort Algoritması"]

    app= QApplication(sys.argv)
    dialog = ProgrammingDialog("Languages", programming)
    dialog.exec_()
