
class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states, config=None):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.config = config if config else {}

    def check_string(self, input_string):
        current_states = []
        next_states = []

        current_states.append(self.start_state)

        for bit in input_string:                                        #iterate every character in string
            # print("current_states",current_states,"next_states", next_states,"bit:", bit)
            for Cstate in current_states:                               #current states, at the end we will check if accept states are in here or not 
                # print("Cstate:", Cstate,"key:",(Cstate, bit),"next if:",(Cstate, bit) in self.transitions.keys())
                if((Cstate, bit) in self.transitions):                  #if has transition continue, else return false.
                    templist = []
                    templist += (self.transitions.get((Cstate, bit)))
                    # print("templist:",templist)
                    for Nstate in templist:  #
                        if (Nstate not in next_states):
                            next_states.append(Nstate)

            # print("next states;", next_states)                
            current_states = next_states[:]
            next_states.clear()
        
        # print("last current states:", current_states,"self.accept_states",self.accept_states,)
        if(any(state in current_states for state in self.accept_states)):
            return True

        return False

    def epsilon_closure(self, states):
        # Implement the epsilon closure here
        closure = list(states)  # Start with the original states
        # Add logic to include states reachable by epsilon transitions
        return closure

    def __str__(self):
        transitions_str = ',\n    '.join([f"({src}, {symbol}): {dsts}" for (src, symbol), dsts in self.transitions.items()])
        return (
        f"NFA(\n"
        f"  states={self.states},\n"
        f"  alphabet={self.alphabet},\n"
        f"  transitions={{\n    {transitions_str}\n  }}\n"
        f"  start_state={self.start_state},\n"
        f"  accept_states={self.accept_states},\n"
        f")"
    )

class NFA_to_DFA:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.transitions = {}
        self.start_state = []
        self.accept_states = []

    def epsilon_closure(self, states):
        # Implement the epsilon closure here
        closure = list(states)  # Start with the original states
        # Add logic to include states reachable by epsilon transitions
        return closure

    def convert_from_nfa(self, nfa):
        self.states.append([nfa.start_state])
        # print("nfa alphabet type:", type(nfa.alphabet))
        self.alphabet = nfa.alphabet[:]
        self.start_state = nfa.start_state

        # print("sefl states:", self.states)
        # print("self alphabet:", self.alphabet,"type:",type(self.alphabet))

        i=0
        #Note states of dfa could be the set of states in nfa.
        for state_set in self.states:                                   
            i+=1
            # print("line:", i ,"dfa state represented by nfa states:", state_set )   
            
            for e in self.alphabet:
                dfa_state_maker=[]
                for state in state_set:                          
                    
                        # print("delta input for state",i,":",state, e)
                        if((state, str(e)) in nfa.transitions):        
                            
                            for a in nfa.transitions.get((state, str(e))):
                                if a not in dfa_state_maker:
                                    dfa_state_maker.append(a)

                            if not dfa_state_maker:
                                if "empty" not in self.states:
                                    self.states.append("empty")
                           
                            if (dfa_state_maker not in self.states):
                                self.states.append(dfa_state_maker)
                # add transitions
                # print("inserting transition:", state_set)
                # print("inserting transition:", tuple(state_set))
                self.transitions[(tuple(state_set), e)] = tuple(dfa_state_maker)
            # print (self.states)

            # add accept states
            if(any(state in state_set for state in nfa.accept_states)):
                self.accept_states.append(state_set)

        #change to tuple 
        
        print("$$$$$$$$$$$$$$$$$$$$$$$", self.accept_states)
        self.accept_states = [tuple(item) for item in self.accept_states]
        

        print("$$$$$$$$$$$$$$$$$$$$$$$", self.accept_states)
        for list in self.states:
            list = tuple(list)
     
        self.start_state = (self.start_state,)
     
    def check_string(self, input_string):
        # current_states = (self.start_state,)  # Ensure this matches the keys in self.transitions

        # for bit in input_string:
        #     bit_as_int = int(bit)
        #     transition_key = (current_states, bit_as_int)

        #     if transition_key in self.transitions:
        #         next_states = self.transitions[transition_key]
        #         current_states = tuple(next_states) if isinstance(next_states, list) else next_states
        #     else:
        #         return False  # No valid transition for this bit, reject the string

        # return current_states in self.accept_states  # Check if the final states include an accept state
        current_states = self.start_state
        next_states = None

        for bit in input_string:
            bit_as_int = int(bit)
            # print(self.transitions)                                      
            # print("current_states",current_states,"next_states", next_states,"bit:", bit, "(current_states, bit):",(current_states, bit),"if:",((current_states, bit) in self.transitions))
            if((current_states, bit_as_int) in self.transitions):                  
                next_states = self.transitions.get((current_states, bit_as_int))

            # print("next states;", next_states)                
            current_states = next_states
        
        # print("last current states:", current_states,"self.accept_states",self.accept_states,)
        if(current_states in self.accept_states):
            return True

        return False
    
    def __str__(self):
        transitions_str = ',\n    '.join([f"({src}, {symbol}): {dsts}" for (src, symbol), dsts in self.transitions.items()])
        return (
        f"DFA(\n"
        f"  states={self.states},\n"
        f"  alphabet={self.alphabet},\n"
        f"  transitions={{\n    {transitions_str}\n  }}\n"
        f"  start_state={self.start_state},\n"
        f"  accept_states={self.accept_states},\n"
        f")"
    )