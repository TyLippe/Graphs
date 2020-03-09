import random
import math

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # # Do a BFT to visit each user in our extended social network
        # # Modify the BFT to store the path to each visited user
        # # For each user we visit, add the social path to the visited dictionary (key is user_id)

        # Create an empty queue
        q = Queue()
        # Add a PATH to the starting_vertex_id to the queue
        q.enqueue([user_id])
        # Create an empty dictionary to store visited users and social paths
        visited = {}
        # While the queue is not empty..
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # Grab the last vertex from the path
            v = path[-1]
            # Check if it has been visited
            if v not in visited:
                # Mark it as visited
                visited[v] = path
                # Then add the Friends to the back of the queue
                for friend_id in self.friendships[v]:
                    if friend_id not in visited:
                        # Copy the path
                        copy_path = path.copy()
                        # Add Friend to the path
                        copy_path.append(friend_id)
                        q.enqueue(copy_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(connections)
    print(len(connections))
    total = 0
    for connection in connections:
        total += len(connections[connection])
    print(total / len(connections) - 1)