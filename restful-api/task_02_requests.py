import requests
import csv
r = requests.get('https://jsonplaceholder.typicode.com/posts')
def fetch_and_print_posts():
    for post in r.json():
        print('Post ID: {}, Title: {}'.format(post.get('id'), post.get('title')))
        status_code = r.status_code
        print('Status Code: {}'.format(status_code))

def fetch_and_save_posts():
    # ... məlumatı çəkmə hissəsi ...
    posts = r.json()
    
    # 1. Yalnız lazım olan sütunları seçərək yeni siyahı hazırlayırıq
    data_to_save = []
    for post in posts:
        data_to_save.append({
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        })

    # 2. Fayla yazma (Ardıcıllığa və writeheader-ə diqqət!)
    with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
        # fieldnames tam olaraq testin gözlədiyi ardıcıllıqda olmalıdır
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader() # Başlıqları yazır: id,title,body
        writer.writerows(data_to_save) # Məlumatları yazır
