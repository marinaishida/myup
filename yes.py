#coding: utf-8
import tweepy

def oauth():
    CK="nyMw0ogyPyzFzXEU7xT5tjnwD"
    CS="lSDgpohpQnLnh0Dn1WZokuomKo4lqS1QJzgvGrgP5k520ORVA9"
    AK="3548750299-jowSzAALxSgikYYvWG3yp8vtYGCBdXlyucqJyku"
    AS="ztjrDkk2DPVY5zSOtbZzH9AjnUY5VqOZcJGCOgHg40xXg"
    api=tweepy.OAuthHandler(CK,CS)
    api.set_access_token(AK,AS)
    auth=tweepy.API(api)
    return auth
    
link_str="<a href={}>{}</a>"
msg=["http://python org","http://"]
auth=oauth()
for i in fruit:
    auth.update_status(status=i)
    