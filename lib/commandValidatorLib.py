import configparser

def commandValidatorLib(args):
    isCommandEmpty = (len(args.command) == 0)
    isModuleEmpty = (len(args.module) == 0)
    if isCommandEmpty:
        print("[ERROR] CMD is invalid.")
        print("[INFO] No action is taken.")
        return False
    elif isModuleEmpty:
        print("[ERROR] Module is invalid.")
        print("[INFO] No action is taken.")
        return False
    else:
        isModuleCnfEmpty = (len(args.config['MODULE'][args.module]) == 0)
        if isModuleCnfEmpty:
            print("[ERROR] This module is unidentified, please check configuration.")
            print("[INFO] No action is taken.")
            return False
        elif args.config['MODULE'][args.module] != "enabled":
            print(f"[ERROR] The module [{args.module}] is not enabled.")
            print("[INFO] No action is taken.")
            return False
        else:
            print(f"[INFO] The [{args.module} {args.command}] is a valid command.")
            return True