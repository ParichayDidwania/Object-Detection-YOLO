import os
from tqdm import tqdm
import csv

classes = ['bicycle','bus','car','cat','cow','dog','horse','motorbike','person','sheep']
TRAIN_DIR='C:/Users/default.DESKTOP-43PHGMT/Desktop/VOCdevkit/VOC2006/Annotations'
list1=[]
def path_list_maker(dir_path):
    for firstname in os.listdir(dir_path):
        name = firstname.split('.')
        full_name = os.path.join(TRAIN_DIR,firstname)
        list1.append([name[0],full_name])
    return list1 

f=1
size = 'Image size (X x Y x C)'
class_text = 'Details for object'
coords = 'Bounding box for object'
with open('C:/Users/default.DESKTOP-43PHGMT/Desktop/VOCdevkit/VOC2006/labels.csv', 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('image', 'width','height','class','min_x','min_y','max_x','max_y'))
        dir_list = path_list_maker(TRAIN_DIR)

        for i in tqdm(dir_list):
            with open(i[1], 'r') as in_file:

                first_name=i[0]
                height=0
                width=0
                class_name=''
                minx=0
                maxx=0
                miny=0
                maxy=0

                content = in_file.readlines()
                content = [x.strip() for x in content] 
                sub=[]
                for j in content:
                    if size in j:
                        total_size = j.split(':')[1].strip()
                        width = int(total_size.split('x')[0].strip())
                        height = int(total_size.split('x')[1].strip())
                    
                    if class_text in j:
                        for names in classes:
                            if(names in j):
                                class_name = names
                                break
                    
                    if coords in j:
                        full_cord = j.split(':')[1].strip()
                        min_coord = full_cord.split('-')[0].replace("(","").replace(")","").strip()
                        max_coord = full_cord.split('-')[1].replace("(","").replace(")","").strip()
                        
                        minx=int(min_coord.split(',')[0].strip())
                        miny=int(min_coord.split(',')[1].strip())

                        maxx=int(max_coord.split(',')[0].strip())
                        maxy=int(max_coord.split(',')[1].strip())
                        f=0
                    if(f==0):
                        writer.writerow(('^'+first_name+'.png',width,height,class_name,minx,miny,maxx,maxy))
                        f=1
        

                   