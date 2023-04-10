from tkinter import *
from tkinter import messagebox,Toplevel
import pyqrcode
from png import *
# from pyqrcode import *
import os

#####################################################################################
root=Tk()
root.geometry('570x400')
root.title('QR Generator')
root.resizable(width=False,height=False)
root.wm_iconbitmap('Martz90-Circle-Qr-code.ico')
root.configure(bg='blue')
###################################################################################Function
def Generate_Qr():
    Qr_name=Qr_Name_Entry_box.get()
    Qr_Id=Qr_Id_Entry_box.get()
    Qr_message=Qr_Message_Entry_box.get()
    # print(Qr_Id,Qr_name,Qr_message)

    Message_Qr='Name : ' + Qr_name+'\n'+'Id : '+Qr_Id+'\n'+'Message : '+Qr_message
    # print(Message_Qr)

    url=pyqrcode.create(Message_Qr)
    # pp=r'C:\Users\hp\Desktop\QR'
    # cc='{}\{}{}.png'.format(pp,Qr_Id,Qr_name)
    # url.png('code.png',scale=5)
    path=r'Qr_code_saver'
    path_of_folder='{}\{}{}.png'.format(path,Qr_Id,Qr_name)
    list_of_all_QRsinFolder=os.listdir(path)
    # url.png('code.png', scale=8)
    if('{}{}.png'.format(Qr_Id,Qr_name) in list_of_all_QRsinFolder):
        messagebox.showinfo('Notification','Please choose another Id or name:( ')
    else:
        url.png(path_of_folder, scale=8)
        msg = 'QrCode Saved as: ' + Qr_Id + Qr_name + '.png'
        QR_Notification_Message_Label.configure(text=msg)
        msg='QrCode Saved as: '+Qr_Id+Qr_name+'.png'
        res=messagebox.askyesno('Notification','Qr Code is Generated and want to see it then click on yes: ')
        if res==True:
            top=Toplevel()
            top.geometry('400x400')
            top.configure(bg='white')
            img=PhotoImage(file=path_of_folder)
            label1=Label(top,image=img,bg='white')
            label1.place(x=10,y=10)
            top.mainloop()



def Clear_Id_Name():
    Qr_Id_Entry_box.delete(0,'end')
    Qr_Name_Entry_box.delete(0,'end')
    Qr_Message_Entry_box.delete(0,'end')
    QR_Notification_Message_Label.configure(text='')


def Quit_root():
    res=messagebox.askyesnocancel('Notificaion','Are you sure you want to quit ?')
    if res==True:
        root.destroy()
    else:
        pass

################################################################################### Labels
QR_ID_Label=Label(master=root,text='Enter your ID : ',bg='Powder blue',fg='red',width=20,height=2
                  ,font=('times',12,'bold'))
QR_ID_Label.place(x=10,y=20)


QR_Name_Label=Label(master=root,text='Enter your Name : ',bg='Powder blue',fg='red',width=20,height=2
                  ,font=('times',12,'bold'))
QR_Name_Label.place(x=10,y=80)


QR_Message_Label=Label(master=root,text='Enter your Message : ',bg='Powder blue',fg='red',width=20,height=2
                  ,font=('times',12,'bold'))
QR_Message_Label.place(x=10,y=140)

QR_Notification_Label=Label(master=root,text='Notification ',bg='Powder blue',fg='red',width=10,height=2
                  ,font=('times',15,'bold underline'))
QR_Notification_Label.place(x=10,y=350)


QR_Notification_Message_Label=Label(master=root,text='',bg='Powder blue',fg='red',width=30,height=2
                  ,font=('times',15,'bold '))
QR_Notification_Message_Label.place(x=200,y=350)


################################################################################### Entry Boxes
Qr_Id_Entry_box=Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'bold'))
Qr_Id_Entry_box.place(x=250,y=20)

Qr_Name_Entry_box=Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'bold'))
Qr_Name_Entry_box.place(x=250,y=80)

Qr_Message_Entry_box=Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'bold'))
Qr_Message_Entry_box.place(x=250,y=140)


######################################################################################Buttons logo
Generate_QRimage =PhotoImage(file="qr-code (1).png")
Generate_QRimage =Generate_QRimage.subsample(2, 2)

clear_Id_Nameimage=PhotoImage(file='rubber.png')
clear_Id_Nameimage=clear_Id_Nameimage.subsample(2, 2)

Quit_root_image=PhotoImage(file='x-button (1).png')
Quit_root_image=Quit_root_image.subsample(2, 2)



################################################################################### Buttons

Generate_Qr_image_Button=Button(master=root,text="Generate",width=100,font=('times',10,'bold'),bd=10,
                         bg='yellow',activebackground='blue',image=Generate_QRimage,compound=RIGHT,
                                command=Generate_Qr)
Generate_Qr_image_Button.place(x=10,y=250)

Clear_Name_Id_Button=Button(master=root,text="Clear",width=100,font=('times',10,'bold'),bd=10,
                         bg='yellow',activebackground='blue',image=clear_Id_Nameimage,compound=RIGHT,
                            command=Clear_Id_Name)
Clear_Name_Id_Button.place(x=210,y=250)

Quit_Root_Button=Button(master=root,text="Quit",width=100,font=('times',10,'bold'),bd=10,
                         bg='yellow',activebackground='blue',image=Quit_root_image,compound=RIGHT,command=Quit_root)
Quit_Root_Button.place(x=410,y=250)
################################################################################################ HoverEffect
#Binding
def Generate_QRimage_ButtonEnter(e):
    Generate_Qr_image_Button['bg']='purple'
def Generate_QRimage_ButtonLeave(e):
    Generate_Qr_image_Button['bg']='yellow'

def Clear_Name_Id_ButtonEnter(e):
    Clear_Name_Id_Button['bg'] = 'purple'
def Clear_Name_Id_ButtonLeave(e):
    Clear_Name_Id_Button['bg'] = 'yellow'

def Quit_root_ButtonEnter(e):
    Quit_Root_Button['bg'] = 'purple'
def Quit_root_ButtonLeave(e):
    Quit_Root_Button['bg'] = 'yellow'


Generate_Qr_image_Button.bind('<Enter>',Generate_QRimage_ButtonEnter)
Generate_Qr_image_Button.bind('<Leave>',Generate_QRimage_ButtonLeave)

Clear_Name_Id_Button.bind('<Enter>',Clear_Name_Id_ButtonEnter)
Clear_Name_Id_Button.bind('<Leave>',Clear_Name_Id_ButtonLeave)

Quit_Root_Button.bind('<Enter>',Quit_root_ButtonEnter)
Quit_Root_Button.bind('<Leave>',Quit_root_ButtonLeave)



root.mainloop()
