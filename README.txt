							Audio Steganography with applied Cryptography
							---------------------------------------------
1. Please use python version 2.7 as the code is built on it for efficient performance


2. Modules Needed: Install the python modules Crypto,Tkinter with the below commands. They are used in the code.

		pip install pycrypto
		pip install Tkinter


3. Code Files Description:
   
	EmbedMessageIntoAudio.py - It contains the code to generate a RSA key pair, encrypt the message and embed it into the audio file using LSB algorithm. 
				   It generates a new audio file with the message embedded.
	
	ExtractMessageFromAudio.py - It contains the code to extract the embedded message from audio and decrypt it with generated RSA public key.
				     It gives the original message as output.

	StegApplication.py - It contains code for UI widgets in audio steganography tool developed to perform the whole operation. It also contains code to execute the above two code files
			  based on events.

4. SampleAudioFiles can be used to test message embedding and extraction process.

5. Execute the StegApplication.py with below command to use the audio steganography tool for performing embedding and extraction of messages from audio files. 
	
	$ python StegApplication.py


   	

	 
