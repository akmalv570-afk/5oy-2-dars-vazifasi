import sqlite3
conn = sqlite3.connect("ilova.db")
cur = conn.cursor()

def ilova (conn,cur):
    cur.execute("""
    create table if not exists vazifa_ilova(
    id integer primary key autoincrement,
    text text,
    data date
    )
    """)

def vazifa_qoshish(conn,cur,text,data):
    cur.execute("""
    insert into vazifa_ilova(text,data) values(?,?)""",(text,data))
    conn.commit()

def vazifa_korish(conn,cur):

    cur.execute("select*from vazifa_ilova")
    vazifalar = cur.fetchall()
    if vazifalar:
        for v in vazifalar:
            print(v)
    else:
        print("Vazifa yoq!")

    return vazifalar


def vazifani_ochirish(conn,cur,id):
    cur.execute("""select * from vazifa_ilova where id=?""",(id,))
    natija = cur.fetchone()
    if natija:
        cur.execute("delete from vazifa_ilova where id=?",(id,))
        conn.commit()
        print("Vazifa o'chirildi")
    else:
        print("Bunday id lik vazifa yoq")
ilova(conn, cur)

while True:
 print("<<<MENU>>>")
 print("1-Vazifa qoshish\n2-Royhatni ko'rish\n3-Vazifani o'chirish\n0-Chiqish")
 tanlov = input("Tanlov: ")

 if tanlov == '1':
     text = input("Vazifa: ")
     data = input("dd-mm-YYYY: ")
     if text == "" or data == "":
         print("Text yoki data bosh bolmasligi kerak")
     else:
         vazifa_qoshish(conn,cur, text, data)
         print("Qoshildi!")

 elif tanlov == '2':
     vazifa_korish(conn, cur)

 elif tanlov =='3':
     vazifa_id = input("id:")

     if vazifa_id.isdigit():
         id = int(vazifa_id)
         vazifani_ochirish(conn, cur, id)
     else:
         print("ID: Faqat raqamdan iborat bolishi kerak!")

 elif tanlov == '0':
     print("Dastur yakunlandi")
     break
 else:
     print("Notog'ri tanlov")



