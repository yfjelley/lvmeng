/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50629
 Source Host           : localhost
 Source Database       : lvmeng

 Target Server Type    : MySQL
 Target Server Version : 50629
 File Encoding         : utf-8

 Date: 05/25/2016 14:50:44 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `api_emailvalidsecond`
-- ----------------------------
DROP TABLE IF EXISTS `api_emailvalidsecond`;
CREATE TABLE `api_emailvalidsecond` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seconds` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `api_emailvalidsecond`
-- ----------------------------
BEGIN;
INSERT INTO `api_emailvalidsecond` VALUES ('1', '3600');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
