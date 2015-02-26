__author__ = 'Michael'
import shlex
from collections import namedtuple
import re
import Queue


class TheoremProver:
    def __init__(self):
        self.var_definitions = {}
        self.facts = {}
        self.rules_list = {}
        self.token_map = {'&': 'AND', '!': 'NOT', '|': 'OR',
                          '(': 'LPAR', ')': 'RPAR'}
        self.Token = namedtuple('Token', ['name', 'value'])
        self.token_precedence = {'&': [4, 3],
                                 '!': [6, 5],
                                 '|': [2, 1],
                                 '(': [0, 100],
                                 ')': [99, 0]}

    def create_new_variable(self, variable, value):
        self.var_definitions[variable] = value
        self.facts[variable] = 'false'

    def create_new_fact(self, variable, boolean):
        if variable in self.var_definitions:
            self.facts[variable] = boolean
        else:
            print 'Variable ' + variable + ' not defined yet. Use "Teach <VAR> = <STRING>" command to create a variable definition.'

    def create_new_rule(self, condition, consequence):
        # split_expr = re.findall('[\d.]+|[%s]' % ''.join(self.token_map), condition)
        split_expr = re.findall('[a-z]+|[A-Z]+|[%s]' % ''.join(self.token_map), condition)
        tokens = [self.Token(self.token_map.get(x, 'VAR'), x) for x in split_expr]
        for token in tokens:
            if getattr(token, 'name') == 'VAR':
                if not getattr(token, 'value') in self.var_definitions:
                    print 'var ' + getattr(token, 'value') + ' not defined'
                    return
        if not condition in self.rules_list.keys():
            self.rules_list[condition] = []
            self.rules_list[condition].append(consequence)
        else:
            self.rules_list[condition].append(consequence)

    def to_postfix(self, split_expression):
        result = Queue.Queue()
        operator_stack = []
        for thing in split_expression:
            if thing.isalpha():
                result.put(thing)
            elif len(operator_stack) == 0:
                operator_stack.append(thing)
            elif self.token_precedence[thing][1] > self.token_precedence[operator_stack[len(operator_stack) - 1]][0]:
                operator_stack.append(thing)
            else:
                while len(operator_stack) > 0 and self.token_precedence[thing][1] <= self.token_precedence[operator_stack[len(operator_stack) - 1]][0]:
                    popped = operator_stack.pop()
                    result.put(popped)
                operator_stack.append(thing)

        while len(operator_stack) > 0:
            popped = operator_stack.pop()
            result.put(popped)
        return result

    def learn(self):
        for rule in self.rules_list:
            split_expr = re.findall('[a-z]+|[A-Z]+|[%s]' % ''.join(self.token_map), rule)

            # convert tokens to postfix equation in the form of a queue
            result = self.to_postfix(split_expr)

            # evaluating the postfix equation
            value = []
            while not result.empty():
                abc = result.get()
                if abc.isalpha():
                    value.append(self.facts[abc])
                if abc == '!':
                    q = value.pop()
                    if q == 'true':
                        q = 'false'
                    elif q == 'false':
                        q = 'true'
                    value.append(q)
                if abc == '&':
                    q = value.pop()
                    w = value.pop()
                    if q == 'true' and w == 'true':
                        value.append('true')
                    else:
                        value.append('false')
                if abc == '|':
                    q = value.pop()
                    w = value.pop()
                    if q == 'false' and w == 'false':
                        value.append('false')
                    else:
                        value.append('true')
            # remaining value is the truth value of entire expression
            # we take remaining value and and it it is true, apply the newly learned fact
            if value[0] == 'true':
                for sneeze in self.rules_list[rule]:
                    self.facts[sneeze] = 'true'

    def query(self, expression):
        split_expr = re.findall('[a-z]+|[A-Z]+|[%s]' % ''.join(self.token_map), expression)
        variables = re.findall('[a-z]+|[A-Z]+', expression)
        for var in variables:
            if var not in self.var_definitions.keys():
                print 'Not all variables in query expression are defined yet.'
                return

        # base case of 1 variable query
        if len(expression) == 1:
            if expression in self.facts:
                if self.facts[expression] == 'true':
                    return True
            for rule in self.rules_list:
                if expression in self.rules_list[rule]:
                    if self.query(rule):
                        return True
                    # otherwise continue to search through rules
            return False

        truth_table = {}
        for var in variables:
            truth_table[var] = self.query(var)
        result = self.to_postfix(split_expr)

        value = []
        while not result.empty():
            abc = result.get()
            if abc.isalpha():
                value.append(truth_table[abc])
            if abc == '!':
                q = value.pop()
                if q:
                    q = False
                elif not q:
                    q = True
                value.append(q)
            if abc == '&':
                q = value.pop()
                w = value.pop()
                if q and w:
                    value.append(True)
                else:
                    value.append(False)
            if abc == '|':
                q = value.pop()
                w = value.pop()
                if not q and not w:
                    value.append(False)
                else:
                    value.append(True)
        # remaining value is the truth value of entire expression

        return value[0]

    def why(self, expression):
        split_expr = re.findall('[a-z]+|[A-Z]+|[%s]' % ''.join(self.token_map), expression)
        variables = re.findall('[a-z]+|[A-Z]+', expression)
        for var in variables:
            if var not in self.var_definitions.keys():
                print 'Not all variables in query expression are defined yet.'
                print expression
                return

        # base case of 1 variable query
        if len(expression) == 1:
            rule_exists = False
            for rule in self.rules_list:
                if expression in self.rules_list[rule]:
                    rule_exists = True
                    if self.why(rule):
                        print 'Because: ' + rule + ', I know that: ' + expression
                        return True
                    else:
                        print 'Because it is not true that: ' + rule + ', I cannot prove: ' + expression
            if not rule_exists:
                if expression in self.facts:
                    if self.facts[expression] == 'true':
                        print 'I know that: ' + expression
                        return True
                    else:
                        print 'I know it is not true that: ' + expression
            return False

        truth_table = {}
        for var in variables:
            truth_table[var] = self.why(var)
        result = self.to_postfix(split_expr)

        value = []
        while not result.empty():
            abc = result.get()
            if abc.isalpha():
                value.append(truth_table[abc])
            if abc == '!':
                q = value.pop()
                if q:
                    q = False
                elif not q:
                    q = True
                value.append(q)
            if abc == '&':
                q = value.pop()
                w = value.pop()
                if q and w:
                    value.append(True)
                else:
                    value.append(False)
            if abc == '|':
                q = value.pop()
                w = value.pop()
                if not q and not w:
                    value.append(False)
                else:
                    value.append(True)
        # remaining value is the truth value of entire expression
        return value[0]

    def list_everything(self):
        print 'Variables:'
        for x in self.var_definitions:
            print '\t' + '\t' + x + ' = "' + self.var_definitions[x] + '"'
        print 'Facts:'
        for y in self.facts:
            if self.facts[y] == 'true':
                print '\t' + '\t' + y
        print 'Rules:'
        for z in self.rules_list:
            for need_to_rename in self.rules_list[z]:
                print '\t' + '\t' + z + ' -> ' + need_to_rename

