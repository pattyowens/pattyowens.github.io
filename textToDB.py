# textToDB.py
import pandas as pd

proj_dest = 'C:\\Users\\Patrick\\PycharmProjects\\CPI_Calculator'
item_list_dest = proj_dest + '\\Item List.txt'


file = open(item_list_dest)
items = file.readlines()

df = pd.read_csv(item_list_dest, sep='\t',)


def appendDict(header, row):
    newDict = {}
    ix = 0
    for val in header:
        newDict.update({val: row[ix]})
        ix += 1
    newDict.update({'subItems': []})
    return newDict

df1=df.sort_values(by='sort_sequence')

def recurFindSub(base, header, val, level, jx):
    if jx == level:
        base["subItems"].append(appendDict(header, val))
    else:
        recurFindSub(base["subItems"][len(base["subItems"])-1], header, val, level, jx+1)
    return base

header = items[0].strip('\n').split('\t')
dict = {
    "items": []
}
ix = -1
level = 0
for val in df1.values:
    prevLevel = level
    level = int(val[2])
    if level == 0:
        ix += 1
        dict["items"].append(appendDict(header, val))
    elif level != 0:
        base = dict["items"][ix]
        dict["items"][ix] = recurFindSub(base, header, val, level, 1)

