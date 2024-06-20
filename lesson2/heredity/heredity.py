import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]

def personGenes(person, one_gene ,two_genes):
    #returns number of GIB2 in person
    person_genes = 0

    if person in one_gene:
        person_genes=1
    
    elif person in two_genes:
        person_genes=2
    
    return person_genes

def inheritance(parent, one_gene, two_genes):
    #probability for parent to transmit a GIB2
    parent_genes=personGenes(parent, one_gene,two_genes)
    
    if parent_genes == 1:
        return 0.5
    
    elif parent_genes ==2:
        return 1 - PROBS["mutation"]
    
    else:
        return PROBS["mutation"]

def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    probability_people=1

    for person in people.keys():
        probability_person=1

        mother = people[person]['mother']
        father = people[person]['father']
        parents = [mother, father]

        person_genes=personGenes(person, one_gene, two_genes)
        
        if not mother and not father:
            probability_person *= PROBS["gene"][person_genes]
        
        elif mother and father:
            if person_genes != 1:
                for parent in parents:
                    if person_genes == 2:
                        probability_person *= inheritance(parent, one_gene, two_genes)
                
                    if person_genes == 0:
                        probability_person *= 1-inheritance(parent, one_gene, two_genes)
            
            else:
                probability_person *= (inheritance(mother, one_gene, two_genes) + inheritance(father, one_gene,two_genes))

        if person in have_trait:
            trait = True
        else:
            trait = False

        probability_person *= PROBS["trait"][person_genes][trait]

        probability_people *= probability_person

    return probability_people

                    
                


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities.keys():
        gene = personGenes(person, one_gene, two_genes)
        probabilities[person]["gene"][gene] += p
        if person in have_trait:
            trait = True
        else:
            trait = False
        probabilities[person]["trait"][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities.keys():
        normalization_trait=sum(list(probabilities[person]["trait"].values()))
        normalization_genes=sum(list(probabilities[person]["gene"].values()))

        for i in probabilities[person]["trait"].keys():
            probabilities[person]["trait"][i] /= normalization_trait

        for i in probabilities[person]["gene"].keys():
            probabilities[person]["gene"][i] /= normalization_genes



if __name__ == "__main__":
    main()
