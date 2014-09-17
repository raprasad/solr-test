from __future__ import print_function
from msg_util import *
import pysolr
from solr_search_formatter import SolrSearchFormatter
from solr_results_handler import SolrResultsHandler

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)

#qstr = 'title:dreamcatcher'
#qstr = 'authorName:Stephen King AND title:dream*'
#qstr = 'authorName:"shining"'
qstr = '(Stephen King) AND (dream*)'
qstr = 'dream'
#qstr = '*'
searchFormatter = SolrSearchFormatter()

results = solr.search(qstr, **searchFormatter.get_solr_kwargs())

solr_results = SolrResultsHandler(results)

msgx(type(results))
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
#keys = doc.keys()
#keys.sort()
#for k in keys:
#   print ("%s: %s" % (k,doc[k]))
dashes()
#msg(dir(results))
dashes()
#msg(results.highlighting)
print (doc)

#print ('docs', results.docs)

