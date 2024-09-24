import csv
import os

description_list = dict()
severity_dict = dict()
precautionDictionary = dict()

class GetDescription:
    """
    This class reads the csv file and returns a dictionay
    """
    
    # class level private variable
    __file_path_description = os.path.join(os.path.dirname(__file__), 'master_data/Symptom_description.csv')
    __file_path_precaution = os.path.join(os.path.dirname(__file__), 'master_data/Symptom_precaution.csv')
    __file_path_severity = os.path.join(os.path.dirname(__file__), 'master_data/Symptom_severity.csv')
    

    def getData(self):
        global description_list
        with open(self.__file_path_severity, mode='r') as fileHandler:
            file_object = csv.reader(fileHandler)
            try: 
                for row in file_object:
                    # updating the global description_list 
                    # description_list.update({row[0]: row[1]})
                    description_list |= {row[0]: row[1]}
                return description_list
            except:
                pass

        
    def getSeverityDict(self):
        global severity_dict
        with open(self.__file_path_severity, mode='r') as fileHandler:

            file_object = csv.reader(fileHandler)
            try:
                for row in file_object:
                    severity_dict |= {row[0]:int(row[1])}
                return severity_dict
            except:
                pass


    def getprecautionDict(self):
        global precautionDictionary
        with open(self.__file_path_precaution) as filehandler:
            file_object = csv.reader(filehandler)
            for row in file_object:
                precautionDictionary |= {row[0]:[row[1],row[2],row[3],row[4]]}
            return precautionDictionary
