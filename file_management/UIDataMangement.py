from Tkinter import *
import tkFileDialog
import tkMessageBox
from Constants import *
from DataCopy import *
from DataSelect import *
from DataRename import *
from DataFold import *


class UIDataManagement:

    #Initialize the Main Window
    def __init__(self, master):
        self.master = master
        self.fromFolderPath = StringVar() #Initialize the source path
        self.toFolderPath = StringVar() #Initialize the destination path
        self.folderPath = StringVar() #Initialize the path
        self.master.geometry(Util.getGeometry(self.master, Constants.MASTER_FRAME_WIDTH, Constants.MASTER_FRAME_HEIGHT))
        self.master.title("Data Arrangement Application v1.0") # Set Title for the main window
        self.labelSelectFunction = Label(root, text="Please select the function:")
        self.labelSelectFunction.grid(row=0, sticky=E, padx=20, pady=20)
        self.labelFunctionDescription = Label(root, text=Constants.FUNCTION_DESCRIPTIONS,
                                              bg="white",
                                              wraplength=200,
                                              width=30,
                                              height=15,
                                              justify=LEFT)
        self.labelFunctionDescription.grid(row=1, column=1, columnspan=2, rowspan=5, padx=(0, 20), pady=(0, 20))
        self.copyButton = Button(master, text="Copy", command=self.openCopyFrame, width=7) # Triggers the copy Frame on click
        self.copyButton.grid(row=1, column=0, padx=20, pady=2, sticky=W)
        self.renameButton = Button(master, text="Rename", command=self.openRenameFrame, width=7) # Triggers the rename Frame on click
        self.renameButton.grid(row=2, column=0, padx=20, pady=2, sticky=W)
        self.selectButton = Button(master, text="Select", command=self.openSelectFrame, width=7) # Triggers the select Frame on click
        self.selectButton.grid(row=3, column=0, padx=20, pady=2, sticky=W)
        self.kfoldButton = Button(master, text="K-Fold", command=self.openKFoldFrame, width=7) # Triggers the Kfold screen
        self.kfoldButton.grid(row=4, column=0, padx=20, pady=2, sticky=W)
        self.labelFooter = Label(root, text="ethigeek Pte Ltd", bg="white")
        self.labelFooter.grid(row=6, columnspan=3, pady=10)

    # ----------------------------------------------------------------------
    # Initializes the copy frame and assigns the handler for all the buttons
    def openCopyFrame(self):
        self.hide()
        self.copyFrame = Tk()
        self.copyFrame.geometry(Util.getGeometry(self.copyFrame, Constants.COPY_FRAME_WIDTH, Constants.COPY_FRAME_HEIGHT))
        self.copyFrame.title("Copy Data")
        self.descriptionLabel = Label(self.copyFrame, text=Constants.COPY_FRAME_DESCRIPTION, wraplength=400)
        self.descriptionLabel.grid(row=0, columnspan=2, sticky=W + E + N + S, pady=(10,0))
        self.sourceFileButton = Button(self.copyFrame, text="Source Path", command=self.browseFromButton, width=15)
        self.sourceFileButton.grid(row=1, column=0, sticky=W, padx=(10, 4), pady=(20, 4))
        self.destinationFileButton = Button(self.copyFrame, text="Destination Path", command=self.browseToButton,
                                            width=15)
        self.destinationFileButton.grid(row=2, column=0, sticky=W, padx=(10, 4), pady=4)
        self.sourceLabel = Entry(self.copyFrame, width=50, textvariable=self.fromFolderPath)
        self.sourceLabel.grid(row=1, column=1, sticky=W, pady=(20, 4))
        self.destinationLabel = Entry(self.copyFrame, width=50, textvariable=self.toFolderPath)
        self.destinationLabel.grid(row=2, column=1, sticky=W)
        self.labelArrangement = Label(self.copyFrame, text="Rules:")
        self.labelArrangement.grid(row=3, sticky=N + E + W + S, padx=4, pady=4)
        self.rule = Entry(self.copyFrame)
        self.rule.grid(row=3, column=1, sticky=W)
        self.rule.insert(END, 'jpg')
        dataCopy = DataCopy(self.sourceLabel, self.destinationLabel, self.rule)
        commandhandler = lambda: self.processDataManagement(dataCopy)
        okButton = Button(self.copyFrame, text="Ok", command=commandhandler, width=5)
        okButton.grid(row=4, column=0)
        handler = lambda: self.onCloseOtherFrame(self.copyFrame)
        cancelButton = Button(self.copyFrame, text="Cancel", command=handler)
        cancelButton.grid(row=4, column=1)

    # ----------------------------------------------------------------------
    # Initializes the rename frame and assigns the handler for all the buttons
    def openRenameFrame(self):
        self.hide()
        self.renameFrame = Tk()
        self.renameFrame.geometry(
            Util.getGeometry(self.renameFrame, Constants.RENAME_FRAME_WIDTH, Constants.RENAME_FRAME_HEIGHT))
        self.renameFrame.title("Rename Data")
        self.descriptionLabel = Label(self.renameFrame, text=Constants.RENAME_FRAME_DESCRIPTION, wraplength=400)
        self.descriptionLabel.grid(row=0, columnspan=2, sticky=W + E + N + S, pady=(10, 0))
        self.folderButton = Button(self.renameFrame, text="Browse", command=self.browseButton, width=15)
        self.folderButton.grid(row=1, column=0, sticky=W, padx=(10, 4), pady=(20, 4))
        self.folderLabel = Entry(self.renameFrame, width=50, textvariable=self.folderPath)
        self.folderLabel.grid(row=1, column=1, sticky=W, pady=(20, 4))
        self.labelArrangement = Label(self.renameFrame, text="Rules:")
        self.labelArrangement.grid(row=3, sticky=N + S + W + E, padx=4, pady=4)
        self.rule = Entry(self.renameFrame)
        self.rule.grid(row=3, column=1, sticky=W)
        self.rule.insert(END, 'jpg')
        dataRename = DataRename(self.folderLabel, self.rule)
        commandhandler = lambda: self.processDataManagement(dataRename)
        okButton = Button(self.renameFrame, text="Ok", command=commandhandler, width=5)
        okButton.grid(row=4, column=0)
        handler = lambda: self.onCloseOtherFrame(self.renameFrame)
        cancelButton = Button(self.renameFrame, text="Cancel", command=handler)
        cancelButton.grid(row=4, column=1)

    # ----------------------------------------------------------------------
    # Initializes the select frame and assigns the handler for all the buttons
    def openSelectFrame(self):
        self.hide()
        self.selectFrame = Tk()
        self.selectFrame.geometry(
            Util.getGeometry(self.selectFrame, Constants.SELECT_FRAME_WIDTH, Constants.SELECT_FRAME_HEIGHT))
        self.selectFrame.title("Select Data")
        percentageFiles = IntVar()
        self.descriptionLabel = Label(self.selectFrame, text=Constants.SELECT_FRAME_DESCRIPTION, wraplength=400)
        self.descriptionLabel.grid(row=0, columnspan=2, sticky=W + E + N + S, pady=(10, 0))
        self.sourceFileButton = Button(self.selectFrame, text="Source Path", command=self.browseFromButton,
                                       width=15)
        self.sourceFileButton.grid(row=1, column=0, sticky=W, padx=2, pady=2)
        self.destinationFileButton = Button(self.selectFrame, text="Destination Path", command=self.browseToButton,
                                            width=15)
        self.destinationFileButton.grid(row=2, column=0, sticky=W, padx=2, pady=2)
        self.sourceLabel = Entry(self.selectFrame, width=50, textvariable=self.fromFolderPath)
        self.sourceLabel.grid(row=1, column=1, sticky=W)
        self.destinationLabel = Entry(self.selectFrame, width=50, textvariable=self.toFolderPath)
        self.destinationLabel.grid(row=2, column=1, sticky=W)
        self.labelArrangement = Label(self.selectFrame, text="Rules:")
        self.labelArrangement.grid(row=3, sticky=N + S + W + E, padx=4, pady=4)
        self.rule = Entry(self.selectFrame)
        self.rule.grid(row=3, column=1, sticky=W)
        self.rule.insert(END, 'jpg')
        self.labelPercentageOfFiles = Label(self.selectFrame, text="Percentage:")
        self.labelPercentageOfFiles.grid(row=4, sticky=W + N + E + S, padx=4, pady=4)
        self.entryPercentageOfFiles = Entry(self.selectFrame, textvariable=percentageFiles)
        self.entryPercentageOfFiles.grid(row=4, column=1, sticky=W)
        self.entryPercentageOfFiles.insert(END, 50)
        dataSelect = DataSelect(self.sourceLabel, self.destinationLabel, self.rule, self.entryPercentageOfFiles)
        commandhandler = lambda: self.processDataManagement(dataSelect)
        okButton = Button(self.selectFrame, text="Ok", command=commandhandler, width=5)
        okButton.grid(row=5, column=0)
        handler = lambda: self.onCloseOtherFrame(self.selectFrame)
        cancelButton = Button(self.selectFrame, text="Cancel", command=handler)
        cancelButton.grid(row=5, column=1)

    # ----------------------------------------------------------------------
    # Initializes the KfoldFrame and assigns the handler for all the buttons
    def openKFoldFrame(self):
        self.hide()
        self.kFoldFrame = Tk()
        self.kFoldFrame.geometry(
            Util.getGeometry(self.kFoldFrame, Constants.K_FOLD_FRAME_WIDTH, Constants.K_FOLD_FRAME_HEIGHT))
        self.kFoldFrame.title("K Fold Data Selection")
        kFoldNumber = IntVar()
        indexNumber = IntVar()
        self.descriptionLabel = Label(self.kFoldFrame, text=Constants.FOLD_FRAME_DESCRIPTION, wraplength=400)
        self.descriptionLabel.grid(row=0, columnspan=2, sticky=W + E + N + S, pady=(10, 0))
        self.sourceFileButton = Button(self.kFoldFrame, text="Source Path", command=self.browseFromButton, width=15)
        self.sourceFileButton.grid(row=1, column=0, sticky=W, padx=2, pady=2)
        self.sourceLabel = Entry(self.kFoldFrame, width=50, textvariable=self.fromFolderPath)
        self.sourceLabel.grid(row=1, column=1, sticky=W)
        self.destinationFileButton = Button(self.kFoldFrame, text="Destination Path", command=self.browseToButton,
                                            width=15)
        self.destinationFileButton.grid(row=2, column=0, sticky=W, padx=2, pady=2)
        self.destinationLabel = Entry(self.kFoldFrame, width=50, textvariable=self.toFolderPath)
        self.destinationLabel.grid(row=2, column=1, sticky=W)
        self.labelArrangement = Label(self.kFoldFrame, text="Rules:")
        self.labelArrangement.grid(row=3, column=0, sticky=W + N + S + E, padx=2, pady=2)
        self.rule = Entry(self.kFoldFrame)
        self.rule.grid(row=3, column=1, sticky=W)
        self.rule.insert(END, 'jpg')
        self.labelNoOfFolds = Label(self.kFoldFrame, text="No of Folds")
        self.labelNoOfFolds.grid(row=4, column=0, sticky=W + N + S + E, padx=2, pady=2)
        self.noOfFolds = Entry(self.kFoldFrame, textvariable=kFoldNumber)
        self.noOfFolds.grid(row=4, column=1, sticky=W)
        self.noOfFolds.insert(END, 5)
        self.labelIndex = Label(self.kFoldFrame, text="Index")
        self.labelIndex.grid(row=5, column=0, sticky=W + N + S + E, padx=2, pady=2)
        self.index = Entry(self.kFoldFrame, textvariable=indexNumber)
        self.index.grid(row=5, column=1, sticky=W)
        self.index.insert(END, 2)
        dataSelect = DataFold(self.sourceLabel, self.destinationLabel, self.rule, self.noOfFolds, self.index)
        commandhandler = lambda: self.processDataManagement(dataSelect)
        okButton = Button(self.kFoldFrame, text="Ok", command=commandhandler, width=5)
        okButton.grid(row=6, column=0)
        handler = lambda: self.onCloseOtherFrame(self.kFoldFrame)
        cancelButton = Button(self.kFoldFrame, text="Cancel", command=handler)
        cancelButton.grid(row=6, column=1)


    # ----------------------------------------------------------------------
    # Hides the main frame when function buttons are clicked
    # Function buttons - Copy,Rename,Select
    def hide(self):
        self.master.withdraw()

    # ----------------------------------------------------------------------
    # Show the main frame again when cancel button is clicked on child function frames(Copy, Rename, Select)
    def show(self):
        self.master.update() # Updates the main frame
        self.master.deiconify() #Redraws the main frame

    # ----------------------------------------------------------------------
    def processDataManagement(self, dataManagement):
        status, msg = dataManagement.valid()
        if status:
            exStatus, exMsg = dataManagement.execute()
            tkMessageBox.showinfo(dataManagement.getName(), exMsg)
        else:
            tkMessageBox.showinfo('Error', msg)

    # ----------------------------------------------------------------------
    # Triggered when cancel button is clicked in child window
    # Closes the child window and triggers the main window to be showed
    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

    # ----------------------------------------------------------------------
    # selects the directory by opening the browse directory window
    # This function is called from Rename Frame
    def browseButton(self):
        filename = tkFileDialog.askdirectory(parent=self.master)
        self.folderPath.set(filename)
        self.folderLabel.delete(0, END)
        self.folderLabel.insert(0, filename)
        print(filename)

    #-----------------------------------------------------------------------
    # selects the directory by opening the browse directory window
    # This function is called from Copy Frame and Select Frame
    def browseFromButton(self):
        filename = tkFileDialog.askdirectory(parent=self.master)
        self.fromFolderPath.set(filename)
        self.sourceLabel.delete(0, END)
        self.sourceLabel.insert(0, filename)
        print(filename)

    #-----------------------------------------------------------------------
    # selects the directory by opening the browse directory window
    # This function is called from Copy Frame and Select Frame
    def browseToButton(self):
        filename = tkFileDialog.askdirectory(parent=self.master)
        self.destinationLabel.delete(0, END)
        self.destinationLabel.insert(0, filename)
        self.toFolderPath.set(filename)
        print(filename)

root = Tk() #Creates the MainWindow
b = UIDataManagement(root)
root.mainloop() #Opens the window forever
