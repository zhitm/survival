import os
class Logger:
    def __init__(self):
        self.logFileName = ""
        self.gameInfoFileName = ""
        current_path = os.path.dirname(__file__)
        logPath = current_path + "\\logs"
        self.createLogFile(logPath)

    def createLogFile(self, path):
        self.logFileName = path + str(self.get_file_name(path, '\\Log'))
        print('Writing logs to %s' % self.logFileName)
        f = open(self.logFileName, 'w')
        f.close()

    def get_file_name(self, path, suffix):
        try:
            if not os.path.exists(path):
                os.mkdir(path)
        except OSError:
            print("Creation of the logs directory %s failed" % path)
        else:
            print("Successfully created the logs directory %s " % path)
        i = 0
        while os.path.exists(path + suffix + str(i) + ".txt"):
            i += 1
        return suffix + str(i) + ".txt"

    def Write(self, msg):
        f = open(self.logFileName, 'a')
        f.writelines(str(msg))
        print('»»»»»»»> ' + str(msg))
        f.writelines('\n')
        f.close()




