#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class Test:
    """docstring for Test"""

    def test(self):
        print('Why so serious?')
        return

    def call_test(self):
        print('call_test was called')
        self.test()


def main():
	Test1 = Test()
	Test1.call_test()


if __name__ == '__main__':
    main()
