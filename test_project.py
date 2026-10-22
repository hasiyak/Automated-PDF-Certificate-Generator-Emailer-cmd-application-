import os
from email.message import EmailMessage
import pymupdf as fitz
from project import is_valid_email, generate_certificate, create_email_message
import pytest

def test_is_valid_email():
    assert is_valid_email("kaveeshwarahasindu@gmail.com") == True
    assert is_valid_email("invalid-email") == False

def test_generate_certificate():
    test_template = "templates/test_template.pdf"
    doc = fitz.open()
    doc.new_page()
    doc.save(test_template)
    doc.close()


    output_path = "output/test_output.pdf"
    
    generate_certificate("Test Name", test_template, output_path)
    
    assert os.path.exists(output_path) == True

    os.remove(test_template)
    os.remove(output_path)

def test_create_email_message():
    sender = "admin@test.com"
    recipient = "user@test.com"
    name = "Kasun"
    
    msg = create_email_message(sender, recipient, name, "dummy.pdf")
    
    assert isinstance(msg, EmailMessage)
    assert msg['To'] == recipient
    assert msg['Subject'] == "Your Certificate of Participation - Kasun"
    
    assert "Dear Kasun" in str(msg)