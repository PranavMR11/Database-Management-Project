from tkinter import *
from tkinter import messagebox,ttk
import psycopg2

def Viewc():
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='rishab',
        database='bank',
        port='5432')

    cur = conn.cursor()
    
    root = Tk()
    root.title("View Customer Records")
    root.geometry("900x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.0, relwidth=0.5, relheight=0.1)
    headingLabel = Label(headingFrame1, text="Existing Customer Records", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    fr = Frame(root)
    fr.place(relx=0.004, rely=0.15, relwidth=1, relheight=0.5)
    l = ttk.Treeview(fr)
    

    l['columns'] = ('CIF', 'Name', 'Uid', 'Phone Number','E-mail')

    l.column("#0", width=0,  stretch=NO)
    l.column("CIF",anchor=CENTER, width=120)
    l.column("Name",anchor=CENTER,width=100)
    l.column("Uid",anchor=CENTER,width=120)
    l.column("Phone Number",anchor=CENTER,width=100)
    l.column("E-mail",anchor=CENTER,width=130)

    l.heading("#0",text="",anchor=CENTER)
    l.heading("CIF",text="CIF",anchor=CENTER)
    l.heading("Name",text='Name',anchor=CENTER)
    l.heading("Uid",text="Uid",anchor=CENTER)
    l.heading("Phone Number",text="Phone Number",anchor=CENTER)
    l.heading("E-mail",text="E-mail",anchor=CENTER)

    qwy = 'select * from customer'
    
    try:
        cur.execute(qwy)
        conn.commit()
        rows=cur.fetchall()
        x=0
        for i in rows:
            l.insert(parent='',index='end',iid=x,text='', values=(i[0],i[1],i[2],i[5],i[6]))
            x+=1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    l.pack()

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    cur.close()
    conn.close()

    root.mainloop()

def Viewl():
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='rishab',
        database='bank',
        port='5432')

    cur = conn.cursor()

    root = Tk()
    root.title("View Loan Records")
    root.geometry("900x600")
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.0, relwidth=0.5, relheight=0.1)
    headingLabel = Label(headingFrame1, text="Existing Loan Records", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    fr = Frame(root)
    fr.place(relx=0.004, rely=0.15, relwidth=1, relheight=0.5)
    l = ttk.Treeview(fr)
    

    l['columns'] = ('Loan ID','CIF Number','Account Number','Loan Duration','Loan Type','Loan Amount','Interest')

    l.column("#0", width=0,  stretch=NO)
    l.column("Loan ID",anchor=CENTER, width=100)
    l.column("CIF Number",anchor=CENTER,width=100)
    l.column("Account Number",anchor=CENTER,width=100)
    l.column("Loan Duration",anchor=CENTER,width=100)
    l.column("Loan Type",anchor=CENTER,width=100)
    l.column("Loan Amount",anchor=CENTER,width=100)
    l.column("Interest",anchor=CENTER,width=100)

    l.heading("#0",text="",anchor=CENTER)
    l.heading("Loan ID",text="Loan Id",anchor=CENTER)
    l.heading("CIF Number",text="Cif Number",anchor=CENTER)
    l.heading("Account Number",text="Account Number",anchor=CENTER)
    l.heading("Loan Duration",text="Loan Duration",anchor=CENTER)
    l.heading("Loan Type",text="Loan Type",anchor=CENTER)
    l.heading("Loan Amount",text="Loan Amount",anchor=CENTER)
    l.heading("Interest",text="Interest",anchor=CENTER)

    qwy='select * from loans'
    
    try:
        cur.execute(qwy)
        conn.commit()
        x=0
        for i in cur:
            l.insert(parent='',index='end',iid=x,text='', values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            x+=1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    l.pack()

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    cur.close

    root.mainloop()
    
    
if __name__=='__main__':
        Viewc()

