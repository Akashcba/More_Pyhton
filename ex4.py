#Handling advanced command line arguments using argparse module
import argparse
# creating a parser Object with all the entered arguments
parser = argparse.ArgumentParser()
# Adding arguments to the parser
parser.add_argument('integers',metavar='akash',type=str,nargs='+')
# Metavar provides an alias name in help messages
parser.add_argument('-f',help='foo help')
parser.add_argument('-b',help='bar help')
# Argument without a '-' becomes a necessary positional argument.
parser.add_argument('bz',help='baz help')
# the below arguments come under optional arguments.
parser.add_argument('-t','--turn-on',action='store_true')
#action : the arguments can trigger different actions based
#on the action argument passed.
#store:Save the value, after optionally converting it to a different type.
#This is the default action taken if none is specified explicitly.
#store_true/store_false: Save the appropriate boolean value.
#store_const: Save a value defined as part of the argument specification,
#rather than a value that comes from the arguments being parsed.
#This is typically used to implement command line flags that aren’t booleans.
#append: Save the value to a list. Multiple values are saved if the argument is repeated.
#append_const: Save a value defined in the argument specification to a list.
#version: Prints version details about the program and then exits.
parser.add_argument('-x','--exclude',action='store_false')
parser.add_argument('-s','--start',action='store_true')
args=parser.parse_args()

print("The arguments ar as follows :\n",args) # Prints these arguments -> We can do other taska also.
