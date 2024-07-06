import os
import shutil

def move_xmp_files(base_folder, xmp_folder):
    # Iterate through each year from 2009 to 2024
    for year in range(2009, 2025):
        year_folder = os.path.join(base_folder, str(year))
        
        # Check if the year folder exists
        if not os.path.exists(year_folder):
            continue
        
        # Iterate through each month from 01 to 12
        for month in range(1, 13):
            month_folder = os.path.join(year_folder, f"{month:02}")
            
            # Check if the month folder exists
            if not os.path.exists(month_folder):
                continue
            
            # Get all image/movie files in the month folder
            image_files = {os.path.splitext(f)[0] for f in os.listdir(month_folder)}
            
            # Get all XMP files in the XMP folder
            xmp_files = [f for f in os.listdir(xmp_folder) if f.endswith('.xmp')]
            
            for xmp_file in xmp_files:
                xmp_base_name = os.path.splitext(xmp_file)[0]
                
                # Check if there is a matching image/movie file in the month folder
                if xmp_base_name in image_files:
                    # Move the XMP file to the month folder
                    src_path = os.path.join(xmp_folder, xmp_file)
                    dest_path = os.path.join(month_folder, xmp_file)
                    shutil.move(src_path, dest_path)
                    print(f"Moved {xmp_file} to {month_folder}")

if __name__ == "__main__":
    # Define the base folder path and the XMP folder path
    base_folder = "/Users/elliottfinney/Desktop/Ag Temp Folder/iPhone CR"
    xmp_folder = "/Users/elliottfinney/Desktop/Aggie Phone Pics/XMPs"

    move_xmp_files(base_folder, xmp_folder)
