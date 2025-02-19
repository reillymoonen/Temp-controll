from idlelib.history import History
from tkinter import *
from functools import partial # To prevent unwanted windows


class Converter:
    """
    Temperature converion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History /Export",
                                        bg="#CC6600",
                                        fg="#ffffff",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, column=0, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialog box and disables history button
        (so that users can't create multiple history boxes).
        """
        HistoryExport(self)

class HistoryExport:
    """
    Displays history dialog box
    """

    def __init__(self, partner):
        # setup dialog box and background colour

        green_back = "#D5E8D4"
        peach_back = "#FFe6cc"

        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and
        # 'releases' history button
        self.history_box.protocol('WH_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

up to 1.48 of video 10