import problem2 as p2
import problem3 as p3
import problem4 as p4
import problem5 as p5

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
    
#Problem 4 tests
def test_problem4():
    assert p4.convert_base16_to_ascii(p4.convert_base16P_to_base16("BCAC99908DBEAD")) == "CSforAR"
    assert p4.convert_base16_to_ascii(p4.convert_base16P_to_base16("B6ABA8B0ADB4ACB0B1ABB7B6ACB2BEBCB7B6B1BA")) == "ITWORKSONTHISMACHINE"
    assert p4.convert_base16_to_ascii(p4.convert_base16P_to_base16("979E9C948B979A8F939E919A8B")) == "hacktheplanet"
    assert p4.convert_base16_to_ascii(p4.convert_base16P_to_base16("ZZTOP")) == "Invalid Input"

#Problem 5 tests:
def test_problem5():
    input_text = p5.get_input_file("2022_Packet\input_file.marky")
    correct_output = p5.get_input_file("2022_Packet\correct_output_file.txt")
    assert p5.run_commands(input_text, p5.parse_commands(input_text)) == correct_output