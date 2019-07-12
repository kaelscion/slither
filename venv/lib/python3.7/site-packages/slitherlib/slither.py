from .proxy import retriever as pr
from .user_agent import ua 

class Slither():
    '''The thread_count variable defines how many user-agent strings and
    IP Addresses should be pulled into your project. There are literally 
    hundreds of both so go nuts but be aware of your thread limits and
    how much memory you have available. You can also read in all of
    the available user-agents and IPs by passing "all" to thread_count
    rather than an integer. Using futures is recommended here
    to help ease the management of threads and processes. Don't fret too
    much as this is an IO bound not CPU bound utility so you can use many
    more worker threads than you have CPU threads. Trust me, there is a lot
    of system waiting involved in http requests.
    '''
    def __init__(self, thread_count='all'):
        self.ips = pr.Retriever(thread_count).thread_ips
        self.uas = ua.UserAgent(thread_count).thread_uas
        self.masks = []
        for i, u in zip(self.ips, self.uas):
            self.masks.append({"address" : i, "user-agent": u})
        