# Change your username and password in config file

import config
from instapy import InstaPy

#login section
session = InstaPy(username=config.username, password=config.password)
session.login()

#like section
session.like_by_tags(['code'], amount = 60) # to input multiple tags use an array ( [''] )

#follow section
session.set_do_follow(True, percentage=25)

#comment section
session.set_do_comment(True, percentage=50)
session.set_comments(['Love It', 'Nice Post'])

session.end()

