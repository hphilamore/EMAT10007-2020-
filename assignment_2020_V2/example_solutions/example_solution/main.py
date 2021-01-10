import numpy as np
from os.path import exists
from funcs import *
import csv

mode, rot, msg, input_mode = setup()

if mode=='e':
    output_msg = encrypt(rot, msg)  
elif mode == 'a':
    output_msg = auto_decrypt(msg)
else:
    output_msg = decrypt(rot, msg)
    
print_metrics(output_msg)

plot_metrics(output_msg)

save_metrics()     



