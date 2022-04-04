def generateIndependentNodes(DAG):
    ind_events = set()
    for key in list(DAG.keys()):
        for value in list(DAG.values()):
            if key == value:
                break
            ind_events.add(key)
    print(f"The Independent Events are : {ind_events}")
    return ind_events


def generateDependentNodes(DAG, ind_events):
    flat_dep_events = [num for sublist in list(DAG.values()) for num in sublist]

    cond_ind_events = list()
    dep_events = list()
    for event in flat_dep_events:
        if event not in dep_events:
            # generates a unique list of values from DAG
            dep_events.append(event)
        else:
            # generates a list containing duplicates of values from DAG
            cond_ind_events.append(event)
    for event in dep_events:
        # removing the duplicate value(s) from the unique list
        if event in cond_ind_events:
            dep_events.remove(event)
    
    cond_ind_event_temp = list()
    # updates cond_ind_event
    for event in ind_events:
        for c_event in cond_ind_events:
            new_event = c_event + "|" + event
            cond_ind_event_temp.append(new_event)

    dep_event_temp = list()
    # updates dep_event
    for event in cond_ind_events:
        for d_event in dep_events:
            new_event = d_event + "|" + event
            dep_event_temp.append(new_event)

    return cond_ind_event_temp, dep_event_temp
        

def computeIEConditionalProbability(events):
    event_cp = dict()
    for event in events:
        temp_event_cp = dict()
        temp_event_cp[event] = dict()
        event_true_probability = float(input(f"Enter P({event}) = T: "))
        temp_event_cp[event]['T'] = event_true_probability
        temp_event_cp[event]['F'] = 1 - event_true_probability
        print(temp_event_cp)
        event_cp.update(temp_event_cp)
    return event_cp


def generateDependentEvents(ind_events, dep_events, cond_ind_events):
    # ind_events => {'B', 'E'}, dep_event => ['DC', 'SC'], cond_ind_events => ['A']
    # dep_event => ['DC|A', 'SC|A'], cond_ind_events => ['A|B', 'A|E']
    cond_ind_event_temp = list()
    # updates cond_ind_event
    for event in ind_events:
        for c_event in cond_ind_events:
            new_event = c_event + "|" + event
            cond_ind_event_temp.append(new_event)
    print(cond_ind_event_temp)

    dep_event_temp = list()
    # updates dep_event
    for event in cond_ind_events:
        for d_event in dep_events:
            new_event = d_event + "|" + event
            dep_event_temp.append(new_event)
    print(dep_event_temp)


def computeCIEConditionalProbability(cond_ind_events):
    temp_cp = {
        'A|B^E':0.94,
        'A|B^~E':0.95,
        'A|~B^E':0.69,
        'A|~B^~E':0.999,
        '~A|B^E':0.06,
        '~A|B^~E':0.05,
        '~A|~B^E':0.31,
        '~A|~B^~E':0.001,
    }
    return temp_cp
    


def computeDEConditionalProbability(dep_events):
    temp_cp = {
        'DC|A': 0.91,
        'DC|~A':0.05, 
        '~DC|A': 0.91,
        '~DC|~A':0.05,
        'SC|A': 0.75,
        'SC|~A':0.02, 
        '~SC|A': 0.25,
        '~SC|~A':0.98,
    }
    return temp_cp


def main():
    ind_events = generateIndependentNodes(DAG)
    # cp_ind_events = computeIEConditionalProbability(ind_events)
    
    cond_ind_events, dep_events = generateDependentNodes(DAG, ind_events)
    print(f"\nConditionally Independent Events : {cond_ind_events}")
    print(f"\nDependent Events : {dep_events}")

    cp_cond_ind_events = computeCIEConditionalProbability(cond_ind_events)
    print(f"\nC.P. for CI Events : {cp_cond_ind_events}")
    cp_dep_events = computeDEConditionalProbability(dep_events)
    print(f"\nC.P. for D Events : {cp_dep_events}")
    
    # TO DO: Update the compute cp functions for conditionally independent & dependent events 
    # each containing different inputs required for the truth tables


if __name__ == "__main__":
    # Burglary -> B, Alarm -> A, Earthquake -> E, 
    # David Calls -> DC, Sophia Calls -> SC
    DAG = {
        'B' : 'A',
        'E' : 'A',
        'A' : ('DC','SC')
    }
    main()
