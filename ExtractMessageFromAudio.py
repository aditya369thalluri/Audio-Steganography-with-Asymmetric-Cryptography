import wave
import binascii
import copy
from Crypto.PublicKey import RSA
import sys


def extract_message_from_audio(audio_file):
      """Extract the bits from audio frames and convert to bytes."""

      byte = ''
      secret_message = ''
      audio_frames = copy.copy(audio_file.readframes(audio_file.getparams()))
      for i in range(44,len(audio_frames)):
            # Extract the Least significant bit from each frame and convert them to bytes.
            current_frame =   bin(ord(audio_frames[i]))[2:].zfill(8)
            byte = byte + current_frame[7]
            if(len(byte)==8):
               secret_message += chr(int(byte,2))
               byte = ''
      return secret_message



def decrypt_message(message):
    """Decrypt the extracted message with RSA private key."""
   
    key_file =  open('RSAkey.pem','rb')
          # Get the stored private key from key file.
    key = RSA.importKey(key_file.read())
          # Decrypt the message with key.
    decrypted_message = key.decrypt(binascii.a2b_hex(message))  
    return decrypted_message


def main():
      """ Takes the console inputs and calls all the functions."""

      # Get the audio file with message embedded .
      """audio_file_name=input('enter file: ')"""
      audio_file = wave.open(sys.argv[1],'rb')
      # Extract the message and decrypt it .
      secret_message = decrypt_message(extract_message_from_audio(audio_file))
      audio_file.close()    
      # Display the message.
      open('result.txt','wb').write(secret_message)
     
main()
