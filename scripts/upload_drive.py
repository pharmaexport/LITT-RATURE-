from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def upload(pdf_path: Path, folder_id: str) -> str:
    raw = os.environ.get('GOOGLE_SERVICE_ACCOUNT_JSON')
    if not raw:
        raise RuntimeError('Secret GOOGLE_SERVICE_ACCOUNT_JSON manquant')

    info = json.loads(raw)
    creds = service_account.Credentials.from_service_account_info(
        info,
        scopes=['https://www.googleapis.com/auth/drive.file'],
    )
    drive = build('drive', 'v3', credentials=creds, cache_discovery=False)

    metadata = {'name': pdf_path.name, 'parents': [folder_id]}
    media = MediaFileUpload(str(pdf_path), mimetype='application/pdf', resumable=True)
    result = drive.files().create(
        body=metadata,
        media_body=media,
        fields='id,webViewLink',
        supportsAllDrives=True,
    ).execute()

    file_id = result['id']
    link = result.get('webViewLink') or f'https://drive.google.com/file/d/{file_id}/view'
    print(link)
    return link


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf')
    parser.add_argument('--folder-id', default=os.environ.get('GOOGLE_DRIVE_FOLDER_ID', ''))
    args = parser.parse_args()
    if not args.folder_id:
        raise RuntimeError('GOOGLE_DRIVE_FOLDER_ID manquant')
    upload(Path(args.pdf), args.folder_id)
