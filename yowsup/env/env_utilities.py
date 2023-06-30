#Done by Leon Tan 28/06/23
#Updated auto-update env_android.py variables based on apk version

from pyaxmlparser import APK
import sys
import base64
import zipfile
import hashlib

if len(sys.argv) < 2:
    print("Usage: python dexMD5.py <WhatsApp.apk>")
    exit()
else:
    apkFile = sys.argv[1]
    apk = APK(apkFile)
try:
    zipFile = zipfile.ZipFile(apkFile,'r')
    classesDexFile = zipFile.read('classes.dex')
    hash = hashlib.md5()
    hash.update(classesDexFile)
    ver = apk.version_name
    md5 = base64.b64encode(hash.digest()).decode("utf-8")

    with open("env_android.py") as file:
        lines = file.readlines()
    lines[19] = "    _MD5_CLASSES = " + '"{0}"'.format(md5) + "\n"
    lines[21] = "    _VERSION = " + '"{0}"'.format(ver) + "\n"
    with open("env_android.py", "w") as file:
        for line in lines:
            file.write(line)

    print("Version: " + apk.version_name)
    print("ClassesDex: " + base64.b64encode(hash.digest()).decode("utf-8"));
except Exception as e:
    print(sys.argv[1] + " not found.")
