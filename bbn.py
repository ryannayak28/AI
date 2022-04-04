def generateIndependentNodes(DAG):
    ind_events = set()
    for key in list(DAG.keys()):
        for value in list(DAG.values()):
            if key == value:
                break
            ind_events.add(key)
    print(f"The Independent Events are : {ind_events}")
    return ind_events


def generateDependentNodes(DAG):
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

    return cond_ind_events, dep_events
        

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


def computeCIEConditionalProbability(cond_ind_events):
    pass


def computeDEConditionalProbability(dep_events):
    pass


def main():
    ind_events = generateIndependentNodes(DAG)
    cp_ind_events = computeIEConditionalProbability(ind_events)
    
    cond_ind_events, dep_events = generateDependentNodes(DAG)
    print(f"Conditionally Independent Events : {cond_ind_events}")
    print(f"Dependent Events : {dep_events}")
    cp_cond_ind_events = computeCIEConditionalProbability(cond_ind_events)
    cp_dep_events = computeDEConditionalProbability(dep_events)
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
