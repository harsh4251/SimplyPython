import re
regexpSubj = re.compile(r'subj')
regexpObj = re.compile(r'obj')
regexNouns = re.compile("^N.*|^PR.*")
root = dep.root["word"]

# A random selection of sentences with different styles, domains etc
sentences = ["He watched the dark eyeslits narrowing with greed till her eyes were green stones",
             "When will the Oracle 12.2 database be released?",
             "Coherence is an in-memory grid cluster for Java code",
             "Oracle 12.2 will be released in March 2017",
             "PyData community gathers to discuss how best to apply languages and tools to continuously evolving challenges in data management, processing, analytics, and visualization.",
             "Arsenal are a football team in North London",
             "When will Arsenal ever win a match?"]

def get_compounds(triples, word):
    compound = []
    for t in triples:
        if t[0][0] == word:
            if regexNouns.search(t[2][1]):
                compound.append(t[2][0])
    return compound

for sentence in sentences:
    
    result = dependency_parser.raw_parse(sentence)
    dep = next(result)
    root = [dep.root["word"]]
    root.append(get_compounds(dep.triples(), root))
    subj = []
    obj = []
    
    for t in dep.triples():
        if regexpSubj.search(t[1]):
            subj.append(t[2][0])
            subj.append(get_compounds(dep.triples(),t[2][0]))
        if regexpObj.search(t[1]):
            obj.append(t[2][0])
            obj.append(get_compounds(dep.triples(),t[2][0]))
    print("\n",sentence)
    print("Subject:",subj, "\nTopic:", root, "\nObject:",obj)
