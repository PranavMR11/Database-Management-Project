from tkinter import *
from tkinter import messagebox
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='rishab',
    database='bank',
    port='5432')
    
cur = conn.cursor()

def exeqry():
    qry = q.get()
    if qry.split()[0]=='select':
        try:
            cur.execute(qry)
            conn.commit()
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

if __name__=='__main__':
        exe()