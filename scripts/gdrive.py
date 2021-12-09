# /home/enrico/go/bin/gdrive sync upload --keep-local Conducting 1ggP6aU93RJT1HzgigtzIA6YLeMWAJtKD
# /home/enrico/go/bin/gdrive sync upload --keep-local Personale/ 1TjF6K5I9oQOH1MosUBSBdfYEoeYZqxGX
# /home/enrico/go/bin/gdrive sync upload --keep-local SysAdmin/ 1tZ_zFkYQav0eH9YQwhcxFT0Twhmh5diX
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def sync_dir(src: str, dest: str, *args):
    gdrive_path = os.getenv("GDRIVE_PATH")
    if not gdrive_path:
        print("gdrive path is empty...")
        quit(1)
    upload = subprocess.run([gdrive_path, 'sync', 'upload', src, dest], stdout=True)
    download = subprocess.run([gdrive_path, 'sync', 'download', dest, src], stdout=True)
    return upload, download

def list_dir():
    pass


