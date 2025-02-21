from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
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
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # strings for 'long' labels...
        recent_intro_txt = ("Below are your recent calculations - showing "
                            "3 / 3 calculations. All calculations are "
                            "shown to the nearest degree")

        calculations = ""

        export_instructions_txt = ("To export your calculation history, "
                                   "click the 'Export' button below.")

        # Label list (label text | format | bg)
        history_label_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            ["calculations list", ("Arial", "14"), green_back],
            [export_instructions_txt, ("Arial", "11"), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_label_list):
            make_label = Label(self.history_frame, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count, column=0)
            history_label_ref.append(make_label)

        # Retrieve export instruction label so that we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # make frame to hold buttons (two columns)
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        button_ref_list = []

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["Export", "#DD4C99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            make_button = Button(self.hist_button_frame,
                                 font=("Arial", "12", "bold"),
                                 text=btn[0], bg=btn[1],
                                 fg="#ffffff", width=12,
                                 command=btn[2])
            make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)
            button_ref_list.append(make_button)

    def close_history(self, partner):
        """
        Closes history dialog box (and enables history button)
        """
        # Put history button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()