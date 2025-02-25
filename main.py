from tkinter import *
from tkinter import messagebox


class Event:
    def __init__(self, name, date, time, location):
        self.__name = name
        self.__date = date
        self.__time = time
        self.__location = location

    def GetName(self):
        return self.__name

    def GetDate(self):
        return self.__date

    def GetTime(self):
        return self.__time

    def GetLocation(self):
        return self.__location

    def GetInfo(self):
        print(
            f"Event Name: {self.__name} \nEvent Date: {self.__date} \nEvent Time: {self.__time} \nEvent Location: {self.__location}")


root = Tk()
root.title("Event Management System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position to open in the center
window_width = 500
window_height = 500
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


def CreateEvent():
    frame.place_forget()
    frame2.place(x=0, y=0)


def AddOrganizer():
    frame2.place_forget()
    frame3.place(x=0, y=0)


def AddParticipant():
    frame3.place_forget()
    frame4.place(x=0, y=0)


def DisplayEvents():
    frame4.place_forget()
    frame5.place(x=0, y=0)


def DeleteEvent():
    frame5.place_forget()
    frame6.place(x=0, y=0)


def UpdateEvent():
    frame6.place_forget()
    frame7.place(x=0, y=0)


frame = Frame(bg="white", width=500, height=500)
frame.grid(row=0, column=0, sticky="nsew")

root.rowconfigure(0, weight=1, minsize=500)
root.columnconfigure(0, weight=1, minsize=500)
root.maxsize(500, 500)

photo1 = PhotoImage(file="EMS.png")
lblbookphoto = Label(frame, image=photo1, width=500, height=200)
lblbookphoto.place(x=0, y=0)

lbl = Label(frame, text="MENU", width=20, background="#A9B388", foreground="white", font=("Times New Roman", 15))
lbl.place(x=0, y=215)

btn_createEvent = Button(frame, text="Create Event", width=15, bg="#acc18a", fg="white", command=CreateEvent)
btn_createEvent.place(x=0, y=250)

btn_addOrganizer = Button(frame, text="Add Organizer", width=15, bg="#acc18a", fg="white", command=AddOrganizer)
btn_addOrganizer.place(x=0, y=285)

btn_addParticipant = Button(frame, text="Add Participant", width=15, bg="#acc18a", fg="white", command=AddParticipant)
btn_addParticipant.place(x=0, y=320)

btn_displayEvents = Button(frame, text="Display Events", width=15, bg="#acc18a", fg="white", command=DisplayEvents)
btn_displayEvents.place(x=0, y=355)

btn_displayEvents = Button(frame, text="Delete Event", width=15, bg="#acc18a", fg="white", command=DeleteEvent)
btn_displayEvents.place(x=0, y=390)

btn_updateEvents = Button(frame, text="Update Event", width=15, bg="#acc18a", fg="white", command=UpdateEvent)
btn_updateEvents.place(x=0, y=425)

# ===================================================================================================================================


frame2 = Frame(bg="white", width=500, height=500)

lbl2 = Label(frame2, text="Create Event", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl2.place(x=140, y=0)


def save_events():
    with open("events.txt", "w") as file:
        for event in lb_createevent.get(0, END):
            file.write(event + "\n")
        for event in lb_addorganizer.get(0, END):
            file.write(event + "\n")
        for event in lb_addparticipant.get(0, END):
            file.write(event + "\n")
    return "Events saved successfully"


def is_valid_date(date):
    return all(char.isdigit() or char.isspace() or char == '/' for char in date)


def is_valid_time(time):
    return all(char.isdigit() or char == ':' for char in time)


def Create():
    name_event = entryname.get()
    date_event = entrydate.get()
    time_event = entrytime.get()
    location_event = entrylocation.get()

    if len(name_event) <= 3:
        messagebox.showwarning("Warning", "Event must be at least 3 characters long.")
        return

    if not is_valid_date(date_event):
        messagebox.showwarning("Warning", "Invalid date format. Use only numbers and spaces.")
        return

    if not is_valid_time(time_event):
        messagebox.showwarning("Warning", "Invalid time format. Use only numbers and colons.")
        return

    new_event = Event(name_event, date_event, time_event, location_event)

    # Add the event to the ls list
    ls.append(new_event.GetInfo())

    lb_createevent.insert(END, name_event)
    lb_createevent.insert(END, date_event)
    lb_createevent.insert(END, time_event)
    lb_createevent.insert(END, location_event)

    save_events()

    entryname.delete(0, END)
    entrydate.delete(0, END)
    entrytime.delete(0, END)
    entrylocation.delete(0, END)

    frame2.place_forget()
    frame.place(x=0, y=0)


ls = []


def Back1():
    frame2.place_forget()
    frame.place(x=0, y=0)


eventname = Label(frame2, text="Event Name", width=20, background="#acc18a", foreground="white",
                  font=("Times New Roman", 12))
eventname.place(x=0, y=50)

entryname = Entry(frame2, width=30, font=("Arial", 10))
entryname.place(x=215, y=50)

eventdate = Label(frame2, text="Event Date", width=20, background="#acc18a", foreground="white",
                  font=("Times New Roman", 12))
eventdate.place(x=0, y=100)

entrydate = Entry(frame2, width=30, font=("Arial", 10))
entrydate.place(x=215, y=100)

eventtime = Label(frame2, text="Event Time", width=20, background="#acc18a", foreground="white",
                  font=("Times New Roman", 12))
eventtime.place(x=0, y=150)

entrytime = Entry(frame2, width=30, font=("Arial", 10))
entrytime.place(x=215, y=150)

eventlocation = Label(frame2, text="Event Location", width=20, background="#acc18a", foreground="white",
                      font=("Times New Roman", 12))
eventlocation.place(x=0, y=200)

entrylocation = Entry(frame2, width=30, font=("Arial", 10))
entrylocation.place(x=215, y=200)

btncreate = Button(frame2, text="Create", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                   command=Create)
btncreate.place(x=150, y=300)

btnback1 = Button(frame2, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back1)
btnback1.place(x=25, y=400)

# ====================================================================================================================================================


frame3 = Frame(bg="white", width=500, height=500)


def AddOrganizer():
    name_organizer = entry_organizername.get()
    email_organizer = entry_organizeremail.get()

    if len(name_organizer) <= 3:
        messagebox.showwarning("Warning", "Organizer name must be at least 3 characters long.")
        return

    lb_addorganizer.insert(END, name_organizer)
    lb_addorganizer.insert(END, email_organizer)

    save_events()

    entry_organizername.delete(0, END)
    entry_organizeremail.delete(0, END)

    frame3.place_forget()
    frame.place(x=0, y=0)


def Back2():
    frame3.place_forget()
    frame.place(x=0, y=0)


lbl3 = Label(frame3, text="Add Organizer", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl3.place(x=140, y=0)

organizername = Label(frame3, text="Organizer Name", width=20, background="#acc18a", foreground="white",
                      font=("Times New Roman", 12))
organizername.place(x=0, y=50)

entry_organizername = Entry(frame3, width=30, font=("Arial", 10))
entry_organizername.place(x=215, y=50)

organizeremail = Label(frame3, text="Organizer Email", width=20, background="#acc18a", foreground="white",
                       font=("Times New Roman", 12))
organizeremail.place(x=0, y=100)

entry_organizeremail = Entry(frame3, width=30, font=("Arial", 10))
entry_organizeremail.place(x=215, y=100)

btnadd_organizer = Button(frame3, text="Add", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                          command=AddOrganizer)
btnadd_organizer.place(x=150, y=150)

btnback2 = Button(frame3, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back2)
btnback2.place(x=25, y=300)

# ==================================================================================================================================================================


frame4 = Frame(bg="white", width=500, height=500)


def AddParticipant():
    name_participant = entry_participantname.get()
    email_participant = entry_participantemail.get()

    if len(name_participant) <= 3:
        messagebox.showwarning("Warning", "Participant name must be at least 3 characters long.")
        return

    lb_addparticipant.insert(END, name_participant)
    lb_addparticipant.insert(END, email_participant)

    save_events()

    entry_participantname.delete(0, END)
    entry_participantemail.delete(0, END)

    frame4.place_forget()
    frame.place(x=0, y=0)


def Back3():
    frame4.place_forget()
    frame.place(x=0, y=0)


lbl4 = Label(frame4, text="Add Participant", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl4.place(x=140, y=0)

participantname = Label(frame4, text="Participant Name", width=20, background="#acc18a", foreground="white",
                        font=("Times New Roman", 12))
participantname.place(x=0, y=50)

entry_participantname = Entry(frame4, width=30, font=("Arial", 10))
entry_participantname.place(x=215, y=50)

participantemail = Label(frame4, text="Participant Email", width=20, background="#acc18a", foreground="white",
                         font=("Times New Roman", 12))
participantemail.place(x=0, y=100)

entry_participantemail = Entry(frame4, width=30, font=("Arial", 10))
entry_participantemail.place(x=215, y=100)

btnadd_participant = Button(frame4, text="Add", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                            command=AddParticipant)
btnadd_participant.place(x=150, y=150)

btnback3 = Button(frame4, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back3)
btnback3.place(x=25, y=300)

# ============================================================================================================================================================================


frame5 = Frame(bg="white", width=500, height=500)


def Back4():
    frame5.place_forget()
    frame.place(x=0, y=0)


lbl5 = Label(frame5, text="Display Events", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl5.place(x=140, y=0)

lbl_event = Label(frame5, text="Events Information", width=20, background="#acc18a", foreground="white",
                  font=("Times New Roman", 15))
lbl_event.place(x=0, y=50)

lb_createevent = Listbox(frame5, bg="#FAEED1", width=20, height=10, fg="#5a572a", font=("Times New Roman", 15))
lb_createevent.place(x=7, y=80)

lbl_organizer = Label(frame5, text="Organizer Information", width=20, background="#acc18a", foreground="white",
                      font=("Times New Roman", 15))
lbl_organizer.place(x=250, y=50)

lb_addorganizer = Listbox(frame5, bg="#FAEED1", width=20, height=5, fg="#5a572a", font=("Times New Roman", 15))
lb_addorganizer.place(x=262, y=80)

lbl_participant = Label(frame5, text="Participant Information", width=20, background="#acc18a", foreground="white",
                        font=("Times New Roman", 15))
lbl_participant.place(x=250, y=220)

lb_addparticipant = Listbox(frame5, bg="#FAEED1", width=20, height=5, fg="#5a572a", font=("Times New Roman", 15))
lb_addparticipant.place(x=262, y=250)

btnback4 = Button(frame5, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back4)
btnback4.place(x=30, y=370)

# =============================================================================================================================================


frame6 = Frame(bg="white", width=500, height=500)


def Delete():
    delete_text = entry_delete.get().strip().lower()
    items_event = lb_createevent.get(0, END)
    items_organizer = lb_addorganizer.get(0, END)
    items_participant = lb_addparticipant.get(0, END)

    # Find the selected event
    event_index = -1
    for index_event, item_event in enumerate(items_event):
        if delete_text in item_event.lower():
            event_index = index_event
            break

    # Delete event information
    if event_index >= 0:
        lb_createevent.delete(event_index)
        lb_createevent.delete(event_index)
        lb_createevent.delete(event_index)
        lb_createevent.delete(event_index)

        # Delete associated organizer information
        organizer_index = event_index // 4  # Each event has 4 lines of information
        lb_addorganizer.delete(organizer_index * 2)  # Delete organizer name
        lb_addorganizer.delete(organizer_index * 2)  # Delete organizer email

        # Delete associated participant information
        participant_index = event_index // 4  # Each event has 4 lines of information
        lb_addparticipant.delete(participant_index * 2)  # Delete participant name
        lb_addparticipant.delete(participant_index * 2)  # Delete participant email

        save_events()

        entry_delete.delete(0, END)

        frame6.place_forget()
        frame.place(x=0, y=0)


def Back5():
    frame6.place_forget()
    frame.place(x=0, y=0)


lbl6 = Label(frame6, text="Delete Event", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl6.place(x=140, y=0)

delete = Label(frame6, text="Delete", width=20, background="#acc18a", foreground="white", font=("Times New Roman", 12))
delete.place(x=0, y=50)

entry_delete = Entry(frame6, width=30, font=("Arial", 10))
entry_delete.place(x=215, y=50)

btndelete = Button(frame6, text="Delete", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                   command=Delete)
btndelete.place(x=150, y=150)

btnback5 = Button(frame6, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back5)
btnback5.place(x=25, y=350)

# =======================================================================================================================================================


frame7 = Frame(bg="white", width=500, height=500)


def Update():
    update_text = entry_update.get().strip().lower()
    items = lb_createevent.get(0, END)

    # Get the field to update
    update_field = var_update_field.get()

    for index, item in enumerate(items):
        if update_text in item.lower():
            if update_field == "Date":
                new_value = entry_update_value.get()
                lb_createevent.delete(index + 1)
                lb_createevent.insert(index + 1, new_value)
            elif update_field == "Time":
                new_value = entry_update_value.get()
                lb_createevent.delete(index + 2)
                lb_createevent.insert(index + 2, new_value)
            elif update_field == "Location":
                new_value = entry_update_value.get()
                lb_createevent.delete(index + 3)
                lb_createevent.insert(index + 3, new_value)
            else:
                # Invalid update field
                return

    save_events()

    entry_update.delete(0, END)
    entry_update_value.delete(0, END)

    frame7.place_forget()
    frame.place(x=0, y=0)


def Back6():
    frame7.place_forget()
    frame.place(x=0, y=0)


lbl7 = Label(frame7, text="Update Event", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl7.place(x=140, y=0)

update_name = Label(frame7, text="Update event name", width=20, background="#acc18a", foreground="white",
                    font=("Times New Roman", 12))
update_name.place(x=0, y=50)

update = Label(frame7, text="Update", width=20, background="#acc18a", foreground="white", font=("Times New Roman", 12))
update.place(x=0, y=100)

entry_update = Entry(frame7, width=30, font=("Arial", 10))
entry_update.place(x=215, y=50)

# Entry widgets for updating value
entry_update_value = Entry(frame7, width=30, font=("Arial", 10))
entry_update_value.place(x=215, y=100)

# Dropdown for selecting the field to update
var_update_field = StringVar(frame7)
update_fields = ["Date", "Time", "Location"]
update_field_menu = OptionMenu(frame7, var_update_field, *update_fields)
update_field_menu.place(x=215, y=150)

btnupdate = Button(frame7, text="Update", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                   command=Update)
btnupdate.place(x=150, y=200)

btnback6 = Button(frame7, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back6)
btnback6.place(x=25, y=350)

root.mainloop()

from tkinter import *
from tkinter import messagebox


class Event:
    def __init__(self, name, date, time, location):
        self.__name = name
        self.__date = date
        self.__time = time
        self.__location = location

    def GetName(self):
        return self.__name

    def GetDate(self):
        return self.__date

    def GetTime(self):
        return self.__time

    def GetLocation(self):
        return self.__location

    def GetInfo(self):
        print(
            f"Event Name: {self.__name} \nEvent Date: {self.__date} \nEvent Time: {self.__time} \nEvent Location: {self.__location}")


root = Tk()
root.title("Event Management System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position to open in the center
window_width = 500
window_height = 500
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


def CreateEvent():
    frame.place_forget()
    frame2.place(x=0, y=0)


def AddOrganizer():
    frame2.place_forget()
    frame3.place(x=0, y=0)


def AddParticipant():
    frame3.place_forget()
    frame4.place(x=0, y=0)


def DisplayEvents():
    frame4.place_forget()
    frame5.place(x=0, y=0)


def DeleteEvent():
    frame5.place_forget()
    frame6.place(x=0, y=0)


def UpdateEvent():
    frame6.place_forget()
    frame7.place(x=0, y=0)


frame = Frame(bg="white", width=500, height=500)
frame.grid(row=0, column=0, sticky="nsew")

root.rowconfigure(0, weight=1, minsize=500)
root.columnconfigure(0, weight=1, minsize=500)
root.maxsize(500, 500)

photo1 = PhotoImage(file="EMS.png")
lblbookphoto = Label(frame, image=photo1, width=500, height=200)
lblbookphoto.place(x=0, y=0)

lbl = Label(frame, text="MENU", width=20, background="#A9B388", foreground="white", font=("Times New Roman", 15))
lbl.place(x=0, y=215)

btn_createEvent = Button(frame, text="Create Event", width=15, bg="#acc18a", fg="white", command=CreateEvent)
btn_createEvent.place(x=0, y=250)

btn_addOrganizer = Button(frame, text="Add Organizer", width=15, bg="#acc18a", fg="white", command=AddOrganizer)
btn_addOrganizer.place(x=0, y=285)

btn_addParticipant = Button(frame, text="Add Participant", width=15, bg="#acc18a", fg="white", command=AddParticipant)
btn_addParticipant.place(x=0, y=320)

btn_displayEvents = Button(frame, text="Display Events", width=15, bg="#acc18a", fg="white", command=DisplayEvents)
btn_displayEvents.place(x=0, y=355)

btn_displayEvents = Button(frame, text="Delete Event", width=15, bg="#acc18a", fg="white", command=DeleteEvent)
btn_displayEvents.place(x=0, y=390)

btn_updateEvents = Button(frame, text="Update Event", width=15, bg="#acc18a", fg="white", command=UpdateEvent)
btn_updateEvents.place(x=0, y=425)

# ===================================================================================================================================


frame2 = Frame(bg="white", width=500, height=500)

lbl2 = Label(frame2, text="Create Event", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl2.place(x=140, y=0)


def save_events():
    with open("events.txt", "w") as file:
        for event in lb_createevent.get(0, END):
            file.write(event + "\n")
        for event in lb_addorganizer.get(0, END):
            file.write(event + "\n")
        for event in lb_addparticipant.get(0, END):
            file.write(event + "\n")
    return "Events saved successfully"


def is_valid_date(date):
    return all(char.isdigit() or char.isspace() or char == '/' for char in date)


def is_valid_time(time):
    return all(char.isdigit() or char == ':' for char in time)


def Create():
    name_event = entryname.get()
    date_event = entrydate.get()
    time_event = entrytime.get()
    location_event = entrylocation.get()

    if len(name_event) <= 3:
        messagebox.showwarning("Warning", "Event must be at least 3 characters long.")
        return

    if not is_valid_date(date_event):
        messagebox.showwarning("Warning", "Invalid date format. Use only numbers and spaces.")
        return

    if not is_valid_time(time_event):
        messagebox.showwarning("Warning", "Invalid time format. Use only numbers and colons.")
        return

    new_event = Event(name_event, date_event, time_event, location_event)

    # Add the event to the ls list
    ls.append(new_event.GetInfo())

    lb_createevent.insert(END, name_event)
    lb_createevent.insert(END, date_event)
    lb_createevent.insert(END, time_event)
    lb_createevent.insert(END, location_event)

    save_events()

    entryname.delete(0, END)
    entrydate.delete(0, END)
    entrytime.delete(0, END)
    entrylocation.delete(0, END)

    frame2.place_forget()
    frame.place(x=0, y=0)


ls = []


def Back1():
    frame2.place_forget()
    frame.place(x=0, y=0)


eventname = Label(frame2, text="Event Name", width=20, background="#acc18a", foreground="white",
                  font=("Times New Roman", 12))
eventname.place(x=0, y=50)

entryname = Entry(frame2, width=30, font=("Arial", 10))
entryname.place(x=215, y=50)

eventdate = Label(frame2, text="Event Date", width=20, background="#acc18a", foreground="white",
                  font=("Times New Roman", 12))
eventdate.place(x=0, y=100)

entrydate = Entry(frame2, width=30, font=("Arial", 10))
entrydate.place(x=215, y=100)

eventtime = Label(frame2, text="Event Time", width=20, background="#acc18a", foreground="white",
                  font=("Times New Roman", 12))
eventtime.place(x=0, y=150)

entrytime = Entry(frame2, width=30, font=("Arial", 10))
entrytime.place(x=215, y=150)

eventlocation = Label(frame2, text="Event Location", width=20, background="#acc18a", foreground="white",
                      font=("Times New Roman", 12))
eventlocation.place(x=0, y=200)

entrylocation = Entry(frame2, width=30, font=("Arial", 10))
entrylocation.place(x=215, y=200)

btncreate = Button(frame2, text="Create", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                   command=Create)
btncreate.place(x=150, y=300)

btnback1 = Button(frame2, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back1)
btnback1.place(x=25, y=400)

# ====================================================================================================================================================


frame3 = Frame(bg="white", width=500, height=500)


def AddOrganizer():
    name_organizer = entry_organizername.get()
    email_organizer = entry_organizeremail.get()

    if len(name_organizer) <= 3:
        messagebox.showwarning("Warning", "Organizer name must be at least 3 characters long.")
        return

    lb_addorganizer.insert(END, name_organizer)
    lb_addorganizer.insert(END, email_organizer)

    save_events()

    entry_organizername.delete(0, END)
    entry_organizeremail.delete(0, END)

    frame3.place_forget()
    frame.place(x=0, y=0)


def Back2():
    frame3.place_forget()
    frame.place(x=0, y=0)


lbl3 = Label(frame3, text="Add Organizer", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl3.place(x=140, y=0)

organizername = Label(frame3, text="Organizer Name", width=20, background="#acc18a", foreground="white",
                      font=("Times New Roman", 12))
organizername.place(x=0, y=50)

entry_organizername = Entry(frame3, width=30, font=("Arial", 10))
entry_organizername.place(x=215, y=50)

organizeremail = Label(frame3, text="Organizer Email", width=20, background="#acc18a", foreground="white",
                       font=("Times New Roman", 12))
organizeremail.place(x=0, y=100)

entry_organizeremail = Entry(frame3, width=30, font=("Arial", 10))
entry_organizeremail.place(x=215, y=100)

btnadd_organizer = Button(frame3, text="Add", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                          command=AddOrganizer)
btnadd_organizer.place(x=150, y=150)

btnback2 = Button(frame3, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back2)
btnback2.place(x=25, y=300)

# ==================================================================================================================================================================


frame4 = Frame(bg="white", width=500, height=500)


def AddParticipant():
    name_participant = entry_participantname.get()
    email_participant = entry_participantemail.get()

    if len(name_participant) <= 3:
        messagebox.showwarning("Warning", "Participant name must be at least 3 characters long.")
        return

    lb_addparticipant.insert(END, name_participant)
    lb_addparticipant.insert(END, email_participant)

    save_events()

    entry_participantname.delete(0, END)
    entry_participantemail.delete(0, END)

    frame4.place_forget()
    frame.place(x=0, y=0)


def Back3():
    frame4.place_forget()
    frame.place(x=0, y=0)


lbl4 = Label(frame4, text="Add Participant", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl4.place(x=140, y=0)

participantname = Label(frame4, text="Participant Name", width=20, background="#acc18a", foreground="white",
                        font=("Times New Roman", 12))
participantname.place(x=0, y=50)

entry_participantname = Entry(frame4, width=30, font=("Arial", 10))
entry_participantname.place(x=215, y=50)

participantemail = Label(frame4, text="Participant Email", width=20, background="#acc18a", foreground="white",
                         font=("Times New Roman", 12))
participantemail.place(x=0, y=100)

entry_participantemail = Entry(frame4, width=30, font=("Arial", 10))
entry_participantemail.place(x=215, y=100)

btnadd_participant = Button(frame4, text="Add", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                            command=AddParticipant)
btnadd_participant.place(x=150, y=150)

btnback3 = Button(frame4, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back3)
btnback3.place(x=25, y=300)

# ============================================================================================================================================================================


frame5 = Frame(bg="white", width=500, height=500)


def Back4():
    frame5.place_forget()
    frame.place(x=0, y=0)


lbl5 = Label(frame5, text="Display Events", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl5.place(x=140, y=0)

lbl_event = Label(frame5, text="Events Information", width=20, background="#acc18a", foreground="white",
                  font=("Times New Roman", 15))
lbl_event.place(x=0, y=50)

lb_createevent = Listbox(frame5, bg="#FAEED1", width=20, height=10, fg="#5a572a", font=("Times New Roman", 15))
lb_createevent.place(x=7, y=80)

lbl_organizer = Label(frame5, text="Organizer Information", width=20, background="#acc18a", foreground="white",
                      font=("Times New Roman", 15))
lbl_organizer.place(x=250, y=50)

lb_addorganizer = Listbox(frame5, bg="#FAEED1", width=20, height=5, fg="#5a572a", font=("Times New Roman", 15))
lb_addorganizer.place(x=262, y=80)

lbl_participant = Label(frame5, text="Participant Information", width=20, background="#acc18a", foreground="white",
                        font=("Times New Roman", 15))
lbl_participant.place(x=250, y=220)

lb_addparticipant = Listbox(frame5, bg="#FAEED1", width=20, height=5, fg="#5a572a", font=("Times New Roman", 15))
lb_addparticipant.place(x=262, y=250)

btnback4 = Button(frame5, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back4)
btnback4.place(x=30, y=370)

# =============================================================================================================================================


frame6 = Frame(bg="white", width=500, height=500)


def Delete():
    delete_text = entry_delete.get().strip().lower()
    items_event = lb_createevent.get(0, END)
    items_organizer = lb_addorganizer.get(0, END)
    items_participant = lb_addparticipant.get(0, END)

    # Find the selected event
    event_index = -1
    for index_event, item_event in enumerate(items_event):
        if delete_text in item_event.lower():
            event_index = index_event
            break

    # Delete event information
    if event_index >= 0:
        lb_createevent.delete(event_index)
        lb_createevent.delete(event_index)
        lb_createevent.delete(event_index)
        lb_createevent.delete(event_index)

        # Delete associated organizer information
        organizer_index = event_index // 4  # Each event has 4 lines of information
        lb_addorganizer.delete(organizer_index * 2)  # Delete organizer name
        lb_addorganizer.delete(organizer_index * 2)  # Delete organizer email

        # Delete associated participant information
        participant_index = event_index // 4  # Each event has 4 lines of information
        lb_addparticipant.delete(participant_index * 2)  # Delete participant name
        lb_addparticipant.delete(participant_index * 2)  # Delete participant email

        save_events()

        entry_delete.delete(0, END)

        frame6.place_forget()
        frame.place(x=0, y=0)


def Back5():
    frame6.place_forget()
    frame.place(x=0, y=0)


lbl6 = Label(frame6, text="Delete Event", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl6.place(x=140, y=0)

delete = Label(frame6, text="Delete", width=20, background="#acc18a", foreground="white", font=("Times New Roman", 12))
delete.place(x=0, y=50)

entry_delete = Entry(frame6, width=30, font=("Arial", 10))
entry_delete.place(x=215, y=50)

btndelete = Button(frame6, text="Delete", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                   command=Delete)
btndelete.place(x=150, y=150)

btnback5 = Button(frame6, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back5)
btnback5.place(x=25, y=350)

# =======================================================================================================================================================


frame7 = Frame(bg="white", width=500, height=500)


def Update():
    update_text = entry_update.get().strip().lower()
    items = lb_createevent.get(0, END)

    # Get the field to update
    update_field = var_update_field.get()

    for index, item in enumerate(items):
        if update_text in item.lower():
            if update_field == "Date":
                new_value = entry_update_value.get()
                lb_createevent.delete(index + 1)
                lb_createevent.insert(index + 1, new_value)
            elif update_field == "Time":
                new_value = entry_update_value.get()
                lb_createevent.delete(index + 2)
                lb_createevent.insert(index + 2, new_value)
            elif update_field == "Location":
                new_value = entry_update_value.get()
                lb_createevent.delete(index + 3)
                lb_createevent.insert(index + 3, new_value)
            else:
                # Invalid update field
                return

    save_events()

    entry_update.delete(0, END)
    entry_update_value.delete(0, END)

    frame7.place_forget()
    frame.place(x=0, y=0)


def Back6():
    frame7.place_forget()
    frame.place(x=0, y=0)


lbl7 = Label(frame7, text="Update Event", width=20, background="#A9B388", foreground="white",
             font=("Times New Roman", 15))
lbl7.place(x=140, y=0)

update_name = Label(frame7, text="Update event name", width=20, background="#acc18a", foreground="white",
                    font=("Times New Roman", 12))
update_name.place(x=0, y=50)

update = Label(frame7, text="Update", width=20, background="#acc18a", foreground="white", font=("Times New Roman", 12))
update.place(x=0, y=100)

entry_update = Entry(frame7, width=30, font=("Arial", 10))
entry_update.place(x=215, y=50)

# Entry widgets for updating value
entry_update_value = Entry(frame7, width=30, font=("Arial", 10))
entry_update_value.place(x=215, y=100)

# Dropdown for selecting the field to update
var_update_field = StringVar(frame7)
update_fields = ["Date", "Time", "Location"]
update_field_menu = OptionMenu(frame7, var_update_field, *update_fields)
update_field_menu.place(x=215, y=150)

btnupdate = Button(frame7, text="Update", width=15, bg="#ede29b", fg="#5a572a", font=("Times New Roman", 10),
                   command=Update)
btnupdate.place(x=150, y=200)

btnback6 = Button(frame7, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back6)
btnback6.place(x=25, y=350)

root.mainloop()


