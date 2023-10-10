class Messenger:
    id
    outbox={"":[]}
    inbox={"":[]}

    def __init__(self, initid):
        self.id=initid
    
    def get_id(self):
        return self.id
    
    #To be used by the data handler, gives dictionary of messages to be delivered by id
    def __sendCache__(self):
        saved = self.outbox
        self.outbox={"":[]}
        return saved
        
       
    

    def __recieveBulk__(self, msgs):
    #should be senderid{[messages]}
        #while loop for the size of senderid

        for sender in msgs.keys():
            #get the array of messages
            arr = msgs[str(sender)]
            #for each message in the array
            for msg in arr:
                #add it to the inbox
                self.__recieve__(sender, msg)
            
    #Adds a message to the inbox so that it can be read
    def __recieve__(self, sender, msg):
      
        #determine if inbox dictionary has sender registered
        if str(sender) in self.inbox.keys():
            #get current array of messages
            history = self.inbox[str(sender)]
            history.append(msg)
            self.inbox[str(sender)]=history
        else:
            arr =[]
            arr.append(msg)
            self.inbox[str(sender)]=arr
    
    #Returns all ids that have sent a message so far
    def getChats(self):
        return self.inbox.keys()

    #Returns the amount of messages the user has from a specific user
    def getMessages(self, id):
        return len(self.inbox[str(id)])
    
    #Returns specific message
    def getMessage(self, id, index):
        return self.inbox[str(id)][index]
    
    #Adds a message to the outbox to be sent when connected to the network
    def send(self, recip, msg):
        if str(recip) in self.outbox.keys():
            history = self.outbox[str(recip)]
            history.append(msg)
            self.outbox[str(recip)]=history
        else:
            arr =[]
            arr.append(msg)
            self.outbox[str(recip)]=arr


        

