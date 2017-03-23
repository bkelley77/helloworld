# -*- coding: utf-8 -*-
# helloworld
#

# load library modules
#
import os
import sys


def config():
  print("Configuring Hello world!")


def stop():
  print("Stopping Hello world!")


def start():
  print("Starting Hello world!")

def main():
  #
  myhost = os.uname()[1]
  print("Hello world!")
  print("On host: " + myhost)
  print("version 13")
  start()
  config()
  stop()
    
print('__name__=' + __name__)
if __name__ == "__main__":
    main()

                                                        


