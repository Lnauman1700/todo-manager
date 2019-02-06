import datetime

class Item(object):


    def __init__(self, contents):
        # timestamp of when it was created
        self.timestamp = datetime.datetime.now()
        # boolean marking the item as complete/not completed (false to begin)
        self.is_complete = False
        # text of the actual to-do item
        self.contents = contents
