#create api 
#install library
#https://developers.google.com/blogger/ documentation

# Learned to do pip install with no help
#!/usr/bin/env python
import httplib2
from oauth2client import client
from apiclient.discovery import build 
from oauth2client.file import Storage

blogid = 0  # put your blog id here
isDraft = True # Dont change this unless you are prepared to modify the script
postfile = ''
title = 'Default Title' # Change this to the deefault title you prefer

# comma delimited of labels for the post 
# if you set a default liist it will be overwritten 
#if labels are supplied in the command line args
#otherwise the default list is used 
labels = 'linux, rocks'

# at a minimum we must include the file containing our blog post
if (len(sys.argv) < 2):
    print("Usage: %s -f \"Filename\" [-t] \"My Title\* [-l] \"label, label\* [--publish]" % sys.argv[0])
    print("Post's are uploaded as drafts by default. Use --publish if you want to " "publish immediately\n")
    sys.exit()

# seems like my from are not taken in

#handle args
# myopts, args = getopt.geoopt(sys.argv[1:], "f:t:l", ['publish])
for o, a in myopts:
    if o == '-f':
        postfile = a
    elif o == '--publish':
        isDraft = False
    elif o == '-t':
        title = a
    elif o == '-l':
        labels = a

# if we want ti publish we must supply the title
if(isDraft == False and title == 'Default Title'):
    print("You must provide a title if you want to publish! ")
    sys.exit()

# if there is no user_key authentication with google and save the key
if(os.path.exists('userkey') == False):
    flow = client.flow_from_clientsecrets('client_id.json'
    scope='https://www.googleapis.com/auth/blogger'
    redirect_urls='urn:letf:wg:oauth:2.0:oob'
    )

    auth_url = flow.step1_get_authorize_url()
    webbrowser.open_new(auth_url)
    auth_code = raw_input('Enter the auth code: ')
    credentials = flow.step2_exchange(auth_code)
    http_auth = credentials.authrize(httplib2.http())
    
    # storage
    storeage = storage( 'userkey')
    storage.put(credentials)
    
else:
    storage = Storage('userkey')
    credentials = storage.get()
    http_auth = credentials.authorize(httplib2.Http())

# initialize the blogger service and get blog
blogger_service = build('blogger', 'v3', http=http_auth)

# ope file for reading
try:
    f = open(postfile, 'r')
except:
    print("Error openning file. Aborting....")
    sys.exit()

# build a label
labels_list = labels.split(',')

# build body of object
body = {
        "content": f.read(),
        "title": title,
        "labels": labels_list
        }

try:
    post = blogger_service.posts().insert(blogid=blogid, body=body, isDraft=isDraft).execute()

except:
    print("Google didn't like our post :(")
    sys.exit()

print("Title: %s" % post['title'])
print("Is Draft: %s" % isDraft)
if(isDraft == False):
    print("URL: %s" % post['url'])
print("label: %s" % post['labels'])


#need to have a blog post in file and the clients_id.json
# first need to fix the froms @ the start the check code