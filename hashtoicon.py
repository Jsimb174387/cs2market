import json

def getIcon(markethash):
    # Opens item_data, which takes in a markethashname and returns the steam image link
    item_data = None
    with open('items.json', 'r', encoding="utf8") as openfile:
        # Reading from json file
        item_data = json.load(openfile)
    return item_data[markethash]


def getmanyIcons(hashList, size = 200):
    # similar to above but more performant for multiple hashes.
    item_data = None
    urlList = []
    with open('items.json', 'r', encoding="utf8") as openfile:
        # Reading from json file
        item_data = json.load(openfile)
    for item in hashList:
        gain = '${:,.2f}'.format(item[1][2] - item[1][1])
        urlList.append([item_data[item[0]][0] + f"/{size}fx{size}f", item[0], item[1], gain])
    return urlList
