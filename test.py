import csv
import json


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

    def fizz_buzz_to_json(self, howdy):
        print howdy

    def json_to_csv(self, json_file_path, outfile_path):
        """Convert a file containing a list of flat JSON objects to a csv.

        Let's try to use DictWriter

        """
        fieldnames = ["Child's First Name", 'Summation of Counts', 'Ethnicity']
        with open(json_file_path) as f:
            data = json.load(f)
        with open(outfile_path, 'w') as fp:
            writer = csv.DictWriter(fp, fieldnames = fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

tc = TestClass('O','M','G')
tc.json_to_csv('../../Summary_data.json', '../../converted_summary_data.csv')
