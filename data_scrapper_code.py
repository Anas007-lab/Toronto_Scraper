
import requests
import csv
import time

# Set your GitHub token here
GITHUB_TOKEN = 'My token here'

# Define headers for requests
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Function to fetch users in Toronto with over 100 followers
def fetch_users():
    users = []
    page = 1
    while True:
        url = f'https://api.github.com/search/users?q=location:Toronto+followers:>100&page={page}'
        response = requests.get(url, headers=headers)
        
        print(f"Fetching users: {response.status_code}")  # Debugging output
        
        if response.status_code != 200:
            print("Failed to fetch users:", response.status_code)
            break
        
        data = response.json()
        if 'items' in data:
            users.extend(data['items'])
        else:
            print("No items found in response.")
            break
        
        if 'next' not in response.links:  # No more pages
            break
        
        page += 1
    
    return users

# Function to save users data to CSV
def save_users_to_csv(users):
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = ['login', 'name', 'company', 'location', 'email', 'hireable', 'bio', 'public_repos', 'followers', 'following', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for user in users:
            user_data = {
                'login': user.get('login'),
                'name': user.get('name', ''),
                'company': user.get('company', '').strip().lstrip('@').upper() if user.get('company') else '',
                'location': user.get('location', ''),
                'email': user.get('email', ''),
                'hireable': user.get('hireable', ''),
                'bio': user.get('bio', ''),
                'public_repos': user.get('public_repos', 0),
                'followers': user.get('followers', 0),
                'following': user.get('following', 0),
                'created_at': user.get('created_at', ''),
            }
            writer.writerow(user_data)

    print("Users data has been saved to users.csv")

# Function to fetch repositories for each user
def fetch_repositories(users):
    repositories = []
    
    for user in users:
        user_login = user['login']
        repos_url = f'https://api.github.com/users/{user_login}/repos?per_page=500'
        response = requests.get(repos_url, headers=headers)
        
        print(f"Fetching repos for {user_login}: {response.status_code}")  # Debugging output
        
        if response.status_code == 200:
            repos_data = response.json()
            for repo in repos_data:
                repo_data = {
                    'login': user_login,
                    'full_name': repo.get('full_name'),
                    'created_at': repo.get('created_at'),
                    'stargazers_count': repo.get('stargazers_count', 0),
                    'watchers_count': repo.get('watchers_count', 0),
                    'language': repo.get('language', ''),
                    'has_projects': repo.get('has_projects', False),
                    'has_wiki': repo.get('has_wiki', False),
                    'license_name': repo.get('license')['name'] if repo.get('license') else ''
                }
                repositories.append(repo_data)
        else:
            print(f"Failed to fetch repositories for {user_login}: {response.status_code}")
        
        # Sleep to avoid hitting rate limits
        time.sleep(1)  # Sleep for 1 second between requests
    
    return repositories

# Function to save repositories data to CSV
def save_repositories_to_csv(repositories):
    with open('repositories.csv', 'w', newline='') as csvfile:
        fieldnames = ['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for repo in repositories:
            writer.writerow(repo)

    print("Repositories data has been saved to repositories.csv")

# Main execution
if __name__ == "__main__":
    users_list = fetch_users()
    save_users_to_csv(users_list)
    
    if users_list:  # Only fetch repositories if users were found
        repositories_list = fetch_repositories(users_list)
        save_repositories_to_csv(repositories_list)
