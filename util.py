import yaml
import nfa_dfa_classes

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