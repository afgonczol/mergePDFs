# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:21:12 2018

Program for merging PDFs

@author: Allen Gonczol
"""

import tkinter
from tkinter import filedialog, Tk, messagebox, simpledialog
from PyPDF2 import PdfFileMerger
import os


def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []
 
    for path in input_paths:
        pdf_merger.append(path)
 
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

 
if __name__ == '__main__':
    print("Loading Window, please wait...")
    
    root = Tk()
    root.withdraw()

    
    #Get name to be used for merged file
    merged_name = simpledialog.askstring("FileName", "Enter the name to use for the merged PDF file.", parent=root)
    #Add .pdf to end if user does not enter it
    #TODO: handle casing
    if not merged_name.endswith(".pdf"):
        merged_name += ".pdf"
    print(merged_name)

#limit to PDF files
    ftypes = [("PDF file", "*.pdf")]
    
#Explain how to use program
    messagebox.showinfo("Instructions",'Choose files in the order you want them merged.\nSelect "cancel" when finished.')

#Get a list of PDF file names to iterate through.
#Must be selected in desired order
    file_names = []
    output_dir = None
    while True:
    
        root.filename = filedialog.askopenfile(filetypes=ftypes)
        try:
            file_names.append(root.filename.name)
            print(root.filename.name)
            if output_dir == None:
                output_dir = os.path.dirname(root.filename.name)
                merged_name = output_dir + "/" + merged_name #Use forward slash to match what is returned from askdialog
                
        except Exception as e:
            print(e)
            break
    
    try:
        merger(merged_name, file_names)
        messagebox.showinfo("Success!",'Files successfully merged into PDF named "{}"'.format(merged_name))
    except Exception as e:
        messagebox.showinfo("Error!","Error: {}. For more help, visit https://github.com/afgonczol/mergePDFs".format(e))
    
    
    root.destroy()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    