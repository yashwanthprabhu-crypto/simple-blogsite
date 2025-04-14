from datetime import datetime
import base64

class Storage:
    def __init__(self):
        self.posts = {}
        self.users = {}
        self.comments = {}
        self.likes = {}
        
    def create_post(self, title, content, author, image=None):
        post_id = len(self.posts) + 1
        slug = f"{'-'.join(title.lower().split())}-{post_id}"
        post = {
            'id': post_id,
            'title': title,
            'content': content,
            'author': author,
            'created_at': datetime.now(),
            'image': image,
            'slug': slug
        }
        self.posts[post_id] = post
        return post
    
    def get_post(self, post_id):
        return self.posts.get(post_id)
    
    def get_all_posts(self):
        return list(self.posts.values())
    
    def update_post(self, post_id, title, content, image=None):
        if post_id in self.posts:
            self.posts[post_id].update({
                'title': title,
                'content': content,
                'image': image,
                'updated_at': datetime.now()
            })
            return True
        return False
    
    def delete_post(self, post_id):
        if post_id in self.posts:
            del self.posts[post_id]
            return True
        return False

# Create a global instance
storage = Storage()