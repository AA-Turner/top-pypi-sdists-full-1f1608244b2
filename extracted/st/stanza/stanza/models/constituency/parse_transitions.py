"""
Defines a series of transitions (open a constituent, close a constituent, etc

Also defines a State which holds the various data needed to build
a parse tree out of tagged words.
"""

from abc import ABC, abstractmethod
import ast
from collections import defaultdict
from enum import Enum
import functools
import logging

from stanza.models.constituency.parse_tree import Tree

logger = logging.getLogger('stanza')

class TransitionScheme(Enum):
    def __new__(cls, value, short_name):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.short_name = short_name
        return obj


    # top down, so the open transition comes before any constituents
    # score on vi_vlsp22 with 5 different sizes of bert layers,
    # bert tagger, no silver dataset:
    #   0.8171
    TOP_DOWN           = 1, "top"
    # unary transitions are modeled as one entire transition
    # version that uses one transform per item,
    # score on experiment described above:
    #   0.8157
    # score using one combination step for an entire transition:
    #   0.8178
    TOP_DOWN_COMPOUND  = 2, "topc"
    # unary is a separate transition.  doesn't help
    # score on experiment described above:
    #   0.8128
    TOP_DOWN_UNARY     = 3, "topu"

    # open transition comes after the first constituent it cares about
    # score on experiment described above:
    #   0.8205
    # note that this is with an oracle, whereas IN_ORDER_COMPOUND does
    # not have a dynamic oracle, so there may be room for improvement
    IN_ORDER           = 4, "in"

    # in order, with unaries after preterminals represented as a single
    # transition after the preterminal
    # and unaries elsewhere tied to the rest of the constituent
    # score: 0.8186
    IN_ORDER_COMPOUND  = 5, "inc"

    # in order, with CompoundUnary on both preterminals and internal nodes
    # score: 0.8166
    IN_ORDER_UNARY     = 6, "inu"

@functools.total_ordering
class Transition(ABC):
    """
    model is passed in as a dependency injection
    for example, an LSTM model can update hidden & output vectors when transitioning
    """
    @abstractmethod
    def update_state(self, state, model):
        """
        update the word queue position, possibly remove old pieces from the constituents state, and return the new constituent

        the return value should be a tuple:
          updated word_position
          updated constituents
          new constituent to put on the queue and None
            - note that the constituent shouldn't be on the queue yet
              that allows putting it on as a batch operation, which
              saves a significant amount of time in an LSTM, for example
          OR
          data used to make a new constituent and the method used
            - for example, CloseConstituent can return the children needed
              and itself.  this allows a batch operation to build
              the constituent
        """

    def delta_opens(self):
        return 0

    def apply(self, state, model):
        """
        return a new State transformed via this transition

        convenience method to call bulk_apply, which is significantly
        faster than single operations for an NN based model
        """
        update = model.bulk_apply([state], [self])
        return update[0]

    @abstractmethod
    def is_legal(self, state, model):
        """
        assess whether or not this transition is legal in this state

        at parse time, the parser might choose a transition which cannot be made
        """

    def components(self):
        """
        Return a list of transitions which could theoretically make up this transition

        For example, an Open transition with multiple labels would
        return a list of Opens with those labels
        """
        return [self]

    @abstractmethod
    def short_name(self):
        """
        A short name to identify this transition
        """

    def short_label(self):
        if not hasattr(self, "label"):
            return self.short_name()

        if isinstance(self.label, str):
            label = self.label
        elif len(self.label) == 1:
            label = self.label[0]
        else:
            label = self.label
        return "{}({})".format(self.short_name(), label)

    def __lt__(self, other):
        # put the Shift at the front of a list, and otherwise sort alphabetically
        if self == other:
            return False
        if isinstance(self, Shift):
            return True
        if isinstance(other, Shift):
            return False
        return str(self) < str(other)


    @staticmethod
    def from_repr(desc):
        """
        This method is to avoid using eval() or otherwise trying to
        deserialize strings in a possibly untrusted manner when
        loading from a checkpoint
        """
        if desc == 'Shift':
            return Shift()
        if desc == 'CloseConstituent':
            return CloseConstituent()
        labels = desc.split("(", maxsplit=1)
        if labels[0] not in ('CompoundUnary', 'OpenConstituent', 'Finalize'):
            raise ValueError("Unknown Transition %s" % desc)
        if len(labels) == 1:
            raise ValueError("Unexpected Transition repr, %s needs labels" % labels[0])
        if labels[1][-1] != ')':
            raise ValueError("Expected Transition repr for %s: %s(labels)" % (labels[0], labels[0]))
        trans_type = labels[0]
        labels = labels[1][:-1]
        labels = ast.literal_eval(labels)
        if trans_type == 'CompoundUnary':
            return CompoundUnary(*labels)
        if trans_type == 'OpenConstituent':
            return OpenConstituent(*labels)
        if trans_type == 'Finalize':
            return Finalize(*labels)
        raise ValueError("Unexpected Transition %s" % desc)

