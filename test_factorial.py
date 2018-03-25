#! /usr/bin/env python3

import unittest
import inspect
import os
import sys
import subprocess


class Test_Factorial(unittest.TestCase):
    def setUp(self):
        self.has_file = os.path.isfile("fact.py")



    def test_1_correct_file(self):
        print("Test started: {}".format(inspect.stack()[0][3]))
        self.assertTrue(self.has_file,
                "File: 'fact.py' required")
        print("Test  passed: {}".format(inspect.stack()[0][3]))

    def test_2_can_call(self):
        print("Test started: {}".format(inspect.stack()[0][3]))
        self.assertTrue(self.has_file, 
                "File: 'fact.py' required")
        proc = subprocess.Popen(["python3", "fact.py", "14"],\
            stdout=subprocess.PIPE)
        try:
            out, errors = proc.communicate()
            self.assertTrue( errors == None )
        except:
            proc.kill()
            self.assertTrue(False)
        print("Test  passed: {}".format(inspect.stack()[0][3]))

    def test_3_fact_0(self):
        print("Test started: {}".format(inspect.stack()[0][3]))
        self.assertTrue(self.has_file, 
                "File: 'fact.py' required")
        proc = subprocess.Popen(["python3", "fact.py", "0"],\
            stdout=subprocess.PIPE)
        try:
            out, errors = proc.communicate()
            temp = int(out)
            self.assertTrue( temp == 1 )
            self.assertTrue( errors == None )
        except Exception as e:
            print(e)
            proc.kill()
            self.assertTrue(False)
        print("Test  passed: {}".format(inspect.stack()[0][3]))

