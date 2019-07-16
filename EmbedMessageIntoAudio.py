import wave
import binascii
import copy
from Crypto.PublicKey import RSA
import sys


def generate_RSA_key_pair():
    """Generate a RSA key pair and store it in a file."""
 
        # generate RSA private of size 2048 bit.
    key = RSA.generate(2048)
    key_file = open('RSAkey.pem','wb')
        # Empty the key file if it has some existing content.
    key_file.truncate(0)        
    key_file.write(key.exportKey('PEM'))
    key_file.close()
    


def encrypt_message(message):
    """Encrypt the message with private key and return the corresponding hex."""

    key_file =  open('RSAkey.pem','rb')
    key = RSA.importKey(key_file.read())
        # Get the corresponding public key for the private key.
    public_key = key.publickey()   
    encrypted_message = ''.join(public_key.encrypt(message,32))
        # Encrypt the message with public key and convert it to hex.
    return binascii.b2a_hex(encrypted_message) 




def embed_message_into_audio(input_audio,secret_message):
    """Take a audio file and the secert message which is to be embedded into it.
     Returns the audio frames with message embedded into them."""   

        # Get the frames from input audio.
    audio_frames = copy.copy(input_audio.readframes(input_audio.getparams()[3])) 
    msg_byte_array = bytearray(secret_message.encode())
         # Starting from the 45th byte as first 44 bytes are the headers of audio file
    i=44                                           
    output_frames = copy.copy(audio_frames[0:i])
    for byte_index in range(0,len(msg_byte_array)):  
        msg_byte = bin(msg_byte_array[byte_index])[2:].zfill(8)
        for j in range(0,len(msg_byte)):
            # Applying LSB algorithm to embed each bit of message in the Least signification position of each audio frame.
          current_frame =   bin(ord(audio_frames[i]))[2:].zfill(8)
          current_frame = current_frame[0:7] + msg_byte[j]
          output_frames = output_frames + str(chr(int(current_frame,2)))
          i=i+1

    return output_frames



def convert_output_frames_to_audio_file(input_audio_file, output_frames, ouput_audio_file_name):
    """Converts the audio frames to audio file with parameters same as input file."""
 
    output_audio_params = input_audio_file.getparams()
    output_audio_file = wave.openfp(ouput_audio_file_name,"wb")
        # Set the parameters of the output audio same as input audio.
    output_audio_file.setparams(output_audio_params) 
    output_audio_file.writeframes(output_frames)
    output_audio_file.close()



def main():    
        """ Takes the console inputs and calls all the functions."""
        print(sys.argv[0],sys.argv[1],sys.argv[2])
            # Generate RSA key.
        generate_RSA_key_pair()
            # Get the input audio file name from console.
        input_audio_file_name = sys.argv[1]
        input_audio_file = wave.open(input_audio_file_name,'rb')
        

            # Get the message to be embedded and encrypt it.
        secret_message = encrypt_message(sys.argv[2])
             # Embed the message into audio frames.
        output_frames = embed_message_into_audio(input_audio_file, secret_message)
            # Get the output file name and write messaged embedded frames to it.
        ouput_audio_file_name = 'Output.wav'
        convert_output_frames_to_audio_file(input_audio_file, output_frames, ouput_audio_file_name)
        input_audio_file.close()       
    
main()






