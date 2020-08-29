import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import test
from test import *
import re
import threading
from time import sleep
from subprocess import call
import BAC0

# Create the Main Application/GUI Class ("Frame" or Window)

class Application(tk.Frame):
    
    # /_\-/_\Initialize the Window or "Frame"/_\-/_\ 
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('OpenVPN - Virtual Lab Setup')
        # Width height
        master.geometry("755x315")
        # Create widgets/grid
        self.create_dropdown_widgets()
        # 
        self.create_entry_widgets()
        #
        self.create_button_widgets()
    def start(self):
        self.this_device = self.device_text.get()
        self.this_name = self.name_text.get()
        self.this_host = test.ethernet_address[self.iface.get()]
        self.this_bbmd = test.ethernet_address[self.iface.get()][:-3] + "/32:" + self.this_bbmd_port_text.get()
        self.remote_bbmd1 = self.remote_bbmd1_text.get() + "/32:" + self.remote_bbmd1_port_text.get()
        self.remote_bbmd2 = self.remote_bbmd2_text.get() + "/32:" + self.remote_bbmd2_port_text.get()
        self.remote_bbmd3 = self.remote_bbmd3_text.get() + "/32:" + self.remote_bbmd3_port_text.get()
        self.remote_bbmd4 = self.remote_bbmd4_text.get() + "/32:" + self.remote_bbmd4_port_text.get()
        self.remote_bbmd5 = self.remote_bbmd5_text.get() + "/32:" + self.remote_bbmd5_port_text.get()
        self.remote_bbmd6 = self.remote_bbmd6_text.get() + "/32:" + self.remote_bbmd6_port_text.get()
        self.remote_bbmd7 = self.remote_bbmd7_text.get() + "/32:" + self.remote_bbmd7_port_text.get()
        self.remote_bbmd8 = self.remote_bbmd8_text.get() + "/32:" + self.remote_bbmd8_port_text.get()
        self.remote_bbmd9 = self.remote_bbmd9_text.get() + "/32:" + self.remote_bbmd9_port_text.get()
        self.remote_bbmd10 = self.remote_bbmd10_text.get() + "/32:" + self.remote_bbmd10_port_text.get()
        #call(["python3.9","/home/pi/Desktop/Bacnet/bacpypes-master/samples/BBMD.py","192.168.2.151/24","192.168.2.151/32:47808","192.168.1.100/32:47809"])
        #ip="192.168.2.151/24",deviceId="7000",localObjName="Anthony"
        self.bbmd_table = BAC0.lite(ip=self.this_host,deviceId=self.this_device,localObjName=self.this_name,bdtable=[self.this_host,self.this_bbmd,self.remote_bbmd1,self.remote_bbmd2,self.remote_bbmd3,self.remote_bbmd4,self.remote_bbmd5,self.remote_bbmd6,self.remote_bbmd7,self.remote_bbmd8,self.remote_bbmd9,self.remote_bbmd10])
        print(self.this_bbmd)
    # /_\-/_\Create Widgets/_\-/_\
    def create_button_widgets(self):
        # Start Button
        self.start_button = tk.ttk.Button(self.master,text='Start',width=8,command=self.start)
        self.start_button.grid(row=5,column=8,pady=5,sticky=tk.E)
        
    def create_dropdown_widgets(self):
        # Set  up Local Device IP
        self.iface = tk.StringVar()
        self.iface_list = test.ethernet_keys
        self.iface_choices = sorted(self.iface_list)
        self.iface.set(test.ethernet_keys[0])
        # Output Interface
        self.iface_text = tk.StringVar()
        self.iface_label = tk.Label(self.master, text='BBMD Interface', font=('bold', 14), pady=10, padx=8)
        self.iface_label.grid(row=5, column=7, sticky=tk.E)
        self.iface_menu = tk.ttk.OptionMenu(self.master,self.iface,*self.iface_choices)
        self.iface_menu.grid(row=5,column=8, sticky=tk.W)
    def create_entry_widgets(self):
        # 1st Remote BBMD
        self.remote_bbmd1_text = tk.StringVar(self.master)
        self.remote_bbmd1_label = tk.Label(self.master, text='Remote BBMD #1', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd1_label.grid(row=2, column=4,sticky=tk.E)
        self.remote_bbmd1_entry = tk.Entry(self.master, textvariable=self.remote_bbmd1_text)
        self.remote_bbmd1_entry.insert(INSERT,"192.168.1.100")
        self.remote_bbmd1_entry.grid(row=2, column=5,sticky=tk.W)
        # 2nd Remote BBMD
        self.remote_bbmd2_text = tk.StringVar(self.master)
        self.remote_bbmd2_label = tk.Label(self.master, text='Remote BBMD #2', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd2_label.grid(row=3, column=4,sticky=tk.E)
        self.remote_bbmd2_entry = tk.Entry(self.master, textvariable=self.remote_bbmd2_text)
        self.remote_bbmd2_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd2_entry.grid(row=3, column=5,sticky=tk.W)
        # 3rd Remote BBMD
        self.remote_bbmd3_text = tk.StringVar(self.master)
        self.remote_bbmd3_label = tk.Label(self.master, text='Remote BBMD #3', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd3_label.grid(row=4, column=4,sticky=tk.E)
        self.remote_bbmd3_entry = tk.Entry(self.master, textvariable=self.remote_bbmd3_text)
        self.remote_bbmd3_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd3_entry.grid(row=4, column=5,sticky=tk.W)
        # 4th Remote BBMD
        self.remote_bbmd4_text = tk.StringVar(self.master)
        self.remote_bbmd4_label = tk.Label(self.master, text='Remote BBMD #4', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd4_label.grid(row=5, column=4,sticky=tk.E)
        self.remote_bbmd4_entry = tk.Entry(self.master, textvariable=self.remote_bbmd4_text)
        self.remote_bbmd4_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd4_entry.grid(row=5, column=5,sticky=tk.W)
        # 5th Remote BBMD
        self.remote_bbmd5_text = tk.StringVar(self.master)
        self.remote_bbmd5_label = tk.Label(self.master, text='Remote BBMD #5', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd5_label.grid(row=6, column=4,sticky=tk.E)
        self.remote_bbmd5_entry = tk.Entry(self.master, textvariable=self.remote_bbmd5_text)
        self.remote_bbmd5_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd5_entry.grid(row=6, column=5,sticky=tk.W)
        # 6th Remote BBMD
        self.remote_bbmd6_text = tk.StringVar(self.master)
        self.remote_bbmd6_label = tk.Label(self.master, text='Remote BBMD #6', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd6_label.grid(row=7, column=4,sticky=tk.E)
        self.remote_bbmd6_entry = tk.Entry(self.master, textvariable=self.remote_bbmd6_text)
        self.remote_bbmd6_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd6_entry.grid(row=7, column=5,sticky=tk.W)
        # 7th Remote BBMD
        self.remote_bbmd7_text = tk.StringVar(self.master)
        self.remote_bbmd7_label = tk.Label(self.master, text='Remote BBMD #7', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd7_label.grid(row=8, column=4,sticky=tk.E)
        self.remote_bbmd7_entry = tk.Entry(self.master, textvariable=self.remote_bbmd7_text)
        self.remote_bbmd7_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd7_entry.grid(row=8, column=5,sticky=tk.W)
        # 8th Remote BBMD
        self.remote_bbmd8_text = tk.StringVar(self.master)
        self.remote_bbmd8_label = tk.Label(self.master, text='Remote BBMD #8', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd8_label.grid(row=9, column=4,sticky=tk.E)
        self.remote_bbmd8_entry = tk.Entry(self.master, textvariable=self.remote_bbmd8_text)
        self.remote_bbmd8_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd8_entry.grid(row=9, column=5,sticky=tk.W)
        # 9th Remote BBMD
        self.remote_bbmd9_text = tk.StringVar(self.master)
        self.remote_bbmd9_label = tk.Label(self.master, text='Remote BBMD #9', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd9_label.grid(row=10, column=4,sticky=tk.E)
        self.remote_bbmd9_entry = tk.Entry(self.master, textvariable=self.remote_bbmd9_text)
        self.remote_bbmd9_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd9_entry.grid(row=10, column=5,sticky=tk.W)
        # 10th Remote BBMD
        self.remote_bbmd10_text = tk.StringVar(self.master)
        self.remote_bbmd10_label = tk.Label(self.master, text='Remote BBMD #10', font=('bold', 14), pady=5, padx=4, width=16)
        self.remote_bbmd10_label.grid(row=11, column=4,sticky=tk.E)
        self.remote_bbmd10_entry = tk.Entry(self.master, textvariable=self.remote_bbmd10_text)
        self.remote_bbmd10_entry.insert(INSERT,"0.0.0.0")
        self.remote_bbmd10_entry.grid(row=11, column=5,sticky=tk.W)
        # 1st Remote BBMD port
        self.remote_bbmd1_port_text = tk.StringVar(self.master)
        self.remote_bbmd1_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd1_port_text)
        self.remote_bbmd1_port_entry.insert(INSERT,"47809")
        self.remote_bbmd1_port_entry.grid(row=2, column=6,sticky=tk.W)
        # 2nd Remote BBMD port
        self.remote_bbmd2_port_text = tk.StringVar(self.master)
        self.remote_bbmd2_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd2_port_text)
        self.remote_bbmd2_port_entry.insert(INSERT,"47809")
        self.remote_bbmd2_port_entry.grid(row=3, column=6,sticky=tk.W)
        # 3rd Remote BBMD port
        self.remote_bbmd3_port_text = tk.StringVar(self.master)
        self.remote_bbmd3_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd3_port_text)
        self.remote_bbmd3_port_entry.insert(INSERT,"47809")
        self.remote_bbmd3_port_entry.grid(row=4, column=6,sticky=tk.W)
        # 4th Remote BBMD port
        self.remote_bbmd4_port_text = tk.StringVar(self.master)
        self.remote_bbmd4_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd4_port_text)
        self.remote_bbmd4_port_entry.insert(INSERT,"47809")
        self.remote_bbmd4_port_entry.grid(row=5, column=6,sticky=tk.W)
        # 5th Remote BBMD port
        self.remote_bbmd5_port_text = tk.StringVar(self.master)
        self.remote_bbmd5_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd5_port_text)
        self.remote_bbmd5_port_entry.insert(INSERT,"47809")
        self.remote_bbmd5_port_entry.grid(row=6, column=6,sticky=tk.W)
        # 6th Remote BBMD port
        self.remote_bbmd6_port_text = tk.StringVar(self.master)
        self.remote_bbmd6_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd6_port_text)
        self.remote_bbmd6_port_entry.insert(INSERT,"47809")
        self.remote_bbmd6_port_entry.grid(row=7, column=6,sticky=tk.W)
        # 7th Remote BBMD port
        self.remote_bbmd7_port_text = tk.StringVar(self.master)
        self.remote_bbmd7_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd7_port_text)
        self.remote_bbmd7_port_entry.insert(INSERT,"47809")
        self.remote_bbmd7_port_entry.grid(row=8, column=6,sticky=tk.W)
        # 8th Remote BBMD port
        self.remote_bbmd8_port_text = tk.StringVar(self.master)
        self.remote_bbmd8_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd8_port_text)
        self.remote_bbmd8_port_entry.insert(INSERT,"47809")
        self.remote_bbmd8_port_entry.grid(row=9, column=6,sticky=tk.W)
        # 9th Remote BBMD port
        self.remote_bbmd9_port_text = tk.StringVar(self.master)
        self.remote_bbmd9_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd9_port_text)
        self.remote_bbmd9_port_entry.insert(INSERT,"47809")
        self.remote_bbmd9_port_entry.grid(row=10, column=6,sticky=tk.W)
        # 10th Remote BBMD port
        self.remote_bbmd10_port_text = tk.StringVar(self.master)
        self.remote_bbmd10_port_entry = tk.Entry(self.master, textvariable=self.remote_bbmd10_port_text)
        self.remote_bbmd10_port_entry.insert(INSERT,"47809")
        self.remote_bbmd10_port_entry.grid(row=11, column=6,sticky=tk.W)
        # local BBMD port
        self.this_bbmd_port_text = tk.IntVar(self.master)
        self.this_bbmd_port_label = tk.Label(self.master, text='Local BBMD Port', font=('bold', 14), pady=5, padx=2, width=16)
        self.this_bbmd_port_label.grid(row=4, column=7,sticky=tk.E)
        self.this_bbmd_port_text = tk.StringVar(self.master)
        self.this_bbmd_port_entry = tk.Entry(self.master, textvariable=self.this_bbmd_port_text)
        self.this_bbmd_port_entry.insert(INSERT,"47808")
        self.this_bbmd_port_entry.grid(row=4, column=8,sticky=tk.W)
        # Device ID
        self.device_text = tk.IntVar(self.master)
        self.device_label = tk.Label(self.master, text='Device ID', font=('bold', 14), pady=5, padx=2, width=10)
        self.device_label.grid(row=3, column=7,sticky=tk.E)
        self.device_entry = tk.Entry(self.master, textvariable=self.device_text)
        self.device_entry.insert(INSERT,7000)
        self.device_entry.grid(row=3, column=8,sticky=tk.W)
        # Device Name
        self.name_text = tk.StringVar(self.master)
        self.name_label = tk.Label(self.master, text='Device Name', font=('bold', 14), pady=5, padx=14, width=10)
        self.name_label.grid(row=2, column=7,sticky=tk.E)
        self.name_entry = tk.Entry(self.master, textvariable=self.name_text)
        self.name_entry.insert(INSERT,"P00ntangPi")
        self.name_entry.grid(row=2, column=8,sticky=tk.W)
        
        
# Handle window closure by terminating all threads
def _delete_window():
    global tk_terminate
    # print("deleting frame")
    tk_terminate = True
    root.destroy()
    
def _destroy():
    print("destroy")
    
root = tk.Tk()
app = Application(master=root)
# bind function for thread termination to Frame closure
root.protocol("WM_DELETE_WINDOW",_delete_window)
root.bind("<Escape>",_destroy)
app.mainloop()
