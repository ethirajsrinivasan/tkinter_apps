import glob
import shutil
from DataMangement import *
import random

class DataSelect(DataManagement):


    def __init__(self, sourceLabel, destinationLabel, rule, percentageOfFiles):
        self.sourceLabel = sourceLabel
        self.destinationLabel = destinationLabel
        self.rule = rule
        self.percentageOfFiles = percentageOfFiles

    def getName(self):
        return 'Select Data'

    # -----------------------------------------------------------------------
    # Validates the action before intended action is performed
    # Checks if all the data is filled up
    def valid(self):
        if len(self.sourceLabel.get()) == 0:
            return False, 'Select Source File Path'
        elif len(self.destinationLabel.get()) == 0:
            return False, 'Select Destination File Path'
        elif len(self.rule.get()) == 0:
            return False, 'Enter rule'
        elif len(self.percentageOfFiles.get()) == 0:
            return False, 'Enter percentage of files'
        return True, 'Valid Data'

    # ----------------------------------------------------------------------
    # Selects random k no of files in the source directory based on the rules
    # and copies it to the destination directory
    # rules are extensions of the file
    def execute(self):
        try:
            files = glob.glob(self.sourceLabel.get() + '/*.' + self.rule.get())
            k = int(self.percentageOfFiles.get()) * len(files) / 100
            files = random.sample(files, k)
            for file in files:
                shutil.copy2(file, self.destinationLabel.get())
            return True, 'Successfully Completed'
        except Exception as e:
            return False, e.message
