#!/usr/bin/python
import re
import time
import Tkinter


class SevenElevenApp(Tkinter.Tk):
    """docstring for SevenElevenApp"""
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def click(self):
        text = self.entry.get()
        g = re.match('(\d{1,2}):(\d{2})', text)
        if g.group(1) is not None and g.group(2) is not None:
            (h,m) = (g.group(1), g.group(2))
            # cast to numbers
            self.destroy()

    def initialize(self):
        self.title(u'Seven/Eleven')
        self.grid()
        label = Tkinter.Label(self,
                              anchor="w",fg="white",bg="blue", \
                              text="Set your alarm clock"
                              " (00:00-23:59): ")
        label.grid(column=0,row=0,sticky='EW')
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=1,row=0,sticky='EW')
        self.entry.insert(0, u"7:30")
        button = Tkinter.Button(self,text=u"Set", command=self.click)
        button.grid(column=2,row=0)
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
