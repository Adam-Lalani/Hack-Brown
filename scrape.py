import os
import csv
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
our_email = 'hackatbrown1@gmail.com'

def gmail_authenticate():
    creds = None
    token_path = "token.pickle"

    if os.path.exists(token_path):
        with open(token_path, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=8081)
        with open(token_path, "wb") as token:
            pickle.dump(creds, token)
    return creds

def create_dataset(service, query):
    results = service.users().messages().list(userId=our_email, q=query).execute()
    messages = results.get('messages', [])

    dataset = []
    
    if not messages:
        print('No messages found.')
    else:
        #print('Messages:')
        for message in messages:
            msg = service.users().messages().get(userId=our_email, id=message['id']).execute()
            dataset.append(msg)

    return dataset

def write_to_csv(dataset, csv_filename='emails.csv'):
    fields = ['Subject', 'From', 'To', 'Date', 'Snippet']

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fields)
        csv_writer.writeheader()

        for msg in dataset:
            subject = msg['subject'] if 'subject' in msg else ''
            sender = msg['from'] if 'from' in msg else ''
            recipient = msg['to'] if 'to' in msg else ''
            date = msg['date'] if 'date' in msg else ''
            snippet = msg['snippet'] if 'snippet' in msg else ''

            csv_writer.writerow({
                'Subject': subject,
                'From': sender,
                'To': recipient,
                'Date': date,
                'Snippet': snippet
            })

def main():
    creds = gmail_authenticate()
    service = build('gmail', 'v1', credentials=creds)
    
    #retrieve all emails
    query = ""

    dataset = create_dataset(service, query)

    # Write the dataset to a CSV file
    write_to_csv(dataset)

if __name__ == '__main__':
    main()







