#!/usr/bin/env python
'''
    This project contains a simple script to extract email messages
    from an IMAP server.
    The messages are written to a simple four-column CSV file.
    ## Dependencies
    This depends on the BeautifulSoup library and `lxml`
    for extracting text from HTML messages.
    ## Running the script
    You will need to have a file `credentials.txt`
    with your IMAP server account name and password on separate lines.
    Gmail - and many other IMAP providers -
    requires you to create a separate "application password"
    to allow this code to run, so probably do that first.
    Then put that password in `credentials.txt`.
    Then simply run
    ```
    python store_emails.py
    ```
    This generates `mails.csv` in the current directory.
    The generated CSV file contains the following fields for each message:
    * Date
    * From (Sender)
    * Subject
    * Message text
'''
import csv
import email
from email import policy
from email import message
import imaplib
import logging
import os
import ssl

from bs4 import BeautifulSoup


credential_path = "credentials.txt"
csv_path = "mails.csv"

logger = logging.getLogger('imap_poller')
host = "imap.gmail.com"
port = 993
ssl_context = ssl.create_default_context()


def connect_to_mailbox():
    # get mail connection
    mail = imaplib.IMAP4_SSL(host, port, ssl_context=ssl_context)

    with open(credential_path, "rt") as fr:
        user = fr.readline().strip()
        pw = fr.readline().strip()
        mail.login(user, pw)

    # get mail box response and select a mail box
    status, messages = mail.select("INBOX")
    return status, messages

# get plain text out of html mails
def get_text(email_body):
    soup = BeautifulSoup(email_body, "lxml")
    return soup.get_text(separator="\n", strip=True)


def write_to_csv(mail, writer, N, total_no_of_mails):
    for i in range(total_no_of_mails, total_no_of_mails - N, -1):
        res, data = mail.fetch(str(i), "(RFC822)")

        response = data[0]
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1], policy=policy.default)

            # get header data
            email_subject = msg["subject"]
            email_from = msg["from"]
            email_date = msg["date"]
            email_text = ""

            # if the email message is multipart
            if msg.is_multipart():
                # itrate over email parts
                for part in msg.walk():
                    # extract content type of email
                    contect_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email email_body
                        email_body = part.get_payload(decode=True)
                        if email_body:
                            email_text = get_text(email_body.decode("utf-8"))
                    except Exception as exc:
                        logger.warning(f"Caught exception: {exc}")

                    if (
                        contect_type == "text/plain"
                        and "attachment" not in content_disposition
                    ):
                        # print text/plain emails and skip attachments
                        # print(email_text)
                        pass
                    elif "attachment" in content_disposition:
                        pass
            else:
                # extract content type of email
                contect_type = msg.get_content_type()
                # get the email email_body
                email_body = msg.get_payload(decode=True)
                if email_body:
                    email_text = get_text(email_body.decode("utf-8"))

            if email_text is not None:
                # Write data in csv file
                row = [email_date, email_from, email_subject, email_text]
                writer.writerow(row)
            else:
                logger.warning(f"{INBOX}{i} No message extracted")


def main():
    mail, messages = connect_to_mailbox()

    logging.basicConfig(level=logging.WARNING)

    total_no_of_mails = int(messages[0])
    # no. of latest mails to fetch
    # set if equal to total_no_of_mails
    N = 2

    with open(csv_path, "wt", encoding="utf-8", newline="") as fw:
        writer = csv.writer(fw)
        writer.writerow(["Date", "From", "Subject", "Text mail"])
        try:
            write_to_csv(mail, writer, N, total_no_of_mails)
        except Exception as exc:
            logger.warning(f"Caught exception: {exc}")


if __name__ == "__main__":
    main()
