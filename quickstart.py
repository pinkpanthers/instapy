"""
This template is written by @cormo1990
What does this quickstart script aim to do?
- Basic follow/unfollow activity.
NOTES:
- I don't want to automate comment and too much likes because I want to do
this only for post that I really like the content so at the moment I only
use the function follow/unfollow.
- I use two files "quickstart", one for follow and one for unfollow.
- I noticed that the most important thing is that the account from where I
get followers has similar contents to mine in order to be sure that my
content could be appreciated. After the following step, I start unfollowing
the user that don't followed me back.
- At the end I clean my account unfollowing all the users followed with
InstaPy.
"""

# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'username'
insta_password = 'USERPASSWORD'

# list of users to follow their followers
user_list = ['gymshark', 'vqfit', 'thegainz', 'bodybuildingcom', 'therock']

# list of hastags to like
tags_list = ['fitness', 'gymshark', 'vqfit', 'bodybuilding', 'chestday', 'health', 'gymflow', 'bootyworkouts', 'legday', 'leggins']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=False,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=1000)

    session.set_skip_users(skip_private=False,
                            private_percentage=100,
                            skip_no_profile_pic=False,
                            no_profile_pic_percentage=100)


    # activities - the variable "user_list" is a list found above

    """ Massive Follow of users followers (I suggest to follow not less than
    3500/4000 users for better results)..."""
    session.follow_user_followers(user_list, amount=800,
                                  randomize=False, interact=False)

    """ First step of Unfollow action - Unfollow not follower users..."""
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after= 12 * 60 * 60, sleep_delay=601)

    """ Second step of Massive Follow..."""
    session.follow_user_followers(user_list, amount=800,
                                  randomize=False, interact=False)

    """ Second step of Unfollow action - Unfollow not follower users..."""
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after= 12 * 60 * 60, sleep_delay=601)

    """ Clean all followed user - Unfollow all users followed by InstaPy..."""
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after= 48 * 60 * 60,
                           sleep_delay=601)


    """ Like by Tags """
    # Like & follow users based on  posts hastags

    session.follow_by_tags(tags_list)
    session.set_delimit_liking(enabled=true, min=102)
    session.set_user_interact(amount=3, randomize=true, percentage=75)
    session.like_by_tags(tags_list, amount = 15, interact=true)
    session.remove_follow_requests(amount=200, unfollow_after = 12 * 60 * 60, sleep_delay=601)


    """ Joining Engagement Pods..."""
    photo_comments = ['Nice shot! @{}',
        'Awesome! @{}',
        'Cool :thumbsup:',
        'Just incredible :open_mouth:',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Nice @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

    session.set_do_comment(enabled = True, percentage = 65)
    session.set_comments(photo_comments)
    session.join_pods()
