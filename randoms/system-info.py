import platform, socket, re, uuid, json, psutil, logging

def getSystemInfo():
    try:
        info = {}
        info["platform"]=platform.system()
        info["platform-release"]=platform.release()
        info["platform-version"]=platform.version()
        info["architecture"]=platform.architecture()
        info["architecture"]=platform.architecture()
        info["hostname"]=socket.gethostname()
        info["ip-address"]=socket.gethostbyname(socket.gethostname())
        info["mac-address"]=":".join(re.findall('..', '%012x' % uuid.getnode()))
        info["processor"]=platform.processor()
        info["ram"]=str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

from pprint import pprint
pprint(getSystemInfo())

# GPU
import torch

if torch.cuda.device_count() == 0:
    print("No GPU Available!")
else:
    for i in range(torch.cuda.device_count()):
        print(torch.cuda.get_device_properties(i))
