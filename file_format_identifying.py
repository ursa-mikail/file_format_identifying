import os

# Define a dictionary of file types and their corresponding magic numbers
magic_numbers = {
    b'%PDF': 'Adobe Illustrator (.ai) or PDF Document (.pdf)',
    b'BM': 'Bitmap graphic (.bmp)',
    b'\xCA\xFE\xBA\xBE': 'Class File (.class)',
    b'\xFF\xD8': 'JPEG graphic file (.jpg)',
    b'\x00\x00\x00\x0CjP  \r\n': 'JPEG 2000 graphic file (.jp2)',
    b'GIF89': 'GIF graphic file (.gif)',
    b'II': 'TIF graphic file (.tif)',
    b'\x89PNG': 'PNG graphic file (.png)',
    b'RIFF': 'WAV audio file (.wav) or AVI video file (.avi)',
    b'\x7FELF': 'ELF Linux EXE',
    b'8BPS': 'Photoshop Graphics (.psd)',
    b'\xD7\xCD\xC6\x9A': 'Windows Meta File (.wmf)',
    b'MThd': 'MIDI file (.mid)',
    b'\x00\x00\x01\x00': 'Icon file (.ico)',
    b'ID3': 'MP3 file with ID3 identity tag (.mp3)',
    b'FWS': 'Flash Shockwave (.swf)',
    b'FLV': 'Flash Video (.flv)',
    b'\x00\x00\x00\x18ftypmp42': 'Mpeg 4 video file (.mp4)',
    b'moov': 'MOV video file (.mov)',
    b'0&\xB2u\x8Ef': 'Windows Video file (.wmv) or Windows Audio file (.wma)',
    b'PK': 'PKZip (.zip) or DOCX/XLSX/PPTX (Office 2010) (.docx, .xlsx, .pptx)',
    b'\x1F\x8B\x08': 'GZip (.gz)',
    b'ustar': 'Tar file (.tar)',
    b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1': 'Microsoft Installer (.msi) or Word Document (.doc) or Excel Document (.xls) or PowerPoint Document (.ppt) or Visio Document (.vsd) or Outlook Message File (.msg)',
    b'L\x01': 'Object Code File (.obj)',
    b'MZ': 'Dynamic Library (.dll) or Executable file (.exe) or SYS file (.sys)',
    b'MSCF': 'CAB Installer file (.cab)',
    b'Rar!\x1A\x07\x00': 'RAR file (.rar)',
    b'?\x5F\x03\x00': 'Help file (.hlp)',
    b'KDMV': 'VMWare Disk file (.vmdk)',
    b'!BDNB': 'Outlook Post Office file (.pst)',
    b'{\\rtf1': 'RTF Document (.rtf)',
    b'Standard Jet DB': 'Microsoft Database (.mdb)',
    b'%!': 'PostScript File (.ps)',
    b'%!PS-Adobe-3.0 EPSF-3.0': 'EPS File (.eps)',
    b'PK\x03\x04\x14\x00\x08\x00\x08\x00': 'Jar File (.jar)',
    b'Microsoft Visual Studio Solution File': 'SLN File (.sln)',
    b'x\x9C': 'Zlib File (.zlib) or SDF File (.sdf)'
}

# Path to the directory containing the files
directory_path = './sample_data/files/'

# Function to get the magic number of a file
def get_magic_number(file_path, num_bytes=20):
    with open(file_path, 'rb') as file:
        magic_number = file.read(num_bytes)  # Read first num_bytes bytes
    return magic_number

# Function to check if the file contains only ASCII characters
def is_text_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read().isascii()
        return True
    except (UnicodeDecodeError, FileNotFoundError):
        return False
   

# Function to identify the file type based on magic number or ASCII content
def identify_file_type(file_path):
    magic_number = get_magic_number(file_path)
    for key in magic_numbers:
        if magic_number.startswith(key):
            return magic_numbers[key]
    if is_text_file(file_path):
        return 'Text file (.txt)'
    return 'Unknown file type'

# Iterate through files in the directory and identify their types
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        file_type = identify_file_type(file_path)
        print(f'{filename}: {file_type}')

"""
sample out:
result_when_N_is1.png: PNG graphic file (.png)
file_to_be_embedded.txt: Text file (.txt)
result_when_N_is7.png: PNG graphic file (.png)
file_target_00.png: JPEG graphic file (.jpg)
file_with_embedded.png: PNG graphic file (.png)
result_when_N_is5_txt_embedded_large.png: PNG graphic file (.png)
file_target.png: WAV audio file (.wav) or AVI video file (.avi)
result_when_N_is1_image_large.png: PNG graphic file (.png)
"""