from dbcon import *

def Register(name, phone, id, password):
    if(isconnected()):
        con = connectdb()
        corsor = con.cursor()
        corsor.execute("SELECT * FROM users WHERE phone ='" +phone+"' OR idno = '"+id+"';")
        rows = corsor.fetchall()
        if corsor.rowcount == 0:
            qr = "INSERT INTO users (name, phone, idno, pass) VALUES ('"+name+"', '"+phone+"', '"+id+"', '"+password+"');"
            corsor.execute(qr)
            con.commit()
            con.close()
            return True
        else:
            return False
        
def Login(phone, password):
    if(isconnected):
        con = connectdb()
        corsor = con.cursor()
        qr = "SELECT * FROM users WHERE phone = '"+phone+"' AND pass = '"+password+"'"
        corsor.execute(qr)
        rows = corsor.fetchall()
        if(corsor.rowcount == 0):
            return False
        else:
            return True

def ISUSER(phone):
    if(isconnected()):
        con = connectdb()
        corsor = con.cursor()
        corsor.execute("SELECT * FROM users WHERE phone ='" +phone+"';")
        rows = corsor.fetchall()
        if corsor.rowcount == 0:
            return False
        else:
            return True
        
def ADDCard(card):
    con = connectdb()
    corsor = con.cursor()
    corsor.execute("UPDATE users SET card = '"+card+"'")
    con.commit()
    con.close()
        

#print(Register("hidhfif", '23082830', '18939282', '9273283782738'))
#print(Login('23082830', '9273283782738'))