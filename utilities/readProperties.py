import configparser
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class readConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get("common info","baseUrl")
        return url
    @staticmethod
    def getusername():
        username = config.get("common info","username")
        return username
    @staticmethod
    def getPassword():
        password = config.get("common info","password")
        return password

