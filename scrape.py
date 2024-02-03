import os
import csv
import base64
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
    messages = results.get("messages", [])
    dataset = []
    count = 0

    if not messages:
        print("You have no New Messages.")
    else:
        for message in messages:
            msg = service.users().messages().get(userId=our_email, id=message['id']).execute()
            count +=1
            
            # Extracting 'From' and 'Subject' information from headers
            from_name = next((value["value"] for value in msg["payload"]["headers"] if value["name"] == "From"), None)
            subject = next((value["value"] for value in msg["payload"]["headers"] if value["name"] == "Subject"), None)

            # Extracting text data from payload parts
            for part in msg["payload"]["parts"]:
                if part["mimeType"] == "text/plain":
                    data = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
                    dataset.append({
                        "From": from_name,
                        "Subject": subject,
                        "Data": data
                    })
    print(count)

    return dataset

def write_to_csv(dataset, csv_filename='emails.csv'):
    fields = ['From', 'Subject', 'Data']

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fields)
        csv_writer.writeheader()

        for email_data in dataset:
            csv_writer.writerow({
                'From': email_data.get('From', ''),
                'Subject': email_data.get('Subject', ''),
                'Data': email_data.get('Data', '')
            })


# def create_dataset(service, query):
    
#     results = service.users().messages().list(userId=our_email, q=query).execute()

#     messages = results.get("messages", [])
#     dataset = []

#     if not messages:
#         print("You have no New Messages.")

#     else:
#         message_count = 0
#         for message in messages:
#             msg = service.users().messages().get(userId=our_email, id=message['id']).execute()
#             message_count = message_count + 1
#             email_data = msg["payload"]["headers"]
#             for values in email_data:
#                 name = values["name"]
#                 if name == "From":
#                     from_name = values["value"]
#                     print("FROM")
#                     print(from_name)
#                     subject = [j["value"] for j in email_data if j["name"] == "Subject"]
#                     print("SUBJECT")
#                     print(subject)

#             # I added the below script.
#             for p in msg["payload"]["parts"]:
#                 if p["mimeType"] in "text/plain":
#                     data = base64.urlsafe_b64decode(p["body"]["data"]).decode("utf-8")
#                     print(data)
#                     dataset.append(data)
#     return dataset
    # results = service.users().messages().list(userId=our_email, q=query).execute()
    # messages = results.get('messages', [])

    # dataset = []
    
    # if not messages:
    #     print('No messages found.')
    # else:
    #     #print('Messages:')
    #     for message in messages:
    #         msg = service.users().messages().get(userId=our_email, id=message['id']).execute()
    #         dataset.append(msg)

    # return dataset

# def write_to_csv(dataset, csv_filename='emails.csv'):
#     fields = ['Snippet', 'Text']

#     with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
#         csv_writer = csv.DictWriter(csvfile, fieldnames=fields)
#         csv_writer.writeheader()

#         for msg in dataset:
#             snippet = msg['snippet'] if 'snippet' in msg else ''
#             body = msg['body'] if 'body' in msg else ''
#             text = body['data'] if 'data' in body else ''
#             print(text)

#             csv_writer.writerow({
#                 'Snippet': snippet,
#                 'Text': text
#             })


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







