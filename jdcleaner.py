from multiprocessing.dummy import current_process
from tkinter import messagebox
import pandas as pd

# BusinessAnalyst
# DataAnalyst
# DataEngineer
# DataScientist
type_name='DataEngineer'
dajd=pd.read_csv("data/origin/{}.csv".format(type_name))
jds=dajd['Job Description']
jdes=[(-1,'Start of file')]*2
for i in range(len(jds)):
    jd_i=list(filter(None,jds[i].splitlines()))
    ind_i=[i]*len(jd_i)
    jdes.extend(zip(ind_i,jd_i))
jdes.extend([(-1,'End of file')]*10)


save_jdes=[(-1,'no_jd_here')]*5


from tkinter import *
window = Tk()
window.title("杰迪清洗器")
window.geometry('1600x800')
lbls = [Message(window, text=jdes[i][1],width=600) for i in range(0,13)]
for i in range(0,13):
    lbls[i].grid(column=0, row=i)
lbls[2].config(fg='red')
global current_index
current_index=2

saves = [Message(window, text=save_jdes[i][1],width=600) for i in range(0,5)]
for i in range(0,5):
    saves[i].grid(column=3, row=i)

def refresh_left_list(ci=2):
    for i in range(0,13):
        lbls[i].config(text=jdes[ci-2+i][1])
def refresh_right_list():
    for i in range(0,5):
        saves[i].config(text=save_jdes[len(save_jdes)-5+i][1])

def up_clicked(event):
    global current_index
    current_index-=1
    refresh_left_list(current_index)
def down_clicked(event):
    global current_index
    current_index+=1
    refresh_left_list(current_index)
def right_clicked(event):
    global current_index
    save_jdes.append(jdes[current_index])
    current_index+=1
    refresh_left_list(current_index)
    refresh_right_list()
def left_clicked(event):
    save_jdes.pop()
    refresh_right_list()
def space_clicked(event):
    dajd['Cleaned JD']=''
    for i in range(6,len(save_jdes)):
        dajd['Cleaned JD'][save_jdes[i][0]]=dajd['Cleaned JD'][save_jdes[i][0]]+save_jdes[i][1]+'\r\n'
    dajd[:(save_jdes[i][0]+1)].to_csv("data/cleaned/{}.csv".format(type_name))        
    messagebox.showinfo("Information","FInished!")
window.bind("<Up>",up_clicked)
window.bind("<Down>",down_clicked)
window.bind("<Right>",right_clicked)
window.bind("<Left>",left_clicked)
window.bind("<Return>",space_clicked)
window.mainloop()