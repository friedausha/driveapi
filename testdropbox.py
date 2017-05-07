import dropbox
import os
from dropbox.client import DropboxClient
import sys
dbx = dropbox.Dropbox('65tw70iHoaAAAAAAAAAAXwx-YPY-f9I3jsigl4p9HKO2rnz0f6VPgxzPNf5ZxFpP')
app_key = 'upawlw4kpobp8f7'
app_secret = '0xi4siv79bkshgp'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()
access_token, user_id = flow.finish(code)
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()
f = open('C:\Users\Frieda\PycharmProjects\Tulips.jpg', 'rb')
response = client.put_file('/Tulips.jpg', f)
print "uploaded:", response
#f, metadata = client.get_file_and_metadata('/video1.avi')
out = open('Tulips.jpg', 'wb')
out.write(f.read())
out.close()


#access_token, local_directory, dropbox_destination = sys.argv[1:4]
#print ("Attempting to upload...")
#rootdir = 'C:/Users/Frieda/PycharmProjects/testdropbox'
# walk return first the current folder that it walk, then tuples of dirs and files not "subdir, dirs, files"
#for dir, dirs, files in os.walk(rootdir):
 #   for file in files:
  #      try:
 #           file_path = os.path.join(dir, file)
   #         dest_path = os.path.join('test dropbox', file)
    #        print 'Uploading %s to %s' % (file_path, dest_path)
     #       with open(file_path) as f:
      #          dbx.files_upload(f, dest_path, mute=True)
       # except Exception as err:
        #    print("Failed to upload %s\n%s" % (file, err))

#print("Finished upload.")
#out = open('Tulips.jpg', 'wb')
#with client.get_file('Tulips.jpg') as f:
 #   out.write(f.read())

 