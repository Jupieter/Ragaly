'''
This python service file asks for the new ragaly-post id. 
If the id is greater than the file containing the id number, it sends a notification.
'''

from time import sleep
import requests
from jnius import autoclass
from  service.notification_android import AndroidNotification
from get_data import DB_questions
db = DB_questions()
an = AndroidNotification()

try:
    ofi = open('max_ragaly_post_id.txt', 'x')
    f = open('max_ragaly_post_id.txt', 'w')
    f.write(str(0))
    f.close()
except:
    print("have file max_ragaly_post_id.txt")

def open_file():
    ofi = open('max_ragaly_post_id.txt', 'r')
    old_id = int(ofi.read())
    ofi.close()
    return old_id

def write_file(old_id = 0):
    f = open('max_ragaly_post_id.txt', 'w')
    f.write(str(old_id))
    f.close()


def load_data():
    try:
        parent_result = db.post_parent()
        inherit_result = db.post_inherit(parent_result)
        last_post_list = db.post_last(inherit_result)
        max_id = max(last_post_list)
    except:
        print('Problem with internet conection')
        max_id = None
    return max_id
# Timer not here in this python file is in JobSheduler


max_id = load_data()
# print("Coffeebar  service running.....", max_id)
if max_id:
    old_id = open_file()
    if max_id > old_id:
        post_title = db.get_post_title(max_id)
        # print("old id:  ", old_id, "requested id:  ", max_id, "Title: ", post_title)
        write_file(max_id)
        try: 
            an.notify(title='Ragály Önkormányzat új híre', message = post_title,  toast=False, app_icon='images/cimer.png')
        except:
            print("No work the notification")
