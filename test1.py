from parameters import Transition, states, init, events, trans, marked

class Automaton(object):
    def __init__(self, states, init, events, trans, marked = None, forbidden = None):
        self.states = states
        self.init = init
        self.events = events
        self.trans = trans
        self.marked = marked if marked else set()
        self.forbidden = forbidden if forbidden else set()

    def __str__(self):
        return 'states: \n\t{}\n' \
                'init: \n\t{}\n' \
                'events: \n\t{}\n' \
                'trans: \n\t{}\n' \
                'marked: \n\t{}\n' \
                'forbidded: \n\t{}\n'.format(self.states, self.init, self.events, \
                '\n\t' .join([str(t) for t in self.trans]), self.marked, self.forbidden)

def main():

    '''trans = {Transition('p1', 'a', 'p2'),
             Transition('p2', 'b', 'p3'),
             Transition('p1', 'c', 'p3')}'''

    #transitions = filter_trans_by_source(trans, {'p2'})
    #assert transitions == {Transition('p2', 'b', 'p3')}, 'Got {} instead'.format(transitions)

    #transitions = filter_trans_by_source(trans, {'p1'})
    #assert transitions == {Transition('p1', 'a', 'p2'), Transition('p1', 'c', 'p3')}, 'Got {} instead'.format(transitions)

    p1 = Automaton(states, init, events, trans, marked)
    print(p1)
    reach_states = reach(trans,{'p2'})
    print(reach_states)

def reach(trans, start_states):
    reach_states = set()

    for x in trans:
        filtered_start_states = filter_trans_by_source(trans, start_states)
        reach_states = extract_elems_from_trans(filtered_start_states, 'target')
        start_states = reach_states

    return reach_states

def extract_elems_from_trans(trans, field):
    elems = set()

    for transition in trans:

        if field is 'source':
            elems.add(transition.source)
        elif field is 'event':
            elems.add(transition.event)
        elif field is 'target':
            elems.add(transition.target)

    return elems

def filter_trans_by_source(trans, states_to_keep={''}):
    filter = set()

    for transition in trans:

        if transition[0] in states_to_keep:
            filter.add(transition)

    return filter

if __name__ == "__main__":
    main()
