"""Create a list of images as the HTML content.
Assumes that all lines in data file beginning with 'http' are image urls.
"""
def readdata(datafilename):
    urls = []
    f = open(datafilename)
    for line in f:
        if line.startswith("http"):
            urls.append(line.strip())
    f.close()
    return urls

def title(urls):
    return str(len(urls)) + " images"

def content(urls):
    itemHtml = '<li><a href="{0}"><img src={0}></a></li>'

    return "<ul>" + \
        "\n".join(map(lambda l: itemHtml.format(l), urls)) + \
        "</ul>\n"
