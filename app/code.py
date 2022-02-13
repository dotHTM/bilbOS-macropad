
import time

from views.ExtendedMacropad import ExtendedMacropad

class BaseController:
    
    applications = []
    macropad = ExtendedMacropad()
    
    def loop(self):
        while True:
            time.sleep(0.001)
            for app in self.applications:
                pass

def main():
    entry = BaseController()
    entry.loop()



if __name__ == '__main__':
    main()
