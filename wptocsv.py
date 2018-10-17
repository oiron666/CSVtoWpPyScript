import csv
import time, datetime
import xmlrpc.client
import requests
requests.packages.urllib3.disable_warnings()
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

wp_credentials = (open('wpcreds.txt', 'r'))
wp_id = wp_credentials.read().split(',')
wp_url = ""
wp_username = wp_id[0]
wp_password = wp_id[1]
wp_blogid = ""
status_draft = 0
status_published = 1

server = xmlrpc.client.ServerProxy(wp_url)

with open('reader.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)


    for line in reader:
        imgurl = line[1]
        post_title = line[2]
        tag1 = line[3]
        tag2 = line[4]
        tag3 = line[5]
        tag4 = line[6]
        tag5 = line[7]
        tag = [tag1, tag2, tag3, tag4, tag5]

        date_created = xmlrpc.client.DateTime(datetime.datetime.strptime("2011-10-20 21:08", "%Y-%m-%d %H:%M"))
        content = post_title + "    " + "<br.>" + "<img src=" + imgurl + " />"
        data = {'title': post_title, 'description': content, 'mt_keywords': tag}
        post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_draft)
        print(i)
        time.sleep(61)