class Shift(Transition):
    def update_state(self, state, model):
        """
        This will handle all aspects of a shift transition

        - push the top element of the word queue onto constituents
        - pop the top element of the word queue
        """
        new_constituent = model.transform_word_to_constituent(state)
        return state.word_position+1, state.constituents, new_constituent, None

    def is_legal(self, state, model):
        """
        Disallow shifting when the word queue is empty or there are no opens to eventually eat this word
        """
        if state.empty_word_queue():
            return False
        if model.is_top_down:
            # top down transition sequences cannot shift if there are currently no
            # Open transitions on the stack.  in such a case, the new constituent
            # will never be reduced
            if state.num_opens == 0:
                return False
            if state.num_opens == 1:
                # there must be at least one transition, since there is an open
                assert state.transitions.parent is not None
                if state.transitions.parent.parent is None:
                    # only one transition
                    trans = model.get_top_transition(state.transitions)
                    # must be an Open, since there is one open and one transitions
                    # note that an S, FRAG, etc could happen if we're using unary
                    # and ROOT-S is possible in the case of compound Open
                    # in both cases, Shift is legal
                    # Note that the corresponding problem of shifting after the ROOT-S
                    # has been closed to just ROOT is handled in CloseConstituent
                    if len(trans.label) == 1 and trans.top_label in model.root_labels:
                        # don't shift a word at the very start of a parse
                        # we want there to be an extra layer below ROOT
                        return False
        else:
            # in-order k==1 (the only other option currently)
            # can shift ONCE, but note that there is no way to consume
            # two items in a row if there is no Open on the stack.
            # As long as there is one or more open transitions,
            # everything can be eaten
            if state.num_opens == 0:
                if not state.empty_constituents:
                    return False
        return True

    def short_name(self):
        return "Shift"

    def __repr__(self):
        return "Shift"

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, Shift):
            return True
        return False

    def __hash__(self):
        return hash(37)

