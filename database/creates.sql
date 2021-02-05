CREATE DATABASE IF NOT EXISTS `restaurants`;
USE restaurants;

DROP TABLE IF EXISTS `restaurants`.`restaurant`;
CREATE TABLE `restaurant` (
  `restaurant_id` INT NOT NULL AUTO_INCREMENT,
  `address` varchar(200) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `province` varchar(2) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `country` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `restaurants`.`daily_coupon_redemptions_per_restaurant`;

CREATE TABLE `daily_coupon_redemptions_per_restaurant` (
  `summary_date` date NOT NULL,
  `coupon_id` int NOT NULL AUTO_INCREMENT,
  `restaurant_id` INT NOT NULL REFERENCES restaurant(restaurant_id),
  `redemption_count` int(11) DEFAULT '0',
  PRIMARY KEY (`coupon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- DROP TABLE IF EXISTS `restaurants`.`daily_coupon_redemptions_per_restaurant`;

-- stream of coupon redemptions, grouped into hours 
-- CREATE TABLE `coupon_redemptions` (
  -- DATETIME NOT NULL
-- )