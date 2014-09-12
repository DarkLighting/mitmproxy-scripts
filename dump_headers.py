
def response(context, flow):

    fp = open('headers','w+')
    fp.write('Server Response Headers:\n')
    fp.write('========================\n')
    for header, value in flow.response.headers.items():
        fp.write(str(header)+': '+str(value)+'\n')
    fp.write('\n')
    fp.close()

