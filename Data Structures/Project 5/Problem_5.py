import hashlib
from datetime import datetime

    
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
      
    def calc_hash(self):
           sha = hashlib.sha256()

           hash_str = (str(self.data) + str(self.timestamp) + str(self.previous_hash)).encode('utf-8')

           sha.update(hash_str)

           return sha.hexdigest()


class linked_list:
    
    def __init__(self):
        self.head = None
        
        
    def add_block (self, data, timestamp = None):
              
        
        if isinstance(timestamp, datetime) == False:
            timestamp = datetime.now()
        
        
        if self.head == None:
            self.head = Block(timestamp, data, 0)
            
        else:
            current_block = self.head
            
            while current_block.next:
                current_block = current_block.next
                
            previous_hash = current_block.hash
            current_block.next = Block(timestamp, data, previous_hash)
            
    def show_chain(self):
        
        if self.head == None:
            print('Block chain is currently empty')
            return
        
        else:
            
            current_block = self.head
            while current_block:
                print("Timestamp : {ts}".format(ts = current_block.timestamp))
                print("Data: {data}".format(data = current_block.data))
                print("Hash value: {ha}".format(ha = current_block.hash))
                print("Previous hash: {pa}".format(pa = current_block.previous_hash))
                print("-------------------")
                
                current_block = current_block.next
                
            

print('\n')

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1 

char_list = linked_list()

char_list.add_block("Terakomari", datetime(2023, 12, 9, 11, 30))
char_list.add_block("Vill", datetime(2023, 12, 16, 10, 30))
char_list.add_block("Sakuna", datetime(2023, 12, 23, 11, 15))
char_list.add_block("Milicient", datetime(2023, 12, 30, 12, 45))
char_list.show_chain()

'''
Expected output:
    Timestamp : 2023-12-09 11:30:00
    Data: Terakomari
    Hash value: 649a6e0506adca7e47b0f2e12786e990cf9d3ca8f67c16ee2e7976f81d98d3aa
    Previous hash: 0
    -------------------
    Timestamp : 2023-12-16 10:30:00
    Data: Vill
    Hash value: 523e6e5c79ef2e1d6e2b7c060af6a83b8d992686735437172c0860e970e91332
    Previous hash: 649a6e0506adca7e47b0f2e12786e990cf9d3ca8f67c16ee2e7976f81d98d3aa
    -------------------
    Timestamp : 2023-12-23 11:15:00
    Data: Sakuna
    Hash value: ca91794470a45fb150279ab78776d711eccf3f670e9305a3f12009b0548886e2
    Previous hash: 523e6e5c79ef2e1d6e2b7c060af6a83b8d992686735437172c0860e970e91332
    -------------------
    Timestamp : 2023-12-30 12:45:00
    Data: Milicient
    Hash value: 37e98acfea18fdb142b2969c75b907816a0b4f1e32effe520793a0395ee3e8a9
    Previous hash: ca91794470a45fb150279ab78776d711eccf3f670e9305a3f12009b0548886e2
    -------------------
'''

print('\n\n')
## Test Case 2 EDGE CASE: Varying data types

Varied_llist = linked_list()

Varied_llist.add_block('Cat', datetime(2023, 4, 20, 18, 30))
Varied_llist.add_block(12345678910, datetime(2023, 9, 8, 7, 25))
Varied_llist.add_block(['Yes', 'No', 123, 987], datetime(2023, 10, 14, 17, 55))
Varied_llist.add_block({'Claire' : 'Rae' , 'Misha' : 'Yuu'}, datetime(2023, 12, 14, 17, 55))
Varied_llist.show_chain()

'''
Expected output:
    Timestamp : 2023-04-20 18:30:00
    Data: None
    Hash value: 3f81de461e47f24aaf782a5879a2ac46ff13e133bd9ce19a587bc07f1a04e059
    Previous hash: 0
    -------------------
    Timestamp : 2023-09-08 07:25:00
    Data: 12345678910
    Hash value: 359c561eabb163d0c6139f33c79f4a1b259269963c1b6f1a66d8fadd8ab6c14f
    Previous hash: 3f81de461e47f24aaf782a5879a2ac46ff13e133bd9ce19a587bc07f1a04e059
    -------------------
    Timestamp : 2023-10-14 17:55:00
    Data: ['Yes', 'No', 123, 987]
    Hash value: 7e8ab1605cf58f698b7d3a7853625259963698d18cee18f6c69a65c51fe62102
    Previous hash: 359c561eabb163d0c6139f33c79f4a1b259269963c1b6f1a66d8fadd8ab6c14f
    -------------------
    Timestamp : 2023-12-14 17:55:00
    Data: {'Claire': 'Rae', 'Misha': 'Yuu'}
    Hash value: b9801049452581c3d81844718b56cbe500467d68a682737937cee3051ac917d4
    Previous hash: 7e8ab1605cf58f698b7d3a7853625259963698d18cee18f6c69a65c51fe62102
    -------------------
'''
print('\n\n')

## Test Case 3 EDGE CASE: missing values

Missing_list = linked_list()


Missing_list.add_block(None, datetime(2023, 4, 20, 18, 30))
Missing_list.add_block(12345678910)
Missing_list.add_block('Sakura', 'Elise')
Missing_list.add_block(None, None)
Missing_list.show_chain()

'''
Expected output: 2ND, 3RD AND 4TH OUTPUT TIMESTAMP VARIES BASED ON CURRENT TIME
    Timestamp : 2023-04-20 18:30:00
    Data: None
    Hash value: 3f81de461e47f24aaf782a5879a2ac46ff13e133bd9ce19a587bc07f1a04e059
    Previous hash: 0
    -------------------
    Timestamp : 2023-12-08 18:09:00.378948
    Data: 12345678910
    Hash value: c4ad3ac940aeb2819779252ca549626fbe129d141609c10e324d37e25fb1f4e0
    Previous hash: 3f81de461e47f24aaf782a5879a2ac46ff13e133bd9ce19a587bc07f1a04e059
    -------------------
    Timestamp : 2023-12-08 18:09:00.378948
    Data: Sakura
    Hash value: 26804a6e433f1bb3116e4b4c713688e290e5761a4e4a11dd4b4274a6c5cc1845
    Previous hash: c4ad3ac940aeb2819779252ca549626fbe129d141609c10e324d37e25fb1f4e0
    -------------------
    Timestamp : 2023-12-08 18:09:00.378948
    Data: None
    Hash value: ac83a03ebc1258b0d1b2882aa8fa937f30f865478b7496f2de8c54457f11cafb
    Previous hash: 26804a6e433f1bb3116e4b4c713688e290e5761a4e4a11dd4b4274a6c5cc1845
    -------------------
'''

