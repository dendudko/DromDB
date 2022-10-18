import sqlite3
import pandas as pd

# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("DromDB.sqlite")

def drop_tables():
    con.executescript('''
    drop table if exists Selling;
    drop table if exists Car;
    drop table if exists Drive;
    drop table if exists Engine;
    drop table if exists Fuel;
    drop table if exists Model;
    drop table if exists Brand;
    drop table if exists Transmission;
    drop table if exists User;
    drop table if exists City;
    drop table if exists Country;
    ''')
    con.commit()

def init():
    # открываем файл с дампом базы данных
    f_dump = open('DromDB.sql', 'r', encoding='utf-8-sig')
    # читаем данные из файла
    dump = f_dump.read()
    # закрываем файл с дампом
    f_dump.close()
    # запускаем запросы
    con.executescript(dump)
    # сохраняем информацию в базе данных
    con.commit()

def fill():
    # открываем файл с инсертами базы данных
    f_dump = open('DromDB_inserts.sql', 'r', encoding='utf-8-sig')
    # читаем данные из файла
    dump = f_dump.read()
    # закрываем файл с дампом
    f_dump.close()
    # запускаем запросы
    con.executescript(dump)
    # сохраняем информацию в базе данных
    con.commit()

drop_tables()
init()
fill()