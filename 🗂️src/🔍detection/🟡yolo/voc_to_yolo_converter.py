import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            file_path = os.path.join(folder_path, filename)
            
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            size = root.find("size")
            width = int(size.find("width").text)
            height = int(size.find("height").text)
            
            yolo_lines = []
            for obj in root.findall("object"):
                name = obj.find("name").text
                bndbox = obj.find("bndbox")
                xmin = int(bndbox.find("xmin").text)
                ymin = int(bndbox.find("ymin").text)
                xmax = int(bndbox.find("xmax").text)
                ymax = int(bndbox.find("ymax").text)
                
                x_center = (xmin + xmax) / (2 * width)
                y_center = (ymin + ymax) / (2 * height)
                obj_width = (xmax - xmin) / width
                obj_height = (ymax - ymin) / height
                
                yolo_line = f"0 {x_center:.6f} {y_center:.6f} {obj_width:.6f} {obj_height:.6f}"
                yolo_lines.append(yolo_line)
            
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_folder, output_filename)
            
            with open(output_path, "w") as f:
                f.write("\n".join(yolo_lines))

folder_path = "C:\\Users\\User\\Desktop\\sample"
output_folder = "C:\\Users\\User\\Desktop\\yolo_labels"
convert_voc_to_yolo(folder_path, output_folder)