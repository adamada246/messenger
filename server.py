class DataHandler:
    #reciever - sender - messages
    pending = {"":{"":[]}}
    def __init__(self):
        print()

    def getLoad(self, msngr):
        load = msngr.__sendCache__()
       #for every key in load
        for key in load.keys():
            #if the key is in pending
            if key in self.pending.keys():
                #get the array of messages
                arr = load[str(key)]
                #for each message in the array
                for msg in arr:
                    #add it to the pending
                    self.pending[str(key)][msngr.get_id()].append(msg)
            else:
                print(key)
              #  self.pending[str(key)][str(msngr.get_id())] = load[str(key)]
                self.pending.update({str(key):{str(msngr.get_id()):load[str(key)]}})
    
    def sendLoad(self, rcvr):
        #get the array of messages
        arr = self.pending[str(rcvr.get_id())]
        #for each message in the array
        rcvr.__recieveBulk__(arr)