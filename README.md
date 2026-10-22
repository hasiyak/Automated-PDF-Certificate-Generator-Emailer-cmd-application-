# CertiFlow: Automated PDF Certificate Generator & Emailer
#### Video Demo:  "https://youtu.be/ud7YiH9RoBw"
#### Description:

Hello everyone! My name is Hasindu Kaveeshwara and I am from Sri Lanka. This is my final project for CS50P. 

As a university student, I always help to organize many events, hackathons, and workshops in our faculty. Usually, after a big event finishes, the organizing commitee has to send participation certificates to all the students who joined. Doing this manually is a very big headache. Someone has to open Photoshop or Canva, type names one by one, save it as a PDF, and then email it to each person. It takes lots of hours and sometimes we make spelling mistakes in names. So, I wanted to build a python software to automate this full process. That is why I created "CertiFlow".

My project mainly does three things. First, it reads a CSV file containing the names and email adresses of the event participants. Second, it takes a pre-designed blank certificate PDF template and writes the participant's name perfectly in the center using a custom beautiful font. Finally, it creates an email message with a nice HTML body and automatically sends the generated certificate as an attachment to the participant's email.

Here is an explanation of the files in my project:

- `project.py`: This is the main python script of my project. I have used libraries like `csv`, `os`, `re`, `smtplib`, and `pymupdf`. In this file, I have my `main()` function and three other custom functions. 
  1. `is_valid_email()` checks if the email from the CSV is in the correct format using regular expressions. 
  2. `generate_certificate()` uses the PyMuPDF library to take the template, put the custom font (Magnolia Script) and text coordinates, and save a new PDF for each user. 
  3. `create_email_message()` builds the email object with an HTML body and attaches the generated PDF.

- `test_project.py`: This file contains all the tests for my custom functions. I used `pytest` to write three test functions (`test_is_valid_email`, `test_generate_certificate`, and `test_create_email_message`). I used a dummy PDF and dummy emails to test if the logic works correctly without actually sending real emails.

- `attendees.csv`: This is the file where the user can put the names and emails of the participants. 

- `templates/template.pdf`: This is the blank certificate design I made.

- `requirements.txt`: This file contains the external pip-installable libraries I used, which are `pymupdf` and `pytest`.

When developing this project, I made some important design choices. Initially, I tried to use the `fpdf` library to create the certificate from scratch. But it was very hard to get a professional look. So I decided it's much better to design the certificate in a software like Canva, export it as a blank PDF, and only use Python to write the name on it. I choose `PyMuPDF` (fitz) for this because it allows me to load external `.otf` custom fonts easily and gives very accurate text placement. 

Also, for sending emails, I decided to use the `smtplib` library. I learned that using my normal Gmail password will give a security block. So I used a 16-digit Google App Password for the script. I also decided to use an HTML body for the email instead of plain text because it looks much more professional and attractive for a university event.

This project will definetly save me and my friends a lot of time in our future university events. Thank you David Malan and the CS50 team for this amazing course!