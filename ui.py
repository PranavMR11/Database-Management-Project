from tkinter import *
from tkinter import messagebox,ttk
import psycopg2
import add

def Viewc():
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
    
    scroll = Scrollbar(fr)
    scroll.pack(side=RIGHT, fill=Y)

    l = ttk.Treeview(fr, yscrollcommand = scroll.set, xscrollcommand = scroll.set)    

    l['columns'] = ('CIF', 'Name', 'Uid', 'Phone Number','E-mail')

    l.column("#0", width=0,  stretch=NO)
    l.column("CIF",anchor=CENTER, width=120)
    l.column("Name",anchor=CENTER,width=100)
    l.column("Uid",anchor=CENTER,width=120)
    l.column("Phone Number",anchor=CENTER,width=100)
    l.column("E-mail",anchor=CENTER,width=140)

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

def Viewa():
    root = Tk()
    root.title("View Accounts")
    root.geometry("900x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.0, relwidth=0.5, relheight=0.1)
    headingLabel = Label(headingFrame1, text="Existing Account Records", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    fr = Frame(root)
    fr.place(relx=0.004, rely=0.15, relwidth=1, relheight=0.5)
    
    scroll = Scrollbar(fr)
    scroll.pack(side=RIGHT, fill=Y)

    l = ttk.Treeview(fr, yscrollcommand = scroll.set, xscrollcommand = scroll.set)    

    l['columns'] = ('Account Number','Branch ID','CIF number','Balance')

    l.column("#0", width=0,  stretch=NO)
    l.column("Account Number",anchor=CENTER, width=120)
    l.column("Branch ID",anchor=CENTER,width=100)
    l.column("CIF number",anchor=CENTER,width=120)
    l.column("Balance",anchor=CENTER,width=100)

    l.heading("#0",text="",anchor=CENTER)
    l.heading("Account Number",text="Account Number",anchor=CENTER)
    l.heading("Branch ID",text='Branch ID',anchor=CENTER)
    l.heading("CIF number",text="CIF number",anchor=CENTER)
    l.heading("Balance",text="Balance",anchor=CENTER)

    qwy = 'select * from account'
    
    try:
        cur.execute(qwy)
        conn.commit()
        rows=cur.fetchall()
        x=0
        for i in rows:
            l.insert(parent='',index='end',iid=x,text='', values=(i[0],i[1],i[2],i[3]))
            x+=1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    l.pack()

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    
def Viewl():
    conn = psycopg2.connect(
        host='127.0.0.1',
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
    
    scroll = Scrollbar(fr)
    scroll.pack(side=RIGHT, fill=Y)
    l = ttk.Treeview(fr, yscrollcommand = scroll.set, xscrollcommand = scroll.set) 
    

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
            l.insert(parent='',index='end',iid=x,text='', values=i)
            #(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            x+=1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    l.pack()

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    cur.close

    root.mainloop()

def exeqry():
    qry = q.get()
    try:
        cur.execute(qry)
        conn.commit()
        if qry.split()[0]=='select':
            root1 = Tk()
            root1.title("Select Query")
            root1.geometry("900x600")
            Canvas1 = Canvas(root1)
            Canvas1.config(bg="#12a4d9")
            Canvas1.pack(expand=True, fill=BOTH)
            fr = Frame(root1)
            fr.place(relx=0.004, rely=0.15, relwidth=1, relheight=0.5)
            
            scroll = Scrollbar(fr)
            scroll.pack(side=RIGHT, fill=Y)
            l = ttk.Treeview(fr, yscrollcommand = scroll.set, xscrollcommand = scroll.set)
            l.column("#0", width=0,  stretch=NO) 
            l.heading("#0",text="",anchor=CENTER)
            
            
            col = [d[0] for d in cur.description]
            l['columns'] = col
            for dec in col:
                l.column(dec,anchor=CENTER, width=100)
                l.heading(dec,text=dec,anchor=CENTER)               
                
            x=0
            for i in cur.fetchall():                
                l.insert(parent='',index='end',iid=x,text='', values=i)
                x+=1
            l.pack()           
        
        messagebox.showinfo('Success',"SQL Query Executed")
    except BaseException as err:
        messagebox.showinfo('fail',f"Unexpected {err=}, {type(err)=}")

def exe():
    global q
    root = Tk()
    root.title('Excute Query')
    root.minsize(width=700, height=600)
    root.geometry('700x600')
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)
    
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="EXECUTE QUERY", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.5)
    lb1 = Label(labelFrame, text="Enter Query : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    
    q = Entry(labelFrame)
    q.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    
    exBtn = Button(root, text="EXECUTE", bg='#d1ccc0',command = exeqry, fg='black')
    exBtn.place(relx=0.25, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.55, rely=0.9, relwidth=0.18, relheight=0.08)
    
    root.mainloop()


conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='rishab',
        database='bank',
        port='5432'
    )
cur = conn.cursor()
print('Postgres')
cur.execute('SELECT version()')
v = cur.fetchone()
print(v)
root = Tk()
root.title('Bank')
root.minsize(width=700, height=600)
root.geometry('700x600')
headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="NorthLand Bank", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Customer Record", bg='black', fg='white',command = add.addRecordui )
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Customer Record", bg='black', fg='white', command = Viewc )
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="View Customer Loans", bg='black', fg='white',command = Viewl)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="View Accounts", bg='black', fg='white', command = Viewa )
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="Execute Query", bg='black', fg='white',command = exe)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()

cur.close()
conn.close()
