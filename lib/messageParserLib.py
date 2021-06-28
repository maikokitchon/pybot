def messageParserLib(message):
    varResult = {}
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
    varResult['parameter'] = arg
    varResult['module'] = arrayWord[0]
    varResult['command'] = '_'.join(arrayCmd)
    return varResult