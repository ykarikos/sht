import codecs

def readdata(datafilename):
    dataLines = []
    f = codecs.open(datafilename, encoding='utf-8')
    for l in f:
        dataLines.append(l.strip())
    f.close()
    return dataLines

def title(data):
    return "The default title"

def content(data):
    return "\n".join(map(lambda l: u"<p>{}</p>".format(l), data))
