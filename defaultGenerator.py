def readdata(datafilename):
    dataLines = []
    f = open(datafilename)
    for l in f:
        dataLines.append(l.strip())
    f.close()
    return dataLines

def title(data):
    return "The default title"

def content(data):
    return "\n".join(map(lambda l: "<p>{}</p>".format(l), data))
