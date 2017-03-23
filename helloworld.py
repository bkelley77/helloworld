# -*- coding: utf-8 -*-
# helloworld
#

# load library modules
#
import os
import sys

#############################################################################
# function: config()
#
# description:
#
#    Used during orchestration for the "configuration event"
#############################################################################
def config():
  print("Configuring Hello world!")

#############################################################################
# function: stop()
#
# description:
#
#    Used during orchestration for the "stop event"
#############################################################################
def stop():
  print("Stopping Hello world!")

#############################################################################
# function: start()
#
# description:
#
#    Used during orchestration for the "start event"
#############################################################################
def start():
  print("Starting Hello world!")


#############################################################################
# function: main()
#
# author: bk
#
# description
#
# simple hello world program
#    1) testing cloud development and deployment
#    2) automation/orchestration using OSM Juju Charms
#############################################################################
def main():

  #
  # initialization
  #
  params = ['none']

  #
  # get first parameter passed into the program (start, stop, config, other)
  #
  print(sys.argv)
  print(' ')
  if len(sys.argv) > 1 : params = sys.argv[1:]
  print ('Action requested: ' + str(params[0]))
  print(' ')

  #
  # print hello world and the computer that we are running on
  #
  # using the version number to play with github and making sure things are working
  #
  myhost = os.uname()[1]
  print("Hello World, On host: " + myhost + " [Version 14]")
  print(' ')

  #
  # take action (start, stop, config)
  #
  if (params[0] == 'start') :
    start()
  elif (params[0] == 'config'):
    config()
  elif (params[0] == 'stop'):
    stop()
  else:
    print("No arguments passed")

#############################################################################
# are we running this program standalone, if so call main()
#############################################################################

if __name__ == "__main__":
    main()

                                                        