class CompoundUnary(Transition):
    def __init__(self, *label):
        # the FIRST label will be the top of the tree
        # so CompoundUnary that results in root will have root as labels[0], for example
        self.label = tuple(label)

    def update_state(self, state, model):
        """
        Apply potentially multiple unary transitions to the same preterminal

        It reuses the CloseConstituent machinery
        """
        # only the top constituent is meaningful here
        constituents = state.constituents
        children = [constituents.value]
        constituents = constituents.pop()
        # unlike with CloseConstituent, our label is not on the stack.
        # it is just our label
        # ... but we do reuse CloseConstituent's update mechanism
        return state.word_position, constituents, (self.label, children), CloseConstituent

    def is_legal(self, state, model):
        """
        Disallow consecutive CompoundUnary transitions, force final transition to go to ROOT
        """
        # can't unary transition nothing
        tree = model.get_top_constituent(state.constituents)
        if tree is None:
            return False
        # don't unary transition a dummy, dummy
        # and don't stack CompoundUnary transitions
        if isinstance(model.get_top_transition(state.transitions), (CompoundUnary, OpenConstituent)):
            return False
        # if we are doing IN_ORDER_COMPOUND, then we are only using these
        # transitions to model changes from a tag node to a sequence of
        # unary nodes.  can only occur at preterminals
        if model.transition_scheme() is TransitionScheme.IN_ORDER_COMPOUND:
            return tree.is_preterminal()
        if model.transition_scheme() is not TransitionScheme.TOP_DOWN_UNARY:
            return True

        is_root = self.label[0] in model.root_labels
        if not state.empty_word_queue() or not state.has_one_constituent():
            return not is_root
        else:
            return is_root

    def components(self):
        return [CompoundUnary(label) for label in self.label]

    def short_name(self):
        return "Unary"

    def __repr__(self):
        return "CompoundUnary(%s)" % ",".join(self.label)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, CompoundUnary):
            return False
        if self.label == other.label:
            return True
        return False

    def __hash__(self):
        return hash(self.label)

class Dummy():
    """
    Takes a space on the constituent stack to represent where an Open transition occurred
    """
    def __init__(self, label):
        self.label = label

    def is_preterminal(self):
        return False

    def __format__(self, spec):
        if spec is None or spec == '' or spec == 'O':
            return "(%s ...)" % self.label
        if spec == 'T':
            return "\Tree [.%s ? ]" % self.label
        raise ValueError("Unhandled spec: %s" % spec)

    def __str__(self):
        return "Dummy({})".format(self.label)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Dummy):
            return False
        if self.label == other.label:
            return True
        return False

    def __hash__(self):
        return hash(self.label)

def too_many_unary_nodes(tree, unary_limit):
    """
    Return True iff there are UNARY_LIMIT unary nodes in a tree in a row

    helps prevent infinite open/close patterns
    otherwise, the model can get stuck in essentially an infinite loop
    """
    if tree is None:
        return False
    for _ in range(unary_limit + 1):
        if len(tree.children) != 1:
            return False
        tree = tree.children[0]
    return True

