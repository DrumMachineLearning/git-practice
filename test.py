import csv
import json
from csv import DictWriter

class TestClass(object):

    def __init__(self, foo, bar, baz):
        self.foo = foo
        self.bar = bar
        self.baz = baz

    def fizz_buzz(self, digit_1, digit_2):
        for i in range(1, 100):
            if i % digit_1 == 0:
                if i % digit_2 == 0:
                    print 'fizzbuzz!'
                else:
                    print 'fizz!'
            elif i % digit_2 == 0:
                print 'buzz!'
            else:
                print i

    def another_function(self):
        """
        5 lines of change here
        """
        print "Howdy"

    def json_to_csv(self, json_file_path, outfile_path, fieldnames = None):
        """Convert a file containing a list of flat JSON objects to a csv.

        Dont fail to use DictWriter (personal note #3287)

        """
        with open(json_file_path) as f:
            data = json.load(f)
        with open(outfile_path, 'w') as fp:
            if fieldnames == null:
                fieldnames = ["Child's First Name", "Ethnicity",
                        "Summation of Counts"]
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writeheaders()
            for row in data:
                writer.writerow(row)

