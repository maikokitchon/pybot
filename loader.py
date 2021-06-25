import sys, os
import configparser

class Loader:

    RESPONSE_MSG_UNKNOWN = "Sorry! I can't understand your command. Please refer to [bot help]."
    RESPONSE_MSG_ERROR   = "Ooops! Something went wrong. Please try again later or contact bot admin."

    def __init__(self, message):
        self.parse_message(message)
        isUserValid = self.validate_user()
        isCmdValid = self.validate_cmd()
        if isUserValid and isCmdValid:
            self.execute_cmd()
        else:
            self.response = self.RESPONSE_MSG_ERROR

    def get_response(self):
        return self.response

    def parse_message(self, message):
        arg = []
        arrayCmd = []
        arrayWord = message.split()
        for idx, word in enumerate(arrayWord):
            if word.find(':') != -1:
                param = word.replace(':','')
                arg.append(param)
                print(f"[INFO] Found a parameter named [{param}].")
            else:
                if idx != 0:
                    arrayCmd.append(word)
        self.parameter = arg
        self.module = arrayWord[0]
        self.command = '_'.join(arrayCmd)
        print(f"[INFO] Detected module named [{self.module}] with command [{self.command}].")

    def execute_cmd(self):
        try:
            sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/module")
            moduleObj = __import__(self.module)
            self.response = getattr(moduleObj, self.command)(self.parameter)
        except AttributeError:
            print(AttributeError)
            print(f"[ERROR] Unable to load module named {self.module}, please check if it exists in module folder and must be enabled.")
            print("[INFO] No action is taken.")
            self.response = self.RESPONSE_MSG_UNKNOWN

    def validate_cmd(self):
        isCommandEmpty = (len(self.command) == 0)
        isModuleEmpty = (len(self.module) == 0)
        if isCommandEmpty:
            print("[ERROR] CMD is invalid.")
            print("[INFO] No action is taken.")
            return False
        elif isModuleEmpty:
            print("[ERROR] Module is invalid.")
            print("[INFO] No action is taken.")
            return False
        else:
            config = configparser.ConfigParser()
            config.read('config/module.ini')
            isModuleCnfEmpty = (len(config['MODULE'][self.module]) == 0)
            if isModuleCnfEmpty:
                print("[ERROR] This module is unidentified, please check configuration.")
                print("[INFO] No action is taken.")
                return False
            elif config['MODULE'][self.module] != "enabled":
                print(f"[ERROR] The module [{self.module}] is not enabled.")
                print("[INFO] No action is taken.")
                return False
            else:
                print(f"[INFO] The [{self.module} {self.command}] is a valid command.")
                return True
                
    def validate_user(self):
        print("[INFO] Validate user is not yet ready.")
        return True