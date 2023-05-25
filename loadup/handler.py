import os
import time
class handler:

    def __init__(self):
        self.load_cNd()
    
    def load_cNd(self):
        root=os.getcwd()
        self.cmds=(f"cd {root}","cd A.D.A/loadup/bin","start ada_ascii_art.bat",)
        #print(self.cmds)

    def execute(self):
        for item in self.cmds:
            (c)=item
            if "ada_ascii_art.bat" in c:
                timeout_sec=15
                start_time=time.time()
                while True:
                    os.system(f"{c}")
                    if time.time() - start_time >= timeout_sec:
                        os.system("start terminate.bat")
                        break
            else:
                os.system(f"{c}")

control=handler()