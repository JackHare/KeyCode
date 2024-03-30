import problem2 as p2
import problem3 as p3

#Problem 2 tests
def test_problem2():
    assert p2.validateInput(["02", "FEB", "22"]) == True
    assert p2.validateInput(["February", "2", "2022"]) == False
    
#Problem 3 tests
def test_problem3():
    assert p3.validateAddress("A01F:0011:5CD3:E321:CCCC:FFFF:0000:0122") == True
    assert p3.validateAddress("127.0.0.1") == False
    assert p3.validateAddress("A01F:11:5CD3:E321:CCCC:FFFF:0:122") == True
    assert p3.validateAddress("A01F:11:5CD3:E321:CCCC:FFFF::122") == True
    assert p3.validateAddress("C23:53:2::FF:3456:3D:483") == True
    assert p3.validateAddress("34.23.13456.3245H.403.7457.2.3DEFF") == False