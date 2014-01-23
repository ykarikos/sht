#!/usr/bin/python
"""watch.py: Simple HTML templating

Usage: ./watch.py [options]

Options:
 -g generatorModule (default defaultGenerator)
 -t templateFile (default template.html)
 -d dataFile (default data.txt)
 -o outputFile (default index.html)
 -h this help
"""

import sys, os, time, getopt, codecs

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def generate(generatorModule, templatefilename, datafilename, outputfilename):
    generator = __import__(generatorModule)

    tf = open(templatefilename, 'r')
    template = tf.read()
    tf.close()

    data = generator.readdata(datafilename)
    title = generator.title(data)
    content = generator.content(data)

    out = codecs.open(outputfilename, encoding='utf-8', mode='w')
    out.write(template % { "title": title, "content": content })
    out.close()


def checkFilesModified(files, target):
    targetTime = os.stat(target).st_mtime
    for filename in files:
        if (os.stat(filename).st_mtime > targetTime):
            print("{} changed, generating...".format(filename))
            return True
    return False

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "g:t:d:o:?h")
        except getopt.error, msg:
            raise Usage(msg)

        # process options
        generator = 'defaultGenerator'
        template = 'template.html'
        data = 'data.txt'
        output = 'index.html'
        for o, a in opts:
            if o == "-g":
                generator = a
            elif o == "-t":
                template = a
            elif o == "-d":
                data = a
            elif o == "-o":
                output = a
            elif o == "-h" or o == "-?":
                print __doc__
                return 0
        if template == output or data == output or template == data:
            sys.stderr.write("Can not use same filenames on template, output or data\n")
            return 2

        # main watch loop
        while True:
            generate(generator, template, data, output)
            print("Generated {} from {} and {}.".format(output, template, data))
            try:
                while True:
                    time.sleep(2)
                    if checkFilesModified([template, data], output):
                        break
            except KeyboardInterrupt:
                print("bye")
                return 0

    except Usage, err:
        sys.stderr.write(str(err.msg))
        sys.stderr.write("\nfor help use -h\n")
        return 3

if __name__ == "__main__":
    sys.exit(main())
