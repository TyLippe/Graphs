# Add queue
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def size(self):
        return len(self.queue)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def print_queue(self):
        output = []
        for item in self.queue:
            output.append(item)
        return output

# Add graph
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exisit!')

def earliest_ancestor(ancestors, starting_node):
    # Initialize an empty graph
    graph = Graph()

    # Iterate through all ancestors 
    print(f'Ancestors: {ancestors}')
    for pair in ancestors:
        print(f'Pair: {pair}')
        # Add both verts
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # Add edge (Child => Parent)
        graph.add_edge(pair[1], pair[0])

    # Initialize a Queue for BFS
    q = Queue()
    # Add starting_node to the Queue
    q.enqueue([starting_node])
    # Initialize the variables
    # If we have a starting_node then we have a initial len of 1 
    max_path_len = 1  
    # If the starting_node does not have a parent then we will never update earliest ancestor and want to return -1
    earliest_ancestor = -1

    # While Queue is not empty
    while q.size() > 0:
        # Create a path
        path = q.dequeue()
        print(f'New path: {path}')

        # Get parent node
        current_vert = path[-1]
        print(f'current_vert: {current_vert}')

        if len(path) == max_path_len:
            if current_vert < earliest_ancestor:
                # Update earliest_ancestor
                earliest_ancestor = current_vert
                # Update max_path_len
                max_path_len = len(path)

        if len(path) > max_path_len:
            # Update earliest_ancestor
            earliest_ancestor = current_vert
            # Update max_path_len
            max_path_len = len(path)

        # Loop through all neigbors of the Parent Node
        for neighbor in graph.vertices[current_vert]:
            # Create a path copy
            path_copy = list(path)
            # Add current neighbor to path
            path_copy.append(neighbor)
            # Add updated path to Queue
            q.enqueue(path_copy)
            print(f'Current Queue: {q.print_queue()}')
            
    print(earliest_ancestor)
    return earliest_ancestor