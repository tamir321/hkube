import time
import json
def start(args, hkubeapi):
    input=args['input'][0]
   
    time.sleep(int(input))
    return {"name":"python test from git",
            "commit":"A3",
            "version":"master margev1"}

