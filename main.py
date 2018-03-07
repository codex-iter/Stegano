from steganolib import stegano as stg 

stg.lsb_embed('text.txt','image.jpg',1)
stg.lsb_retv('eimage.png')
