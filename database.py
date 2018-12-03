# -*- coding: cp1254 -*-
import sqlite3
bag = sqlite3.connect("veritabani.db")
sql = bag.cursor()

sql.execute("create table if not exists ogrenci (ad text, soyad text, numara int, dyeri text)")

def kayit_ekle(*parametreler):
    ad,soyad,numara,dyeri = parametreler
    sql.execute("insert into ogrenci values ('"+ad+"','"+soyad+"',"+str(numara)+",'"+dyeri+"')")
    bag.commit()

def kayit_oku():
    veriler = sql.execute("select * from ogrenci")
    satirlar = veriler.fetchall()
    print satirlar
    for satir in satirlar:
        for x in satir:
            print x

        
p1 = u'üüüüü'
p2 = u'şşşşşşşşş'
p3 = 12345
p4 = u'ÜĞİŞÇÖıüğşçö'

kayit_ekle(p1,p2,p3,p4)

kayit_oku()    


bag.close()


