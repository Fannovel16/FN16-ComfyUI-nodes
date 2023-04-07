import requests
import shutil
import platform
import os
import subprocess
import tempfile

EXT_DIR = os.path.dirname(os.path.realpath(__file__))

def download_file(url):
    filename = os.path.join(EXT_DIR, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return filename

def get_ffmpeg_build_url():
    if platform.system() == "Windows" and "PROGRAMFILES(X86)" in os.environ:
        return "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n6.0-latest-win64-gpl-6.0.zip"
    if platform.system() == "Linux" and platform.architecture()[0] == '64bit':
        if platform.machine().startswith('arm'):
            return "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n6.0-latest-linuxarm64-gpl-6.0.tar.xz"
        return "ffmpeg-n6.0-latest-linux64-gpl-6.0.tar.xz"
    return None
    
print("----------INSTALLING DEPENDENCIES----------")
os.system("pip install -r requirements.txt")
print("----------INSTALLING FFMPEG----------")
try:
    subprocess.check_output(['ffmpeg', '--version'])
    print('ffmpeg is already installed.')
except OSError:
    print('ffmpeg is not installed.')
    
    target_dir = os.path.join(EXT_DIR, "ffmpeg")

    if not os.path.exists(os.path.join(target_dir, "bin")):
        if get_ffmpeg_build_url() is None:
            print("Can't download ffmpeg automatically due to the system arch and os.")
            exit()
        ffmpeg_compress_name = download_file(get_ffmpeg_build_url())

        with tempfile.TemporaryDirectory() as temp_dir:
            shutil.unpack_archive(ffmpeg_compress_name, temp_dir)
            extracted_folder = os.path.join(temp_dir, os.listdir(temp_dir)[0])
            for item in os.listdir(extracted_folder):
                shutil.move(os.path.join(extracted_folder, item), target_dir)
