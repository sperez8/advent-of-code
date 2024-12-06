import networkx as nx

def parse_rules(file):
    """ Since the rules are in the format A->B, we store these as directed edges in a graph """
    G = nx.DiGraph()
    for rule in file:
        before,after = rule.strip("\n").split("|")
        G.add_edge(before,after)
    return G

def parse_updates(file):
    updates = []
    for update in file:
        updates.append(update.strip("\n").split(","))
    return updates

def middle(updates):
    middle_index = int(len(updates)/2)
    return updates[middle_index]        
        
if __name__ == "__main__":
    # for part 1
    middles_valid_updates = 0
    
    # for part 2
    middles_corrected_updates = 0

    # open page ordering rules file and store the rules as a directed graph
    # such that 75|97 is and edge 75->97
    with open('input1_day5.txt', 'r') as file:
        rules_graph = parse_rules(file)
    
    # open updates files
    with open('input2_day5.txt', 'r') as file:
        update_paths = parse_updates(file)
    
    print(rules_graph)
    print(len(update_paths))

    # Check if update is valid
    for update in update_paths:
        # a valid update should be a path in the rules graph
        if nx.is_path(rules_graph, update):
            middles_valid_updates += int(middle(update))
        else:
            # update isn't valid so we try to fix it
            # first get the subgraph from the nodes we need
            update_subgraph = nx.subgraph(rules_graph, update)

            # and get the longuest path which must have all the nodes
            # since it's a DAG (right? I hope so) there should only be one
            fixed_update = nx.dag_longest_path(update_subgraph)
            middles_corrected_updates += int(middle(fixed_update))

    print(f"And the answer for part 1 is {middles_valid_updates}")
    print(f"And the answer for part 2 is {middles_corrected_updates}")
