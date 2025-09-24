import storage
import os

storage.remount("/", readonly=False)
try:
    os.rename("/boot.py", "/boot_old.py")
except:
    pass
