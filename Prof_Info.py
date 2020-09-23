from scholarly import scholarly

def return_pub_name(var):
    dd = var.replace("\'", "\"")
    if dd.find('year') == -1:
        var = dd[dd.find('title')+8:dd.find('filled')-5]
    else:
        var = dd[dd.find('title')+8:dd.find('year')-12]
    var = var.split('  ')
    return var[0][1:-3]+' '+var[-1][1:-1]

def return_author(pub):
    author = []
    for i in pub:
        var = str(i)
        cites = var[var.find('cites')+9:var.find('cites')+12]
        if cites[-1] == "'" or cites[-1] == ",":
            if cites[-2] == "'":
                cites = cites[0].rstrip('\n')
            else:
                cites = cites[0:-1].rstrip('\n')
        publication = return_pub_name(var)
        yr = var.find('year')

        if yr == -1 or var[yr+8:yr+12].isnumeric() == False:
            year = '1000'
        else:
            year = var[yr+8:yr+12].rstrip('\n')

        author.append({'Cites':int(cites),'Publication':publication,'Year':int(year)})

    author = sorted(author, key=lambda k: (k['Year'],k['Cites']),reverse=True)
    return author



names = input()
names = names.split(',')
for i in names: 
    author = scholarly.search_author(i)
    author = next(author,None)
    if author is None:
        continue

    print(author.name)
    print(author.affiliation)
    print(author.interests)
    print('====================')
    pub = author.fill(sections=['publications']).publications
    info = return_author(pub)

    for i in info[0:30]:
        print('Paper Name: ',i['Publication'])
        print('Year: ',i['Year'])
        print('Citation',i['Cites'])
        print('\n')
    print('===========================================')