from markov_chain import MarkovGraph

bad_endings = ["a", "if", "the", "your", "but", "not", "and", "god"]
punctuation = [".", ",", "!", "?", ";", ":"]

def create_markov_chain(locale):
    filename = f"Messages_{locale}.txt"
    print(locale)
    markov_chain = MarkovGraph()
    message_doc = open(filename, "r", encoding="utf-8")
    doc_lines = message_doc.readlines()
    for line in doc_lines:
        cur_line = line.split()
        prev_word = ""
        for cur_word in cur_line:
            if cur_word[-1] in punctuation :
                cur_word = cur_word[:-1]
            markov_chain.add_link(prev_word.lower(), cur_word.lower())
            prev_word = cur_word
    return markov_chain

def produce_phrases(locale):
    phrase = ""
    chain = create_markov_chain(locale)
    count = 0
    anti_end = 10
    while((count != anti_end) and (chain.cur_state == "" or count != 0)):
        cur_word = chain.next_state()
        if cur_word == "":
            cur_word = chain.next_state()
        phrase += cur_word + " "
        if cur_word in bad_endings:
            anti_end += 2
        count += 1
    return phrase