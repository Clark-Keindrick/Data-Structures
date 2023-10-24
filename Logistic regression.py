import numpy as np
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


class Logistic_Regression:
    logr = linear_model.LogisticRegression(solver='lbfgs', C=110.0, random_state=0)

    def __init__(self):
        self.X = np.array(
            [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0,
             5.25]).reshape(-1, 1)
        self.Y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

    @staticmethod
    def display_data():
        d = {0.5: 0, 0.75: 0, 1.0: 0, 1.25: 0, 1.5: 0, 1.75: 0, 2.0: 1, 2.25: 0, 2.5: 1, 2.75: 0, 3.0: 1, 3.25: 0,
             3.5: 1, 3.75: 0, 4.0: 1, 4.25: 1, 4.5: 1, 4.75: 1, 5.0: 1,
             5.25: 1}

        print("Independent Variables : Dependent Variables\n")
        for i, j in d.items():
            print("%1.2f  : %2d \n" % (i, j))

    def get_attributes(self):
        lr.logr.fit(self.X, self.Y)
        log_odds = lr.logr.coef_
        odds = np.exp(log_odds)

        print("Coefficient:", lr.logr.coef_)
        print("Intercept:", lr.logr.intercept_)
        print("Classes:", lr.logr.classes_)
        print()
        print("Odds:", odds,
              " This tells us that as the hours studied increases by 1 hour the odds of it increases by 3x.")

    def get_the_probability(self):
        lr.logr.fit(self.X, self.Y)
        log_odds = lr.logr.coef_ * self.X + lr.logr.intercept_
        odds = np.exp(log_odds)
        probability = odds / (1 + odds)
        l = list(probability)

        print("Hours Studied: ", end='')
        for i in self.X:
            print("%7.2f" % i, end='    ')

        print()
        print("Probability:    ", end='')
        for j in l:
            print("%2f" % j, end='   ')

        print()

    def correct_prediction(self):
        lr.logr.fit(self.X, self.Y)
        predicted = lr.logr.predict(self.X.reshape(-1, 1))
        l = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0,
             5.25]

        print(' ', end='\t\t\t\t                                        \t\t\t\t\t')
        print("0-Failed     1-Passed: \n")
        for i in l:
            print("%7.2f" % i, end='  ')

        print()

        for j in predicted:
            print("%6d" % j, end='   ')

        print('\n\n', end='\t\t\t\t                                        \t\t\t\t\t')
        print("Model Accuracy:", lr.logr.score(self.X, self.Y))

    def ConfusionMatrix(self):
        lr.logr.fit(self.X, self.Y)
        cm = confusion_matrix(self.Y, lr.logr.predict(self.X))

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(cm)
        ax.grid(False)
        ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
        ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
        ax.set_ylim(1.5, -0.5)
        for i in range(2):
            for j in range(2):
                ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
        plt.show()


lr = Logistic_Regression()

while True:
    print("1. Display Data\n")
    print("2. Display the Model Attributes\n")
    print("3. Display the Probability of each Hours Studied\n")
    print("4. Display the Correct Prediction\n")
    print("5. Display the Confusion Matrix\n")
    print("6. Exit\n")

    choice = int(input("Input Your choice: "))
    print()

    while choice == 1:
        lr.display_data()

        press = input("\nPress any key to continue or X to exit: ").upper()

        if press == 'X':
            break

    while choice == 2:
        lr.get_attributes()

        press = input("\nPress any key to continue or X to exit: ").upper()

        if press == 'X':
            break

    while choice == 3:
        lr.get_the_probability()

        press = input("\nPress any key to continue or X to exit: ").upper()

        if press == 'X':
            break

    while choice == 4:
        lr.correct_prediction()

        press = input("\nPress any key to continue or X to exit: ").upper()

        if press == 'X':
            break

    while choice == 5:
        lr.ConfusionMatrix()

        press = input("\nPress any key to continue or X to exit: ").upper()

        if press == 'X':
            break

    if choice == 6:
        break
