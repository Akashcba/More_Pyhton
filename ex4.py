#Handling advanced command line arguments using argparse module
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers',metavar='akash',type=str,nargs='+')
parser.add_argument('-f',help='foo help')
parser.add_argument('-b',help='bar help')
parser.add_argument('bz',help='baz help')
parser.add_argument('-t','--turn-on',action='store_true')
parser.add_argument('-x','--exclude',action='store_false')
parser.add_argument('-s','--start',action='store_true')
args=parser.parse_args()

print("The arguments ar as follows :\n",args)
