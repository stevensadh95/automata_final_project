import re, os
from random import randint
from random import choice as c
from fsm2 import Sentence
from word_check import word_type as part

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

    for prod in production_list:
        nonterminal = prod[0].strip()
        other_terms = []
        for x in prod:
            words2 =[]
            if x != nonterminal:
                words = re.findall(r"\s*([^\s\n]*)\s*", x.strip())
                # words2 += words
                # for word in words:
                #     if word:
                other_terms.append(words)
        prod_dict[nonterminal] = other_terms

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
        if non_term in [".", "?", "!", ",", ":", "-"]:
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

def clear_whitespace(s):
    wsRegex = re.compile(r'\s+')
    return wsRegex.sub(' ', s)


def create_symbol_table(sentence):
    table = {}
    print('Creating Symbol Table')
    for word in sentence:
        if 'BlQWdW' in word:
            table[word] = 'end'
            continue

        if clear_whitespace(word) != '':
            if word in [".", "?", "!", ",", ":", "-"]:
                table[word] = 'PUNCTUATION'
            elif word[0].isdigit():
                table[word] = 'NUMBER'
            else:
                if 'THE' == word.upper():
                    table[word] = 'PRONOUN'
                    continue
                if word not in table.keys():
                    table[word] = part(clear_whitespace(word.lower()))   
    # table = {'The': 'Pronoun',
    #         'waves': 'Noun',
    #         'die': 'Verb',
    #         'grumpily': 'Adverb',
    #         'tonight': 'Noun',
    #         '.': 'Punctuation',
    #         'BlQWdW': 'end_marker' }

    return table


def get_file():
    files = os.listdir('grammar')
    while True:
        try:
            in_file = c(files)
            in_file = 'Poem.g'
            rules = read_production_rules(os.path.join('grammar',in_file))
            grammar = []

            for i in rules:
                grammar.append(split_definition(i))


            grammar_dict = grammar_to_dict(grammar)
            s = clear_whitespace(evaluate_grammar(grammar_dict))
            return s, in_file, grammar_dict
        except:
            pass
def main():
    
    print('----------------------------------')
    print('Welcome to Grammar/Lexicon Central')
    print('')
    print('----------------------------------')
    while True: 
        s, in_file, grammar_dict = get_file()

        choice = input('Please select an option:\n1. Random Sentence from grammar\n2. FSM sentence checker + tokenizer\nAny key to quit\n')
        if choice == '1':
            print('Grammar input: {}'.format(in_file))
            
            print('Sentence: {}\n'.format(s))
        elif choice == '2':
 
            end = ' BlQWdW'
            # some default test cases
            # s = 'they eats pie?'
            # s = 'The waves die grumpily tonight.'               #example of incorrect symbol table
            # s = 'they read piano'


            s = clear_whitespace(evaluate_grammar(grammar_dict))
            # s = 'The quick, brown fox jumps over the lazy dog.'

            input_str = re.findall(r"[\w']+|[.,!?;:]",(s+end))
            symbols = create_symbol_table(input_str)

            print('Symbol Table\n')
            for i in symbols.items():print(i)

            print('\n1Tokenizing with FSM')
            s1 = Sentence(symbols)
            for word in input_str:
                try:
                    s1.on_input(word)
                except AttributeError as e:
                    print('\nNO new state acquired. FAIL!')
                    break
        else:
            print('Quiting...')
            exit()


if __name__ == '__main__':
    main()







