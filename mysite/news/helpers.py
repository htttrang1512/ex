import uuid
import os

import re
def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('news/images/article', filename)

def get_skip_slug_article(path):
        skip_slug = None

        match = re.search(r'^(?P<article_slug>[\w-]+)-a\d+\.html$', path)

        if match:
                skip_slug = match.group('article_slug')
        
        return skip_slug
