class db_connection:
    import mysql.connector as mc
    conn = mc.connect(host="localhost", user="root", passwd="", database="Management")
    cur = conn.cursor()
    if cur:
        print("Connected Sucessfully.....")
