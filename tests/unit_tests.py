import sys
sys.path.append("..\..\src\summative_project")
import src.summative_project.Encryption as Encryption
import src.summative_project.Cards as Cards

"""Functions run from here cannot find main, for example running encryption.encrypt_text() will complain that
encryption cannot find main , no idea why"""

def test_encryption():
    encryption = Encryption()
    encrypted_text = encryption.encrypt_text("test", None)
    unencrypted_text = encryption.decrypt_text(encrypted_text, None)
    assert unencrypted_text == encrypted_text

def test_cards():
    cards_object = Cards()
    cards = cards_object.get_full_deck()
    assert len(cards) == 52



