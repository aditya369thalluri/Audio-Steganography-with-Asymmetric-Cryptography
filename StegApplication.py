import Tkinter
from Tkinter import *
import tkFileDialog as filedialog
import ttk
import os
import tkMessageBox

def get_audio_file():
    """ Set the audio file path browsed by the user"""
    global file_path 
    filename = filedialog.askopenfilename(initialdir = "/",filetypes = (("Audio files","*.wav"),("all files","*.*")))
        # Set the selected audio file path to a global variable file_path to use it
    file_path.set(filename)

def convert_to_wav(filename):
    """Convert audio file of any other format to wav"""
    
    raw_audio = AudioSegment.from_file(filename,format="raw",frame_rate=44100, channels=1,sample_width=1)
        #Write a new file song.wav from any other file format file
    raw_audio.export("song.wav", format="wav")

    
def encrypt_audio():
    """ Execute the code to embed the message into audio file"""
    
    global message
    global file_path
        # Execute the file EmbedMessageIntoAudio.py by passing the selected file and message as parameters
    os.system('EmbedMessageIntoAudio.py ' +e1.get()+' "'+e2.get()+'"')
    message.set('')
    file_path.set('')
        # Show a message box on UI with the new audio file generated
    tkMessageBox.showinfo("Result", "generated new audio file Output.wav in the same directory with message embedded in it")
        
        
def decrypt_audio():
    """ Execute the code to extract and decrypt the message from audio file"""
    
    global message
    global file_path
        # Execute the file ExtractMessageFromAudio.py by passing the selected file and message as parameters
    os.system('ExtractMessageFromAudio.py '+e3.get())
    message_file= open('result.txt','rb')
        # Write the decrypted message to the message box on UI
    message.set(message_file.read())
    file_path.set('')


""" Create of UI widgets for the audio steganography tool"""
    
    #Initialize the window using tkinter
master = Tk()
    #Set the window title
master.title('Audio Steganography')
    #Set the window dimensions
master.geometry("700x500")
master.resizable(0, 0)
    #Add for to the window
form = ttk.Notebook(master)
    #Add encryption tab
encrypt_tab=ttk.Frame(form)
    #Add decryption tab
decrypt_tab=ttk.Frame(form)
form.add(encrypt_tab,text='Encryption')
form.add(decrypt_tab,text='Decryption')
file_path=StringVar()
message = StringVar()
    #Browse option to select an audio file on encryption tab
button1 = Button(encrypt_tab, text='Choose Audio File', command = get_audio_file)
button1.grid(row=0,column=0)
    #Textbox to enter the message that will be embedded into the audio file
e1= Entry(encrypt_tab, textvariable = file_path,width='200')
e1.grid(row=0,column=1)
Label1 = Label(encrypt_tab, text='Enter the Message').grid(row=1,column=0)
e2= Entry(encrypt_tab, textvariable=message, width='200')
e2.grid(row=1,column=1)
    #Button to execute the code for message embedding
button2 = Button(encrypt_tab, text='Encrypt', command = encrypt_audio)
button2.grid(row=2,column=0)
    #Browse option to select an audio file on decryption tab
button3 = Button(decrypt_tab, text='Choose Audio File', command = get_audio_file)
button3.grid(row=0,column=0)
    #Textbox to show the message that will be extracted from the audio file
e3= Entry(decrypt_tab, textvariable = file_path,width='200')
e3.grid(row=0,column=1)
    #Button to execute the code for message extraction
button4 = Button(decrypt_tab, text='Decrypt', command = decrypt_audio)
button4.grid(row=1,column=0)
Label2 = Label(decrypt_tab, text='Message is').grid(row=2,column=0)
e2= Entry(decrypt_tab, width='200',textvariable=message)
e2.grid(row=2,column=1)
    # Pack all the elements to form
form.pack(expand='1',fill='both')
    # Run the window
master.mainloop()


