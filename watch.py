#!/usr/bin/python

import sys, os, time

def generate(generatorModule, templatefilename, datafilename, outputfilename):
    generator = __import__(generatorModule)

    tf = open(templatefilename, 'r')
    template = tf.read()
    tf.close()

    generator.readdata(datafilename)
    title = generator.title()
    content = generator.content()

    out = open(outputfilename, 'w')
    out.write(template % { "title": title, "content": content })
    out.close()


def checkFilesModified(files, target):
    targetTime = os.stat(target).st_mtime
    for filename in files:
        if (os.stat(filename).st_mtime > targetTime):
            print("{} changed, generating...".format(filename))
            return True
    return False

def main():
    template = 'template.html'
    data = 'data.txt'
    target = 'index.html'
    generator = 'defaultGenerator'
    while True:
        generate(generator, template, data, target)
        print("Generated {} from {} and {}.".format(target, template, data))
        try:
            while True:
                time.sleep(2)
                if checkFilesModified([template, data], target):
                    break
        except KeyboardInterrupt:
            print("bye")
            return 0

if __name__ == "__main__":
    sys.exit(main())
