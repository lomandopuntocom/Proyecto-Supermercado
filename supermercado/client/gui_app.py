from tkinter import *

root = Tk()

root.title('Market Manager')
root.geometry('1024x624')

head = Label(root, text='Manager', font=('times new roman', 30, 'bold'), bg='DarkOrange1', fg='white', bd=10, relief=RIDGE)
head.pack(fill=X)

customer_details = LabelFrame(root, text='Customer Details', font=('arial', 15, 'bold'), bg='navy', fg='white', bd=6, relief= GROOVE)
customer_details.pack(fill=X)

customer_label = Label(customer_details, text='Name', font=("arial", 15, 'bold'), fg='white', bg='navy')
customer_label.grid(row=0,column=0,padx=30)

name_entry = Entry(customer_details, font=('arial', 10, 'bold'), fg= 'black', bg='white', bd= 2,  relief=GROOVE, width=18)
name_entry.grid(row=0, column=1)

accept_button = Button(customer_details, text='accept')
accept_button.grid(row=0, column=2)

root.mainloop()
