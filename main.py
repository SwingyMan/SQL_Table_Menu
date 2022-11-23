import mysql.connector
import pymongo
try:
    f = open("config.cfg","r")
except Exception:
    print("Brak pliku config.cfg")
credentials=[]
for x in f.readlines():
    credentials.append(x.strip("user:").strip("password:").strip("address:").strip("\n"))
try:
    sql = mysql.connector.Connect(
        host=credentials[2],
        user=credentials[0],
        password=credentials[1]
    )
except Exception:
    print("Nieprawidłowe dane w pliku config.cfg")
cursor = sql.cursor()
cursor.execute("CREATE DATABASE user")
cursor.execute("USE user")
cursor.execute("CREATE TABLE employee (id int NOT NULL AUTO_INCREMENT primary key,name varchar(255),surname varchar(255),date varchar(255),job varchar(255))")
while True:
    print("1.Dodaj nowy rekord")
    print("2.Edytuj rekord")
    print("3.Usuń rekord")
    print("4.Pokaż rekord")
    print("5.Wyjdź")
    print("Wybierz opcję: ")
    x=int(input())
    if x==1:
        print("Dodaj rekord w formacie imie;nazwisko;data_urodzenia;zawód")
        y = input()
        insert = []
        for z in y.split(";"):
            insert.append(z)
        cursor.executemany("INSERT INTO employee (name,surname,date,job) values (%s,%s,%s,%s)",[insert])
    elif x==2:
        print("Edytuj rekord w formacie imie;nazwisko;data_urodzenia;zawód;id")
        y=input()
        insert = []
        for z in y.split(";"):
            insert.append(z)
        cursor.executemany("UPDATE employee SET name=%s,surname=%s,date=%s,job=%s WHERE id=%s", [insert])
    elif x==3:
        print("Podaj ID rekordu do usunięcia")
        id = int(input())
        cursor.execute("DELETE FROM employee where id=%s",[id])
    elif x==4:
        cursor.execute("SELECT * FROM employee")
        for x in cursor.fetchall():
            print(x)
    else:
        cursor.execute("DROP DATABASE user")
        sql.commit()
        sql.close()
        break
