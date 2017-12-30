import glob
import shutil
from DataMangement import *

class DataRename(DataManagement):


    def __init__(self, folderLabel, rule):
        self.folderLabel = folderLabel
        self.rule = rule

    def getName(self):
        return 'Rename Data'

    # -----------------------------------------------------------------------
    # Validates the copy frame before performing the intented action
    # Checks all the data is filled up else throws error message
    def valid(self):
        if len(self.folderLabel.get())==0:
            return False, 'Select Folder Path'
        elif len(self.rule.get())==0:
            return False, 'Enter rule'
        return True, 'Valid Data'

    # ----------------------------------------------------------------------
    # Renames file in destination based on the rules
    # rules are generally extension of the files
    def execute(self):
        try:
            files = glob.glob(self.folderLabel.get() + '/*.' + self.rule.get())
            for i in range(len(files)):
                shutil.move(files[i], self.folderLabel.get() + '/' + str(i) + '.' + self.rule.get())
            return True, 'Successfully Completed'
        except Exception as e:
            return False, e.message
