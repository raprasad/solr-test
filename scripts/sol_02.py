from __future__ import print_function
from msg_util import *
import pysolr
from solr_search_formatter import SolrSearchFormatter

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)

#qstr = 'title:dreamcatcher'
#qstr = 'authorName:Stephen King AND title:dream*'
#qstr = 'authorName:"shining"'
qstr = '(Stephen King) AND (dream*)'
qstr = 'dream'
qstr = '*'
searchFormatter = SolrSearchFormatter()

results = solr.search(qstr, **searchFormatter.get_solr_kwargs())
xresults = solr.search(qstr, **{
            'start':0,      # result offset
            'rows': 1,      # num results
            #'stats' : 'true',
            #'stats.field' : ['dvtype', 'subject_ss'],
            'debug': 'true',
            'hl': 'true',
            'hl.fragsize': 50,
            'hl.fl' : ['title','authorName', 'dsDescription', 'publicationCitation', 'authorName_ss'],
            'hl.simple.pre' : '<span class="slr_fnd">',
            'hl.simple.post' : '</span>',
            'facet': 'on',
            #'facet.field': 'dvtype',
            'facet.field': ['dvtype'\
                        ,'published_ss'\
                        , 'affiliation_ss'\
                        , 'authorName_ss'\
                        , 'subject_ss'\
                        , 'authorName'\
                        , 'producerName_ss'\
                        ],\
            'sort' : ['id desc', 'dsDescription desc'],\
            #'fq' : [ 'dvtype:(asets OR files)'],\
            'fq' : [ 'dvtype:(dataverses OR datasets OR files)'],\
            #'fq' : ['dvtype:(dataverses OR datasets)', '{!join from=groups_s to=perms_ss}id:group_public']
            #'fq': 'authorName:*King',
            #'spellcheck': 'true',
            #'spellcheck.collate': 'true',
            #'spellcheck.count': 1,
            # TODO: Can't get these working in my test setup.
            # 'group': 'true',
            # 'group.field': 'id',
        })
print ('docs', results.docs)
print ('-' * 60)
msgt('facets')#, results.facets)
if len(results.facets) > 0:
    for kval, val_dict in results.facets.items():
        for k, v in val_dict.items():
            msg ("\n%s: %s" % (k, v))
dashes()
print ('grouped', results.grouped)
print ('-' * 60)
print ('hits', results.hits)
print ('-' * 60)
print ('stats', results.stats)
print ('-' * 60)
print ('spellcheck', results.spellcheck)
print ('-' * 60)
print ('qtime', results.qtime)
print ('-' * 60)
#print (dir(results))
print ('-' * 60)
print ('docs', len(results.docs))
msgt('highlighting')
if len(results.highlighting) > 0:
    for kval, val_dict in results.highlighting.items():
        for k, v in val_dict.items():
            print ("%s: %s" % (k, v))
#msg(results.highlighting)
dashes()

cnt = 0
for doc in results.docs:
    cnt +=1
    #info_str = '%s, %s' % (doc['title'], doc['authorName_ss'])
    info_str = doc.get('publicationCitation', 'not found')
    if type(info_str) is list:
        info_str = info_str[0]
    print ('(%s) %s' % (cnt, info_str))
print ('-'*40)
keys = doc.keys()
keys.sort()
for k in keys:
    print ("%s: %s" % (k,doc[k]))
dashes()
msg(dir(results))
dashes()
msg(results.highlighting)
#print (doc)

#print ('docs', results.docs)

