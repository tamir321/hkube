import time
import json
def start(args, hkubeapi):
    input=args['input'][0]
   
    time.sleep(input)
    return {"name":"python test from git",
            "version":"master-v2"}
