#!/usr/bin/env python3

import datetime
import email.message
import mimetypes
import os
import smtplib
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(descriptions_directory, pdf_attachment_path):
    tmp_body_string = ""
    for file in os.listdir(descriptions_directory):
        with open(descriptions_directory + file) as txt_file:
            tmp_body_string = tmp_body_string + "<br/><br/>name: " + txt_file.readline() + "<br/>weight: " + txt_file.readline()
    report = SimpleDocTemplate(pdf_attachment_path)
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    pdf_title = Paragraph("Processed Update on " + datetime.datetime.strftime(datetime.datetime.today(), '%B %d, %Y'), title_style)
    body_style = styles["BodyText"]
    pdf_body = Paragraph(tmp_body_string, body_style)
    empty_line = Spacer(1,20)
    report.build([pdf_title, empty_line, pdf_body])
    return


def send_email_report(pdf_attachment_path, sender, receiver, subject, body):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(pdf_attachment_path)
    mime_type, _ = mimetypes.guess_type(pdf_attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(pdf_attachment_path, 'rb') as attachment:
        message.add_attachment(attachment.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)

    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
    return


def main():
    student_username = "student-02-750768f8a1b9"
    #create the PDF
    descriptions_directory = "/home/" + student_username + "/supplier-data/descriptions/"
    pdf_attachment_path = "/tmp/processed.pdf"
    create_pdf(descriptions_directory, pdf_attachment_path)
    #send the email with PDF created above
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    send_email_report(pdf_attachment_path, sender, receiver, subject, body)



if __name__ == "__main__":
    main()

