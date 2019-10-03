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
        
        
class State:
    states = {}
    
    @staticmethod
    def memoize(_id, state):
        conditions = _id not in State.states or State.states[_id] != state
        if conditions:
            State.states[_id] = state
        
    def __init__(self, _id = None, **kwargs):
        self.value = kwargs
        self._id = _id
        if _id is not None:
            State.memoize(_id, self)
        
    def __eq__(self, compare):
        if len(self.value) is not len(compare.value):
            return False
        for key in self.value:
            if key not in compare.value or self.value[key] is not compare.value[key]:
                return False
        return True
    
    def transform(self, function):
        s = State(**self.value)
        function(s.value)
        return s
        

def assert_division(poids_chien, resultat, remainder):
    print("Résultat: ")
    assert_answer(poids_chien/2, resultat)
    print("Remainder")
    assert_answer(poids_chien%2, remainder)
    
    
def assert_sub(initial_state, end_state):
    def fun(state):
        state["poids_chien"] -= 1
        state["poids_ideal"] -= 2
    result = initial_state.transform(fun)
    assert_answer(end_state, result)
    
    
def assert_equal(poids_chien, poids_ideal, comparison):
    assert_answer(comparison, poids_chien == poids_ideal)
    
    
def assert_comparison(poids_chien, poids_ideal, comparison):
    assert_answer(comparison, poids_chien <= poids_ideal)
    
    
def assert_strings(python3, lettre_h, signe_ex):
    print("python3")
    if len(python3) < 13:
        red_print("Python 3 devrait contenir au moins 13 charactères")
        return
    assert_answer(type(python3), type("sample"))
    print("Première lettre")
    assert_answer(lettre_h, python3[0])
    print("Dernière lettre")
    assert_answer(signe_ex, python3[-1])

    
def assert_slicing(python3, quatre, neuf_treize, cinq_huit):
    if len(python3) < 13:
        red_print("Python 3 devrait contenir au moins 13 charactères")
        return
    print("Quatre premiers charactères")
    assert_answer(quatre, python3[:4])
    print("Charatères 9 à 13")
    assert_answer(neuf_treize, python3[9:13])
    print("Charactères 5 à 8")
    assert_answer(cinq_huit, python3[5:8])
    
    
def assert_half(python3, _in):
    assert_answer(python3[:int(len(python3)/2)], _in)
    
def assert_dont_worry(dont_worry, upper, lower):
    print("Don't worry")
    assert_answer(dont_worry, "Don't worry, you're gonna become a king!")
    print("Lower")
    assert_answer(lower, dont_worry.lower())
    print("Upper")
    assert_answer(upper, dont_worry.upper())