import shutil
import glob
from DataMangement import *


class DataCopy(DataManagement):

    def __init__(self, sourceLabel, destinationLabel, rule):
        self.sourceLabel = sourceLabel
        self.destinationLabel = destinationLabel
        self.rule = rule

    def getName(self):
        return 'Copy Data'

    # -----------------------------------------------------------------------
    # Validates the copy frame before performing the intented action
    # Checks all the data is filled up else throws error message
    def valid(self):
        if len(self.sourceLabel.get()) == 0:
            return False, 'Select source path'
        elif len(self.destinationLabel.get()) == 0:
            return False, 'Select Destination Path'
        elif len(self.rule.get()) == 0:
            return False, 'Enter the rule'
        return True, 'Valid Data'

    # ----------------------------------------------------------------------
    # Copies file from source to destination based on the rules
    # rules are generally extension of the files
    def execute(self):
        try:
            sourceDir = glob.glob(self.sourceLabel.get() + "/*." + self.rule.get())
            for file in sourceDir:
                shutil.copy2(file, self.destinationLabel.get())
            return True, 'Successfully Completed'
        except Exception as e:
            return False, e.message
