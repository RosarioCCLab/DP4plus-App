# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:45:03 2023

@author: Franco, Bruno Agustín 

This is a helper script to install a PyPI module, designed for users who are not familiar with operating system command line usage.
"""

import subprocess, os, shutil
import tkinter as tk

try: 
  subprocess.run('sudo apt-get install python3-pip')
  subprocess.run('sudo apt-get install python3-tk')
except: pass

try: 
  subprocess.run('sudo apt-get install python-pip')
  subprocess.run('sudo apt-get install python-tk')
except: pass

subprocess.run('pip install --upgrade dp4plus-app') 

def create_exe():
    '''Creates a direc acces executable file in the user desktop'''
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    exe = shutil.which("dp4plus")
    
    shutil.copy(exe, desktop)
    return 

print ('Creating direct access "dp4plus.exe" . . .')
create_exe()

#-----------------------------------------------------------------

byby = tk.Tk()
byby.wm_title("DP4+ App")

tk.Label(byby,text = u' Procces completed \u2713', 
         font = ("Arial Black", "12")).grid(row=0,padx=10, pady=(10,0))
tk.Label(byby,text ='DP4+ App has been installed successfully', 
         font = ("Arial Bold", "10")).grid(row=1,padx=10, pady=5)
tk.Label(byby,text ='Run it whith dp4plus.exe on your desktop', 
         font = ("Arial Bold", "10")).grid(row=2,padx=10, pady=5)
tk.Label(byby,text ='Press Exit to finish', 
         font = ("Arial Bold", "10")).grid(row=3,padx=10, pady=5)
tk.Button(byby, text='Exit', 
          command= byby.destroy).grid(row=4, pady=(5,10))

byby.mainloop()
