# 加载AccessKey
import csv
import logging

# key加载器
class KeyLoader:
    ID_COL = "AccessKey ID"
    SECRET_COL = "AccessKey Secret"

    def __init__(self, filename="AccessKey.csv"):
        self.__filename = filename
        self._id = ""
        self._secret = ""
        # 加载文件
        self.load()

    """
    加载key文件
    """

    def load(self):
        # open file
        try:
            with open(self.__filename, "rt") as file:
                csvFile = csv.DictReader(file)
                csvDict = next(csvFile)
                self._id = csvDict[KeyLoader.ID_COL]
                self._secret = csvDict[KeyLoader.SECRET_COL]
        except:
            logging.error("{} error!!!".format(self.__filename))
            exit(0)

    def getId(self):
        return self._id

    def getSecret(self):
        return self._secret