# --------------------------------------- end of class --------------------------------------------


def parse_input(command):
    chunks = shlex.split(command.encode('utf8'))
    return chunks

if __name__ == '__main__':
    input_file = open('mid3.in', 'r')
    prover = TheoremProver()
    for line in input_file:
        line_input = line.replace('\n', '')
        # cmd = raw_input("Input a command:")
        # cmd_segments = parse_input(cmd)
        cmd_segments = parse_input(line_input)

        if cmd_segments[0] == 'Teach':
            # facts and variable definitions
            if cmd_segments[2] == '=':
                if cmd_segments[3] == 'true' or cmd_segments[3] == 'false':
                    prover.create_new_fact(cmd_segments[1], cmd_segments[3])
                else:
                    prover.create_new_variable(cmd_segments[1], cmd_segments[3])

            # rule creation
            if cmd_segments[2] == '->':
                prover.create_new_rule(cmd_segments[1], cmd_segments[3])

        elif cmd_segments[0] == 'List':
            prover.list_everything()

        elif cmd_segments[0] == 'Learn':
            prover.learn()

        elif cmd_segments[0] == 'Query':
            print 'query starts for ' + cmd_segments[1]
            print prover.query(cmd_segments[1])
            print 'query ends for ' + cmd_segments[1]

        elif cmd_segments[0] == 'Why':
            print 'why starts for ' + cmd_segments[1]
            if prover.why(cmd_segments[1]):
                print 'I thus know that ' + cmd_segments[1]
            else:
                print 'Thus I cannot prove that ' + cmd_segments[1]
            print 'why ends for ' + cmd_segments[1]

        else:
            print "Invalid command. Please use Teach, List, Learn, Query, or Why with proper parameters."