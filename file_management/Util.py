import os

class Util:

    @staticmethod
    def get_immediate_subdirectories(a_dir):
        return [name for name in os.listdir(a_dir)
                if os.path.isdir(os.path.join(a_dir, name))]

    @staticmethod
    def getGeometry(frame, w, h):
        # get screen width and height
        ws = frame.winfo_screenwidth()  # width of the screen
        hs = frame.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        return '%dx%d+%d+%d' % (w, h, x, y)
