from __future__ import print_function
import pysolr

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)

#solrquery = "(.................. )" 
#solr.search([solrquery],facet = 'on' ,** {'facet.field' : ['fieldname']})

results = solr.search('*')

results = solr.search('shape', **{
    'hl': 'true',
    'hl.fragsize': 10,
})
print("Saw {0} result(s).".format(len(results)))
print(results.highlighting)

for result in results:
    print ('-'*50)
    #print(result.id)
    #print(result.highlighting)
    #print (results.highlighting[result]['id'].get('id', {}).get('content', 'n/a'))

    #continue
    keys = result.keys()
    keys.sort()
    for k in keys:
        print('%s : %s' % (k, result[k]))
    #print (result.k)
    #print(type(result))
    #print(result)
    #print("The title is '{0}'.".format(result['title']))
print ('-'*50)
    