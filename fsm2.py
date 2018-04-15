class State(object):
    "define state objects - will contain current words in sentence"
    def __init__(self, bag):
        print('Current State:', str(self))
        self.bag = bag

    def on_input(self, event):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__



class StartState(State):

    def on_input(self, event):
  
        if self.bag[event] and event[0]:
            if 'PRONOUN' in self.bag[event].upper():
                print('(<Subject>:  {})'.format(event))
                return TransitState(self.bag)
            if 'NOUN' in self.bag[event].upper():
                print('(<Subject>:  {})'.format(event))
                return SubjectState(self.bag)
            if 'VERB' in self.bag[event].upper():
                print('(<Subject>:  {})'.format(event))
                return TransitState(self.bag)

        return self

class SubjectState(State):

    def on_input(self, event):
        if 'VERB' in self.bag[event].upper():
            print('(<Verb>: {})'.format(event))
            return VerbState(self.bag)
        elif 'ADJECTIVE' in self.bag[event].upper():
            print('(<Adjective>: {})'.format(event))
            return TransitState(self.bag)
        elif 'PUNCTUATION' in self.bag[event].upper():
            print('(<Punctuation>: {})'.format(event))
            return TransitState(self.bag)
        return self

class VerbState(State):

    def on_input(self, event):
        if 'ADVERB' in self.bag[event].upper():
            print('(<Adverb>: {})'.format(event))
            return AdverbState(self.bag)
        if 'NOUN' in self.bag[event].upper():
            print('(<Object>: {})'.format(event))
            return SubjectState(self.bag)
        elif 'ADJECTIVE' in self.bag[event].upper():
            print('(<Adjective>: {})'.format(event))
            return TransitState(self.bag)
        elif 'PUNCTUATION' in self.bag[event].upper():
            print('(<Punctuation>: {})'.format(event))
            return TransitState(self.bag)
        elif 'CONJUNCTION' in self.bag[event].upper():
            print('(<Conjunction>: {})'.format(event))
            return TransitState(self.bag)

class ConjuctionState(State):

    def on_input(self, event):
        if 'NOUN' in self.bag[event].upper():
            print('(<Object>: {})'.format(event))
            return SubjectState(self.bag)
        elif 'ADJECTIVE' in self.bag[event].upper():
            print('(<Adjective>: {})'.format(event))
            return TransitState(self.bag)
        elif 'PUNCTUATION' in self.bag[event].upper():
            print('(<Punctuation>: {})'.format(event))
            return TransitState(self.bag)
        elif 'VERB' in self.bag[event].upper():
            print('(<Verb>: {})'.format(event))
            return VerbState(self.bag)

class AdverbState(State):

    def on_input(self, event):
        if 'NOUN' in self.bag[event].upper():
            print('(<Object>:  {})'.format(event))
            return TransitState(self.bag)
        elif 'PUNCTUATION' in self.bag[event].upper():
            print('(<Punctuation>: {})'.format(event))
            return TransitState(self.bag)
        elif 'PREPOSITION' in self.bag[event].upper():
            print('(<Preposition>: {})'.format(event))
            return TransitState(self.bag)

class TransitState(State):

    def on_input(self, event):
        if 'NOUN' in self.bag[event].upper():
            print('(<Object>: {})'.format(event))
            return SubjectState(self.bag)
        elif 'ADJECTIVE' in self.bag[event].upper():
            print('(<Adjective>: {})'.format(event))
            return TransitState(self.bag)
        elif 'PUNCTUATION' in self.bag[event].upper():
            print('(<Punctuation>: {})'.format(event))
            return TransitState(self.bag)
        elif 'VERB' in self.bag[event].upper():
            print('(<Verb>: {})'.format(event))
            return VerbState(self.bag)
        elif 'CONJUNCTION' in self.bag[event].upper():
            print('(<Conjunction>: {})'.format(event))
            return VerbState(self.bag)
        elif 'PREPOSITION' in self.bag[event].upper():
            print('(<Preposition>: {})'.format(event))
            return SubjectState(self.bag)
        elif event == 'BlQWdW':
            print('Valid sentence')
            return FinalState(self.bag)

class FinalState(State):

    def on_input(self, event):
        return self


class Sentence(object):
    "sentence object"


    def __init__(self, bag):

        self.state = StartState(bag)

    def on_input(self, event):
        self.state = self.state.on_input(event)















