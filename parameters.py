from collections import namedtuple

Transition = namedtuple(typename='Transition', field_names=['source', 'event', 'target'])
states = {'p1', 'p2', 'p3', 'p4', 'p5', 'p6'}
init = 'p1'
events = {'a', 'b', 'c'}
trans = {Transition(source='p1', event='a', target='p2'),
         Transition(source='p1', event='b', target='p3'),
         Transition(source='p2', event='a', target="p2"),
         Transition(source='p2', event='b', target='p4'),
         Transition(source='p3', event='a', target='p4'),
         Transition(source='p4', event='b', target='p5'),
         Transition(source='p5', event='a', target='p4'),
         Transition(source='p5', event='b', target='p4'),
         Transition(source='p6', event='b', target='p3')}
marked = 'p5'
