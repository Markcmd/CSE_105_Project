import util
import nfa_dfa_classes
import yaml


def create_nfa_from_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        nfa_config = yaml.safe_load(file)

    states = nfa_config['states']
    alphabet = nfa_config['alphabet']
    start_state = nfa_config['start_state']
    accept_states = nfa_config['accept_states']
    transitions = {(t['from_state'], str(t['input'])): t['to_states'] for t in nfa_config['transitions']}
    config = nfa_config.get('config', {})

    return NFA(states, alphabet, transitions, start_state, accept_states, config)



nfa = util.create_nfa_from_yaml('./configs/nfa_1.yaml')
print(nfa)
# print(nfa.transitions)
# print(nfa.transitions.keys())

print(nfa.check_string("0111"))
print(nfa.check_string("0110"))
print(nfa.check_string("1111"))
print(nfa.check_string(""))


dfa = NFA_to_DFA()
dfa.convert_from_nfa(nfa)
# print(dfa)


print(dfa.check_string("0111"))
print(dfa.check_string("0110"))
print(dfa.check_string("1111"))
print(dfa.check_string(""))