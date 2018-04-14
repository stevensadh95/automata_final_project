
import re
from random import randint, choice
from fsm2 import Sentence

def read_production_rules(filename):
    #filename = 'grammars/' + filename
    contents = open(filename, 'r')
    grammar = contents.read()

    productions = re.findall(r'\{([^\}]*)\}', grammar,flags=re.DOTALL)
    return productions



def split_definition(raw_production):
   raw_production = raw_production.strip().replace("\t","")
   production_rules = raw_production.replace(";","").split("\n")

   return production_rules

def grammar_to_dict(production_list):
    prod_dict = {}
    global prod_dict2
    prod_dict2 = {}
    for prod in production_list:
        nonterminal = prod[0]
        other_terms = []
        other_terms2 = []
        for x in prod:
            if x != nonterminal:
                words = re.findall(r"\s*([^\s\n]*)\s*", x.strip())
                
                other_terms.append(words)
                other_terms2+=words
        prod_dict[nonterminal] = other_terms
        prod_dict2[nonterminal] =other_terms2

    return prod_dict

def is_non_terminal(term):

    x= re.findall(r"<([^>])*>",term)
    return x

def evaluate_grammar(grammar_dict, non_term="<start>"):
    sentence = ""

    if isinstance(non_term, list):
        for item in non_term:
            sentence+= evaluate_grammar(grammar_dict,item)
        return sentence
    if not is_non_terminal(non_term):
        if non_term == "." or non_term == "?" or non_term == "!" or non_term == "," or non_term == ":" or non_term == "-":
            return non_term
        else:
            return " " + non_term

    elif non_term =="<start>":
        my_list = grammar_dict[non_term]
        for rule in my_list:
            for variable in rule:
                sentence+= evaluate_grammar(grammar_dict, variable)

        return sentence

    else:
        my_list = grammar_dict[non_term]

        if not my_list:
            raise Exception("Undefined production rule: {}".format(non_term))

        return evaluate_grammar(grammar_dict,my_list[randint(0,len(my_list)-1)])


def remove_extra_spaces(sentence):
    return re.sub("\s\s+"," ",sentence)




prod_dict2 = {}
rules = read_production_rules("Poem.g")
grammar = []

for i in rules:
    grammar.append(split_definition(i))

print('----------------------------------')
print('Evaluating grammar found in Poem')
print('i. Grammar is parsed\nii. Production rules executed to create sentences\niii. Sentence passed through FSM to check if valid')
print('----------------------------------')

for i in range(1,11):
    s = remove_extra_spaces(evaluate_grammar(grammar_to_dict(grammar)))
    print('\n{}. {}'.format(i,s))
    s1 = Sentence(s.split())
    for j in range(len(s.split())):
        s1.on_event(prod_dict2)







