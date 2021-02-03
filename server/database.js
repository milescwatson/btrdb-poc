var mysql = require('mysql2/promise'),
    dbCredentials = {
	host: 'localhost',
	user: 'btrdb',
	password: 'btrdb123',
	database: 'restaurants',
	waitForConnections: true,
	connectionLimit: 10,
	queueLimit: 0
    },
    restaurantN = 1000,
    couponN = 1000;

var insertRandomData = async function(){
	const connection = await mysql.createConnection(dbCredentials);
	
	for(var i = 0; i < restaurantN; i++){
		var zip = parseInt((Math.random()*100000).toFixed());
		var addr = parseInt(parseInt(Math.random()*100)) + ' Main St';
		const [rows, fields] = await connection.execute('INSERT INTO restaurant(address, city, province,postal_code,country) VALUES(?,?,?,?,?)',[addr, 'New York', 'NY', zip, 'USA'])
		.catch((error)=>{
			console.log('error inserting restaurant random data ', error)
		});
	}
	console.log('Finished inserting random restaurant data');

	function getRandomInt(max) {
  		return Math.floor(Math.random() * Math.floor(max));
	}
	for(var i = 0; i < couponN; i++){
		const [rows, fields] = await connection.execute('INSERT INTO daily_coupon_redemptions_per_restaurant (summary_date, restaurant_id, redemption_count) VALUES(?,?,?)', ['2020-02-02',getRandomInt(restaurantN-1), parseInt(Math.random()*100)])
		.catch((error)=>{
			console.log('error inserting random coupon data ', error)
		})
	}
	console.log('Finished inserting random coupon data');
	await connection.end();
}

var getRestaurantData = async function(){
	const connection = await mysql.createConnection(dbCredentials);
	const [rows, fields] = await connection.execute('SELECT * FROM restaurant')
	console.log(rows)
	await connection.end();
}

var getCouponData = async function(){
	const connection = await mysql.createConnection(dbCredentials);
	const [rows, fields] = await connection.execute('SELECT * FROM restaurant')
	await connection.end();
}

var clearDatabase = async function(){
	const connection = await mysql.createConnection(dbCredentials);
	const [rows, fields] = await connection.execute('DELETE FROM restaurant')
	const [rowsC, fieldsC] = await connection.execute('DELETE FROM daily_coupon_redemptions_per_restaurant')
	await connection.end();

}

insertRandomData()
//getRestaurantData()
//getCouponData()
