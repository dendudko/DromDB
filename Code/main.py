import sqlite3
import pandas as pd

# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("DromDB.sqlite")
pd.set_option('display.max_colwidth', None, 'display.max_rows', None,
              'display.max_columns', None, 'display.expand_frame_repr', False)

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

def queries_1_2():
    print('-----------------------------------------------------------------------------')
    print('Запрос 1 (Выбор всех нерусских городов):')
    df = pd.read_sql('''select C.CountryName as Страна, CityName as Город from City
    join Country C on C.CountryName = City.CountryName
    where C.CountryName!='Россия'
    order by CityName''', con)
    print(df)

    print()

    print('Запрос 2 (Выбор всех двигателей, которые устанавливаются на а/м Toyota Vitz):')
    df = pd.read_sql('''select BodyOrVinNumber as 'Номер_кузова',
    C.IDEngine as 'Номер_двигателя', Capacity as 'Объем', HP as 'Мощность',
    FuelType as 'Тип_топлива' from Engine
    join Car C on Engine.IDEngine = C.IDEngine
    where C.BrandName = 'Toyota' and C.ModelName='Vitz'
    order by HP desc''', con)
    print(df)
    print('-----------------------------------------------------------------------------')

# drop_tables()
# init()
# fill()

queries_1_2()

