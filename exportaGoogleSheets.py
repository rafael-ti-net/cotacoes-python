from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main(*args):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId='1RM-QmVcRTagSRqZAl1p2hhxbhd5kBhW0Qns-m2FVeoo',
                                    range='Pagina1!A1:J20').execute()
        values = result.get('values', [])
       
        valores_adicionar = [[*args]]        
        ultima_linha = len(values) + 1

        result = result = sheet.values().update(spreadsheetId='1RM-QmVcRTagSRqZAl1p2hhxbhd5kBhW0Qns-m2FVeoo',
                                    range='Pagina1!A'+str(ultima_linha),valueInputOption = 'RAW',
                                    body={'values':valores_adicionar}).execute()

        print('Planilha atualizada com sucesso!')

    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()