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

    def bubble_sort(self, alist):
        length = len(alist) - 1
        for i in range(0, length):
            if alist[i] > alist[i + 1]:
                # alist[i], alist[i+1] = alist[i+1], alist[i]  # python way
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

    def json_to_csv(self, json_file_path, outfile_path):
        """DictWriter has saved my life!!!
        """
        with open(json_file_path) as f:
            data = json.load(f)
        with open(outfile_path, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())

if __name__ == '__main__':
    t = TestClass(1, 2, 3)
    TestClass.fizz_buzz(3, 5)
