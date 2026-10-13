from collections import deque # importing deque


def person_is_seller(name): # function for checking the mango seller
    return name[-1] == 'm'


def search(graph): #
    search_queue = deque()
    search_queue += graph["you"]
    searched = set()  # Keep track of already searched people to avoid cycles
    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            continue
        searched.add(person)
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        search_queue += graph.get(person, [])

    return False

# Example usage
if __name__ == "__main__":
    graph = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }

    search(graph)