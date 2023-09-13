#!/usr/bin/env python3

def return_evens(num_list):
    x = [e for e in num_list if e%2 == 0 ]
    return x
# return_evens([1, 1, 3, 5, 7, 1, 9])
def make_exclamation(sentence_list):
    x= [e+"!" for e in sentence_list]
    return x
# make_exclamation(["Hello", "I'm doing great", "Python is fun"])