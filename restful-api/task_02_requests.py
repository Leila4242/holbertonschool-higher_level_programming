import requests
import csv
r = requests.get('https://jsonplaceholder.typicode.com/posts')
def fetch_and_print_posts():
    for post in r.json():
        print('Post ID: {}, Title: {}'.format(post.get('id'), post.get('title')))
        status_code = r.status_code
        print('Status Code: {}'.format(status_code))

def fetch_and_save_posts():
    for post in r.json():
        status_code = r.status_code
        if status_code == 200:
            posts = r.json()
            keys = posts[0].keys()
            values = [post.values() for post in posts]

    with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
        # DictWriter obyektini yaradırıq
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        
        # Sütun adlarını (başlıqları) fayla yazırıq
        dict_writer.writeheader()
        
        # Bütün siyahını (list) fayla yazırıq
        dict_writer.writerows(posts)
