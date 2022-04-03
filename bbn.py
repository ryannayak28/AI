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
    dep_events = set(flat_dep_events)
    print(f"The Dependent Events are : {dep_events}")
    return dep_events
        

def computeConditionalProbability(events):
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


def main():
    ind_events = generateIndependentNodes(DAG)
    cp_ind_events = computeConditionalProbability(ind_events)
    dep_events = generateDependentNodes(DAG)
    cp_dep_events = computeConditionalProbability(dep_events)
    # TO DO: Update the genCp() to enable the computing of diff probabilities for 'A' & for 'DC','SC'



if __name__ == "__main__":
    # Burglary -> B, Alarm -> A, Earthquake -> E, 
    # David Calls -> DC, Sophia Calls -> SC
    DAG = {
        'B' : 'A',
        'E' : 'A',
        'A' : ('DC','SC')
    }
    main()
