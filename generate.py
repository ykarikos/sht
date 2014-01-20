#!/usr/bin/python

import sys

def generateTitle():
    return "title"

def generateContent():
    return "<p>{}</p>".format("foobar")

def main():
    tf = open('template.html', 'r')
    template = tf.read()
    tf.close()

    title = generateTitle()
    content = generateContent()
    print template % { "title": title, "content": content }
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
