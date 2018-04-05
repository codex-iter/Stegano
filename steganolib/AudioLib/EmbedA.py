import sys
import wave
import random
import os
import math

#input arguments 1)audio file 2) hidden file 3)destiny file name 4)key

audio_file = wave.open(sys.argv[1], 'r')
hidden_file = open(sys.argv[2], 'r')
key = sys.argv[4]
random.seed(int(key))
file_size = os.path.getsize(sys.argv[2])
spreading_factor = audio_file.getnframes() //(file_size)    #remove decimal
#print (file_size
#print (audio_file.getnframes()
if spreading_factor >= 100:                     #find optimal spread factor
      spread = math.floor(spreading_factor / 2) #used to generate random number to modify lsb of said random number index
      print ("The Spreading Factor is " + str(spreading_factor) + "\nDo you want to Continue?(yes or no)")
      while True:

            destiny_file = wave.open(sys.argv[3], 'w')
            destiny_file.setnchannels(audio_file.getnchannels())
            destiny_file.setsampwidth(audio_file.getsampwidth())
            destiny_file.setframerate(audio_file.getframerate())
            destiny_file.setnframes(audio_file.getnframes())


            user_choice = input("")
            if(user_choice.lower() == "yes" or user_choice.lower() == "y"):
                  print ("Starting process:.. ")
                  buf = bytearray(audio_file.readframes(spreading_factor))  #get and store string of bytes for spreading factor based number of frames

                  while(len(buf) > 0):                      # for every audio frame in a spreading factor
                        data = hidden_file.read(1)          #get only one byte of hidden file
                        if data:                            # and kinda spread it
                              data = ord(data)
                              for i in range(8):
                                    bit = data >> i                                             #change lsb for retreival later
                                    f_byte = int(i * spread + random.randint(0,spread - 1))     #selecting psuedo random byte index to modify( defined by spread factor pattern and key seed)
                                    if f_byte % 2 == 1:   #making sure its eaither Byte0 or Byte2 otherwise noise is detected on M50x
                                          f_byte -=1
                                    #print (f_byte
                                    if buf[f_byte] % 2 == 0 and bit % 2 == 1:                #if its an odd ascii bit in an even byte index
                                          buf[f_byte] += 1                                   #modify byte acording to bit read from data
                                    elif buf[f_byte] % 2 == 1 and bit % 2 == 0:
                                          buf[f_byte] -= 1
                        try:                                                                 #wav librabry errors
                              destiny_file.writeframes(buf)                                  #write the buffer
                              buf = bytearray(audio_file.readframes(spreading_factor))
                        except wave.Error as e:
                              print(str(e))

                  print ("100%")
                  print ("\nProcess done!")
                  print ("The Spreading Factor is " + str(spreading_factor * 4) + " bytes per byte")
                  print ("To recover your hidden file put it on the recovery program")
                  print ("Your File key is: " + str(file_size))
                  print ("Example:\n\npython recovery.py <Audio File> <Private Key> <File Key> > <Destiny File> \n\n")
                  break
            elif user_choice.lower() == "no" or user_choice.lower() == "n":
                  print ("Proceed to exit")
                  break
            else:
                  print ("Please enter yes or no")
            destiny_file.close()

else:
      print ("Is NOT secure to continue, you need a bigger wav file")

hidden_file.close()
audio_file.close()
