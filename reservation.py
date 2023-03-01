import tkinter
import tkinter.messagebox


class MyGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('300x500')
        self.main_window.title("Joe's Burger's")

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame8 = tkinter.Frame(self.main_window)
        self.frame9 = tkinter.Frame(self.main_window)
        self.frame10 = tkinter.Frame(self.main_window)
        self.frame11 = tkinter.Frame(self.main_window)
        self.frame12 = tkinter.Frame(self.main_window)
        self.frame13 = tkinter.Frame(self.main_window)

        self.nameLabel = tkinter.Label(self.frame1, text="Name:")
        self.nameEntry = tkinter.Entry(self.frame1, width=30)

        self.nameLabel.pack(side='left')
        self.nameEntry.pack(side='right', anchor='ne')

        self.dummyLabel = tkinter.Label(self.frame2, text="")
        self.dummyLabel.pack(side='left')

        self.phoneLabel = tkinter.Label(self.frame3, text="Phone:")
        self.phoneEntry = tkinter.Entry(self.frame3, width=20)

        self.phoneLabel.pack(side='left')
        self.phoneEntry.pack(side='right')

        self.dummyLabel2 = tkinter.Label(self.frame4, text="")
        self.dummyLabel2.pack(side='left')

        self.numberLabel = tkinter.Label(
            self.frame5, text="Number in your party:")
        self.numberEntry = tkinter.Entry(self.frame5, width=5)

        self.numberLabel.pack(side='left')
        self.numberEntry.pack(side='right')

        self.dummyLabel3 = tkinter.Label(self.frame6, text="")
        self.dummyLabel3.pack(side='left')

        self.dateLabel = tkinter.Label(self.frame7, text='Reservation Date:')
        self.radio_var = tkinter.IntVar()

        self.dateRB1 = tkinter.Radiobutton(
            self.frame8, text='March 1 2023', variable=self.radio_var, value='3/1/23', command=self.show_choice)
        self.dateRB2 = tkinter.Radiobutton(
            self.frame8, text='March 2 2023', value='3/2/23', command=self.show_choice)
        self.dateRB3 = tkinter.Radiobutton(
            self.frame8, text='March 3 2023', value='3/3/23', command=self.show_choice)

        self.dateLabel.pack(side='left', anchor='w')
        self.dateRB1.pack(anchor='e')
        self.dateRB2.pack(anchor='e')
        self.dateRB3.pack(anchor='e')

        self.dummyLabel4 = tkinter.Label(self.frame9, text="")
        self.dummyLabel4.pack(side='left')

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.optionsLabel = tkinter.Label(
            self.frame10, text='Please select all that apply:')
        self.option1 = tkinter.Checkbutton(
            self.frame11, text='Gluten Free   ', variable=self.cb_var1)
        self.option2 = tkinter.Checkbutton(
            self.frame11, text='Vegan         ', variable=self.cb_var2)
        self.option3 = tkinter.Checkbutton(
            self.frame11, text='Peanut Allergy', variable=self.cb_var3)

        self.optionsLabel.pack(anchor='w')
        self.option1.pack(anchor='w')
        self.option2.pack(anchor='w')
        self.option3.pack(anchor='w')

        self.dummyLabel5 = tkinter.Label(self.frame12, text="")
        self.dummyLabel5.pack(side='left')

        self.submitButton = tkinter.Button(
            self.frame13, text="Submit", command=self.reserve)
        self.dummyLabel6 = tkinter.Label(self.frame13, text="", width=20)
        self.cancelButton = tkinter.Button(
            self.frame13, text="Cancel", command=self.main_window.destroy)

        self.submitButton.pack(side='left', anchor='w')
        self.dummyLabel6.pack(side='left', anchor='c')
        self.cancelButton.pack(side='right', anchor='e')

        self.frame1.pack(anchor='w')
        self.frame2.pack(anchor='w')
        self.frame3.pack(anchor='w')
        self.frame4.pack(anchor='w')
        self.frame5.pack(anchor='w')
        self.frame6.pack(anchor='w')
        self.frame7.pack(anchor='w')
        self.frame8.pack(anchor='c')
        self.frame9.pack(anchor='w')
        self.frame10.pack(anchor='w')
        self.frame11.pack(anchor='c')
        self.frame12.pack(anchor='w')
        self.frame13.pack(anchor='c')

        tkinter.mainloop()

    def reserve(self):
        if self.nameEntry == '':
            reserve = False
            tkinter.messagebox.showinfo(
                title="Missing Info", message="Please fill out your name")

        if self.phoneEntry == '':
            reserve = False
            tkinter.messagebox.showinfo(
                title="Missing Info", message="Please Give us your phone number")

        reserve = True

        if reserve:
            tkinter.messagebox.showinfo(
                'Success', 'Your reservation is confirmed for ' + self.radio_var.get())


myDinner = MyGUI()
