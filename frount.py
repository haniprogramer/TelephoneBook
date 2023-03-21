from tkinter import *
import phonebac

root = Tk()
root.title('Telephone Book')
root.geometry('390x505')
root.resizable(width=False, height=False)
root.configure(bg='light yellow')


trackfram=LabelFrame(root,text='Entry track',font=('Arial',11,'bold'),bg='light yellow',bd=5,fg='black')
trackfram.place(x=5,y=200,width=380,height=160)

# --------LABEL----------
lname = Label(root, text='NAME', bg='light yellow',font=('Arial',10,'bold'))
lname.place(x=50,y=230)

lnumber = Label(root, text='NUMBER', bg='light yellow',font=('Arial',10,'bold'))
lnumber.place(x=50,y=260)

lemail = Label(root, text='EMAIL', bg='light yellow',font=('Arial',10,'bold'))
lemail.place(x=50,y=290)

lgroph = Label(root, text='GROPH', bg='light yellow',font=('Arial',10,'bold'))
lgroph.place(x=50,y=320)


# ---------Entries---------

nametaxt = StringVar()
ename = Entry(root, textvariable=nametaxt, width=24,font=('Arial',9,'bold'),bd=1.25)
ename.place(x=175,y=230)

numbertaxt = StringVar()
enumber = Entry(root, textvariable=numbertaxt, width=24,font=('Arial',9,'bold'),bd=1.25)
enumber.place(x=175,y=260)

emailtaxt = StringVar()
eemail = Entry(root, textvariable=emailtaxt, width=24,font=('Arial',9,'bold'),bd=1.25)
eemail.place(x=175,y=290)

grophtext = StringVar()
egroph = Entry(root, textvariable=grophtext, width=24,font=('Arial',9,'bold'),bd=1.25)
egroph.place(x=175,y=320)


# ----------------------listbox---------------------
fram=LabelFrame(root,text='Phone book list',font=('Arial',11,'bold'),bg='light yellow',bd=5,fg='black',pady=10)
fram.place(x=5,y=0,width=380,height=200)
list1 = Listbox(fram, width=43, height=10,font=('Arial',11),selectbackground='gold')
list1.place(x=5,y=-5,width=345,height=160)

sb1 = Scrollbar(fram,)
sb1.place(x=352, y=50)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


def get_selected_row(x):
    global selected

    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected = list1.get(index)
        # name
        ename.delete(0, END)
        ename.insert(END, selected[1])
        # number
        enumber.delete(0, END)
        enumber.insert(END, selected[2])
        # email
        eemail.delete(0, END)
        eemail.insert(END, selected[3])
        # groph
        egroph.delete(0, END)
        egroph.insert(END, selected[4])


list1.bind("<<ListboxSelect>>", get_selected_row)


# ----------------function---------------
def clear_list():
    list1.delete(0, END)


def fill_list(books):
    for book in books:
        list1.insert(END, book)


# -------------button--------------

def view_command():
    clear_list()
    books = phonebac.view()
    fill_list(books)

def search_command():
    clear_list()
    books = phonebac.search(nametaxt.get(), numbertaxt.get(), emailtaxt.get(), grophtext.get())
    fill_list(books)


contorolpanel=LabelFrame(root,text='Contorol Panel',font=('Arial',11,'bold'),bg='light yellow',bd=5,fg='black',pady=10)
contorolpanel.place(x=5,y=359,width=380,height=140)
bView = Button(root, text='View All', width=19, command=lambda: view_command(), bg='gold',font=('Arial',10,'bold'))
bView.place(x=15,y=385)


bSearch = Button(root, text='Search Entry', width=19, command=search_command, bg='gold',font=('Arial',10,'bold'))
bSearch.place(x=200,y=385)


def add_command():
    phonebac.insert(nametaxt.get(), numbertaxt.get(), emailtaxt.get(), grophtext.get())
    view_command()
bAdd = Button(root, text='Add Entry', width=19, command=add_command, bg='gold',font=('Arial',10,'bold'))
bAdd.place(x=15,y=420)

def update_command():
    phonebac.update(selected[0], nametaxt.get(), numbertaxt.get(), emailtaxt.get(), grophtext.get())
    view_command()
bUpdate = Button(root, text='Update Selected', width=19, command=update_command, bg='gold',font=('Arial',10,'bold'))
bUpdate.place(x=200,y=420)



def delet_command():
    phonebac.delet(selected[0])
    view_command()
bDelet = Button(root, text='Delet Selected', width=19,bg='gold', command=delet_command,font=('Arial',10,'bold'))
bDelet.place(x=15,y=455)


bClose= Button(root, text='Close', width=19, command=root.destroy ,bg='red',font=('Arial',10,'bold'))
bClose.place(x=200,y=455)



view_command()
root.mainloop()