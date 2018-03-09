from steganolib import stegano_az as stg_az

stg_az.lsb_embed('text.txt','image.jpg',1)
stg_az.lsb_retv('output.txt','eimage.png',1)

stg_az.lsb_alpha_embed('text.txt','image.jpg',1)
stg_az.lsb_alpha_retv('outalpha.txt','eimagealpha.png',1)