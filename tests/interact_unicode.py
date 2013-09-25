#!/usr/bin/env python
'''
Just like interact.py, but using spawnu instead of spawn
'''
import pexpect

def main():
    p = pexpect.spawn('cat')
    p.interact()

if __name__ == '__main__':
    main()