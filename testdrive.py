from __future__ import print_function

from apiclient.http import MediaFileUpload

file_metadata = {
  'name' : 'Book1',
  'mimeType' : 'application/vnd.google-apps.spreadsheet'
}
media = MediaFileUpload('Book1.csv',
                        mimetype='text/csv',
                        resumable=True)
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print ('File ID: %s' % file.get('id'))