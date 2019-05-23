import os
import cv2
import csv
from lxml import etree
import xml.etree.cElementTree as ET


csv_dir = "C:/Users/default.DESKTOP-43PHGMT/Desktop/VOCdevkit/test/VOC2006/labels.csv"


def write_xml(folder, fname, width, height, class_name, xmin, ymin, xmax, ymax):

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = fname
    ET.SubElement(annotation, 'segmented').text='0'
    
    size = ET.SubElement(annotation,'size')
    ET.SubElement(size,'width').text = str(width)
    ET.SubElement(size,'height').text = str(height)
    ET.SubElement(size,'depth').text = '3'

    for i in range(len(class_name)):
        ob = ET.SubElement(annotation,'object')
        ET.SubElement(ob,'name').text = str(class_name[i])
        ET.SubElement(ob,'pose').text = 'Unspecified'
        ET.SubElement(ob,'truncated').text = '0'
        ET.SubElement(ob,'difficult').text = '0'
        bbox = ET.SubElement(ob,'bndbox')
        ET.SubElement(bbox,'xmin').text = str(xmin[i])
        ET.SubElement(bbox,'ymin').text = str(ymin[i])
        ET.SubElement(bbox,'xmax').text = str(xmax[i])
        ET.SubElement(bbox,'ymax').text = str(ymax[i])

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)

    save_path = 'C:/Users/default.DESKTOP-43PHGMT/Desktop/darkflow versions/darkflow-master/test_annot/'+fname.split('.')[0]+'.xml'
    with open(save_path,'wb') as temp_xml:
        temp_xml.write(xml_str)  

      

with open(csv_dir) as csv_file:
    csvreader = csv.reader(csv_file)
    filename=''
    width=0
    height=0
    class_name=[]
    xmin=[]
    ymin=[]
    xmax=[]
    ymax=[]
    temp=''
        
    for x in csvreader:
        if(x[0]!='image'):
            if(x[0]!=temp):
                print(filename,width,height,class_name,xmin,ymin,xmax,ymax)
                
                if(filename!=''):
                    write_xml('annot',filename,width,height,class_name,xmin,ymin,xmax,ymax)
                    
                
                filename=''
                width=0
                height=0
                class_name=[]
                xmin=[]
                ymin=[]
                xmax=[]
                ymax=[]

                temp=x[0]
                filename = x[0].split('^')[1]
                width = x[1]
                height = x[2]
                class_name.append(x[3])
                xmin.append(x[4])
                ymin.append(x[5])
                xmax.append(x[6])
                ymax.append(x[7])
            else:
                class_name.append(x[3])
                xmin.append(x[4])
                ymin.append(x[5])
                xmax.append(x[6])
                ymax.append(x[7])
        


