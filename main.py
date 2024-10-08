# to hide depricated warnings
import warnings
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

warnings.filterwarnings(action="ignore", category=DeprecationWarning)


class HealthCareChatbot:
    def __init__(self):
        # Read the data
        self.training = pd.read_csv('src/Data/Training.csv')
        self.testing = pd.read_csv('src/Data/Testing.csv')

        # prepare the feature data and target cols
        self.cols = self.training.columns[:-1]
        self.x = self.training[self.cols]
        self.y = self.training['prognosis']

        # encode the data with LabelEncoder to assign target values to integer
        self.le = LabelEncoder()
        self.le.fit(self.y)
        self.y = self.le.transform(self.y)

        # split the data into training and testing sets
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.33, random_state=42)
        self.testx = self.testing[self.cols]
        self.testy = self.le.transform(self.testing["prognosis"])



h = HealthCareChatbot()
print(h.x_train)
print(h.x_test)