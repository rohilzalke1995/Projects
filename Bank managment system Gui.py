# bank application Guik
from tkinter import *
import tkinter.messagebox
import sqlite3
import time
import random

root = Tk()
root.title("$$$$$$$$$$ BANK OF INDIA $$$$$$$$$$")
root.geometry("1400x1200")
C = Canvas(root, bg="black", height=250, width=300)
#filename = PhotoImage(file=r"bank.png")                          # select your image to display  
background_label = Label(root)#, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.grid()


class Bank:
    def __init__(self, m1, m2, m3, m4, m5, c1, c2, c3, c4, bal, k, cur, conn, x, de, a, To, A, k1, k2, L,year,p,O,r):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.bal = 0
        self.k = k
        self.cur = cur
        self.conn = conn
        self.x = x
        self.de = de
        self.a = 0
        self.To = To
        self.A = A
        self.k1 = k1
        self.k2 = k2
        self.L = L
        self.year = year
        self.p = p
        self.O=O
        self.r=r

    def create(self):
        a = self.c1.get()
        b = self.c2.get()
        c = self.c3.get()
        d = self.c4.get()
        s2 = "select * from Bank"
        self.cur.execute(s2)
        rows = self.cur.fetchall()
        check=0
        if( (( a == "" )|(b == "" )|( c == "" )|(d == "" ))&(self.r==1)):
            tkinter.messagebox.showinfo("Bank", "Enter the Details! ;}")
        else:
            for row in rows:
                AccountNo = row[1]
                if (AccountNo == int(self.c2.get())):
                    tkinter.messagebox.showinfo("Bank", "Choose Different Account No Account no All Ready in Use")
                    check=1
       
            if(check==0):
                s1 = "insert into Bank(Username ,AccountNo,AccountType,Balance,Password ) values ('%s','%d','%s','%d','%d')" % (a, int(b), c, int(self.bal), int(d))
                self.cur.execute(s1)
                self.conn.commit()
                tkinter.messagebox.showinfo("Bank", "Bank Account Created successfully!!!")

    def create_account_click(self):
        root = Tk()
        self.r=1
        root.configure(bg="white")
        root.title("$$$$$CREATE ACCOUNT :-)$$$$$")
        print("you can now create account")
        l1 = Label(root, text="Enter your name ", font=('Helvetica', '20' ), width=30, height=2, borderwidth=12,
                   bg="black", fg="white")
        l1.grid(row=0, column=0, sticky=E)
        self.c1 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
        self.c1.grid(row=0, column=3)
        l2 = Label(root, text="Enter your account no ", font=('Helvetica', '20' ), width=30, height=2,
                   borderwidth=12, bg="black", fg="white")
        l2.grid(row=1, column=0, sticky=E)
        self.c2 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
        self.c2.grid(row=1, column=3)
        l3 = Label(root, text="Enter account type", font=('Helvetica', '20' ), width=30, height=2, borderwidth=12,
                   bg="black", fg="white")
        l3.grid(row=2, column=0, sticky=E)
        self.c3 = Spinbox(root, font=('Helvetica', '20' ), values=("current", "savings", "balance"), borderwidth=12)
        self.c3.grid(row=2, column=3)
        l4 = Label(root, text="Enter the password", font=('Helvetica', '20' ), width=30, height=2, borderwidth=12,
                   bg="black", fg="white")
        l4.grid(row=3, column=0, sticky=E)
        self.c4 = Entry(root, show="*", font=('Helvetica', '20' ), borderwidth=12)
        self.c4.grid(row=3, column=3)
        b = Button(root, text="create", font=('Helvetica', '20' ), width=10, height=2, borderwidth=12,
                   bg="black", fg="white", command=self.create)
        b.grid(row=4, column=2)
        root.after(60000, lambda: root.destroy())
        root.mainloop()

    def deposit_click(self):
        if (self.L == 1):
            root = Tk()
            l1 = Label(root, text="Enter your name ", font=('Helvetica', '20' ), width=30, height=2, borderwidth=12,
                       bg="black", fg="white")
            l1.grid(row=0, column=0, sticky=E)
            self.m1 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
            self.m1.grid(row=0, column=3)
            l2 = Label(root, text="Enter your account no ", font=('Helvetica', '20' ), width=30, height=2,
                       borderwidth=12, bg="black", fg="white")
            l2.grid(row=1, column=0, sticky=E)
            self.m2 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
            self.m2.grid(row=1, column=3)
            l3 = Label(root, text="Enter account type", font=('Helvetica', '20' ), width=30, height=2,
                       borderwidth=12, bg="black", fg="white")
            l3.grid(row=2, column=0, sticky=E)
            self.m3 = Spinbox(root, font=('Helvetica', '20' ), values=("current", "savings", "balance"),
                              borderwidth=12)
            self.m3.grid(row=2, column=3)
            l4 = Label(root, text="Enter the password", font=('Helvetica', '20' ), width=30, height=2,
                       borderwidth=12, bg="black", fg="white")
            l4.grid(row=3, column=0, sticky=E)
            self.m4 = Entry(root, show="*", font=('Helvetica', '20' ), borderwidth=12)
            self.m4.grid(row=3, column=3)
            b = Button(root, text="Verify", font=('Helvetica', '20' ), width=10, height=2, borderwidth=12,
                       bg="black", fg="white", command=self.login_click_deposit)
            b.grid(row=4, column=2)
            root.after(60000, lambda: root.destroy())
            root.mainloop()
        else:
            tkinter.messagebox.showinfo("BALANCE IS", "You Can't Deposit You Have To Login First")

    def transfer_bal(self):
        if (self.bal <= 0):
            tkinter.messagebox.showinfo("Bank", "You Cannot Transfer Money")
        else:
            root = Tk()
            l2 = Label(root, text="To Account No: ", font=('Helvetica', '20' ), width=15, height=2, borderwidth=12,
                       bg="black", fg="white")
            l2.grid(row=1, column=0, sticky=E)
            self.To = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
            self.To.grid(row=1, column=2)
            l4 = Label(root, text="Enter Amount: ", font=('Helvetica', '20' ), width=15, height=2, borderwidth=12,
                       bg="black", fg="white")
            l4.grid(row=3, column=0, sticky=E)
            self.A = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
            self.A.grid(row=3, column=2)
            b = Button(root, text="Transfer", font=('Helvetica', '20' ), width=15, height=2, borderwidth=12,
                       bg="black", fg="white", command=self.transfer)
            b.grid(row=4, column=2)


    def transfer(self):
        s3 = "select * from Bank"
        self.cur.execute(s3)
        rows = self.cur.fetchall()
        for row in rows:
            Username = row[0]
            AccountNo = row[1]
            AccountType = row[2]
            Balance = row[3]
            Password = row[4]
            if( ( self.To.get() == "" )|( self.A.get() == "" )):
                tkinter.messagebox.showinfo("Bank", "Enter the Details! ;}")
            else:
                if ((AccountNo == int(self.To.get()))&(self.bal < (self.O + 1))):
                    Balance = Balance + int(self.A.get())
                    a31 = ("UPDATE Bank SET Balance='%d' WHERE  AccountNo= '%d'") % (int(Balance), int(self.To.get()))
                    self.cur.execute(a31)
                    self.conn.commit()
                    self.bal = self.bal - int(self.A.get())
                    a32 = ("UPDATE Bank SET Balance='%d' WHERE  AccountNo= '%d'") % (int(self.bal), int(self.k2.get()))
                    self.cur.execute(a32)
                    self.conn.commit()
        tkinter.messagebox.showinfo("Bank", "Balance Transfered Successfully!!!")

    def withdraw_click(self):
        if (self.L == 1):
            root = Tk()
            l1 = Label(root, text="Enter your name ", font=('Helvetica', '20' ), width=30, height=2, borderwidth=12,
                       bg="black", fg="white")
            l1.grid(row=0, column=0, sticky=E)
            self.m1 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
            self.m1.grid(row=0, column=3)
            l2 = Label(root, text="Enter your account no ", font=('Helvetica', '20' ), width=30, height=2,
                       borderwidth=12,
                       bg="black", fg="white")
            l2.grid(row=1, column=0, sticky=E)
            self.m2 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
            self.m2.grid(row=1, column=3)
            l3 = Label(root, text="Enter account type", font=('Helvetica', '20' ), width=30, height=2,
                       borderwidth=12,
                       bg="black", fg="white")
            l3.grid(row=2, column=0, sticky=E)
            self.m3 = Spinbox(root, font=('Helvetica', '20' ), values=("current", "savings", "balance"),
                              borderwidth=12)
            self.m3.grid(row=2, column=3)
            l4 = Label(root, text="Enter the password", font=('Helvetica', '20' ), width=30, height=2,
                       borderwidth=12,
                       bg="black", fg="white")
            l4.grid(row=3, column=0, sticky=E)
            self.m4 = Entry(root, show="*", font=('Helvetica', '20' ), borderwidth=12)
            self.m4.grid(row=3, column=3)
            b = Button(root, text="Verify", font=('Helvetica', '20' ), width=10, height=2, borderwidth=12,
                       bg="black", fg="white", command=self.login_click_withdraw)
            b.grid(row=4, column=2)
        else:
            tkinter.messagebox.showinfo("BALANCE IS", "You Can't Withdraw You Have To Login First")

    def withd(self):
        if int(self.m5.get()) > int(self.bal):
            tkinter.messagebox.showinfo("INVALID TRANSACTION", "INSUFFICIENT BALANCE")
        else:
            self.bal = self.bal - int(self.m5.get())
            tkinter.messagebox.showinfo("BALANCE IS", self.bal)
        # update
        self.update()

    def Logout(self):
        self.L = 0
        self.bal = 0
        tkinter.messagebox.showinfo("BALANCE IS", "Balance: 0")

    def depo(self):
        if (int(self.m5.get()) <= 0):
            tkinter.messagebox.showinfo("INVALID AMOUNT", "AMOUNT CAN'T BE DEPOSITED")
        else:
            self.bal = self.a + int(self.m5.get())
            tkinter.messagebox.showinfo("BALANCE IS", self.bal)
        # update
        self.update()

    def update(self):
        a2 = ("UPDATE Bank SET Balance='%d' WHERE  AccountNo= '%d'") % (int(self.bal), int(self.m2.get()))
        self.cur.execute(a2)
        self.conn.commit()

    def balance(self):
        s3 = "select * from Bank"
        self.cur.execute(s3)
        rows = self.cur.fetchall()
        if (self.L == 1):
            for row in rows:
                Username = row[0]
                AccountNo = row[1]
                Balance = row[3]
                Password = row[4]
                if(( self.k2.get() == "" )|( self.k1.get() == "" )):
                    pass
                else:
                    if ((Password == int(self.k2.get())) & (Username == str(self.k1.get()))):
                        self.bal = Balance
                        tkinter.messagebox.showinfo("BALANCE IS", self.bal)
        else:
            tkinter.messagebox.showinfo("BALANCE IS", "Balance: 0")

    def profile(self):
        if (self.bal == 0):
            tkinter.messagebox.showinfo("Bank", "You need to deposit first!!please Login :=)@@@")
        else:
            s3 = "select * from Bank"
            self.cur.execute(s3)
            rows = self.cur.fetchall()
            for row in rows:
                Username = row[0]
                AccountNo = row[1]
                AccountType = row[2]
                Balance = row[3]
                Password = row[4]
                if ((row[4] == int(self.m4.get())) & (row[1] == int(self.m2.get()))):
                    root = Tk()
                    root.title("PROFILE")
                    ll1 = Label(root, text=" Name is :- {0} ".format(row[0]), font=('Helvetica', '20' ), bg="black",
                                fg="white", borderwidth=12)
                    ll1.grid(row=0, column=0, sticky=W)
                    ll2 = Label(root, text="Your account no is :- {0}".format(row[1]), font=('Helvetica', '20' ),
                                bg="black", fg="white", borderwidth=12)
                    ll2.grid(row=1, column=0, sticky=W)
                    ll3 = Label(root, text="Your accounttype is :- {0}".format(row[2]), font=('Helvetica', '20' ),
                                bg="black", fg="white", borderwidth=12)
                    ll3.grid(row=2, column=0, sticky=W)
                    ll4 = Label(root, text="Current Balance :- {0}".format(row[3]), font=('Helvetica', '20' ),
                                bg="black", fg="white", borderwidth=12)
                    ll4.grid(row=3, column=0, sticky=W)
                    

    def login_click_withdraw(self):
        s3 = "select * from Bank"
        self.cur.execute(s3)
        rows = self.cur.fetchall()
        for row in rows:
            Username = row[0]
            AccountNo = row[1]
            AccountType = row[2]
            Balance = row[3]
            Password = row[4]
            if (row[4] == int(self.m4.get())):
                self.a = row[3]
            if ((self.m1.get() == Username) & (int(self.m2.get()) == int(AccountNo)) & (
                    self.m3.get() == AccountType) & (int(self.m4.get()) == int(Password))):
                root = Tk()
                la = Label(root, text="Login Successful", font=('Helvetica', '20' ), width=30, height=2,
                           borderwidth=12, bg="black", fg="white")
                la.grid(row=6, column=0)
                l4 = Label(root, text=" Withdraw Amount", font=('Helvetica', '20' ), width=30, height=2,
                           borderwidth=12, bg="black", fg="white")
                l4.grid(row=5, column=0, sticky=E)
                self.m5 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
                self.m5.grid(row=5, column=3)
                b = Button(root, text="Withdraw", font=('Helvetica', '20' ), width=10, height=1, borderwidth=12,
                           bg="black", fg="white", command=self.withd)
                b.grid(row=6, column=3)
            else:
                pass

    def login_click_deposit(self):
        s2 = "select * from Bank"
        self.cur.execute(s2)
        rows = self.cur.fetchall()
        for row in rows:
            Username = row[0]
            AccountNo = row[1]
            AccountType = row[2]
            Balance = row[3]
            Password = row[4]
            if (row[4] == int(self.m4.get())):
                self.a = row[3]
            if ((self.m1.get() == Username) & (int(self.m2.get()) == int(AccountNo)) & (
                    self.m3.get() == AccountType) & (int(self.m4.get()) == int(Password))):
                root = Tk()
                la = Label(root, text="Login Successfully", font=('Helvetica', '20' ), width=30, height=2,
                           borderwidth=12, bg="black", fg="white")
                la.grid(row=6, column=0)

                l4 = Label(root, text="Deposit Amount", font=('Helvetica', '20' ), width=30, height=2,
                           borderwidth=12, bg="black", fg="white")
                l4.grid(row=5, column=0, sticky=E)
                self.m5 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
                self.m5.grid(row=5, column=3)
                b = Button(root, text="Deposit", font=('Helvetica', '20' ), width=10, height=1, borderwidth=12,
                           bg="black", fg="white", command=self.depo)
                b.grid(row=6, column=3)
                root.after(10000, lambda: root.destroy())
            else:
                pass
    def create_connection(self):
        self.conn = sqlite3.connect('bank')
        self.cur = self.conn.cursor()
        print('Connection created Successfully')

    def create_table(self):
        s = "create table Bank(Username TEXT,AccountNo INT,AccountType TEXT,Balance INT,Password INT)"
        self.cur.execute(s)
        self.conn.commit()
        tkinter.messagebox.showinfo("bank", "Table Created SuccessFully")

    def show_Table(self):
        print("Username AccountType AccountNo Balance \n")
        s2 = "select * from Bank"
        self.cur.execute(s2)
        rows = self.cur.fetchall()
        root = Tk()
        root.title("Accounts")
        l1 = Label(root, text="          Welcome To Our Bank         ", font=('Helvetica', '30' ), bg="magenta",
                   fg="white", borderwidth=12)
        l1.grid(row=1, column=0)
        i = 2
        for row in rows:
            Username = row[0]
            AccountNo = row[1]
            AccountType = row[2]
            Balance = row[3]
            Password = row[4]
            str1 = "Name:  " + row[0] + "  AccountNo:  " + str(row[1]) + "  AccountType:  " + row[
                2] + "  Balance:  " + str(row[3])
            li = Label(root, text=" {0} ".format(str(str1)), font=('Helvetica', '20' ), bg="black", fg="white",
                       borderwidth=12)
            li.grid(row=i, column=0, sticky=W)
            i = i + 1

    def delete(self):
        root = Tk()
        l4 = Label(root, text="Enter AccountNo", font=('Helvetica', '20' ), width=20, height=2,
                   borderwidth=12, bg="black", fg="white")
        l4.grid(row=5, column=0)
        self.de = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
        self.de.grid(row=6, column=0)
        b1 = Button(root, text="Delete", font=('Helvetica', '20' ), width=20, height=2, borderwidth=12,
                    bg="black", fg="white", command=self.delete_account)
        b1.grid(row=7, column=0)

    def Log(self):
        log=0
        c=0
        s2 = "select * from Bank"
        self.cur.execute(s2)
        rows = self.cur.fetchall()
        for row in rows:
            Username = row[0]
            AccountNo = row[1]
            AccountType = row[2]
            Balance = row[3]
            Password = row[4]
            if ((Password == int(self.k2.get())) & (Username == str(self.k1.get()))):
                self.bal = Balance
                tkinter.messagebox.showinfo("bank", "Login Successful:)")
                log = 1
            else:
                print(Username)
                print(Password)
                print(c)
                c=c+1
                pass
        self.L = 1
        self.O=self.bal
        

    def Login_Acc(self):
        root = Tk()
        root.title("Login")
        l2 = Label(root, text="Login", font=('Helvetica', '20' ), width=20, height=2, borderwidth=12,
                   bg="black", fg="white")
        l2.grid(row=0, column=1)
        l1 = Label(root, text="Username: ", font=('Helvetica', '20' ), width=30, height=2,
                   borderwidth=12, bg="black", fg="white")
        l1.grid(row=1, column=0, sticky=E)
        self.k1 = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
        self.k1.grid(row=1, column=1)
        l4 = Label(root, text="Password: ", font=('Helvetica', '20' ), width=30, height=2, borderwidth=12,
                   bg="black", fg="white")
        l4.grid(row=2, column=0, sticky=E)
        self.k2 = Entry(root, show="*", font=('Helvetica', '20' ), borderwidth=12)
        self.k2.grid(row=2, column=1)
        b = Button(root, text="Login", font=('Helvetica', '20' ), width=10, height=2, borderwidth=12,
                   bg="black", fg="white", command=self.Log)
        b.grid(row=3, column=1)
    

    def delete_account(self): 
        s2 = "select * from Bank"
        self.cur.execute(s2)
        rows = self.cur.fetchall()
        for row in rows:
            Username = row[0]
            AccountNo = row[1]
            if (AccountNo==int(self.de.get())):
                tkinter.messagebox.showinfo("bank", "{0} Your Account is Deleted Successfully".format(Username))
        k = ("DELETE FROM Bank WHERE AccountNo='%d'") % (int(self.de.get()))
        self.cur.execute(k)
        self.conn.commit()

    def Account_no(self):
        ans = tkinter.messagebox.askyesno("Bank", "Wanna Create Account???")
        if (ans == YES):
            tkinter.messagebox.showinfo("AccountNo",
                                        "Sir Your Account No is :{0}".format(int(random.randint(0, 100000))))
    def S_int(self):
        if(int(self.year.get()) < 0):
            tkinter.messagebox.showinfo("bank", "Year Cannot be Negative")
        else:
            s = 0
            if (int(self.year.get()) < 5 ):
                s = int(self.p.get())*int(self.year.get())*8/100
                tkinter.messagebox.showinfo("bank","Your Simple Interest is: {0}".format(s))
            elif (int(self.year.get()) > 5)&(int(self.year.get()) < 10):
                s = int(self.p.get()) * int(self.year.get())/10
                tkinter.messagebox.showinfo("bank", "Your Simple Interest is: {0}".format(s))
            else:
                s = int(self.p.get()) * int(self.year.get())*12/100
                tkinter.messagebox.showinfo("bank", "Your Simple Interest is: {0}".format(s))
    def Condition(self):
        root = Tk()
        l3 = Label(root, text="      Welcome To Our Bank      ", font=('Helvetica', '30' ), width=50, height=2, borderwidth=12,
                   bg="magenta", fg="white")
        l3.grid(row=0, column=0)
        str1="Deposit Money Conditons:\n \n1--->Deposit Money < 5 Years you will get 8% interest\n \n" \
             "2--->Deposit Money > 5 but <= 10 Years you will get 10% interest\n \n" \
             "3--->Deposit Money > 10 Years you will get 12% interest\n \n" \
             "SO Hurry UP!!!Deposit Money :)"
        l2 = Label(root, text="{0}".format(str1), font=('Helvetica', '30' ), width=50, height=10, borderwidth=12,
                   bg="black", fg="Yellow")
        l2.grid(row=1, column=0)
        root.mainloop()

    def  Simple_int(self):
        root=Tk()
        l2 = Label(root, text="Simple Interest", font=('Helvetica', '20' ), width=20, height=2, borderwidth=12,
                   bg="black", fg="white")
        l2.grid(row=0, column=1)
        root.title("Simple Interest")
        l1 = Label(root, text="Principle Amount:  ", font=('Helvetica', '20' ), width=20, height=2, borderwidth=12,
                   bg="black", fg="white")
        l1.grid(row=1, column=0, sticky=E)
        self.p = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
        self.p.grid(row=1, column=1)

        l3 = Label(root, text="Years: ", font=('Helvetica', '20' ), width=20, height=2, borderwidth=12,
                   bg="black", fg="white")
        l3.grid(row=2, column=0, sticky=E)
        self.year = Entry(root, font=('Helvetica', '20' ), borderwidth=12)
        self.year.grid(row=2, column=1)
        b1 = Button(root, text="calculate", font=('Helvetica', '20' ), width=15, height=2, borderwidth=12,
                    bg="black", fg="white", activebackground="white", activeforeground="black",
                    command=self.S_int)
        b1.grid(row=3,column=1)


