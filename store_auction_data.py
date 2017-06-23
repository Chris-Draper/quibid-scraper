from peewee import * 
# should be able to use "import peewee" but that doesn't work
# I had to pip install PyMySQL to be able to use SQL databases

db = MySQLDatabase(database='chris_quibids_db', host='216.219.81.80', 
        port=3306, user='chris_admin', password='Rhshornet21!!')

class BaseModel(Model): # specify database for all subsequent models
    class Meta:
        database = db

class Voucher(BaseModel):
    title = CharField()
    end_date = DateTimeField()
    end_price = DoubleField()
    winner = CharField()

class VoucherBidder(BaseModel):
    auction_item = ForeignKeyField(Voucher, related_name='bidders')
    bidder_name = CharField()
    bidder_val = DoubleField()
    bidder_type = CharField()

def store_auction_data(data):
    db.connect()
    db.create_tables([Voucher, VoucherBidder], safe=True)
    voucher = Voucher.create(title=data[0], end_date=data[1], end_price=data[2], winner=data[3])
    for bidder in data[4]:
        bidder = VoucherBidder.create(
                auction_item=voucher, 
                bidder_name=bidder[0], 
                bidder_val=bidder[1], 
                bidder_type=bidder[2])
    db.close()

# run this in main to test storing the data in the mysql database
if __name__ == '__main__':
    # data from a scraped bid
    auction_data = ('15 Voucher Bids', '2017-06-22 01:25:58', 0.05, 'mctrip', 
        [('Kimzboyz5', 0.01, 'Single Bid'), ('krasjs1', 0.02, 'Single Bid'), 
        ('mctrip', 0.03, 'BidOMatic'), ('krasjs1', 0.04, 'Single Bid'), 
        ('mctrip', 0.05, 'BidOMatic')])
    store_auction_data(auction_data)
    
