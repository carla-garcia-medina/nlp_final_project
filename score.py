import sys
import matplotlib.pyplot as plt
import numpy as np


def score(keyFileName, responseFileName):
    keyFile = open(keyFileName, 'r')
    key = keyFile.readlines()
    responseFile = open(responseFileName, 'r')
    response = responseFile.readlines()
    if len(key) != len(response):
        print("length mismatch between key and submitted file")
        exit()
    correct = 0
    incorrect = 0
    response_total = 0
    key_total = 0

    for i in range(len(key)):
        key[i] = key[i].rstrip('\n')
        response[i] = response[i].rstrip('\n')

        if key[i] == response[i]:
            correct += 1
        else:
            incorrect += 1

        if response[i]:
            response_total += 1
        if key[i]:
            key_total += 1

    print(correct, "out of", str(correct + incorrect) + " tags correct")
    accuracy = 100.0 * correct / (correct + incorrect)
    print("  accuracy: %5.2f" % accuracy)

    """
    precision = 100.0 * correct / response_total
    recall = 100.0 * correct / key_total
    F = 2 * precision * recall / (precision + recall)
    print("  precision: %5.2f" % precision)
    print("  recall:    %5.2f" % recall)
    print("  F1:        %5.2f" % F)
    """

    return accuracy


def visualize(titles, model_accuracy, manual_accuracy):

    X_axis = np.arange(len(titles))

    plt.bar(X_axis - 0.15, manual_accuracy, 0.30, label='Manual')
    plt.bar(X_axis + 0.15, model_accuracy, 0.30, label='LSTM Model')

    plt.xticks(X_axis, titles)
    plt.yticks(np.arange(0, 101, 10))
    plt.xlabel("Dataset")
    plt.ylabel("Accuracy")
    plt.title("Accuracy of model by dataset")
    plt.legend()
    plt.show()


def main(args):

    manual_accuracy = [74, 48, 90, 19]

    model_accuracy = [50, 50, 50, 50]  # temporary

    datasets = ["Yelp Polarity", "Yelp Rating",
                "Rotten Tomatoes Polarity", "Tweet Emoji Labeling"]

    """
    model_accuracy = []
    for name in datasets:
        name = name.replace(" ", "_")

        key_file = name + "_key" + ".txt"  # add correct file extension
        response_file = name + "_res" + ".txt"  # add correct file extension

        s = score(key_file, response_file)
        model_accuracy.append(s)
    """
    #key_file = args[1]
    #response_file = args[2]

    #s = score(key_file, response_file)

    visualize(datasets, model_accuracy, manual_accuracy)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
