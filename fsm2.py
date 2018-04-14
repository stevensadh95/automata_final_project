class State(object):
    "define state objects - will contain current words in sentence"
    def __init__(self, bag):
        self.bag = bag
        print('Processing current state:', str(self))

    def on_event(self, event):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__



class StartState(State):

    def on_event(self, event):
        # print(self.bag)
        if self.bag[0] in event['<start>'] and self.bag[0][0].isupper():
            if len(self.bag) > 0:
                return ObjectState(self.bag[1:])

        return self

class ObjectState(State):

    def on_event(self, event):
        # print(self.bag)
        if self.bag[0] in event['<object>']:
            if len(self.bag) > 0:
                return VerbState(self.bag[1:])

        return self

class VerbState(State):

    def on_event(self, event):
        # print(self.bag)
        if self.bag[0] in event['<verb>']:
            return AdverbState(self.bag[1:])
        else:
            return FinalState(self.bag[1:])
        return self

class AdverbState(State):

    def on_event(self, event):
        # print(self.bag)
        if self.bag[0] in event['<adverb>']:
            return TransitState(self.bag[1:])
        return self


class TransitState(State):

    def on_event(self, event):
        # print(self.bag)
        if self.bag[0] in event['<adverb>']:
            return AdverbState(self.bag[1:])

        elif self.bag[0] in event['<verb>']:
            return VerbState(self.bag[1:])

        elif self.bag[0] in event['<object>']:
            return ObjectState(self.bag[1:])
        else:
            return FinalState(self.bag[1:])
        return self

class FinalState(State):

    def on_event(self, event):
        return self


class Sentence(object):
    "sentence object"


    def __init__(self, bag):

        self.state = StartState(bag)

    def on_event(self, event):
        self.state = self.state.on_event(event)















