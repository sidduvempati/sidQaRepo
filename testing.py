# Testing
# We can have lots of errors, so we should test. 
# writing tests as you code is a cheaper soloution to finding errors than in producion.
# types of tests: 
# functional - units testing - test each block of code
#            - integration testing - how does the code work in reltion to other code \
#            - delete a function and see how it affects others. 
#            - user acceptance testing - by staff or group of customers - does the do 
#               what it is intended to do.
# non-functioal - performance, scalability, usuability.
# maintainence - we push a change then we test to see if impacted. 
# pytest allows for automated. 
# pip install pytest

# assert statements:

def func(num):
    return num * 2

def test_answer():
    assert func(6) == 12 

# pytest looks for files called test_*.py or *_test.py
# pytest testing.py

