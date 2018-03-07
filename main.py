from steganolib import stegano_az as stg_az

stg_az.lsb_embed('text.txt','image.jpg',1)
stg_az.lsb_retv('eimage.png')
