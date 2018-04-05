import wave
import sys
import random
import math

audio_file = wave.open(sys.argv[1], 'r')
private_key = sys.argv[2]
file_key = int(sys.argv[3])

random.seed(int(private_key))                                       #same seed as embed

recovery_factor = audio_file.getnframes() // (file_key)             #same as spread factor
spread = math.floor(recovery_factor / 2)                            #same spread to calculate same  bytes selected
n = 0                                                               #number of bytes written
buf = bytearray(audio_file.readframes(recovery_factor))
while len(buf) > 0:
    d = 0
    for i in range(8):
        f_byte = int(i * spread + random.randint(0, spread - 1))
        if f_byte % 2 == 1:
            f_byte -= 1
        d += (buf[f_byte] % 2) << i                                 #left shift and retreive data in form of byte
    sys.stdout.write(chr(d))
    n += 1
    if n >= file_key:
        break
    buf = bytearray(audio_file.readframes(recovery_factor))
