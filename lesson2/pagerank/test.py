from pagerank import *

#print(transition_model(crawl("corpus2"), "recursion.html", 0))


dictest=crawl("corpus2")
test=transition_model(dictest,"ai.html",DAMPING)
#print(test)
#print(sum(test.values()))
testsample=sample_pagerank(dictest,DAMPING,100000)
#print(testsample)
#print(sum(testsample.values()))
links=dict()
for link in dictest.keys():
        links.update({link : 1/len(dictest)})
print(links)


iterate_pagerank(dictest,DAMPING)