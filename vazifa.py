import sqlite3
def connect():
 conn = sqlite3.connect("ilova.db")
 cur = conn.cursor()
 return conn,cur

def ilova (cur):
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
