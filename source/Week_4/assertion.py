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
        
        
def check_in(liste, possible_values):
    return len(set(liste).intersection(possible_values)) > 0

def nb_pays(liste, _input):
    assert_answer(len(liste), _input)

    
GRECE_SET = {"Grèce", "grece", "grèce", "Grece"}

def add_greece(liste):
    assert_answer(check_in(liste, GRECE_SET), True)
    
    
def est_membre(liste, _input):
    assert_answer(len(GRECE_SET.intersection(set(liste))) > 0, _input)
    
def Canada(liste):
    assert_answer(liste[4], {"Canada", "canada"})
    
    
def papillon(_dict, _input):
    assert_answer(_dict["papillon"], _input)
    
def add_cow(_dict):
    try:
        assert_answer(_dict["vache"], "cow")
    except KeyError:
        assert_answer(True, False)
        
def correct(_dict):
    assert_answer(_dict["oiseau"], "bird")