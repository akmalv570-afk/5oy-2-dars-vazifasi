from vazifa import vazifa_qoshish,vazifa_korish,vazifani_ochirish,connect,ilova
conn,cur = connect()
ilova(cur)

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



