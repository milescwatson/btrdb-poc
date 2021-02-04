import btrdb4
import uuid
import mysql.connector

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
    
def createStreams():
    sqlConn = getSQLConnection()
    cursor = sqlConn.cursor()

    query = ("SELECT * FROM restaurant")
    

    cursor.execute(query)

    restaurants = [] # by id
    for(restaurant_id) in cursor:
        restaurants.append(restaurant_id)
    print('Restaurant_id = ', restaurants)
    cursor.close()
    sqlConn.close()

    conn = getBTrConnection()
    tags = {"associated_restaurant": "1"}
    
    stream = conn.create(
            uu= (uuid.uuid4()),
            collection= "restaurant_5"
    )
    
    #stream = conn.create(
    #    uuid=uuid.uuid4(),
    #    collection="NORTHWEST/90001",
    #    tags={"name": "L1MAG", "unit": "volts"}
    #)

    #structure:
    #restaurant

def deleteStreams():
    conn = getConnection()
    pass

createStreams()
