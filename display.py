from node import *
from sys import argv
import pickle

if len(argv) < 2:
    print("Usage: python3 %s [flowchart file]" % argv[0])
    raise SystemExit()

def walkthrough(node):
    print(node.text)
    if type(node) is StopNode:
        return
    if type(node) is ConditionalNode:
        path = input("(Y/N) ")
        if path == "Y":
            walkthrough(node.yes)
        elif path == "N":
            walkthrough(node.no)
    elif node.next:
        input()
        walkthrough(node.next)
    else:
        raise Exception("Need to end flowchart with a stop node!!")


flowchart = pickle.load(open(argv[1], "rb"))
walkthrough(flowchart)