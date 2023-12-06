import os
from edi_envelope_to_json import *



def transform_files():
    #file_list = os.listdir(directory)
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Split list of lines by space into two strings
        _837, _999 = line.split(' ')
        _837 = './837/'+ _837
        _999 = './999/'+ _999.strip()

        #file_path = os.path.join(directory, file_name)
        edi_envelope_to_json(_837, _999)
        
        # Perform the simple transformation on each file
#         transformed_data = transform_file(file_path)
        
#         # Write the transformed data back to the file
#         with open(file_path, 'w') as file:
#             file.write(transformed_data)

# def transform_file(file_path):
#     # Perform the simple transformation on the file
#     # Replace this code with your own transformation logic
#     transformed_data = f"Transformed data from {file_path}"
    
#     return transformed_data

# Specify the directory containing the files
#directory = './837'

# Call the method to transform the files
transform_files()