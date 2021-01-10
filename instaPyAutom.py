from instapy import InstaPy

session = InstaPy(username="-----", password="-----",)

# Run bot without browser GUI -- less CPU intensive, improve performance
# session = InstaPy(username="un", password="pw", headless_browser=True)

session.login()
session.like_by_tags(["홈베이킹", "메이컵"], amount=1)
session.set_dont_like(["naked", "nsfw", "follow4follow", "like4like", "body", "diet"])

session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Awesome :heart_eyes:"])

# Set quotas to avoid bot ban
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

# Use clarifai AI with image and video recognition to prevent liking NSFW posts
session.set_use_clarifai(enabled=True, api_key='63b7e611bb5f4d7191cfd16be8a55a48')
session.clarifai_check_img_for(['nsfw'])

# Set relationship bounds to save bot resources
session.set_relationship_bounds(enabled=True, max_followers=10000)

session.end()
