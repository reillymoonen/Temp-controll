from tkinter import *


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

        self.to_help_button = Button(self.temp_frame,
                                        text="Help / Info",
                                        bg="#CC6600",
                                        fg="#ffffff",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=self.help_info)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

    def help_info(self):
        DisplayHelp()


class DisplayHelp:

    def __init__(self):
        # setup dialog box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=400,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                  text="Help / Info",
                                  font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        self.help_text_label = Label(self.help_frame,
                                       text="This is a help / info window",
                                       wraplength=350,
                                       justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", command=self.close_help)
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set background colour on
        # everything except the button
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self):  # Unindented to make it a class method
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
    
    up to 3.26 of video 8