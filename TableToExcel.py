import os
import wget
import subprocess

# Navigate to the desired directory (assuming you're in the working directory where you want the script to run)

# You can replace the placeholder "# run" with your actual code for using the downloaded models
#print("Downloaded and unzipped the models. Now you can proceed with using them in your code.")

def process_directory(directory):
    """Processes a single directory containing images using PaddleOCR for table detection and recognition.

    Args:
        directory (str): The path to the directory containing images.
    """
    print(directory)
    det_model_dir = "./en_ppocr_mobile_v2.0_table_det_infer"
    rec_model_dir = "./ch_PP-OCRv3_rec_infer"
    table_model_dir = "./en_ppocr_mobile_v2.0_table_structure_infer"
    rec_char_dict_path = "./PaddleOCR/ppocr/utils/ppocr_keys_v1.txt"
    table_char_dict_path = "./PaddleOCR/ppocr/utils/dict/table_structure_dict.txt"
    image_dir = directory
    #output_name=directory.split("\\")[0].split("/")[-1]

    page=directory.split("\\")[-1]
    print("page: ",page)

    output_dir = f"./Output/{page}"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)  # Handle pre-existing directories gracefully

    # Construct the command with string formatting for flexibility
    command = f""" python C:/Users/HHR6/PycharmProjects/Task1/PaddleOCR/ppstructure/table/predict_table.py --det_model_dir={det_model_dir} --rec_model_dir={rec_model_dir} --table_model_dir={table_model_dir} --rec_char_dict_path={rec_char_dict_path}  --table_char_dict_path={table_char_dict_path}  --image_dir={image_dir}  --merge_no_span_structure=False --output={output_dir} """
    #print(command)
    subprocess.run(command,shell=True)
    print("done")
