import os
class handler:

    def params(self):
        self.command=""
        self.detail=""
    
    def execute(self):
        os.system(f"{self.command} {self.detail}")