def readSetting():
    settings = {}
    try:
        with open('settings.ini','r') as f:
            try:
                for line in f:
                    settingLine = line.split("=")
                    settings[settingLine[0]] = settingLine[1]
                if 'darknetLocation' not in settings.keys():
                    raise Exception("can't find darknet location")
                #Si on rajoute des options, on peut faire comme au dessus
                #On pourrait à priori même faire des tests en plus si on demande un type de valeur particulier
                return settings
            except Exception as err:
                print("Error: "+ str(err))
                return
    except Exception as err:
        print("Error: "+str(err))
        return


try:
    settings = readSetting()
    if type(settings) is not dict:
        raise SystemExit('Settings file is missing or incomplete')
except Exception as e:
    print(e)
