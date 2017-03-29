#!/usr/bin/env python3

'a simple pillow demo'

__author__ = 'Liu Zhuan'

from PIL import Image
im = Image.open('../assets/avatar_github.png')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('../assets/avatar_github_thumb.jpg', 'JPEG')