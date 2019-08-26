from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-f", "--strcount", dest="strcount", help="count of last strings fetched from file")
args = parser.parse_args()

f = open('text.txt', 'r+')
for i in f.readlines()[-int(args.strcount):]:
    print(i)
