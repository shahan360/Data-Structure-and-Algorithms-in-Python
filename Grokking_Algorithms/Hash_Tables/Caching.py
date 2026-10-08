cache = {}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        data = get_data_from_server(url)  # Assume this function fetches data from the server
        cache[url] = data
        return data

def get_data_from_server(url):
    # Simulate fetching data from a server
    return f"Data from {url}"

# Test the caching function
print(get_page("https://example.com/page1"))  # Fetches from server
print(get_page("https://example.com/page1"))  # Fetches from cache