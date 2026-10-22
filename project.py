import csv
import re
import os
import smtplib
from email.message import EmailMessage
import pymupdf as fitz


sender_email = "[EMAIL_ADDRESS]"
sender_password = "[PASSWORD]"

def main():

    print("Auto PDF Certificate Generator & Email Sender!")

    # create output floder if not exists
    if not os.path.exists("output"):
        os.makedirs("output")

    # path to the certificate template
    template_path = "templates/template.pdf"

    # check if the template exists
    if not os.path.exists(template_path):
        print("Error: Certificate template not found!")
        return
    
    
    try:
        # read the csv file
        with open("attendees.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
        
            # loop through each row in the csv file
            for row in reader:
                name = row["name"].strip()
                email = row["email"].strip()

                # check if the email is valid
                if is_valid_email(email):
                    print(f"✅ Processing: {name}...")

                    # create the output path for the certificate
                    output_pdf = os.path.join("output", f"{name.replace(' ' , '_')}_certificate.pdf")
                    
                    # generate the certificate
                    generate_certificate(name, template_path, output_pdf)

                    # create the email message
                    msg = create_email_message(sender_email, email, name, output_pdf)

                    # send the email
                    try:
                        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                            smtp.login(sender_email, sender_password)
                            smtp.send_message(msg)
                        print(f"   -> Email sent to {email}")
                    
                    # if email fails
                    except Exception as error:
                        print(f"   -> Failed to send email: {error}")

                else:
                    # if email is invalid
                    print(f"⚠️ Skipping {name} - Invalid email: {email}")
    # if csv file not found
    except FileNotFoundError:
        print("❌ Error: attendees.csv not found!")

def is_valid_email(email):
    # pattern for validating email
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.search(pattern, email):
        return True
    return False


def generate_certificate(name, template_path, output_path):
    # open the template pdf
    doc = fitz.open(template_path)
    # select first page
    page = doc[0]
    # x and y coordinates of the text
    x =  59.514
    y = 283.4
    text_point = fitz.Point(x,y)
    # insert the text
    page.insert_text(text_point, name, fontsize=45, fontfile="Magnolia Script.otf", fontname="magnolia", color=(21/255, 13/255, 87/255))
    # save the certificate
    doc.save(output_path)
    doc.close()
    return output_path

# function to create an email message
def create_email_message(sender_email, recipient_email, name, pdf_path):
    # create an email message
    msg = EmailMessage()
    msg['Subject'] = f"Your Certificate of Participation - {name}"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # html body of the email
    html_body = f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333333;">
        <h2 style="color: #150d57;">Dear {name},</h2>
        <p>With great honor, please find attached your <b>Certificate of Achievement</b>.</p>
        <p>This certificate is awarded to you in recognition of your exceptional perseverance, dedication, and success in achieving remarkable goals. We are incredibly proud of your accomplishments.</p>
        <p>Please download the attached PDF to view your certificate.</p>
        <br>
        <p>Best Regards,</p>
        <p><b>Chidi Eze</b> (Mentor) & <b>Matt Zhang</b> (Manager)</p>
      </body>
    </html>
    """

    # set the content of the email
    msg.set_content("Please enable HTML to view this email.") 
    # add the html body
    msg.add_alternative(html_body, subtype='html')
    
    # add the pdf as an attachment
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            pdf_data = f.read()
        msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename=os.path.basename(pdf_path))

    return msg


if __name__ == "__main__":
    main()