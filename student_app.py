#import the required libraries
from pathlib import path 
import json

from pytest import mark 

class Student:
    def __init__(self,name,roll_no):
        '''initialize the needed attributes'''
        self.name = name
        self.roll_no = roll_no
        self.marks = {}
        self.student = {name:{roll_no:self.roll_no, self.marks:{}}}

