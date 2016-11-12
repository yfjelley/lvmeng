/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50629
 Source Host           : localhost
 Source Database       : lvmeng2

 Target Server Type    : MySQL
 Target Server Version : 50629
 File Encoding         : utf-8

 Date: 08/10/2016 17:25:17 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `api_point`
-- ----------------------------
DROP TABLE IF EXISTS `api_point`;
CREATE TABLE `api_point` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL,
  `points` int(11) NOT NULL,
  `max_points` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_point_type_6338b8cabc4a0b13_uniq` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `api_point`
-- ----------------------------
BEGIN;
INSERT INTO `api_point` VALUES ('1', '0', '10', null), ('2', '1', '10', null), ('3', '2', '10', null), ('4', '3', '1', null), ('5', '4', '5', null), ('6', '5', '5', null), ('7', '7', '2', null), ('8', '6', '2', '10'), ('9', '8', '10', null);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
