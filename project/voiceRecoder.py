import sounddevice as sd
import soundfile as sf
from tkinter import *


def voice_rec():
    fs = 48000

    duration = 5


myrecording = sd.rec(int(duration * fs),
                     samplerate=fs, channels=2)
sd.wait()

return sf.write('my_audio_file.flac', myrecording, fs)

master = Tk()
Label(master, text="voice recoder : ).grid(row-, sticky-w, rowspan=5)",)

b = Button(master, text="start", command=voice_rec)
b.grid(row=0, column=2, columspan=2, rowspan=2, padx=5, pady=5)

mainloop()
