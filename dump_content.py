import os
import hashlib

def response(context, flow):

    for header, value in flow.response.headers.items():
        if header.lower() == 'content-type':
            if value.find(';') > -1: 			# if ';' exists in the content-type
                value = value[:value.find(';')]
            if value.find('/') > -1:				# if '/' exists in the content-type
                name = str(value).replace('/', '_')
            path = 'content/'+name.lower()
            ext = name[name.find('_'):]
            if not os.path.exists(path):
                os.makedirs(path)
            content = open(path+'/'+hashlib.sha1(flow.response.content).hexdigest()+ext, 'w+')
            content.write(flow.response.content)
            content.close()
            break

