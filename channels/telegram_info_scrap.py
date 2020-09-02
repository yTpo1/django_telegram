import requests
from bs4 import BeautifulSoup


# username = 'pet_me_feed_me'
def get_soup_telegram(username):
    url = 'https://t.me/' + username
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_title(soup):
    find_title = soup.find('div', class_='tgme_page_title')
    channel_title = find_title.get_text()[3:-1]

    #if find_title is None:
    #    channel_title = "Name not found.."
    #else:
    #    channel_title = find_title.get_text()[3:-1]
    #channel_title = "Name not found.."

    return channel_title


def get_description(soup):
    find_description = soup.find('div', class_='tgme_page_description')
    channel_description = find_description.get_text()
    return channel_description


def get_members(soup):
    find_members = soup.find('div', class_='tgme_page_extra')
    channel_members = find_members.get_text()
    # TODO: user .strip instead of .split
    number_of_members = channel_members.split('members')[0][:-1]
    number_of_members = number_of_members.replace(" ", "")
    return number_of_members


def get_image(soup, username):
    first_img = soup.find_all('img')[0]
    link = first_img['src']
    save_location = 'media/channel_imgs/' + username + '.jpg'
    #save_location = '/var/www/html/django_telegram/media/channel_imgs/' + username + '.jpg'
    name_location = 'channel_imgs/' + username + '.jpg'
    with open(save_location, 'wb') as file:
        file.write(requests.get(link).content)

    return name_location
    # return requests.get(link).content
