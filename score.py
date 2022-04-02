import sys


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

    print(correct, "out of", str(correct + incorrect) + " tags correct")
    accuracy = 100.0 * correct / (correct + incorrect)
    print("  accuracy: %5.2f" % accuracy)

    precision = 100.0 * correct / response_total
    recall = 100.0 * correct / key_total
    F = 2 * precision * recall / (precision + recall)
    print("  precision: %5.2f" % precision)
    print("  recall:    %5.2f" % recall)
    print("  F1:        %5.2f" % F)


def main(args):
    key_file = args[1]
    response_file = args[2]
    score(key_file, response_file)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
