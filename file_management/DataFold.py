import glob
import shutil
from DataMangement import *
from  Util import *


class DataFold(DataManagement):


    def __init__(self, sourceLabel, destinationLabel, rule, noOfFolds, index):
        self.sourceLabel = sourceLabel
        self.destinationLabel = destinationLabel
        self.rule = rule
        self.noOfFolds = noOfFolds
        self.index = index

    def getName(self):
        return 'Fold Data'

    # -----------------------------------------------------------------------
    # Validates all the data required for the K fold Process to perform
    def valid(self):
        if len(self.sourceLabel.get()) == 0:
            return False, "Select Source File Path"
        elif len(self.destinationLabel.get()) == 0:
            return False,"Select Destination File Path"
        elif len(self.rule.get()) == 0:
            return False, "Enter Rule"
        elif len(self.noOfFolds.get()) == 0:
            return False, "Enter No of Folds"
        elif len(self.index.get()) == 0:
            return False, "Enter the index"
        return True, 'Valid Data'


    # ----------------------------------------------------------------------
    # Transfers the files from source to destination based on the K Fold
    def execute(self):
        try:
            subFolders = Util.get_immediate_subdirectories(self.sourceLabel.get())
            if len(subFolders) > 0:
                for subFolder in subFolders:
                    self.executeKFold(self.sourceLabel.get()+"/"+subFolder)
            else:
                self.executeKFold(self.sourceLabel.get())
            return True, 'Successfully Completed'
        except Exception as e:
            return False, e.message

    def executeKFold(self, path):
        files = glob.glob(path + "/*." + self.rule.get())
        folds = int(self.noOfFolds.get())
        index = int(self.index.get())
        for i in range(1, folds + 1):
            n = i * index
            print(n)
            if n < len(files):
                shutil.copy2(files[n], self.destinationLabel.get())