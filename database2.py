# -*- coding: cp1254 -*-
import sqlite3
bag = sqlite3.connect("veritabani2.db")
sql = bag.cursor()
sql.execute("""
create table bolumler
(
	bolum_id int identity(1,1) primary key,
	bolum_adi text,
	bolum_kurulus_tarihi text,
	bolumun_tarihcesi text 
)""")
sql.execute("""
create table programlar
(
	program_id int identity(1,1) primary key,
	bolumu int references bolumler(bolum_id),
	program_adi text,
	program_tarihcesi text
)
""")
sql.execute("""
create table hocalar
(
	ogr_eleman_id int identity(1,1) primary key,
	ogr_eleman_adi text,
	ogr_eleman_soyadi text,
	ogr_eleman_tel text,
	ogr_eleman_bolumu int references bolumler(bolum_id)
)""")
