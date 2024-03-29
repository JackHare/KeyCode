import problem2 as p2

def test_answer():
    
    #Problem 2 tests
    assert p2.validateInput(["02", "FEB", "22"]) == True
    assert p2.validateInput(["February", "2", "2022"]) == False