_dataLines = []

def readdata(datafilename):
    f = open(datafilename)
    for l in f:
        _dataLines.append(l.strip())
    f.close()

def title():
    return "The default title"

def content():
    return "\n".join(map(lambda l: "<p>{}</p>".format(l), _dataLines))
