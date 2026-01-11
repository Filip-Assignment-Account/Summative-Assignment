import sys
sys.path.append("..\..\src\summative_project")
import pytest
import src.summative_project.Encryption as Encryption
import src.summative_project.main as main


def test_encryption():
    encryption = Encryption()
    encrypted_text = encryption.encrypt_text("test", None)
    unencrypted_text = encryption.decrypt_text(encrypted_text, None)
    assert unencrypted_text == encrypted_text


