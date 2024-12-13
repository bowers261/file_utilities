import os
from datetime import datetime
import xlsxwriter

def list_files_in_directory(directory_path, output_file_path):
    workbook = xlsxwriter.Workbook(output_file_path)
    worksheet = workbook.add_worksheet()
    headers = ['File/Folder Name', 'File Extension', 'File Size (bytes)', 'Create Date', 'Hyperlink']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)
    files_and_folders = os.listdir(directory_path)
    
    row = 1
    for item in files_and_folders:
        item_path = os.path.join(directory_path, item)
        
        worksheet.write(row, 0, item)
       
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1]
            worksheet.write(row, 1, file_extension)
      
        if os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            worksheet.write(row, 2, file_size)
       
        create_date = datetime.fromtimestamp(os.path.getctime(item_path)).strftime('%Y-%m-%d %H:%M:%S')
        worksheet.write(row, 3, create_date)
        
        hyperlink = f'=HYPERLINK("{item_path}", "Open File/Folder")'
        worksheet.write_url(row, 4, item_path, string='Open File/Folder', tip=hyperlink)
        
        row += 1
    
    workbook.close()


