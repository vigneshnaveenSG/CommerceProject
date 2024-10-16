from configparser import ConfigParser


def readconfig(sec, key):
       config = ConfigParser()
       config.read("./Configurations/Config.ini")
       return config.get(sec, key)
