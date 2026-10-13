from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(graph):
    search_queue = deque()
    search_queue += graph["you"]

    while search_queue:
        person = search_queue.popleft()
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