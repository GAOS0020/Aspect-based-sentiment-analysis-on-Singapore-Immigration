import re

# Remove urls
def remove_urls(text):
    url_remove = re.compile(r'http?://\S+|www\.\S+|https?://\S+|http?\S+')
    return url_remove.sub(r'', text)

# Remove htmls
def remove_html(text):
    html = re.compile(r'<.*?>')
    return html.sub(r'', text)


# Remove mentions
def remove_mention(x):
    text = re.sub(r'@\w+', '', x)
    return text

# Remove hashtags
def remove_hash(x):
    text = re.sub(r'#\w+', '', x)
    return text
