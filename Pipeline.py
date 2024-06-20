import os
from TableDetector import yolo_process_image
from ultralyticsplus import YOLO
from TableToExcel import process_directory
import Utils


# First the PDf need to be divide into chunks or many PDF each fo size chunk size
input_filename = "C:/Users/HHR6/PycharmProjects/Task2/Discac/DISCAC-Tarif-Cuisines-24-25.pdf"
output_dir = "./PdfChunks"
pages_per_chunk = 50 # Adjust this to your desired chunk size
Utils.split_pdf(input_filename, output_dir, pages_per_chunk)



# after that we will transform, the CHUNKS into an image
# create a dircetory here i called Images
Utils.pdftoImages("./PdfChunks", Save_folder="./Images")



# now we extract all the table inside each of the picture
model = YOLO('./Table_Detection.pt')
files_list=Utils.deep_search_file_type("./Images",".jpg")
for Path in files_list:
    if (Path.endswith(".jpg")):
        Path = Path.replace("\\", "/")
        Path = Path.replace("//", "/")
        print(Path)
        index = yolo_process_image(Path, "./Tables_Detected", 0,model)

# from the Tbales detceted in each pages of the PDf We will tranfrom each one of fhtem into xlsx file
print("heelo")
import os


# Replace this with your actual path
directory_path = "./Tables_Detected/"
Utils.remove_empty_directories(directory_path)
tables_detected_path = "./Tables_Detected"
Utils.flatten_and_rename(tables_detected_path)


Dirs=Utils.get_all_dirs_paths("C:/Users/HHR6/PycharmProjects/Task1/Tables_Detected")
for dir in Dirs:
        process_directory(dir)

# now we delete all Empty XLSX file
XLSX_paths=Utils.deep_search_file_type("./Output/",".xlsx")
for XLSX_path in XLSX_paths:
    Utils.is_xlsx_empty_wrap(XLSX_path)

# next we need to comnine all XLSX file in one file
input_folder = "./Output"
output_filename = "./combined_data.xlsx"

Utils.combine_xlsx_files(input_folder, output_filename)