B = Bank("a", "b", "c", "d", 1, "f", 1, "h", 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0)


class call:
    b1 = Button(root, text="Create Account", font=('Helvetica', '20' ), width=20, height=2, borderwidth=12,
                bg="black", fg="white", activebackground="white", activeforeground="black",
                command=B.create_account_click)
    b2 = Button(root, text="Deposit", font=('Helvetica', '20' ), width=10, height=2, borderwidth=12, bg="black",
                fg="white",
                command=B.deposit_click)
    b3 = Button(root, text="Withdraw", font=('Helvetica', '20' ), width=10, height=2, borderwidth=12,
                bg="black", activebackground="white", activeforeground="black", fg="white", command=B.withdraw_click)
    b4 = Button(root, text="Balance", font=('Helvetica', '20' ), activebackground="white", activeforeground="black",
                width=10, height=2, borderwidth=12, bg="black", fg="white", command=B.balance)
    b5 = Button(root, text="Accounts", font=('Helvetica', '20' ), width=10, height=2, borderwidth=12,
                activebackground="white", activeforeground="black",
                bg="black", fg="white", command=B.show_Table)
    b6 = Button(root, text="Delete Account", font=('Helvetica', '20' ), width=17, height=2, borderwidth=12,
                activebackground="white", activeforeground="black",
                bg="red", fg="white", command=B.delete)
    b7 = Button(root, text="Logout", font=('Helvetica', '20' ), width=10, height=2, borderwidth=12,
                activebackground="white", activeforeground="black",
                bg="red", fg="white", command=B.Logout)
    b8 = Button(root, text="Get Account no", font=('Helvetica', '20' ), width=20, height=2, borderwidth=12,
                bg="black", fg="white", command=B.Account_no)
    b9 = Button(root, text="Profile", font=('Helvetica', '20' ), width=15, height=2, borderwidth=12,
                bg="green", fg="white", command=B.profile)
    b10 = Button(root, text="Transfer Balance", font=('Helvetica', '20' ), width=17, height=2, borderwidth=12,
                 bg="blue", fg="white", command=B.transfer_bal)
    b11 = Button(root, text="Login", font=('Helvetica', '20' ), width=15, height=2, borderwidth=12,
                 bg="blue", fg="white", command=B.Login_Acc)
    b12 = Button(root, text="Simple Interest", font=('Helvetica', '20'), width=17, height=2, borderwidth=12,
                 bg="white", fg="black", command=B.Simple_int)
    b13 = Button(root, text="Terms & Condition", font=('Helvetica','20'), width=17, height=2, borderwidth=12,
                 bg="white", fg="black", command=B.Condition)
    b1.grid(row=3, column=2)
    b2.grid(row=6, column=1)
    b3.grid(row=6, column=3)
    b4.grid(row=7, column=1)
    b5.grid(row=7, column=3)
    b6.grid(row=10, column=4)
    b7.grid(row=0, column=4)
    b8.grid(row=10, column=2)
    b9.grid(row=0, column=2)
    b10.grid(row=10, column=0)
    b11.grid(row=0, column=0)
    b12.grid(row=3, column=0)
    b13.grid(row=3, column=4)
    B.create_connection()
    B.create_table()#remove once you create table 
    B.Account_no()
root.mainloop()



