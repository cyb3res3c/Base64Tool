import tkinter as tk
from tkinter import font
from myBase64Encode import myBase64Encode
from myBase64Decode import myBase64Decode


def setFontSize(textWidget):
    textWidget.tag_config("big", font=("Arial", 16))
    textWidget.tag_add("big", "1.0", "end")


def showEncodeText(textBoxInput, textBoxOutput):
    text = textBoxInput.get("1.0", "end-1c")
    showContent = myBase64Encode(text)
    textBoxOutput.delete("1.0", "end")
    textBoxOutput.insert("1.0", showContent)


def showDecodeText(textBoxInput, textBoxOutput):
    text = textBoxInput.get("1.0", "end-1c")
    showContent = myBase64Decode(text)
    textBoxOutput.delete("1.0", "end")
    textBoxOutput.insert("1.0", showContent)


def toolGui():
    window = tk.Tk()
    window.title("Base64Tool v1.0 by Cyb3rES3c")

    width = 600
    height = 600
    textRowCount = 10
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    screensize = '%dx%d+%d+%d' % (width, height, (screenWidth - width) / 2, (screenHeight - height) / 2)
    # print("screen size: " + screensize)
    window.geometry(screensize)
    # Set window self-adaption
    window.resizable(width=True, height=True)

    guiFont = font.Font(family='Helvetica', size=16, weight='bold')

    textBoxInput = tk.Text(window, height=textRowCount, font=guiFont)
    # Set text box self-adaption width
    textBoxInput.pack(fill=tk.X, expand=True)

    textBoxOutput = tk.Text(window, height=textRowCount, font=guiFont)
    textBoxOutput.pack(fill=tk.X, expand=True)

    # Create a button to show text
    encodeButton = tk.Button(window, text='Encode', command=lambda: showEncodeText(textBoxInput, textBoxOutput))
    encodeButton.pack(pady=10)

    decodeButton = tk.Button(window, text='Decode', command=lambda: showDecodeText(textBoxInput, textBoxOutput))
    decodeButton.pack()

    window.mainloop()


if __name__ == '__main__':
    toolGui()
