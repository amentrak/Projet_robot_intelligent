import subprocess

treshold = 25
darknetLocation = "/home/zowi/Documents/Projet/facenet/contributed3/darknet"

with open("log.txt", 'w') as w:
    process = subprocess.Popen([darknetLocation+'darknet.exe', 'detector', 'demo', darknetLocation+'cfg/coco.data', darknetLocation+'cfg/yolov3.cfg', darknetLocation+'yolov3.weights','-dont_show'],
                            stdout=subprocess.PIPE,
                            stderr=w
                            )
    inObject = False
    objectRecognized = dict()
    while True:
        output = process.stdout.readline()
        if output:
            output = output.strip()
            output = str(output)
            output = output.replace("b'","")
            output = output.replace("'",'')
            w.write(output)
            if output != '':

                if output == "Objects:":
                    objectRecognized = dict()
                    inObject = True
                if "FPS:" in output:
                    print(objectRecognized)
                    inObject = False

                if inObject and output != 'Objects:':
                    output = output.replace('%','')
                    output = output.split(':')
                    output=list(map(lambda x:x.replace(" ",''),output))
                    output = list(map(lambda x: x.split(','), output))
                    output = [item for sublist in output for item in sublist] #turn a list of list into a simple list
                    if int(output[1]) >= treshold:
                        if output[0] in objectRecognized:
                            objectRecognized[output[0]] +=1
                        else:
                            objectRecognized[output[0]] = 1
    process.kill() #Kill the program to exit, here it's outside the loop bc there's no button to exit
