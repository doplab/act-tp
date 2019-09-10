from binary_conversion import NumberConverter

def red_print(_input):
    print("\x1b[31m\""+ str(_input) +"\"\x1b[0m")
    
def green_print(_input):
    print("\033[32m\""+ str(_input) +"\"\x1b[0m")

    
def assert_answer(_input, correct):
    correct_answer = False
    if isinstance(correct, set):
        correct_answer = _input in correct
    else:
        correct_answer = _input == correct
    if correct_answer:
        green_print("Bonne réponse!")
    else:
        red_print("Mauvaise réponse, réessayez")
    
def check_1_a(_input):
    assert_answer(_input, "1010")
    
def check_1_b(_input):
    assert_answer(_input, "101101")
    
def check_1_c(_input):
    assert_answer(_input, "10101101")
    
def check_2_a(_input):
    assert_answer(_input, NumberConverter(40, 10).convert(8))
    
def check_2_b(_input):
    assert_answer(_input, NumberConverter(52, 10).convert(3))
    
def check_2_c(_input):
    assert_answer(_input, NumberConverter(254, 10).convert(16))
    
def check_3_a(_input):
    assert_answer(_input, NumberConverter("10110", 2).convert(10))
    
def check_3_b(_input):
    assert_answer(_input, NumberConverter("4321", 5).convert(10))
    
def check_3_c(_input):
    assert_answer(_input, NumberConverter("ABC", 16).convert(10))
    
def check_add_binary(n1, n2, _input):
    a = NumberConverter(n1, 2)
    b = NumberConverter(n2, 2)
    c = a+b
    assert_answer(_input, c.convert(2))
    
def check_4_a(_input):
    check_add_binary("01010101", "10101010", _input)
    
def check_4_b(_input):
    check_add_binary("01011111", "10000001", _input)
    
def check_4_c(_input):
    check_add_binary("01110100", "00011010", _input)
    
    
def check_5_FETCH(counter, register):
    print("PROCESS COUNTER:")
    assert_answer(counter, "00100001")
    print("INSTRUCTION REGISTER:")
    assert_answer(register, "10110110")
    
def check_5_DECODE(operation, resultat, premier, deuxieme):
    print("OPERATION:")
    assert_answer(operation, {"add", "ADD"})
    print("ADRESSE DU RESULTAT:")
    assert_answer(resultat, {"11", "00000011", "r3", "R3"})
    print("PREMIER NOMBRE:")
    assert_answer(premier, "01101100")
    print("DEUXIEME NOMBRE:")
    assert_answer(deuxieme, "00100101")
    
    
def check_5_EXECUTE(resultat):
    assert_answer(resultat, "10010001")