import pdfplumber
import pyttsx3
from tkinter import *
from tkinter import filedialog


# ---------------------------- INITIAL PARAMETERS --------------------- #
FONT_NAME = "Arial"
WHITE = "#ecf4f3"
DBLUE = "#006a71"
ORANGE = "#ff7e67"


# ------------------------ FIND PDF AND CONVERT TO AUDIO ----------------- #
def find_file():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open PDF file",
                                          filetypes=[("PDF Files", ".pdf")])

    if filename:
        doc_text = ""
        with pdfplumber.open(filename) as pdf:
            for page in range(len(pdf.pages)):
                page_text = pdf.pages[page].extract_text()
                doc_text += page_text

        output = pyttsx3.init()
        output.say(doc_text)
        output.runAndWait()


# ------------------ UI SETUP ------------------  #
window = Tk()
window.title("PDF to Audio App")
window.config(padx=100, pady=50, bg=WHITE)

header_label = Label(text="Welcome to your PDF to Audio App. Please select your PDF:",
                     bg=WHITE, fg=DBLUE, font=(FONT_NAME, 20, "bold"))
header_label.grid(column=0, row=0, pady=30)
file_button = Button(text="Find File", command=find_file, bg=ORANGE, fg=WHITE, highlightthickness=0, font=(FONT_NAME, 20, "bold"), width=20)
file_button.grid(column=0, row=1, pady=30)
window.mainloop()



