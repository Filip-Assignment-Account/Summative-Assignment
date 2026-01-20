import sys
sys.path.append("..\..\src\summative_project")
from summative_project.Encryption import Encryption
from summative_project.Cards import Cards
from summative_project.Sorting import Sorting
from summative_project.Fibonacci import Fibonacci
from summative_project.Factorial import Factorial

"""Functions run from here cannot find main, for example running encryption.encrypt_text() will complain that
encryption cannot find main , no idea why"""

def test_encryption():
    encrypted_text = Encryption.encrypt_text(Encryption, "test", None)
    unencrypted_text = Encryption.decrypt_text(encrypted_text, "test", None)
    assert unencrypted_text == encrypted_text

def test_sorting():
    sorted_array = Sorting.selection_sort(Sorting, [10, 50, 324759034, 203])
    assert sorted_array == [10, 50, 203, 324759034]

def test_cards():
    cards = Cards.get_full_deck()
    assert len(cards) == 52

def test_fibonacci():
    fibonacci_number = Fibonacci.find_fibonacci(Fibonacci, 50)
    assert fibonacci_number == 12586269025

def test_factorial():
    factorial = Factorial.factorial(Factorial, 20)
    assert factorial == 121645100408832000




