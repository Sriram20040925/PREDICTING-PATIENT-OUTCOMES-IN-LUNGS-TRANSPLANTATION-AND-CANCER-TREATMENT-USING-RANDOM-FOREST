import os
os.chdir('normal_lung')
i=1
for file in os.listdir():
    src=file
    dst="normal_lung"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

