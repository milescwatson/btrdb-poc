import btrdb4
import uuid
import mysql.connector
import datetime
import time

def getSQLConnection():
    cnx = mysql.connector.connect(user='btrdb', password='btrdb123', host='127.0.0.1', database='restaurants')
    return cnx

def getSQLData():
    cnx = mysql.connector.connect(user='btrdb', password='btrdb123', host='127.0.0.1', database='btrdb')

    cursor = cnx.cursor()
    query = ("SELECT * FROM daily_coupon_redemptions_per_restaurant")
    cursor.execute(query)
    for(coupon_id,restaurant_id,x) in cursor:
        print(x,x,x)
    cursor.close()

    cnx.close()

def getBTrConnection():
    conn = btrdb4.connect("127.0.0.1:4410")
    return conn
    #conn = btrdb.connect("127.0.0.1:4411", apikey="123456789123456789")
    #print(conn.info())

def getStreams():
    sqlConn = getSQLConnection()
    cursor = sqlConn.cursor()
    conn = getBTrConnection()

    query = ("SELECT * FROM restaurant")

    cursor.execute(query)

    restaurants = [] # by id
    for(restaurant) in cursor:
        restaurants.append(restaurant[0])

    cursor.close()
    sqlConn.close()
    return restaurants

def createStreams():
    restaurants = getStreams()
    for r in restaurants:
        stream = conn.create(
                uu= (uuid.uuid4()),
                collection= ("restaurant_" + str(r))
        )

def insertRandomData():
    restaurants = getStreams()
    treesPerRestaurant = ['redemptions','user_id','item_id']

    DAY = 24*60*60

    dtStart = datetime.datetime.fromtimestamp(time.time()-(DAY*14)) # 2 weeks ago
    dtEnd = datetime.datetime.fromtimestamp(time.time()) # now

    dtStart = dtStart.replace(microsecond=0, second=0)
    dtEnd = dtEnd.replace(microsecond=0, second=0)

    dtIterator = dtStart.timestamp()

    conn = getBTrConnection()
    # open stream
    streams = conn.lookupStreams("restaurant_5", False)
    # open stream
    # print('streams = ', streams)

    payload = [
        (1500000000000000000, 1.0), (1500000000000100000, 2.1),
        (1500000000000200000, 3.3), (1500000000000300000, 5.1),
        (1500000000000400000, 5.7), (1500000000000500000, 6.1),
    ]
    version = stream.insert(payload)

    # for restaurant in restaurants:
        # newTreeTitle = str(restaurant)+'_'+str('defaultTree')
        # print(newTreeTitle)

def deleteStreams():
    conn = getConnection()
    pass

# createStreams()
insertRandomData()