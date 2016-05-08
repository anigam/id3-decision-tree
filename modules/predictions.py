import os
import csv
from operator import xor
from parse import *

# DOCUMENTATION
# ========================================
# this function outputs predictions for a given data set.
# NOTE this function is provided only for reference.
# You will not be graded on the details of this function, so you can change the interface if 
# you choose, or not complete this function at all if you want to use a different method for
# generating predictions.

def create_predictions(tree, predict):
    '''
    Given a tree and a url to a data_set. Create a csv with a prediction for each result
    using the classify method in node class.
    '''

    output_path = os.path.join(os.path.dirname(__file__), "output")

    if not os.path.exists(output_path):
        # Create output directory if none exists
        os.makedirs(output_path)
        print "Created output directory " + str(output_path)

    data_set, attribute_metadata = parse(predict, True)

    with open(output_path + "/" + "output.csv", "wb") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        fieldnames = [attr["name"] for attr in attribute_metadata]

        writer.writerow(fieldnames)

        for x in data_set:
            x[0] = tree.classify(x)
            writer.writerow(x)

    print "CSV written to file"