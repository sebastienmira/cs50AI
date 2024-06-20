import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    if len(corpus[page])==0:
        prob=dict()
        for link in corpus.keys():
            prob.update({link : 1/len(corpus)})
        return prob

    else:
        probdict=dict()
        for link in corpus.keys():
            damped_surf = (1-damping_factor) * (1/len(corpus)) #if damped
            direct_surf = 0
            if link in corpus[page]:
                direct_surf = damping_factor * (1/len(corpus[page])) #if direct
            probdict.update({link : damped_surf + direct_surf})
        return probdict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    visited_links=dict()
    for i in corpus.keys():
        visited_links.update({i : 0})

    start=random.choice(list(corpus.keys()))
    current_link=start

    for i in range(n):
        transition = transition_model(corpus, current_link, damping_factor)
        current_link = random.choices(list(transition.keys()), list(transition.values()))[0]
        visited_links[current_link] += 1/n

    return visited_links


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    tolerance = 0.001

    pagerank=dict()
    
    for link in corpus.keys():
        pagerank.update({link : 1/len(corpus)})

    while True:

        variation = []
        for i in pagerank.values():
            variation.append(i)

        for link in corpus.keys():    
            weight = 0
            
            for linkedpage in corpus.keys():
                if len(corpus[linkedpage]) == 0:
                    weight += pagerank[linkedpage] / len(corpus)

                else:
                    if link in corpus[linkedpage]:
                        weight += pagerank[linkedpage]/len(corpus[linkedpage])


            pagerank[link] = (1-damping_factor)/len(corpus) + damping_factor * weight

        ctr = 0
        for i in range(len(variation)):
            variation[i] = abs(variation[i]-list(pagerank.values())[i])
            if variation[i] < tolerance:
                ctr += 1

        if ctr == len(variation):
            return pagerank



if __name__ == "__main__":
    main()
