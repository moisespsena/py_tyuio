#!/usr/env/bin python

__author__ = 'moisespsena@gmail.com'

from subprocess import call

def main(ex, *args):
    args = [ex, 'setup.py'] + list(args)
    print("%s %s %s" % ("=" * 20, " ".join(args), "=" * 20))
    call(args)

py2 = lambda *args: main('python2', *args)
py3 = lambda *args: main('python3', *args)

runnings = [py2, py3]

commands = [
    ['register'],
    ['test'],
    ['sdist', 'bdist_egg', 'upload'],
]

for r in runnings:
    for args in commands:
        r(*args)