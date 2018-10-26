# little webservice to dispatch pushes via urbanairship
# see http://docs.urbanairship.com/reference/libraries/python/1.0.0/
# dependencies:
# pip install urbanairship
# pip install web.py

import urbanairship as ua
import logging
import warnings
import web

appKey = 'insertYourAppKeyHere'
masterSecret = 'YourKnowTheMasterPassword'
airship = ua.Airship(appKey, masterSecret)

urls = (
    '/broadcast', 'broadcast',
    '/push/(.*)', 'push_user'
)

# debug logging
#logging.basicConfig()
#logging.getLogger('urbanairship').setLevel(logging.DEBUG)
#warnings.simplefilter('default')

app = web.application(urls, globals())

class broadcast:
    def GET(self):
        #print "broadcasting"
        #broadcastingSimple()
        #return "broadcasted"
        push = airship.create_push()
        push.audience = ua.all_
        push.notification = ua.notification(
            ios=ua.ios(
                #alert='Hello iOS',
                extra={'tid': '1000', 'more':"even more payload"}
            ),
            android=ua.android(
                #alert='Hello Android',
                extra={'tid': '1000', 'more':"even more payload"}
            )
        )
        push.device_types = ua.device_types('ios', 'android')
        push.send()
        return "broadcasted"

class push_user:
    def GET(self, user):
        #print "sending push to %s" % user
        push = airship.create_push()
        push.audience = ua.android_channel(user)
        push.notification = ua.notification(
            ios=ua.ios(alert='Hello user', extra={'tid': '1000', 'more':'even more payload'}),
            android=ua.android(alert='Hello user', extra={'tid': '1000', 'more':'even more payload'})
        )
        push.device_types = ua.device_types('ios', 'android')
        push.send()
        return "sent to %s" % user

def broadcastingSimple():
    push = airship.create_push()
    push.audience = ua.all_
    push.notification = ua.notification(alert="Hello, world!")
    push.device_types = ua.all_
    push.send()

if __name__ == "__main__":
    app.run()
