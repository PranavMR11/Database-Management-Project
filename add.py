from tkinter import *
from tkinter import messagebox
import psycopg2

def addrecord():
    conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='rishab',
    database='bank',
    port='5432')

    cur = conn.cursor()
    cif=CIFNumber.get()
    name=Name.get()
    id=uid.get()
    uname=username.get()
    passs=password.get()
    phno=Ph.get()
    em=email.get()
    
    qwr = f'insert into customer values(\'{cif}\',\'{name}\',\'{id}\',\'{uname}\',\'{passs}\',\'{phno}\',\'{em}\')'
    try:
        #qwr = 'insert into customer values(\'12345678221\',\'JONES\',\'9878123498763230\',\'01JONES20\',\'JONES123\',\'9365352517\',\'JONES1@XYZ.COM\')'
        cur.execute(qwr)
        conn.commit()
        messagebox.showinfo('Success',"Record succesfully inserted")
    except BaseException as err:
        messagebox.showinfo('fail',f"Unexpected {err=}, {type(err)=}")
    cur.close()
    conn.close()


def addRecordui():

    global CIFNumber,Name,uid,username,password,Ph,email, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Bank")
    root.minsize(width=400, height=400)
    root.geometry("700x600")
    
    table='CUSTOMER' 

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Customer Record", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.75)

    lb1 = Label(labelFrame, text="CIFNumber", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    CIFNumber = Entry(labelFrame)
    CIFNumber.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame, text="Name", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.30, relheight=0.08)
    Name = Entry(labelFrame)
    Name.place(relx=0.3, rely=0.30, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame, text="UID : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.40, relheight=0.08)
    uid= Entry(labelFrame)
    uid.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame, text="UserName : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.50, relheight=0.08)
    username = Entry(labelFrame)
    username.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)
    
    lb5 = Label(labelFrame, text="password : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.60, relheight=0.08)
    password = Entry(labelFrame)
    password.place(relx=0.3, rely=0.60, relwidth=0.62, relheight=0.08)
    
    lb6= Label(labelFrame, text="CustomerPH : ", bg='black', fg='white')
    lb6.place(relx=0.05, rely=0.70, relheight=0.08)
    Ph = Entry(labelFrame)
    Ph.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)
    
    lb7 = Label(labelFrame, text="email : ", bg='black', fg='white')
    lb7.place(relx=0.05, rely=0.80, relheight=0.08)
    email = Entry(labelFrame)
    email.place(relx=0.3, rely=0.80, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0',command=addrecord, fg='black')
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

if __name__=='__main__':
    addRecordui()
