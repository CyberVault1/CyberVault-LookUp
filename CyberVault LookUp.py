import requests
import os
import pyfiglet

def search_google(query):
    api_key = 'AIzaSyCNPzNz2QJQrpf5AWSsWYokBoHqwtCb8vk'
    search_engine_id = 'c0b15fb3267294a0c'
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}'
    
    try:
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            results = data['items']
            for result in results:
                title = result['title']
                link = result['link']
                print(f'Title: {title}\nLink: {link}\n')
        else:
            print('No results found.')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
        print("\n\n")
        print(pyfiglet.figlet_format("CyberVault LookUp", font='big'))  # Print CyberVault in big letters
        search_term = input('Enter the word to search for (or type "exit" to quit): ')
        if search_term.lower() == 'exit':
            break
        
        print("\n" + search_term.lower())  # Print the search term in smaller letters
        search_google(search_term)
        input("Search concluded: Press Enter to continue...")