class OpenConstituent(Transition):
    def __init__(self, *label):
        self.label = tuple(label)
        self.top_label = self.label[0]

    def delta_opens(self):
        return 1

    def update_state(self, state, model):
        # open a new constituent which can later be closed
        # puts a DUMMY constituent on the stack to mark where the constituents end
        return state.word_position, state.constituents, model.dummy_constituent(Dummy(self.label)), None

    def is_legal(self, state, model):
        """
        disallow based on the length of the sentence
        """
        if state.num_opens > state.sentence_length + 10:
            # fudge a bit so we don't miss root nodes etc in very small trees
            # also there's one really deep tree in CTB 9.0
            return False
        if model.is_top_down:
            # If the model is top down, you can't Open if there are
            # no words to eventually eat
            if state.empty_word_queue():
                return False
            # Also, you can only Open a ROOT iff it is at the root position
            # The assumption in the unary scheme is there will be no
            # root open transitions
            if not model.has_unary_transitions():
                # TODO: maybe cache this value if this is an expensive operation
                is_root = self.top_label in model.root_labels
                if is_root:
                    return state.empty_transitions()
                else:
                    return not state.empty_transitions()
        else:
            # in-order nodes can Open as long as there is at least one thing
            # on the constituency stack
            # since closing the in-order involves removing one more
            # item before the open, and it can close at any time
            # (a close immediately after the open represents a unary)
            if state.empty_constituents:
                return False
            if isinstance(model.get_top_transition(state.transitions), OpenConstituent):
                # consecutive Opens don't make sense in the context of in-order
                return False
            if not model.transition_scheme() is TransitionScheme.IN_ORDER:
                # eg, IN_ORDER_UNARY or IN_ORDER_COMPOUND
                # if compound unary opens are used
                # or the unary transitions are via CompoundUnary
                # can always open as long as the word queue isn't empty
                # if the word queue is empty, only close is allowed
                return not state.empty_word_queue()
            # one other restriction - we assume all parse trees
            # start with (ROOT (first_real_con ...))
            # therefore ROOT can only occur via Open after everything
            # else has been pushed and processed
            # there are no further restrictions
            is_root = self.top_label in model.root_labels
            if is_root:
                # can't make a root node if it will be in the middle of the parse
                # can't make a root node if there's still words to eat
                # note that the second assumption wouldn't work,
                # except we are assuming there will never be multiple
                # nodes under one root
                return state.num_opens == 0 and state.empty_word_queue()
            else:
                if (state.num_opens > 0 or state.empty_word_queue()) and too_many_unary_nodes(model.get_top_constituent(state.constituents), model.unary_limit()):
                    # looks like we've been in a loop of lots of unary transitions
                    # note that we check `num_opens > 0` because otherwise we might wind up stuck
                    # in a state where the only legal transition is open, such as if the
                    # constituent stack is otherwise empty, but the open is illegal because
                    # it causes too many unaries
                    # in such a case we can forbid the corresponding close instead...
                    # if empty_word_queue, that means it is trying to make infinitiely many
                    # non-ROOT Open transitions instead of just transitioning ROOT
                    return False
                return True
        return True

    def components(self):
        return [OpenConstituent(label) for label in self.label]

    def short_name(self):
        return "Open"

    def __repr__(self):
        return "OpenConstituent({})".format(self.label)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, OpenConstituent):
            return False
        if self.label == other.label:
            return True
        return False

    def __hash__(self):
        return hash(self.label)

class Finalize(Transition):
    """
    Specifically applies at the end of a parse sequence to add a ROOT

    Seemed like the simplest way to remove ROOT from the
    in_order_compound transitions while still using the mechanism of
    the transitions to build the parse tree
    """
    def __init__(self, *label):
        self.label = tuple(label)

    def update_state(self, state, model):
        """
        Apply potentially multiple unary transitions to the same preterminal

        Only applies to preterminals
        It reuses the CloseConstituent machinery
        """
        # only the top constituent is meaningful here
        constituents = state.constituents
        children = [constituents.value]
        constituents = constituents.pop()
        # unlike with CloseConstituent, our label is not on the stack.
        # it is just our label
        label = self.label

        # ... but we do reuse CloseConstituent's update
        return state.word_position, constituents, (label, children), CloseConstituent

    def is_legal(self, state, model):
        """
        Legal if & only if there is one tree, no more words, and no ROOT yet
        """
        return state.empty_word_queue() and state.has_one_constituent() and not state.finished(model)

    def short_name(self):
        return "Finalize"

    def __repr__(self):
        return "Finalize(%s)" % ",".join(self.label)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Finalize):
            return False
        return other.label == self.label

    def __hash__(self):
        return hash((53, self.label))

