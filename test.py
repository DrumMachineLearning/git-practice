import csv
import json
import subprocess
import tempfile
import unittest

class TestClass:

    def __init__(self, foo, bar, baz):
        """Initializes foo bar and baz

        Params:
            foo: foo
            bar: bar
            baz: baz
        """
        self.foo = foo
        self.bar = bar
        self.baz = baz

    @staticmethod
    def fizz_buzz(digit_1, digit_2, begin=1, end=101):
        """Prints number or some combination of fizz and buzz

        Params:
            digit_1: the number evenly divided that gives fizz
            digit_2: the number evenly divided that gives buzz
        """
        output = []
        for i in range(begin, end):
            if i % digit_1 == 0:
                if i % digit_2 == 0:
                    output.append('fizzbuzz!')
                else:
                    output.append('fizz!')
            elif i % digit_2 == 0:
                output.append('buzz!')
            else:
                output.append(str(i))
        return output

    def print_list(self, item_list):
        """Prints a list of items separated by '\n'

        Params:
            item_list: the list of items to print
        """
        print('\n'.join(item_list))

    def oh_this_is_trouble(self, param1, param2):
        """Oh man this fucntion is trouble"""
        for i in range(20):
            print 'trouble' + i * '!'
            for j in range(10):
                print i * j

    @staticmethod
    def json_to_csv(json_file_path, outfile_path):
        """Convert a file containing a list of flat JSON objects to a csv.

        What's a DictWriter, you say? Never heard of it!
        Params:
            json_file_path: the path to json
            outfile_path: the output csv file_path
        """
        with open(json_file_path) as f:
            data = f.read()
        data = json.loads(data)
        
        with open(outfile_path, 'w') as fp:
            writer = csv.DictWriter(fp, fieldnames=data[0].keys())
            writer.writeheader()
            for item in data:
                writer.writerow(item.values())

if __name__ == '__main__':
    t = TestClass(1, 2, 3)
    TestClass.fizz_buzz(3, 5)
