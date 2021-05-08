#                   image editor
# put whatever data to be processed in input folder
# the final folder will be formed in the base directory
# comment out the function which u want to apply
# cheers!!
#         -&copy;Heisenberg

import cv2
import os
def greyNresize(dir_n,w,h):
    os.mkdir('grey')
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    inp_dir = os.path.join(cur_dir,dir_n)
    a=0
    for root , dir , files in os.walk(inp_dir):
        for file in files:
            gr = cv2.imread(os.path.join(dir_n,file),0)
            print(gr)
            re=cv2.resize(gr,(w,h))
            cv2.imwrite(os.path.join('grey',str(a)+'.png'), re)
            a+=1
            
greyNresize('input',w=575,h=882)       #for making cascades