class CloseConstituent(Transition):
    def delta_opens(self):
        return -1

    def update_state(self, state, model):
        # pop constituents until we are done
        children = []
        constituents = state.constituents
        while not isinstance(model.get_top_constituent(constituents), Dummy):
            # keep the entire value from the stack - the model may need
            # the whole thing to transform the children into a new node
            children.append(constituents.value)
            constituents = constituents.pop()
        # the Dummy has the label on it
        label = model.get_top_constituent(constituents).label
        # pop past the Dummy as well
        constituents = constituents.pop()
        if not model.is_top_down:
            # the alternative to TOP_DOWN_... is IN_ORDER
            # in which case we want to pop one more constituent
            children.append(constituents.value)
            constituents = constituents.pop()
        # the children are in the opposite order of what we expect
        children.reverse()

        return state.word_position, constituents, (label, children), CloseConstituent

    @staticmethod
    def build_constituents(model, data):
        """
        builds new constituents out of the incoming data

        data is a list of tuples: (label, children)
        the model will batch the build operation
        again, the purpose of this batching is to do multiple deep learning operations at once
        """
        labels, children_lists = map(list, zip(*data))
        new_constituents = model.build_constituents(labels, children_lists)
        return new_constituents


    def is_legal(self, state, model):
        """
        Disallow if there is no Open on the stack yet

        in TOP_DOWN, if the previous transition was the Open (nothing built yet)
        in IN_ORDER, previous transition does not matter, except for one small corner case
        """
        if state.num_opens <= 0:
            return False
        if model.is_top_down:
            if isinstance(model.get_top_transition(state.transitions), OpenConstituent):
                return False
            if state.num_opens <= 1 and not state.empty_word_queue():
                # don't close the last open until all words have been used
                return False
            if model.transition_scheme() == TransitionScheme.TOP_DOWN_COMPOUND:
                # when doing TOP_DOWN_COMPOUND, we assume all transitions
                # at the ROOT level have an S, SQ, FRAG, etc underneath
                # this is checked when the model is first trained
                if state.num_opens == 1 and not state.empty_word_queue():
                    return False
            elif not model.has_unary_transitions():
                # in fact, we have to leave the top level constituent
                # under the ROOT open if unary transitions are not possible
                if state.num_opens == 2 and not state.empty_word_queue():
                    return False
        elif model.transition_scheme() is TransitionScheme.IN_ORDER:
            if not isinstance(model.get_top_transition(state.transitions), OpenConstituent):
                # we're not stuck in a loop of unaries
                return True
            if state.num_opens > 1 or state.empty_word_queue():
                # in either of these cases, the corresponding Open should be eliminated
                # if we're stuck in a loop of unaries
                return True
            node = model.get_top_constituent(state.constituents.pop())
            if too_many_unary_nodes(node, model.unary_limit()):
                # at this point, we are in a situation where
                # - multiple unaries have happened in a row
                # - there is stuff on the word_queue, so a ROOT open isn't legal
                # - there's only one constituent on the stack, so the only legal
                #   option once there are no opens left will be an open
                # this means we'll be stuck having to open again if we do close
                # this node, so instead we make the Close illegal
                return False
        else:
            # model.transition_scheme() == TransitionScheme.IN_ORDER_COMPOUND or
            # model.transition_scheme() == TransitionScheme.IN_ORDER_UNARY:
            # in both of these cases, we cannot do open/close
            #   IN_ORDER_COMPOUND will use compound opens and preterminal unaries
            #   IN_ORDER_UNARY will use compound unaries
            # the only restriction here is that we can't close immediately after an open
            #   internal unaries are handled by the opens being compound
            #   preterminal unaries are handled with CompoundUnary
            if isinstance(model.get_top_transition(state.transitions), OpenConstituent):
                return False
        return True

    def short_name(self):
        return "Close"

    def __repr__(self):
        return "CloseConstituent"

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, CloseConstituent):
            return True
        return False

    def __hash__(self):
        return hash(93)

def check_transitions(train_transitions, other_transitions, treebank_name):
    """
    Check that all the transitions in the other dataset are known in the train set

    Weird nested unaries are warned rather than failed as long as the
    components are all known

    There is a tree in VLSP, for example, with three (!) nested NP nodes
    If this is an unknown compound transition, we won't possibly get it
    right when parsing, but at least we don't need to fail
    """
    unknown_transitions = set()
    for trans in other_transitions:
        if trans not in train_transitions:
            for component in trans.components():
                if component not in train_transitions:
                    raise RuntimeError("Found transition {} in the {} set which don't exist in the train set".format(trans, treebank_name))
            unknown_transitions.add(trans)
    if len(unknown_transitions) > 0:
        logger.warning("Found transitions where the components are all valid transitions, but the complete transition is unknown: %s", sorted(unknown_transitions))
