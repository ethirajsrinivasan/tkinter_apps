from Tkinter import *
import tkFileDialog
import tkMessageBox
import shutil
import glob
import random

class DataManagement:

    def __init__(self, master):
        self.master = master
        self.to_folder_path = StringVar()
        self.from_folder_path = StringVar()
        self.folder_path = StringVar()
        self.master.title("Data Arrangement Application v1.0")
        self.label_select_function = Label(root, text="Please select the function:")
        self.label_select_function.grid(row=0, sticky=E, padx=20, pady=20)
        functionDescription = "* Copy Function is  used to copy files of particular extension from source directory to destination directory.\n\n* Rename Function renames files of certain extension in a folder.\n\n* Select function selects certain percentage of files with a specific extension and copies it to destination "
        self.label_function_description = Label(root, text=functionDescription,
                                               bg="white",
                                               wraplength=200,
                                               width=30,
                                               height=10,
                                                justify=LEFT)
        self.label_function_description.grid(row=1, column=1, columnspan=2, rowspan=5, padx=(0, 20), pady=(0, 20))

        self.copyButton = Button(master, text="Copy", command=self.openCopyFrame, width=7)
        self.copyButton.grid(row=1, column=0, padx=20, pady=2, sticky=W)
        self.renameButton = Button(master, text="Rename", command=self.openRenameFrame, width=7)
        self.renameButton.grid(row=2, column=0, padx=20, pady=2, sticky=W)

        self.selectButton = Button(master, text="Select", command=self.openSelectFrame, width=7)
        self.selectButton.grid(row=3, column=0, padx=20, pady=2, sticky=W)
        self.label_footer = Label(root, text="Trakomatic Pte Ltd", bg="white")
        self.label_footer.grid(row=6, columnspan=3,pady=10)

    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.master.withdraw()

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.master.update()
        self.master.deiconify()

    # ----------------------------------------------------------------------
    def openCopyFrame(self):
        self.hide()
        self.copyFrame = Tk()
        self.copyFrame.geometry("450x150")
        self.copyFrame.title("Copy Data")
        self.sourceFileButton = Button(self.copyFrame, text="Source Path", command=self.browse_from_button, width=15)
        self.sourceFileButton.grid(row=0, column=0, sticky=W, padx=(10, 4), pady=(20,4))
        self.destinationFileButton = Button(self.copyFrame, text="Destination Path", command=self.browse_to_button, width=15)
        self.destinationFileButton.grid(row=1, column=0, sticky=W, padx=(10, 4), pady=4)
        self.sourceLabel = Entry(self.copyFrame, width=50, textvariable=self.from_folder_path)
        self.sourceLabel.grid(row=0, column=1, sticky=W, pady=(20, 4))
        self.destinationLabel = Entry(self.copyFrame, width=50, textvariable=self.to_folder_path)
        self.destinationLabel.grid(row=1, column=1, sticky=W)
        self.label_arrangement = Label(self.copyFrame, text="Rules:")
        self.label_arrangement.grid(row=2, sticky=N+E+W+S, padx=4, pady=4)
        self.rule = Entry(self.copyFrame, width=50)
        self.rule.grid(row=2, column=1)
        okButton = Button(self.copyFrame, text="Ok", command=self.copyData, width=5)
        okButton.grid(row=3, column=0)
        handler = lambda: self.onCloseOtherFrame(self.copyFrame)
        cancelButton = Button(self.copyFrame, text="Cancel", command=handler)
        cancelButton.grid(row=3, column=1)

    # ----------------------------------------------------------------------
    def copyData(self):
        if self.validateCopyData():
            sourceDir = glob.glob(self.sourceLabel.get()+"/*."+self.rule.get())
            for file in sourceDir:
                shutil.copy2(file, self.destinationLabel.get())
            tkMessageBox.showinfo('Copy Data', 'Successfully completed')

    def validateCopyData(self):
        if len(self.sourceLabel.get()) == 0:
           tkMessageBox.showinfo('Error', 'Select source path')
           return False
        elif len(self.destinationLabel.get()) == 0:
            tkMessageBox.showinfo('Error', 'Select Destination Path')
            return False
        elif len(self.rule.get())==0:
            tkMessageBox.showinfo('Error', 'Enter the rule')
            return False
        return True

    # ----------------------------------------------------------------------
    def openRenameFrame(self):
        self.hide()
        self.renameFrame = Tk()
        self.renameFrame.geometry("450x120")
        self.renameFrame.title("Rename Data")
        self.fileButton = Button(self.renameFrame, text="Browse", command=self.browse_button, width=15)
        self.fileButton.grid(row=0, column=0, sticky=W, padx=(10, 4), pady=(20, 4))
        self.fileLabel = Entry(self.renameFrame, width=50, textvariable=self.folder_path)
        self.fileLabel.grid(row=0, column=1, sticky=W, pady=(20,4))
        self.label_arrangement = Label(self.renameFrame, text="Rules:")
        self.label_arrangement.grid(row=2, sticky=N+S+W+E, padx=4, pady=4)
        self.rule = Entry(self.renameFrame, width=50)
        self.rule.grid(row=2, column=1)
        okButton = Button(self.renameFrame, text="Ok", command=self.renameData, width=5)
        okButton.grid(row=3, column=0)
        handler = lambda: self.onCloseOtherFrame(self.renameFrame)
        cancelButton = Button(self.renameFrame, text="Cancel", command=handler)
        cancelButton.grid(row=3, column=1)


    # ----------------------------------------------------------------------
    def renameData(self):
        if self.validateRenameData():
            files = glob.glob(self.fileLabel.get()+'/*.'+self.rule.get())
            for i in range(len(files)):
                shutil.move(files[i], self.fileLabel.get()+'/'+str(i)+'.'+self.rule.get())
            tkMessageBox.showinfo('Rename Data', 'Successfully completed')

    # ----------------------------------------------------------------------
    def validateRenameData(self):
        if len(self.fileLabel.get())==0:
            tkMessageBox.showinfo('Error', 'Enter File Path')
            return False
        elif len(self.rule.get())==0:
            tkMessageBox.showinfo('Error', 'Enter rule')
            return  False
        return True

    # ----------------------------------------------------------------------
    def openSelectFrame(self):
        self.hide()
        self.selectFrame = Tk()
        self.selectFrame.geometry("450x150")
        self.selectFrame.title("Rename Data")
        percentage_files = IntVar()
        self.sourceFileButton = Button(self.selectFrame, text="Source Path", command=self.browse_from_button, width=15)
        self.sourceFileButton.grid(row=0, column=0, sticky=W, padx=2, pady=2)
        self.destinationFileButton = Button(self.selectFrame, text="Destination Path", command=self.browse_to_button,
                                            width=15)
        self.destinationFileButton.grid(row=1, column=0, sticky=W, padx=2, pady=2)
        self.sourceLabel = Entry(self.selectFrame, width=50, textvariable=self.from_folder_path)
        self.sourceLabel.grid(row=0, column=1, sticky=W)
        self.destinationLabel = Entry(self.selectFrame, width=50, textvariable=self.to_folder_path)
        self.destinationLabel.grid(row=1, column=1, sticky=W)
        self.label_arrangement = Label(self.selectFrame, text="Rules:")
        self.label_arrangement.grid(row=2, sticky=N+S+W+E, padx=4, pady=4)
        self.rule = Entry(self.selectFrame, width=50)
        self.rule.grid(row=2, column=1)
        self.label_percentage_of_files = Label(self.selectFrame,text="Percentage:")
        self.label_percentage_of_files.grid(row=3, sticky=W+N+E+S, padx=4, pady=4)
        self.entry_percentage_of_files = Entry(self.selectFrame, width=50, textvariable=percentage_files)
        self.entry_percentage_of_files.grid(row=3, column=1)
        okButton = Button(self.selectFrame, text="Ok", command=self.selectData, width=5)
        okButton.grid(row=4, column=0)
        handler = lambda: self.onCloseOtherFrame(self.selectFrame)
        cancelButton = Button(self.selectFrame, text="Cancel", command=handler)
        cancelButton.grid(row=4, column=1)

    # ----------------------------------------------------------------------
    def selectData(self):
        if self.validateSelectData():
            files = glob.glob(self.sourceLabel.get()+'/*.'+self.rule.get())
            k = int(self.entry_percentage_of_files.get())*len(files)/100
            files = random.sample(files, k)
            for file in files:
                shutil.copy2(file, self.destinationLabel.get())
            tkMessageBox.showinfo('Select Data', 'Successfully completed')

    #-----------------------------------------------------------------------
    def validateSelectData(self):
        if len(self.sourceLabel.get())==0:
            tkMessageBox.showinfo('Error','Select Source File Path')
            return False
        elif len(self.destinationLabel.get())==0:
            tkMessageBox.showinfo('Error', 'Select Destination File Path')
            return False
        elif len(self.rule.get())==0:
            tkMessageBox.showinfo('Error','Enter rule')
            return False
        elif len(self.entry_percentage_of_files.get())==0:
            tkMessageBox.showinfo('Error','Enter percentage of files')
        return True

    # ----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    # ----------------------------------------------------------------------
    def browse_button(self):
        filename = tkFileDialog.askdirectory(parent=self.master)
        self.folder_path.set(filename)
        self.fileLabel.delete(0, END)
        self.fileLabel.insert(0, filename)
        print(filename)

    def browse_from_button(self):
        filename = tkFileDialog.askdirectory(parent=self.master)
        self.from_folder_path.set(filename)
        self.sourceLabel.delete(0, END)
        self.sourceLabel.insert(0, filename)
        print(filename)

    def browse_to_button(self):
        filename = tkFileDialog.askdirectory(parent=self.master)
        self.destinationLabel.delete(0, END)
        self.destinationLabel.insert(0, filename)
        self.to_folder_path.set(filename)
        print(filename)

root = Tk()
b = DataManagement(root)
root.mainloop()
