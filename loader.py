import sys, os
import configparser
from lib import messageParserLib, commandValidatorLib

class Loader:

    def __init__(self, message):
        self.load_cnf()
        self.parse_message(message)
        isUserValid = self.validate_user()
        isCmdValid  = self.validate_cmd()
        if isUserValid and isCmdValid:
            self.execute_cmd()
        else:
            self.response = self.config['RESPONSE']['ERROR']

    def get_response(self):
        return self.response

    def load_cnf(self):
        config = configparser.ConfigParser()
        config.read([
            'config/git.ini',
            'config/response.ini',
            'config/module.ini',
            'config/global.ini'
        ])
        self.config = config

    def parse_message(self, message):
        result = messageParserLib(message)
        self.parameter = result['parameter']
        self.module    = result['module']
        self.command   = result['command']
        print(f"[INFO] Detected module named [{self.module}] with command [{self.command}].")

    def validate_cmd(self):
        return commandValidatorLib(self)
                
    def validate_user(self):
        print("[INFO] Validate user is not yet ready.")
        return True
    
    def execute_cmd(self):
        try:
            sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/module")
            moduleObj = __import__(self.module)
            if len(self.parameter) == 0:
                methodCall = getattr(moduleObj, self.command)
                self.response = methodCall()
            else:
                self.response = getattr(moduleObj, self.command)(self.parameter)
        except AttributeError:
            print(f"[ERROR] It's either module named {self.module}, disabled or a method call does not exist.")
            print("[INFO] No action is taken.")
            self.response = self.config['RESPONSE']['UNKNOWN']