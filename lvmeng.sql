/*
Navicat MySQL Data Transfer

Source Server         : 192.168.10.125_3306
Source Server Version : 50550
Source Host           : 192.168.10.234:3306
Source Database       : lvmeng

Target Server Type    : MYSQL
Target Server Version : 50550
File Encoding         : 65001

Date: 2016-09-14 10:29:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for agent_api_agent_version
-- ----------------------------
DROP TABLE IF EXISTS `agent_api_agent_version`;
CREATE TABLE `agent_api_agent_version` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version` varchar(10) NOT NULL,
  `url` varchar(200) NOT NULL,
  `context` varchar(100) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of agent_api_agent_version
-- ----------------------------

-- ----------------------------
-- Table structure for agent_api_cell_records_customer
-- ----------------------------
DROP TABLE IF EXISTS `agent_api_cell_records_customer`;
CREATE TABLE `agent_api_cell_records_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `agent_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `agent_api_cell_records_c_customer_id_474bcb20_fk_erp_customer_id` (`customer_id`),
  KEY `agent_api_cell_records_custome_agent_id_6698b53a_fk_erp_agent_id` (`agent_id`),
  CONSTRAINT `agent_api_cell_records_custome_agent_id_6698b53a_fk_erp_agent_id` FOREIGN KEY (`agent_id`) REFERENCES `erp_agent` (`id`),
  CONSTRAINT `agent_api_cell_records_c_customer_id_474bcb20_fk_erp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `erp_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of agent_api_cell_records_customer
-- ----------------------------

-- ----------------------------
-- Table structure for agent_api_cell_records_pcustomer
-- ----------------------------
DROP TABLE IF EXISTS `agent_api_cell_records_pcustomer`;
CREATE TABLE `agent_api_cell_records_pcustomer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `agent_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `agent_api_cell_records_p_customer_id_749c7553_fk_erp_customer_id` (`customer_id`),
  KEY `agent_api_cell_records_pcustom_agent_id_796b8aa1_fk_erp_agent_id` (`agent_id`),
  CONSTRAINT `agent_api_cell_records_pcustom_agent_id_796b8aa1_fk_erp_agent_id` FOREIGN KEY (`agent_id`) REFERENCES `erp_agent` (`id`),
  CONSTRAINT `agent_api_cell_records_p_customer_id_749c7553_fk_erp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `erp_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of agent_api_cell_records_pcustomer
-- ----------------------------

-- ----------------------------
-- Table structure for agent_api_temporary_file
-- ----------------------------
DROP TABLE IF EXISTS `agent_api_temporary_file`;
CREATE TABLE `agent_api_temporary_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `upload_time` datetime NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `agent_api_temporary_file_user_id_57bab53c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `agent_api_temporary_file_user_id_57bab53c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of agent_api_temporary_file
-- ----------------------------

-- ----------------------------
-- Table structure for api_attention
-- ----------------------------
DROP TABLE IF EXISTS `api_attention`;
CREATE TABLE `api_attention` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `register_time` datetime DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_attention_customer_id_700c9aea_uniq` (`customer_id`,`product_id`),
  KEY `api_attention_product_id_1c2024a2_fk_erp_product_id` (`product_id`),
  CONSTRAINT `api_attention_customer_id_7df0b248_fk_erp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `erp_customer` (`id`),
  CONSTRAINT `api_attention_product_id_1c2024a2_fk_erp_product_id` FOREIGN KEY (`product_id`) REFERENCES `erp_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_attention
-- ----------------------------

-- ----------------------------
-- Table structure for api_checkin
-- ----------------------------
DROP TABLE IF EXISTS `api_checkin`;
CREATE TABLE `api_checkin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `continuous_days` int(10) unsigned DEFAULT NULL,
  `abscissa` varchar(30) DEFAULT NULL,
  `latest_date` date DEFAULT NULL,
  `ordinate` varchar(30) DEFAULT NULL,
  `points` int(10) unsigned DEFAULT NULL,
  `user_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `api_checkin_user_id_34c283d0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_checkin
-- ----------------------------
INSERT INTO `api_checkin` VALUES ('1', '10', '0', '2016-05-16', '0', '10', null);
INSERT INTO `api_checkin` VALUES ('2', '0', null, null, null, '10', '112');
INSERT INTO `api_checkin` VALUES ('3', '0', null, null, null, '10', '113');

-- ----------------------------
-- Table structure for api_collection
-- ----------------------------
DROP TABLE IF EXISTS `api_collection`;
CREATE TABLE `api_collection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `register_time` datetime DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_collection_customer_id_506c6cbb_uniq` (`customer_id`,`product_id`),
  KEY `api_collection_product_id_618394f3_fk_erp_product_id` (`product_id`),
  CONSTRAINT `api_collection_customer_id_22fd20cf_fk_erp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `erp_customer` (`id`),
  CONSTRAINT `api_collection_product_id_618394f3_fk_erp_product_id` FOREIGN KEY (`product_id`) REFERENCES `erp_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_collection
-- ----------------------------

-- ----------------------------
-- Table structure for api_comment
-- ----------------------------
DROP TABLE IF EXISTS `api_comment`;
CREATE TABLE `api_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(1000) NOT NULL,
  `time` datetime NOT NULL,
  `headline_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `is_valid` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_comment_headline_id_3062c74b_fk_api_headline_id` (`headline_id`),
  KEY `api_comment_user_id_67e7baa6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `api_comment_headline_id_3062c74b_fk_api_headline_id` FOREIGN KEY (`headline_id`) REFERENCES `api_headline` (`id`),
  CONSTRAINT `api_comment_user_id_67e7baa6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_comment
-- ----------------------------

-- ----------------------------
-- Table structure for api_comment_praise
-- ----------------------------
DROP TABLE IF EXISTS `api_comment_praise`;
CREATE TABLE `api_comment_praise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `comment_id` (`comment_id`,`user_id`),
  KEY `api_comment_praise_user_id_2d0ca0d0_fk_auth_user_id` (`user_id`),
  CONSTRAINT `api_comment_praise_comment_id_2d0e3479_fk_api_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `api_comment` (`id`),
  CONSTRAINT `api_comment_praise_user_id_2d0ca0d0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_comment_praise
-- ----------------------------

-- ----------------------------
-- Table structure for api_emailcode
-- ----------------------------
DROP TABLE IF EXISTS `api_emailcode`;
CREATE TABLE `api_emailcode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `code` varchar(18) NOT NULL,
  `register_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_emailcode
-- ----------------------------

-- ----------------------------
-- Table structure for api_emailvalidsecond
-- ----------------------------
DROP TABLE IF EXISTS `api_emailvalidsecond`;
CREATE TABLE `api_emailvalidsecond` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seconds` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_emailvalidsecond
-- ----------------------------

-- ----------------------------
-- Table structure for api_headline
-- ----------------------------
DROP TABLE IF EXISTS `api_headline`;
CREATE TABLE `api_headline` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `register_date` datetime DEFAULT NULL,
  `title` varchar(30) NOT NULL,
  `context` longtext,
  `url` varchar(200) DEFAULT NULL,
  `picture` varchar(100) DEFAULT NULL,
  `read_num` int(10) unsigned DEFAULT NULL,
  `add_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_headline_title_431e5713_uniq` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_headline
-- ----------------------------
INSERT INTO `api_headline` VALUES ('3', '2016-04-18 14:32:27', '金融2号', '<p><span style=\"font-size: medium;\">中新社香港5月18日电(记者 赵建华)全国人大常委会委员长张德江18日在香港谈了对&ldquo;一国两制&rdquo;和香港问题的看法。他说，概括起来就是三句话：勿忘初心、保持耐心、坚定信心。</span></p>', null, 'api/headlines/kfue3huzzt0v7ifb8n6lfikoyjunvcpd9gejbgvnfszpvkhgmpxknhlimcbw.jpg', '5', null);
INSERT INTO `api_headline` VALUES ('6', '2016-05-19 13:09:17', '和规范化', '<p><span style=\"font-size: medium;\">如邻家大哥般唠家常 李克强：给教学科研人员更多经费使用权 两高：贪污万元可追刑责 终身监禁不得减刑 [两高明确贪污受贿案量刑 标准:5千改3万 终身监禁不得减刑假释] 江苏493名学生患病 新校污染物超标10万倍 [学校未批先建 有学生患癌 环保部调查 锐见:谁该负责 视频] 广东原副省长刘志庚严重违纪被开除党籍1 [通报称其搞权色交易 被举报拜假和尚为师 &ldquo;师父&rdquo;被逐后报复]</span></p>', null, 'api/headlines/8fww3xwygg9jqgj1kxj5gyfofr8r5iic6qhjm9baafeepnystz2dbw0aexnl.png', '17', null);
INSERT INTO `api_headline` VALUES ('7', '2016-06-06 16:07:55', '范德萨发斯蒂芬', '<p>发生的房顶上发送到发送到</p>', null, 'api/headlines/w4wk04uu1pk68hdtunoxgtmus4rfw4fvjmmpofanytysihvgvoockz7yei50.jpg', '0', null);
INSERT INTO `api_headline` VALUES ('8', '2016-06-06 16:12:05', '范德萨发生的', '<p>会很反感恢复恢复规划</p>', null, 'api/headlines/qmhsl8hiurcmweqkf1prfueadgta8pdeo9jlw89druib3shofc6u4ticwkie.jpg', '0', null);
INSERT INTO `api_headline` VALUES ('9', '2016-06-20 14:35:25', 'dsdsdsd', '<p>cdscdssdcd</p>', null, 'api/headlines/6hhxehpzjkkmsjjd2ccvyxnmrtvrujxrdkxcv63gzlpaxz18ibfps3zw5ex1.jpg', '0', null);
INSERT INTO `api_headline` VALUES ('10', '2016-07-21 14:24:53', '件合格机构', '<p>jhhjhj</p>', null, 'api/headlines/bobrgp0r6fl4t6kvds7iyabjdrkofzik0hslwkh1pk43dtevkqcz8d6vmccd.png', '0', '2016-07-04');
INSERT INTO `api_headline` VALUES ('11', '2016-07-04 00:00:00', 'yyy', '<p>eee</p>', null, '', '0', '2016-07-04');
INSERT INTO `api_headline` VALUES ('12', '2016-07-04 00:00:00', '计划', '<p>刚和法规和规范化</p>', null, 'api/headlines/rxzjmx0anmzowo4pumz6mbsbveybnoutqthoku1fydkarx3glsa9svcdcpiy.jpg', '0', '2016-07-04');
INSERT INTO `api_headline` VALUES ('13', '2016-07-04 16:56:22', '空间和空间好看', '<p>考虑空间了监控路口</p>', null, 'api/headlines/7xzduginpitwhn0f6j6ve7oyujjd4e2wppycaa4shpbbcdpenvtl3yewijin.jpg', '0', '2016-07-04');

-- ----------------------------
-- Table structure for api_history_checkin
-- ----------------------------
DROP TABLE IF EXISTS `api_history_checkin`;
CREATE TABLE `api_history_checkin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `register_date` date DEFAULT NULL,
  `abscissa` varchar(30) NOT NULL,
  `ordinate` varchar(30) NOT NULL,
  `user_id` int(11),
  PRIMARY KEY (`id`),
  KEY `api_history_checkin_e8701ad4` (`user_id`),
  CONSTRAINT `api_history_checkin_user_id_14582311_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_history_checkin
-- ----------------------------

-- ----------------------------
-- Table structure for api_point
-- ----------------------------
DROP TABLE IF EXISTS `api_point`;
CREATE TABLE `api_point` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL,
  `points` int(11) NOT NULL,
  `max_points` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_point_type_6338b8cabc4a0b13_uniq` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_point
-- ----------------------------
INSERT INTO `api_point` VALUES ('1', '0', '10', null);
INSERT INTO `api_point` VALUES ('2', '1', '10', null);
INSERT INTO `api_point` VALUES ('3', '2', '10', null);
INSERT INTO `api_point` VALUES ('4', '3', '1', null);
INSERT INTO `api_point` VALUES ('5', '4', '5', null);
INSERT INTO `api_point` VALUES ('6', '5', '5', null);
INSERT INTO `api_point` VALUES ('7', '7', '2', null);
INSERT INTO `api_point` VALUES ('8', '6', '2', '10');
INSERT INTO `api_point` VALUES ('9', '8', '10', null);

-- ----------------------------
-- Table structure for api_validsecond
-- ----------------------------
DROP TABLE IF EXISTS `api_validsecond`;
CREATE TABLE `api_validsecond` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seconds` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_validsecond
-- ----------------------------
INSERT INTO `api_validsecond` VALUES ('1', '300');

-- ----------------------------
-- Table structure for api_verificationcode
-- ----------------------------
DROP TABLE IF EXISTS `api_verificationcode`;
CREATE TABLE `api_verificationcode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phoneNum` varchar(18) NOT NULL,
  `code` varchar(18) NOT NULL,
  `register_date` datetime NOT NULL,
  `purpose` varchar(18) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_verificationcode
-- ----------------------------
INSERT INTO `api_verificationcode` VALUES ('1', '13520404512', '701440', '2016-03-17 15:48:59', '注册验证');
INSERT INTO `api_verificationcode` VALUES ('2', '13520404512', '496591', '2016-03-17 16:05:41', '注册验证');
INSERT INTO `api_verificationcode` VALUES ('3', '13520404512', '634668', '2016-03-17 16:41:31', '注册验证');
INSERT INTO `api_verificationcode` VALUES ('4', '18701730286', '866384', '2016-07-22 10:44:18', '0');
INSERT INTO `api_verificationcode` VALUES ('5', '13520404512', '814122', '2016-07-22 10:46:20', '0');
INSERT INTO `api_verificationcode` VALUES ('6', '18701212121', '720999', '2016-07-22 14:59:09', '0');
INSERT INTO `api_verificationcode` VALUES ('7', '18701730286', '313186', '2016-07-26 11:55:45', '0');
INSERT INTO `api_verificationcode` VALUES ('8', '13917757705', '689558', '2016-07-27 13:25:42', '0');
INSERT INTO `api_verificationcode` VALUES ('9', '18701730286', '255512', '2016-08-05 11:14:55', '0');
INSERT INTO `api_verificationcode` VALUES ('10', '18701730286', '310434', '2016-08-08 14:04:12', '0');
INSERT INTO `api_verificationcode` VALUES ('11', '18701730286', '139631', '2016-08-08 14:09:15', '0');
INSERT INTO `api_verificationcode` VALUES ('12', '15422445525', '147396', '2016-08-08 14:56:08', '0');
INSERT INTO `api_verificationcode` VALUES ('13', '18701730286', '609760', '2016-08-10 10:32:35', '0');
INSERT INTO `api_verificationcode` VALUES ('14', '18701730286', '918816', '2016-08-10 10:38:26', '0');
INSERT INTO `api_verificationcode` VALUES ('15', '18221888969', '506844', '2016-08-10 10:40:22', '0');
INSERT INTO `api_verificationcode` VALUES ('16', '17722493271', '759363', '2016-08-10 10:42:38', '0');
INSERT INTO `api_verificationcode` VALUES ('17', '18701730286', '192972', '2016-08-10 15:07:40', '0');
INSERT INTO `api_verificationcode` VALUES ('18', '18701730286', '164700', '2016-08-10 15:20:20', '0');
INSERT INTO `api_verificationcode` VALUES ('19', '15221243212', '688589', '2016-08-10 15:30:50', '0');
INSERT INTO `api_verificationcode` VALUES ('20', '15221243218', '386120', '2016-08-10 15:33:41', '0');
INSERT INTO `api_verificationcode` VALUES ('21', '18221888969', '874432', '2016-08-10 15:36:10', '0');
INSERT INTO `api_verificationcode` VALUES ('22', '15221243218', '280354', '2016-08-10 15:41:44', '0');
INSERT INTO `api_verificationcode` VALUES ('23', '18714758659', '603850', '2016-08-10 15:48:13', '0');
INSERT INTO `api_verificationcode` VALUES ('24', '18221888969', '497005', '2016-08-10 16:01:44', '0');
INSERT INTO `api_verificationcode` VALUES ('25', '18701730286', '983411', '2016-08-11 13:59:04', '0');
INSERT INTO `api_verificationcode` VALUES ('26', '18701730286', '739722', '2016-08-15 11:43:11', '0');
INSERT INTO `api_verificationcode` VALUES ('27', '18701730286', '941696', '2016-08-16 16:13:58', '0');
INSERT INTO `api_verificationcode` VALUES ('28', '18701730286', '627181', '2016-08-22 09:55:58', '0');
INSERT INTO `api_verificationcode` VALUES ('29', '18701730286', '879288', '2016-08-22 10:20:16', '0');

-- ----------------------------
-- Table structure for api_version
-- ----------------------------
DROP TABLE IF EXISTS `api_version`;
CREATE TABLE `api_version` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version` varchar(10) NOT NULL,
  `url` varchar(200) NOT NULL,
  `date` datetime DEFAULT NULL,
  `context` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of api_version
-- ----------------------------

-- ----------------------------
-- Table structure for authtoken_token
-- ----------------------------
DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_535fb363_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authtoken_token
-- ----------------------------
INSERT INTO `authtoken_token` VALUES ('37e8aac7826d9118ed4ccdb8435f4b16798c485f', '2016-03-16 15:55:44', '28');
INSERT INTO `authtoken_token` VALUES ('fa7fe22f67537f045856d03848e8b7f9ab55ebbd', '2016-03-17 14:41:13', '24');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=255 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add token', '7', 'add_token');
INSERT INTO `auth_permission` VALUES ('20', 'Can change token', '7', 'change_token');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete token', '7', 'delete_token');
INSERT INTO `auth_permission` VALUES ('22', 'Can add registration profile', '8', 'add_registrationprofile');
INSERT INTO `auth_permission` VALUES ('23', 'Can change registration profile', '8', 'change_registrationprofile');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete registration profile', '8', 'delete_registrationprofile');
INSERT INTO `auth_permission` VALUES ('25', 'Can add cors model', '9', 'add_corsmodel');
INSERT INTO `auth_permission` VALUES ('26', 'Can change cors model', '9', 'change_corsmodel');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete cors model', '9', 'delete_corsmodel');
INSERT INTO `auth_permission` VALUES ('28', 'Can add business', '10', 'add_business');
INSERT INTO `auth_permission` VALUES ('29', 'Can change business', '10', 'change_business');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete business', '10', 'delete_business');
INSERT INTO `auth_permission` VALUES ('31', 'Can add agent', '11', 'add_agent');
INSERT INTO `auth_permission` VALUES ('32', 'Can change agent', '11', 'change_agent');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete agent', '11', 'delete_agent');
INSERT INTO `auth_permission` VALUES ('34', 'Can add product', '12', 'add_product');
INSERT INTO `auth_permission` VALUES ('35', 'Can change product', '12', 'change_product');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete product', '12', 'delete_product');
INSERT INTO `auth_permission` VALUES ('37', 'Can add customer', '13', 'add_customer');
INSERT INTO `auth_permission` VALUES ('38', 'Can change customer', '13', 'change_customer');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete customer', '13', 'delete_customer');
INSERT INTO `auth_permission` VALUES ('43', 'Can add purchase', '15', 'add_purchase');
INSERT INTO `auth_permission` VALUES ('44', 'Can change purchase', '15', 'change_purchase');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete purchase', '15', 'delete_purchase');
INSERT INTO `auth_permission` VALUES ('46', 'Can add version', '16', 'add_version');
INSERT INTO `auth_permission` VALUES ('47', 'Can change version', '16', 'change_version');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete version', '16', 'delete_version');
INSERT INTO `auth_permission` VALUES ('52', 'Can add headline', '18', 'add_headline');
INSERT INTO `auth_permission` VALUES ('53', 'Can change headline', '18', 'change_headline');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete headline', '18', 'delete_headline');
INSERT INTO `auth_permission` VALUES ('55', 'Can add checkin', '19', 'add_checkin');
INSERT INTO `auth_permission` VALUES ('56', 'Can change checkin', '19', 'change_checkin');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete checkin', '19', 'delete_checkin');
INSERT INTO `auth_permission` VALUES ('77', 'Can add product_ type', '20', 'add_product_type');
INSERT INTO `auth_permission` VALUES ('78', 'Can change product_ type', '20', 'change_product_type');
INSERT INTO `auth_permission` VALUES ('79', 'Can delete product_ type', '20', 'delete_product_type');
INSERT INTO `auth_permission` VALUES ('84', 'Can add valid second', '22', 'add_validsecond');
INSERT INTO `auth_permission` VALUES ('85', 'Can change valid second', '22', 'change_validsecond');
INSERT INTO `auth_permission` VALUES ('86', 'Can delete valid second', '22', 'delete_validsecond');
INSERT INTO `auth_permission` VALUES ('87', 'Can add verification code', '23', 'add_verificationcode');
INSERT INTO `auth_permission` VALUES ('88', 'Can change verification code', '23', 'change_verificationcode');
INSERT INTO `auth_permission` VALUES ('89', 'Can delete verification code', '23', 'delete_verificationcode');
INSERT INTO `auth_permission` VALUES ('90', 'Can add announcement', '24', 'add_announcement');
INSERT INTO `auth_permission` VALUES ('91', 'Can change announcement', '24', 'change_announcement');
INSERT INTO `auth_permission` VALUES ('92', 'Can delete announcement', '24', 'delete_announcement');
INSERT INTO `auth_permission` VALUES ('96', 'Can add check work', '25', 'add_checkwork');
INSERT INTO `auth_permission` VALUES ('97', 'Can change check work', '25', 'change_checkwork');
INSERT INTO `auth_permission` VALUES ('98', 'Can delete check work', '25', 'delete_checkwork');
INSERT INTO `auth_permission` VALUES ('99', 'Can add check work_history', '26', 'add_checkwork_history');
INSERT INTO `auth_permission` VALUES ('100', 'Can change check work_history', '26', 'change_checkwork_history');
INSERT INTO `auth_permission` VALUES ('101', 'Can delete check work_history', '26', 'delete_checkwork_history');
INSERT INTO `auth_permission` VALUES ('102', 'Can add check work', '27', 'add_checkwork');
INSERT INTO `auth_permission` VALUES ('103', 'Can change check work', '27', 'change_checkwork');
INSERT INTO `auth_permission` VALUES ('104', 'Can delete check work', '27', 'delete_checkwork');
INSERT INTO `auth_permission` VALUES ('105', 'Can add check work_history', '28', 'add_checkwork_history');
INSERT INTO `auth_permission` VALUES ('106', 'Can change check work_history', '28', 'change_checkwork_history');
INSERT INTO `auth_permission` VALUES ('107', 'Can delete check work_history', '28', 'delete_checkwork_history');
INSERT INTO `auth_permission` VALUES ('111', 'Can add internal_announcement', '30', 'add_internal_announcement');
INSERT INTO `auth_permission` VALUES ('112', 'Can change internal_announcement', '30', 'change_internal_announcement');
INSERT INTO `auth_permission` VALUES ('113', 'Can delete internal_announcement', '30', 'delete_internal_announcement');
INSERT INTO `auth_permission` VALUES ('114', 'Can add daily_work', '31', 'add_daily_work');
INSERT INTO `auth_permission` VALUES ('115', 'Can change daily_work', '31', 'change_daily_work');
INSERT INTO `auth_permission` VALUES ('116', 'Can delete daily_work', '31', 'delete_daily_work');
INSERT INTO `auth_permission` VALUES ('117', 'Can add cost_application', '32', 'add_cost_application');
INSERT INTO `auth_permission` VALUES ('118', 'Can change cost_application', '32', 'change_cost_application');
INSERT INTO `auth_permission` VALUES ('119', 'Can delete cost_application', '32', 'delete_cost_application');
INSERT INTO `auth_permission` VALUES ('120', 'Can add leave_management', '33', 'add_leave_management');
INSERT INTO `auth_permission` VALUES ('121', 'Can change leave_management', '33', 'change_leave_management');
INSERT INTO `auth_permission` VALUES ('122', 'Can delete leave_management', '33', 'delete_leave_management');
INSERT INTO `auth_permission` VALUES ('123', 'Can add travel_apply', '34', 'add_travel_apply');
INSERT INTO `auth_permission` VALUES ('124', 'Can change travel_apply', '34', 'change_travel_apply');
INSERT INTO `auth_permission` VALUES ('125', 'Can delete travel_apply', '34', 'delete_travel_apply');
INSERT INTO `auth_permission` VALUES ('126', 'Can add captcha store', '35', 'add_captchastore');
INSERT INTO `auth_permission` VALUES ('127', 'Can change captcha store', '35', 'change_captchastore');
INSERT INTO `auth_permission` VALUES ('128', 'Can delete captcha store', '35', 'delete_captchastore');
INSERT INTO `auth_permission` VALUES ('129', 'Can add read_message', '36', 'add_read_message');
INSERT INTO `auth_permission` VALUES ('130', 'Can change read_message', '36', 'change_read_message');
INSERT INTO `auth_permission` VALUES ('131', 'Can delete read_message', '36', 'delete_read_message');
INSERT INTO `auth_permission` VALUES ('147', 'Can add customer_ pending', '41', 'add_customer_pending');
INSERT INTO `auth_permission` VALUES ('148', 'Can change customer_ pending', '41', 'change_customer_pending');
INSERT INTO `auth_permission` VALUES ('149', 'Can delete customer_ pending', '41', 'delete_customer_pending');
INSERT INTO `auth_permission` VALUES ('150', 'Can add cell_ records_ customer', '42', 'add_cell_records_customer');
INSERT INTO `auth_permission` VALUES ('151', 'Can change cell_ records_ customer', '42', 'change_cell_records_customer');
INSERT INTO `auth_permission` VALUES ('152', 'Can delete cell_ records_ customer', '42', 'delete_cell_records_customer');
INSERT INTO `auth_permission` VALUES ('153', 'Can add cell_ records_p customer', '43', 'add_cell_records_pcustomer');
INSERT INTO `auth_permission` VALUES ('154', 'Can change cell_ records_p customer', '43', 'change_cell_records_pcustomer');
INSERT INTO `auth_permission` VALUES ('155', 'Can delete cell_ records_p customer', '43', 'delete_cell_records_pcustomer');
INSERT INTO `auth_permission` VALUES ('156', 'Can add daily_to_do', '44', 'add_daily_to_do');
INSERT INTO `auth_permission` VALUES ('157', 'Can change daily_to_do', '44', 'change_daily_to_do');
INSERT INTO `auth_permission` VALUES ('158', 'Can delete daily_to_do', '44', 'delete_daily_to_do');
INSERT INTO `auth_permission` VALUES ('159', 'Can add message', '45', 'add_message');
INSERT INTO `auth_permission` VALUES ('160', 'Can change message', '45', 'change_message');
INSERT INTO `auth_permission` VALUES ('161', 'Can delete message', '45', 'delete_message');
INSERT INTO `auth_permission` VALUES ('162', 'Can add pending message', '45', 'add_pendingmessage');
INSERT INTO `auth_permission` VALUES ('163', 'Can change pending message', '45', 'change_pendingmessage');
INSERT INTO `auth_permission` VALUES ('164', 'Can delete pending message', '45', 'delete_pendingmessage');
INSERT INTO `auth_permission` VALUES ('166', 'Can add real_ purchase', '47', 'add_real_purchase');
INSERT INTO `auth_permission` VALUES ('167', 'Can change real_ purchase', '47', 'change_real_purchase');
INSERT INTO `auth_permission` VALUES ('168', 'Can delete real_ purchase', '47', 'delete_real_purchase');
INSERT INTO `auth_permission` VALUES ('171', 'Can add history_ checkin', '48', 'add_history_checkin');
INSERT INTO `auth_permission` VALUES ('172', 'Can change history_ checkin', '48', 'change_history_checkin');
INSERT INTO `auth_permission` VALUES ('173', 'Can delete history_ checkin', '48', 'delete_history_checkin');
INSERT INTO `auth_permission` VALUES ('176', 'Can add agent_ version', '49', 'add_agent_version');
INSERT INTO `auth_permission` VALUES ('177', 'Can change agent_ version', '49', 'change_agent_version');
INSERT INTO `auth_permission` VALUES ('178', 'Can delete agent_ version', '49', 'delete_agent_version');
INSERT INTO `auth_permission` VALUES ('179', 'Can add position', '50', 'add_position');
INSERT INTO `auth_permission` VALUES ('180', 'Can change position', '50', 'change_position');
INSERT INTO `auth_permission` VALUES ('181', 'Can delete position', '50', 'delete_position');
INSERT INTO `auth_permission` VALUES ('182', 'Can add collection', '51', 'add_collection');
INSERT INTO `auth_permission` VALUES ('183', 'Can change collection', '51', 'change_collection');
INSERT INTO `auth_permission` VALUES ('184', 'Can delete collection', '51', 'delete_collection');
INSERT INTO `auth_permission` VALUES ('185', 'Can add attention', '52', 'add_attention');
INSERT INTO `auth_permission` VALUES ('186', 'Can change attention', '52', 'change_attention');
INSERT INTO `auth_permission` VALUES ('187', 'Can delete attention', '52', 'delete_attention');
INSERT INTO `auth_permission` VALUES ('188', 'Can add lv_ announcement', '53', 'add_lv_announcement');
INSERT INTO `auth_permission` VALUES ('189', 'Can change lv_ announcement', '53', 'change_lv_announcement');
INSERT INTO `auth_permission` VALUES ('190', 'Can delete lv_ announcement', '53', 'delete_lv_announcement');
INSERT INTO `auth_permission` VALUES ('194', 'Can add all_ examine', '55', 'add_all_examine');
INSERT INTO `auth_permission` VALUES ('195', 'Can change all_ examine', '55', 'change_all_examine');
INSERT INTO `auth_permission` VALUES ('196', 'Can delete all_ examine', '55', 'delete_all_examine');
INSERT INTO `auth_permission` VALUES ('197', 'Can add cost_examine', '56', 'add_cost_examine');
INSERT INTO `auth_permission` VALUES ('198', 'Can change cost_examine', '56', 'change_cost_examine');
INSERT INTO `auth_permission` VALUES ('199', 'Can delete cost_examine', '56', 'delete_cost_examine');
INSERT INTO `auth_permission` VALUES ('200', 'Can add leave_examine', '57', 'add_leave_examine');
INSERT INTO `auth_permission` VALUES ('201', 'Can change leave_examine', '57', 'change_leave_examine');
INSERT INTO `auth_permission` VALUES ('202', 'Can delete leave_examine', '57', 'delete_leave_examine');
INSERT INTO `auth_permission` VALUES ('203', 'Can add travel_examine', '58', 'add_travel_examine');
INSERT INTO `auth_permission` VALUES ('204', 'Can change travel_examine', '58', 'change_travel_examine');
INSERT INTO `auth_permission` VALUES ('205', 'Can delete travel_examine', '58', 'delete_travel_examine');
INSERT INTO `auth_permission` VALUES ('206', 'Can add email valid second', '59', 'add_emailvalidsecond');
INSERT INTO `auth_permission` VALUES ('207', 'Can change email valid second', '59', 'change_emailvalidsecond');
INSERT INTO `auth_permission` VALUES ('208', 'Can delete email valid second', '59', 'delete_emailvalidsecond');
INSERT INTO `auth_permission` VALUES ('209', 'Can add email code', '60', 'add_emailcode');
INSERT INTO `auth_permission` VALUES ('210', 'Can change email code', '60', 'change_emailcode');
INSERT INTO `auth_permission` VALUES ('211', 'Can delete email code', '60', 'delete_emailcode');
INSERT INTO `auth_permission` VALUES ('212', 'Can add point', '61', 'add_point');
INSERT INTO `auth_permission` VALUES ('213', 'Can change point', '61', 'change_point');
INSERT INTO `auth_permission` VALUES ('214', 'Can delete point', '61', 'delete_point');
INSERT INTO `auth_permission` VALUES ('215', 'Can add business_carousel', '62', 'add_business_carousel');
INSERT INTO `auth_permission` VALUES ('216', 'Can change business_carousel', '62', 'change_business_carousel');
INSERT INTO `auth_permission` VALUES ('217', 'Can delete business_carousel', '62', 'delete_business_carousel');
INSERT INTO `auth_permission` VALUES ('218', '新增/修改/删除公司公告(外部)', '2', 'business_announcement_out');
INSERT INTO `auth_permission` VALUES ('219', '新增/修改/删除产品', '2', 'product_process');
INSERT INTO `auth_permission` VALUES ('220', '客户查看', '2', 'customer_show');
INSERT INTO `auth_permission` VALUES ('221', '新增/修改/删除公司公告(内部)', '2', 'business_announcement_inner');
INSERT INTO `auth_permission` VALUES ('222', '公司基本信息修改', '2', 'business_info_modify');
INSERT INTO `auth_permission` VALUES ('223', '财务管理', '2', 'financial_management');
INSERT INTO `auth_permission` VALUES ('224', '新增/修改/删除员工账户信息', '2', 'employee_process');
INSERT INTO `auth_permission` VALUES ('225', '员工查看', '2', 'employee_show');
INSERT INTO `auth_permission` VALUES ('226', '考勤管理', '2', 'check_work');
INSERT INTO `auth_permission` VALUES ('227', 'Can add source', '63', 'add_source');
INSERT INTO `auth_permission` VALUES ('228', 'Can change source', '63', 'change_source');
INSERT INTO `auth_permission` VALUES ('229', 'Can delete source', '63', 'delete_source');
INSERT INTO `auth_permission` VALUES ('230', 'Can add thumbnail', '64', 'add_thumbnail');
INSERT INTO `auth_permission` VALUES ('231', 'Can change thumbnail', '64', 'change_thumbnail');
INSERT INTO `auth_permission` VALUES ('232', 'Can delete thumbnail', '64', 'delete_thumbnail');
INSERT INTO `auth_permission` VALUES ('233', 'Can add thumbnail dimensions', '65', 'add_thumbnaildimensions');
INSERT INTO `auth_permission` VALUES ('234', 'Can change thumbnail dimensions', '65', 'change_thumbnaildimensions');
INSERT INTO `auth_permission` VALUES ('235', 'Can delete thumbnail dimensions', '65', 'delete_thumbnaildimensions');
INSERT INTO `auth_permission` VALUES ('236', 'Can add temporary_ file', '66', 'add_temporary_file');
INSERT INTO `auth_permission` VALUES ('237', 'Can change temporary_ file', '66', 'change_temporary_file');
INSERT INTO `auth_permission` VALUES ('238', 'Can delete temporary_ file', '66', 'delete_temporary_file');
INSERT INTO `auth_permission` VALUES ('239', 'Can add comment', '67', 'add_comment');
INSERT INTO `auth_permission` VALUES ('240', 'Can change comment', '67', 'change_comment');
INSERT INTO `auth_permission` VALUES ('241', 'Can delete comment', '67', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('245', 'Can add redister_ business', '69', 'add_redister_business');
INSERT INTO `auth_permission` VALUES ('246', 'Can change redister_ business', '69', 'change_redister_business');
INSERT INTO `auth_permission` VALUES ('247', 'Can delete redister_ business', '69', 'delete_redister_business');
INSERT INTO `auth_permission` VALUES ('248', 'Can add check_ time_ setting', '70', 'add_check_time_setting');
INSERT INTO `auth_permission` VALUES ('249', 'Can change check_ time_ setting', '70', 'change_check_time_setting');
INSERT INTO `auth_permission` VALUES ('250', 'Can delete check_ time_ setting', '70', 'delete_check_time_setting');
INSERT INTO `auth_permission` VALUES ('251', '考勤时间设定', '2', 'check_time_setting');
INSERT INTO `auth_permission` VALUES ('252', 'Can add online_chat', '71', 'add_online_chat');
INSERT INTO `auth_permission` VALUES ('253', 'Can change online_chat', '71', 'change_online_chat');
INSERT INTO `auth_permission` VALUES ('254', 'Can delete online_chat', '71', 'delete_online_chat');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$20000$BYpXBjCwK7Ng$sKjRiGz+eipjVhWacH6ap8zM3DlHEhfbxguQMfdolmQ=', '2016-09-07 15:04:07', '1', 'admin', '律錳管理', '超级管理员', 'admin@qq.com', '1', '1', '2016-03-08 16:38:00');
INSERT INTO `auth_user` VALUES ('17', 'pbkdf2_sha256$20000$JZKB3KwkNOu8$B7MXqAToGnXPjeB5d48/c+DOr7RiQKMFVz3h0qZ+ZoE=', '2016-09-07 16:07:15', '0', '1668380928@qq.com1', '上海凡达', '客户机构', '1668380928@qq.com', '0', '1', '2016-03-10 14:30:00');
INSERT INTO `auth_user` VALUES ('18', 'pbkdf2_sha256$20000$99PTTUhsK769$bibDs6RDYhbljPYhJttr5byKYIrAnIp+0GAMbs2HWBM=', '2016-04-27 15:47:00', '0', '18725698756', '浙江华硕', '客户机构', '819493212@qq.com', '0', '1', '2016-03-10 14:33:00');
INSERT INTO `auth_user` VALUES ('20', 'pbkdf2_sha256$20000$zwcwBOAdDGBh$kuYbxNXaDWDqT+/MhFEGuzlqM1tG4b+DxHtDlQh3DWo=', '2016-04-27 14:38:00', '0', '18725698758', '温州忽悠', '客户机构', '819493212@qq.com', '0', '1', '2016-03-10 14:35:00');
INSERT INTO `auth_user` VALUES ('21', 'pbkdf2_sha256$20000$waJZ1wHh7vZS$uhSMvOVx9B1vEDlxvo6mDOxCV6IXj65+JNmyAcUCb3M=', '2016-09-13 16:28:38', '0', 'B0011', 'ssss', '员工', '18701730286@163.com', '0', '1', '2016-03-10 15:57:39');
INSERT INTO `auth_user` VALUES ('22', 'pbkdf2_sha256$20000$rAilLYHEeCRM$30+SKx3fJP4HdOdwvYjWGmqu0a1WSwUVEbvYfiERUF0=', '2016-04-22 15:55:12', '0', '18701752689', '王二小', '员工', '', '0', '0', '2016-03-10 16:23:51');
INSERT INTO `auth_user` VALUES ('23', 'pbkdf2_sha256$20000$EPBXFtPugKT5$55clxWTJ+OyxYnCAas0hIAY/dHg7pz+vqmgFTT1aDyk=', '2016-04-01 14:03:26', '0', '18701730222', '王五字', '员工', '', '0', '1', '2016-03-11 09:26:07');
INSERT INTO `auth_user` VALUES ('24', 'pbkdf2_sha256$20000$GkJAQpro6t7e$H7YJYxYCaeJYdNseqsgNF4uccLpry97Vam/xJVx0+eQ=', '2016-08-03 11:39:42', '0', '18701789653', '黎明', '客户', '', '0', '1', '2016-03-11 09:36:52');
INSERT INTO `auth_user` VALUES ('25', 'pbkdf2_sha256$20000$Hqqol3r3QShI$8kGSIj2LAlAatum5hFOwHNxD5ltFIC9Dx8fN6esRfbA=', '2016-07-26 14:39:52', '0', '18701730556', '上海你猜', '客户机构', '1668380928@qq.com', '0', '1', '2016-03-14 15:04:00');
INSERT INTO `auth_user` VALUES ('26', 'pbkdf2_sha256$20000$oClJK5n9IHIO$ZfSZctn3ZK0nHDpi4E9fuCyX5REtj7i+PjNfmDtaY6s=', '2016-06-06 16:37:49', '0', 'B8883', '王麻子', '员工', '18701730286@qq.com', '0', '1', '2016-03-14 15:22:49');
INSERT INTO `auth_user` VALUES ('27', 'pbkdf2_sha256$20000$pKV9lWMkpX6l$+YTizpDJErVuu2AqohjUOVA1KtYWNzPVGHl1/AH/GHw=', '2016-03-28 09:56:56', '0', '18758965485', '立柱', '会计', '', '0', '1', '2016-03-14 15:24:36');
INSERT INTO `auth_user` VALUES ('28', 'pbkdf2_sha256$20000$yySFOVSRJh0I$chZP8VLIkGt7jh6NSozUwqthIITGjcRZm+cqqZ+4Qcw=', '2016-05-19 16:51:41', '0', '18701736526', '灰机', '客户', '', '0', '1', '2016-03-14 15:28:43');
INSERT INTO `auth_user` VALUES ('29', 'pbkdf2_sha256$20000$zPym6Egszbkh$H3PAJKnUACdulxcZ/SoQ4Uq1FHgFUGU112uV0tLJ8VE=', '2016-06-16 15:50:32', '0', 'B0024', '赵四', '员工', '', '0', '1', '2016-03-14 16:21:26');
INSERT INTO `auth_user` VALUES ('32', 'pbkdf2_sha256$20000$H2B39AXTI88J$TGlZtpU9sGMhPiQTv+Nxe6BBF/AeF4y7IVY8svpHShM=', null, '0', '13520404512', '李志', '客户', '', '0', '1', '2016-03-17 16:41:51');
INSERT INTO `auth_user` VALUES ('40', 'pbkdf2_sha256$20000$wV7urQNJkXEh$uMyDkDvQ6KGKeo7iqoo4sHs13JcmC2aVMErQIHi9hXU=', '2016-07-29 16:11:00', '0', 'B00111', '张思', '员工', '1668380928@qq.com', '0', '1', '2016-04-22 15:28:30');
INSERT INTO `auth_user` VALUES ('45', 'pbkdf2_sha256$20000$lHn8raCbmyE0$ymP3UHjeHhoSUvdd6qBwT8ZuD+g2l7BNmP72ugk5nqU=', null, '0', '55555@qq.com', '浙江沪和', '客户机构', '55555@qq.com', '0', '1', '2016-04-22 15:53:04');
INSERT INTO `auth_user` VALUES ('47', 'pbkdf2_sha256$20000$cqXFJUDpUhq7$BJUnCO3kKo8oOsTcYAuZWXeSMJBUkeoH0ZZLoREwbmk=', null, '0', '727053701@qq.com', '涠洲达华', '客户机构', '727053701@qq.com', '0', '1', '2016-04-26 10:09:00');
INSERT INTO `auth_user` VALUES ('50', 'pbkdf2_sha256$20000$s1d1Xzmx7XOQ$+amXhbEEo0IsjJXKcYA1bgGGXET6ZuWk6c+8wCAQLOk=', null, '0', '18722566996', '呵呵', '员工', '', '0', '0', '2016-04-27 14:14:28');
INSERT INTO `auth_user` VALUES ('51', 'pbkdf2_sha256$20000$Ynplfu4n4FGa$DBnc71Ck4GR7wi+jYcHT4+AsqfUUcx7mnxJVsT7Q3mY=', null, '0', '13438385598', '回家', '员工', '', '0', '0', '2016-04-27 14:39:33');
INSERT INTO `auth_user` VALUES ('52', 'pbkdf2_sha256$20000$TdGysV5tmv6F$RQO33lMREBTkFFEw9hhCBt65ukWK8Qs1zCb5IlDOETA=', '2016-05-26 14:30:30', '0', 'B0031', '回家', '员工', '', '0', '1', '2016-04-27 14:41:12');
INSERT INTO `auth_user` VALUES ('53', 'pbkdf2_sha256$20000$WC003nWA85fZ$q3s44ceTVna3jFgh7ZAP3AMa2nOeKGiBfjK/O1n4TsE=', null, '0', 'B0032', '地方', '员工', '', '0', '1', '2016-04-27 14:52:24');
INSERT INTO `auth_user` VALUES ('54', 'pbkdf2_sha256$20000$MvGiXBvmUD9l$YaUr/Z7mSAfqYy84315+UaUxQorQFfFb9sbN2FdwcYs=', null, '0', 'B0033', '高的', '员工', '', '0', '1', '2016-04-27 14:56:50');
INSERT INTO `auth_user` VALUES ('55', 'pbkdf2_sha256$20000$A0VhvPN9oN1T$iWoHreAZMp7vAyRsl4QtJz2bz7+gX+45nWgx4dTZTTA=', null, '0', 'B0034', '发个', '员工', '', '0', '1', '2016-04-27 15:21:23');
INSERT INTO `auth_user` VALUES ('56', 'pbkdf2_sha256$20000$rAFnFDRY5E1J$ufCamYSZfT26qogf4vv1MOhAbPAMGrDfawVqIeYgW4s=', '2016-07-27 15:15:15', '0', 'B0035', '链接', '员工', '', '0', '1', '2016-04-27 15:23:07');
INSERT INTO `auth_user` VALUES ('57', 'pbkdf2_sha256$20000$vwnLt7PM8srh$r9hIF5Tiq+J31x4BViUAzUgBoEhoX8vG4vGwpAX6uh8=', null, '0', 'B0036', '丰东股份', '员工', '', '0', '1', '2016-04-27 15:26:58');
INSERT INTO `auth_user` VALUES ('58', 'pbkdf2_sha256$20000$Msh8DMsV2qto$C0a3zjDhxYLFUaCSnHCiJOA0qliX7G09XZLkSQy5MO0=', null, '0', 'B0025', '申达', '员工', '', '0', '1', '2016-04-27 15:48:22');
INSERT INTO `auth_user` VALUES ('60', 'pbkdf2_sha256$20000$7E37KSNViGLv$bNVSqM3Nq7cVM8lyEjn9uKNxheJB6JL8aObT5M8y1iM=', null, '0', '1305251473@qq.com', '发个梵蒂冈', '客户机构', '1305251473@qq.com', '0', '1', '2016-04-28 16:59:00');
INSERT INTO `auth_user` VALUES ('66', 'pbkdf2_sha256$20000$xAn0GkeRziXI$+uiUTIVRXYmg2xWzxlaNlZ0MS4IlQ2eqYYayDJ1PGZg=', '2016-08-01 09:56:26', '0', 'B00123', '第三方', '员工', '666@qq.com', '0', '1', '2016-05-12 13:57:12');
INSERT INTO `auth_user` VALUES ('68', 'pbkdf2_sha256$20000$ZE3C8wBtmEvE$syLOYW3oY5pninLmzre2ZBlVWnFY42yEIhlMgJYIMT4=', null, '0', '18701255456', '的撒', '员工', '', '0', '1', '2016-05-12 14:01:25');
INSERT INTO `auth_user` VALUES ('75', 'pbkdf2_sha256$20000$WVSdCom9ZhTy$w0UO2xdmLzA05cnIinlP2WwNG/JaNDwN6BDaVaNw4u8=', null, '0', 'B8885', '几个点', '员工', '1668380928@qq.com', '0', '1', '2016-06-01 14:50:35');
INSERT INTO `auth_user` VALUES ('76', 'pbkdf2_sha256$20000$i65W31G160fa$XfOfJu3q3nEYEoZhXpySdh1Opwn6TWIdJbIrBHM/Dqo=', null, '0', 'B8886', '改成才', '员工', '1668380928@qq.com', '0', '1', '2016-06-01 15:29:14');
INSERT INTO `auth_user` VALUES ('77', 'pbkdf2_sha256$20000$KqwWpKIfc9ly$lty/6jFPl0PfTvoym4cHykpPpK0UYs/NPUZMbHRc6EY=', null, '0', 'B00131', 'qqq', '员工', '55555@qq.com', '0', '1', '2016-06-24 15:09:31');
INSERT INTO `auth_user` VALUES ('78', 'pbkdf2_sha256$20000$JLQua8cRg5IF$vhkXy7qrzDNEjRmug5j04AIAW+A85qIwxzPk+nZMVm0=', null, '0', 'B00132', 'qqq', '员工', '55555@qq.com', '0', '1', '2016-06-24 15:09:47');
INSERT INTO `auth_user` VALUES ('87', 'pbkdf2_sha256$20000$gizEDVPHLYpI$ZiOuqHPWBFoiZ590hTJawp0Zeeu7ohnh0ue8HGBKLLs=', '2016-07-26 15:10:58', '0', '16683860928@qq.com1', '上海力帆', '客户机构', '16683280928@qq.com', '0', '1', '2016-07-26 10:25:22');
INSERT INTO `auth_user` VALUES ('90', 'pbkdf2_sha256$20000$BVdVLcjt6N9v$1bfDfj/AwflUSwXebFnHQhlg2ygwbC7+JrE5XLvIaaM=', null, '0', '90cancel@qq.com', '深圳虎就', '客户机构', '16683809328@qq.com', '0', '0', '2016-07-26 11:56:09');
INSERT INTO `auth_user` VALUES ('93', 'pbkdf2_sha256$20000$w2KzdjrKhBvp$xwmTOcPqqyyrGgp5viRyJXkeN0TTXUeZm9ogTj2amt0=', null, '0', '1870173028611', '小王', '客户', '', '0', '1', '2016-08-08 14:22:21');
INSERT INTO `auth_user` VALUES ('106', 'pbkdf2_sha256$20000$49OuVgJOdoqy$Reqg3UDt56FyQej/YzNJ8BzaMMWBLq1PxqVLbDYDwhY=', null, '0', '177242493271', 'fdsf', '客户', '1668380928@qq.com', '0', '1', '2016-08-10 10:43:19');
INSERT INTO `auth_user` VALUES ('107', 'pbkdf2_sha256$20000$MtieFVAa5NvE$0fg2F53J2T9JxH169DuxgWyMNsZe904kQsJqZctlGnQ=', null, '0', '17722493271', 'fdsfdsfd', '客户', '1668380928@qq.com', '0', '1', '2016-08-10 11:13:54');
INSERT INTO `auth_user` VALUES ('110', 'pbkdf2_sha256$20000$AfFN5F6upyDq$IUir9/DPsW/kkhuUfJXV5LzTCDRTlOV5CURZtoiwyEI=', null, '0', '187017302868', 'fdfdfdfd', '客户', '18701730286@163.com', '0', '1', '2016-08-10 13:17:54');
INSERT INTO `auth_user` VALUES ('111', 'pbkdf2_sha256$20000$zGr22nr7Pm5Q$Douqg0ARCp1ORlpSqPJ0LfrmcA9FdI1fiIFqRGbNEXY=', null, '0', '18221888969', '发送到', '客户', '1668380928@qq.com', '0', '1', '2016-08-10 16:10:39');
INSERT INTO `auth_user` VALUES ('112', 'pbkdf2_sha256$20000$XnEU00dIz0DS$pErgj/Gt53rIqzc746MHlddewW4lHEeYAgRURyRujqE=', null, '0', '187017302865', 'dfds', '客户', '1668380928@qq.com', '0', '1', '2016-08-11 14:02:06');
INSERT INTO `auth_user` VALUES ('113', 'pbkdf2_sha256$20000$xtEcCjky29ao$v3kbxG+ncH/KMW8OT2SHc2CT6J1hKQYaCJvpjRMSVtE=', null, '0', '18701730286', 'dfds', '客户', '1668380928@qq.com', '0', '1', '2016-08-11 14:04:05');
INSERT INTO `auth_user` VALUES ('114', 'pbkdf2_sha256$20000$EdLUk0gD3LeH$6E5esOh5nHjFDcnrz9Arn980U1AVsb8FNPovCLjGKDk=', null, '0', '16683850928@qq.com', '11111', '客户机构', '1668380928@qq.com', '0', '1', '2016-08-11 17:31:25');
INSERT INTO `auth_user` VALUES ('115', 'pbkdf2_sha256$20000$56UL8JQoep28$HWl0Bb7DT9Jjty8WH/UY+FfXKSWa+BLILTJ58B9tGLI=', null, '0', '1668380928@qq.com', '防守打法', '客户机构', '1668380928@qq.com', '0', '1', '2016-08-12 11:19:03');
INSERT INTO `auth_user` VALUES ('119', 'pbkdf2_sha256$20000$Vbx2ZgttwwDn$v0oAn5GsMiNUBPDXi59o9lFRaLt4EWQWfGmDrbpK/Ks=', null, '0', 'fsdfdsf@qq.com', 'dfds', '客户机构', 'fsdfdsf@qq.com', '0', '0', '2016-08-15 11:43:11');
INSERT INTO `auth_user` VALUES ('120', 'pbkdf2_sha256$20000$6vO3EWRLlyNc$a3mzhGRsiSKCxRF/EzYepaUnIUfzDO5upsZgB7AVp5g=', null, '0', 'dsds@qq.com', '的萨达', '客户机构', 'dsds@qq.com', '0', '0', '2016-08-16 09:55:33');
INSERT INTO `auth_user` VALUES ('121', 'pbkdf2_sha256$20000$AZSXKNJ2ZFqg$lgkXszDc28rBCJjVHgO5jZEIAcuyPzI387SKr1OJxKw=', null, '0', 'dsdad@qq.com', 'dwdw', '客户机构', 'dsdad@qq.com', '0', '0', '2016-08-16 10:19:04');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2207 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
INSERT INTO `auth_user_user_permissions` VALUES ('1967', '1', '1');
INSERT INTO `auth_user_user_permissions` VALUES ('1968', '1', '2');
INSERT INTO `auth_user_user_permissions` VALUES ('1969', '1', '3');
INSERT INTO `auth_user_user_permissions` VALUES ('1970', '1', '4');
INSERT INTO `auth_user_user_permissions` VALUES ('1971', '1', '5');
INSERT INTO `auth_user_user_permissions` VALUES ('1972', '1', '6');
INSERT INTO `auth_user_user_permissions` VALUES ('1973', '1', '7');
INSERT INTO `auth_user_user_permissions` VALUES ('1974', '1', '8');
INSERT INTO `auth_user_user_permissions` VALUES ('1975', '1', '9');
INSERT INTO `auth_user_user_permissions` VALUES ('1976', '1', '10');
INSERT INTO `auth_user_user_permissions` VALUES ('1977', '1', '11');
INSERT INTO `auth_user_user_permissions` VALUES ('1978', '1', '12');
INSERT INTO `auth_user_user_permissions` VALUES ('1979', '1', '13');
INSERT INTO `auth_user_user_permissions` VALUES ('1980', '1', '14');
INSERT INTO `auth_user_user_permissions` VALUES ('1981', '1', '15');
INSERT INTO `auth_user_user_permissions` VALUES ('1982', '1', '16');
INSERT INTO `auth_user_user_permissions` VALUES ('1983', '1', '17');
INSERT INTO `auth_user_user_permissions` VALUES ('1984', '1', '18');
INSERT INTO `auth_user_user_permissions` VALUES ('1985', '1', '19');
INSERT INTO `auth_user_user_permissions` VALUES ('1986', '1', '20');
INSERT INTO `auth_user_user_permissions` VALUES ('1987', '1', '21');
INSERT INTO `auth_user_user_permissions` VALUES ('1988', '1', '22');
INSERT INTO `auth_user_user_permissions` VALUES ('1989', '1', '23');
INSERT INTO `auth_user_user_permissions` VALUES ('1990', '1', '24');
INSERT INTO `auth_user_user_permissions` VALUES ('1991', '1', '25');
INSERT INTO `auth_user_user_permissions` VALUES ('1992', '1', '26');
INSERT INTO `auth_user_user_permissions` VALUES ('1993', '1', '27');
INSERT INTO `auth_user_user_permissions` VALUES ('1994', '1', '28');
INSERT INTO `auth_user_user_permissions` VALUES ('1995', '1', '29');
INSERT INTO `auth_user_user_permissions` VALUES ('1996', '1', '30');
INSERT INTO `auth_user_user_permissions` VALUES ('1997', '1', '31');
INSERT INTO `auth_user_user_permissions` VALUES ('1998', '1', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('1999', '1', '33');
INSERT INTO `auth_user_user_permissions` VALUES ('2000', '1', '34');
INSERT INTO `auth_user_user_permissions` VALUES ('2001', '1', '35');
INSERT INTO `auth_user_user_permissions` VALUES ('2002', '1', '36');
INSERT INTO `auth_user_user_permissions` VALUES ('2003', '1', '37');
INSERT INTO `auth_user_user_permissions` VALUES ('2004', '1', '38');
INSERT INTO `auth_user_user_permissions` VALUES ('2005', '1', '39');
INSERT INTO `auth_user_user_permissions` VALUES ('2006', '1', '43');
INSERT INTO `auth_user_user_permissions` VALUES ('2007', '1', '44');
INSERT INTO `auth_user_user_permissions` VALUES ('2008', '1', '45');
INSERT INTO `auth_user_user_permissions` VALUES ('2009', '1', '46');
INSERT INTO `auth_user_user_permissions` VALUES ('2010', '1', '47');
INSERT INTO `auth_user_user_permissions` VALUES ('2011', '1', '48');
INSERT INTO `auth_user_user_permissions` VALUES ('2012', '1', '52');
INSERT INTO `auth_user_user_permissions` VALUES ('2013', '1', '53');
INSERT INTO `auth_user_user_permissions` VALUES ('2014', '1', '54');
INSERT INTO `auth_user_user_permissions` VALUES ('2015', '1', '55');
INSERT INTO `auth_user_user_permissions` VALUES ('2016', '1', '56');
INSERT INTO `auth_user_user_permissions` VALUES ('2017', '1', '57');
INSERT INTO `auth_user_user_permissions` VALUES ('2018', '1', '77');
INSERT INTO `auth_user_user_permissions` VALUES ('2019', '1', '78');
INSERT INTO `auth_user_user_permissions` VALUES ('2020', '1', '79');
INSERT INTO `auth_user_user_permissions` VALUES ('2021', '1', '84');
INSERT INTO `auth_user_user_permissions` VALUES ('2022', '1', '85');
INSERT INTO `auth_user_user_permissions` VALUES ('2023', '1', '86');
INSERT INTO `auth_user_user_permissions` VALUES ('2024', '1', '87');
INSERT INTO `auth_user_user_permissions` VALUES ('2025', '1', '88');
INSERT INTO `auth_user_user_permissions` VALUES ('2026', '1', '89');
INSERT INTO `auth_user_user_permissions` VALUES ('2027', '1', '90');
INSERT INTO `auth_user_user_permissions` VALUES ('2028', '1', '91');
INSERT INTO `auth_user_user_permissions` VALUES ('2029', '1', '92');
INSERT INTO `auth_user_user_permissions` VALUES ('2030', '1', '96');
INSERT INTO `auth_user_user_permissions` VALUES ('2031', '1', '97');
INSERT INTO `auth_user_user_permissions` VALUES ('2032', '1', '98');
INSERT INTO `auth_user_user_permissions` VALUES ('2033', '1', '99');
INSERT INTO `auth_user_user_permissions` VALUES ('2034', '1', '100');
INSERT INTO `auth_user_user_permissions` VALUES ('2035', '1', '101');
INSERT INTO `auth_user_user_permissions` VALUES ('2036', '1', '102');
INSERT INTO `auth_user_user_permissions` VALUES ('2037', '1', '103');
INSERT INTO `auth_user_user_permissions` VALUES ('2038', '1', '104');
INSERT INTO `auth_user_user_permissions` VALUES ('2039', '1', '105');
INSERT INTO `auth_user_user_permissions` VALUES ('2040', '1', '106');
INSERT INTO `auth_user_user_permissions` VALUES ('2041', '1', '107');
INSERT INTO `auth_user_user_permissions` VALUES ('2042', '1', '111');
INSERT INTO `auth_user_user_permissions` VALUES ('2043', '1', '112');
INSERT INTO `auth_user_user_permissions` VALUES ('2044', '1', '113');
INSERT INTO `auth_user_user_permissions` VALUES ('2045', '1', '114');
INSERT INTO `auth_user_user_permissions` VALUES ('2046', '1', '115');
INSERT INTO `auth_user_user_permissions` VALUES ('2047', '1', '116');
INSERT INTO `auth_user_user_permissions` VALUES ('2048', '1', '117');
INSERT INTO `auth_user_user_permissions` VALUES ('2049', '1', '118');
INSERT INTO `auth_user_user_permissions` VALUES ('2050', '1', '119');
INSERT INTO `auth_user_user_permissions` VALUES ('2051', '1', '120');
INSERT INTO `auth_user_user_permissions` VALUES ('2052', '1', '121');
INSERT INTO `auth_user_user_permissions` VALUES ('2053', '1', '122');
INSERT INTO `auth_user_user_permissions` VALUES ('2054', '1', '123');
INSERT INTO `auth_user_user_permissions` VALUES ('2055', '1', '124');
INSERT INTO `auth_user_user_permissions` VALUES ('2056', '1', '125');
INSERT INTO `auth_user_user_permissions` VALUES ('2057', '1', '126');
INSERT INTO `auth_user_user_permissions` VALUES ('2058', '1', '127');
INSERT INTO `auth_user_user_permissions` VALUES ('2059', '1', '128');
INSERT INTO `auth_user_user_permissions` VALUES ('2060', '1', '129');
INSERT INTO `auth_user_user_permissions` VALUES ('2061', '1', '130');
INSERT INTO `auth_user_user_permissions` VALUES ('2062', '1', '131');
INSERT INTO `auth_user_user_permissions` VALUES ('2063', '1', '147');
INSERT INTO `auth_user_user_permissions` VALUES ('2064', '1', '148');
INSERT INTO `auth_user_user_permissions` VALUES ('2065', '1', '149');
INSERT INTO `auth_user_user_permissions` VALUES ('2066', '1', '150');
INSERT INTO `auth_user_user_permissions` VALUES ('2067', '1', '151');
INSERT INTO `auth_user_user_permissions` VALUES ('2068', '1', '152');
INSERT INTO `auth_user_user_permissions` VALUES ('2069', '1', '153');
INSERT INTO `auth_user_user_permissions` VALUES ('2070', '1', '154');
INSERT INTO `auth_user_user_permissions` VALUES ('2071', '1', '155');
INSERT INTO `auth_user_user_permissions` VALUES ('2072', '1', '156');
INSERT INTO `auth_user_user_permissions` VALUES ('2073', '1', '157');
INSERT INTO `auth_user_user_permissions` VALUES ('2074', '1', '158');
INSERT INTO `auth_user_user_permissions` VALUES ('2075', '1', '159');
INSERT INTO `auth_user_user_permissions` VALUES ('2076', '1', '160');
INSERT INTO `auth_user_user_permissions` VALUES ('2077', '1', '161');
INSERT INTO `auth_user_user_permissions` VALUES ('2078', '1', '162');
INSERT INTO `auth_user_user_permissions` VALUES ('2079', '1', '163');
INSERT INTO `auth_user_user_permissions` VALUES ('2080', '1', '164');
INSERT INTO `auth_user_user_permissions` VALUES ('2081', '1', '166');
INSERT INTO `auth_user_user_permissions` VALUES ('2082', '1', '167');
INSERT INTO `auth_user_user_permissions` VALUES ('2083', '1', '168');
INSERT INTO `auth_user_user_permissions` VALUES ('2084', '1', '171');
INSERT INTO `auth_user_user_permissions` VALUES ('2085', '1', '172');
INSERT INTO `auth_user_user_permissions` VALUES ('2086', '1', '173');
INSERT INTO `auth_user_user_permissions` VALUES ('2087', '1', '176');
INSERT INTO `auth_user_user_permissions` VALUES ('2088', '1', '177');
INSERT INTO `auth_user_user_permissions` VALUES ('2089', '1', '178');
INSERT INTO `auth_user_user_permissions` VALUES ('2090', '1', '179');
INSERT INTO `auth_user_user_permissions` VALUES ('2091', '1', '180');
INSERT INTO `auth_user_user_permissions` VALUES ('2092', '1', '181');
INSERT INTO `auth_user_user_permissions` VALUES ('2093', '1', '182');
INSERT INTO `auth_user_user_permissions` VALUES ('2094', '1', '183');
INSERT INTO `auth_user_user_permissions` VALUES ('2095', '1', '184');
INSERT INTO `auth_user_user_permissions` VALUES ('2096', '1', '185');
INSERT INTO `auth_user_user_permissions` VALUES ('2097', '1', '186');
INSERT INTO `auth_user_user_permissions` VALUES ('2098', '1', '187');
INSERT INTO `auth_user_user_permissions` VALUES ('2099', '1', '188');
INSERT INTO `auth_user_user_permissions` VALUES ('2100', '1', '189');
INSERT INTO `auth_user_user_permissions` VALUES ('2101', '1', '190');
INSERT INTO `auth_user_user_permissions` VALUES ('2102', '1', '194');
INSERT INTO `auth_user_user_permissions` VALUES ('2103', '1', '195');
INSERT INTO `auth_user_user_permissions` VALUES ('2104', '1', '196');
INSERT INTO `auth_user_user_permissions` VALUES ('2105', '1', '197');
INSERT INTO `auth_user_user_permissions` VALUES ('2106', '1', '198');
INSERT INTO `auth_user_user_permissions` VALUES ('2107', '1', '199');
INSERT INTO `auth_user_user_permissions` VALUES ('2108', '1', '200');
INSERT INTO `auth_user_user_permissions` VALUES ('2109', '1', '201');
INSERT INTO `auth_user_user_permissions` VALUES ('2110', '1', '202');
INSERT INTO `auth_user_user_permissions` VALUES ('2111', '1', '203');
INSERT INTO `auth_user_user_permissions` VALUES ('2112', '1', '204');
INSERT INTO `auth_user_user_permissions` VALUES ('2113', '1', '205');
INSERT INTO `auth_user_user_permissions` VALUES ('2114', '1', '206');
INSERT INTO `auth_user_user_permissions` VALUES ('2115', '1', '207');
INSERT INTO `auth_user_user_permissions` VALUES ('2116', '1', '208');
INSERT INTO `auth_user_user_permissions` VALUES ('2117', '1', '209');
INSERT INTO `auth_user_user_permissions` VALUES ('2118', '1', '210');
INSERT INTO `auth_user_user_permissions` VALUES ('2119', '1', '211');
INSERT INTO `auth_user_user_permissions` VALUES ('2120', '1', '212');
INSERT INTO `auth_user_user_permissions` VALUES ('2121', '1', '213');
INSERT INTO `auth_user_user_permissions` VALUES ('2122', '1', '214');
INSERT INTO `auth_user_user_permissions` VALUES ('2123', '1', '215');
INSERT INTO `auth_user_user_permissions` VALUES ('2124', '1', '216');
INSERT INTO `auth_user_user_permissions` VALUES ('2125', '1', '217');
INSERT INTO `auth_user_user_permissions` VALUES ('2126', '1', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('2127', '1', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('2128', '1', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('2129', '1', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('2130', '1', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('2131', '1', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('2132', '1', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('2133', '1', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('2134', '1', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('2135', '1', '227');
INSERT INTO `auth_user_user_permissions` VALUES ('2136', '1', '228');
INSERT INTO `auth_user_user_permissions` VALUES ('2137', '1', '229');
INSERT INTO `auth_user_user_permissions` VALUES ('2138', '1', '230');
INSERT INTO `auth_user_user_permissions` VALUES ('2139', '1', '231');
INSERT INTO `auth_user_user_permissions` VALUES ('2140', '1', '232');
INSERT INTO `auth_user_user_permissions` VALUES ('2141', '1', '233');
INSERT INTO `auth_user_user_permissions` VALUES ('2142', '1', '234');
INSERT INTO `auth_user_user_permissions` VALUES ('2143', '1', '235');
INSERT INTO `auth_user_user_permissions` VALUES ('2144', '1', '236');
INSERT INTO `auth_user_user_permissions` VALUES ('2145', '1', '237');
INSERT INTO `auth_user_user_permissions` VALUES ('2146', '1', '238');
INSERT INTO `auth_user_user_permissions` VALUES ('2147', '1', '239');
INSERT INTO `auth_user_user_permissions` VALUES ('2148', '1', '240');
INSERT INTO `auth_user_user_permissions` VALUES ('2149', '1', '241');
INSERT INTO `auth_user_user_permissions` VALUES ('2150', '1', '245');
INSERT INTO `auth_user_user_permissions` VALUES ('2151', '1', '246');
INSERT INTO `auth_user_user_permissions` VALUES ('2152', '1', '247');
INSERT INTO `auth_user_user_permissions` VALUES ('2153', '1', '248');
INSERT INTO `auth_user_user_permissions` VALUES ('2154', '1', '249');
INSERT INTO `auth_user_user_permissions` VALUES ('2155', '1', '250');
INSERT INTO `auth_user_user_permissions` VALUES ('2156', '1', '251');
INSERT INTO `auth_user_user_permissions` VALUES ('1931', '17', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('1932', '17', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('1933', '17', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('1934', '17', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('1935', '17', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('1936', '17', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('1927', '17', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('1928', '17', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('1929', '17', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('1930', '17', '251');
INSERT INTO `auth_user_user_permissions` VALUES ('1961', '18', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('1962', '18', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('1963', '18', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('1964', '18', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('1965', '18', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('1966', '18', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('1957', '18', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('1958', '18', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('1959', '18', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('1960', '18', '251');
INSERT INTO `auth_user_user_permissions` VALUES ('2161', '20', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('2162', '20', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('2163', '20', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('2164', '20', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('2165', '20', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('2166', '20', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('2157', '20', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('2158', '20', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('2159', '20', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('2160', '20', '251');
INSERT INTO `auth_user_user_permissions` VALUES ('1951', '25', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('1952', '25', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('1953', '25', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('1954', '25', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('1955', '25', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('1956', '25', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('1947', '25', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('1948', '25', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('1949', '25', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('1950', '25', '251');
INSERT INTO `auth_user_user_permissions` VALUES ('1690', '47', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('1691', '47', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('1692', '47', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('1693', '47', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('1694', '47', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('1695', '47', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('1687', '47', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('1688', '47', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('1689', '47', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('1699', '60', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('1700', '60', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('1701', '60', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('1702', '60', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('1703', '60', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('1704', '60', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('1696', '60', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('1697', '60', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('1698', '60', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('1941', '87', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('1942', '87', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('1943', '87', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('1944', '87', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('1945', '87', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('1946', '87', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('1937', '87', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('1938', '87', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('1939', '87', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('1940', '87', '251');
INSERT INTO `auth_user_user_permissions` VALUES ('2188', '114', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('2196', '114', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('2192', '114', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('2187', '114', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('2189', '114', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('2195', '114', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('2193', '114', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('2194', '114', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('2191', '114', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('2190', '114', '251');
INSERT INTO `auth_user_user_permissions` VALUES ('2198', '115', '218');
INSERT INTO `auth_user_user_permissions` VALUES ('2206', '115', '219');
INSERT INTO `auth_user_user_permissions` VALUES ('2202', '115', '220');
INSERT INTO `auth_user_user_permissions` VALUES ('2197', '115', '221');
INSERT INTO `auth_user_user_permissions` VALUES ('2199', '115', '222');
INSERT INTO `auth_user_user_permissions` VALUES ('2205', '115', '223');
INSERT INTO `auth_user_user_permissions` VALUES ('2203', '115', '224');
INSERT INTO `auth_user_user_permissions` VALUES ('2204', '115', '225');
INSERT INTO `auth_user_user_permissions` VALUES ('2201', '115', '226');
INSERT INTO `auth_user_user_permissions` VALUES ('2200', '115', '251');

-- ----------------------------
-- Table structure for captcha_captchastore
-- ----------------------------
DROP TABLE IF EXISTS `captcha_captchastore`;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of captcha_captchastore
-- ----------------------------
INSERT INTO `captcha_captchastore` VALUES ('1', '833', '833', '84cfcb39087e8f75b460d628c0ead48f33733caa', '2016-07-22 10:48:58');
INSERT INTO `captcha_captchastore` VALUES ('2', '688', '688', '0995f0821f185821079101758294afd81d730da4', '2016-07-22 10:50:58');
INSERT INTO `captcha_captchastore` VALUES ('3', '892', '892', 'ff33c239d489583e67fbe8be482504a9b1b90522', '2016-07-22 10:55:33');
INSERT INTO `captcha_captchastore` VALUES ('4', '536', '536', 'debb4548caf4137c6807dbc043a99785a17b9760', '2016-07-22 10:55:38');
INSERT INTO `captcha_captchastore` VALUES ('5', '034', '034', '9ecadf0c5db55c55f53451b5a933b7602c40f53f', '2016-07-22 10:55:39');
INSERT INTO `captcha_captchastore` VALUES ('6', '885', '885', 'c1608553180aee191c4f50541225e98017d319d0', '2016-07-22 10:55:40');
INSERT INTO `captcha_captchastore` VALUES ('7', '685', '685', 'fc2019d6e0573f34d069daea41345de41114cc9f', '2016-07-22 15:22:18');
INSERT INTO `captcha_captchastore` VALUES ('8', '964', '964', 'e69d5a0e4374efcebb7901e6295c5ddf802a3682', '2016-08-05 15:48:05');
INSERT INTO `captcha_captchastore` VALUES ('9', '027', '027', '0137550ff3a123a9b71e4dc3db536641f6268fe5', '2016-08-05 15:48:50');
INSERT INTO `captcha_captchastore` VALUES ('10', '056', '056', '1c97954251cbdd27646acf9553656a2dc074574d', '2016-08-05 15:49:49');
INSERT INTO `captcha_captchastore` VALUES ('11', '016', '016', '79f1ee2b5840591bbf1930763aa8e4fabfa055b3', '2016-08-05 16:28:41');
INSERT INTO `captcha_captchastore` VALUES ('12', '009', '009', '227a1824a38542ccd2310b7ac2ed9fdf13d13c4b', '2016-09-08 16:36:01');

-- ----------------------------
-- Table structure for corsheaders_corsmodel
-- ----------------------------
DROP TABLE IF EXISTS `corsheaders_corsmodel`;
CREATE TABLE `corsheaders_corsmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cors` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of corsheaders_corsmodel
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=277 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2016-03-08 16:47:30', '58', '员工隐私查看(电话,身份证号)', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2016-03-08 16:47:43', '58', '员工隐私查看(电话,身份证号)', '2', '没有字段被修改。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2016-03-08 16:48:00', '58', '员工隐私查看(电话,身份证号)', '2', '没有字段被修改。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2016-03-08 16:48:03', '58', '员工隐私查看(电话,身份证号)', '2', '没有字段被修改。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2016-03-08 16:48:33', '59', '客户隐私查看(电话,身份证号)', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2016-03-08 16:49:03', '60', '理财师隐私查看(电话,身份证号)', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2016-03-08 16:49:58', '61', '产品查看', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2016-03-08 16:51:03', '62', '产品修改', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2016-03-08 16:51:31', '63', '产品添加', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2016-03-08 16:51:49', '64', '产品删除', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2016-03-08 16:52:36', '65', '员工添加', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2016-03-08 16:53:06', '66', '员工删除', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2016-03-08 16:53:34', '67', '员工修改', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2016-03-08 16:54:07', '68', '员工查看', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2016-03-08 16:54:41', '69', '理财师添加', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2016-03-08 16:55:02', '70', '理财师删除', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2016-03-08 16:55:27', '71', '理财师修改', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2016-03-08 16:55:54', '72', '理财师查看', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2016-03-08 16:56:22', '73', '查看客户', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2016-03-08 16:57:09', '74', '修改员工密码', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2016-03-08 16:57:34', '75', '修改理财师密码', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2016-03-08 16:57:54', '75', '修改理财师密码', '2', '已修改 codename 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2016-03-08 16:58:14', '76', '修改客户密码', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2016-03-08 16:58:30', '74', '修改员工密码', '2', '已修改 codename 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2016-03-08 16:58:59', '76', '修改客户密码', '2', '已修改 codename 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2016-03-08 17:01:36', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2016-03-11 13:56:58', '80', '添加机构图片', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2016-03-11 14:01:36', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2016-03-11 15:46:56', '59', '客户隐私查看', '2', '已修改 name 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2016-03-11 15:47:05', '60', '理财师隐私查看', '2', '已修改 name 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2016-03-11 15:47:13', '58', '员工隐私查看', '2', '已修改 name 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2016-03-11 17:58:22', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2016-03-11 17:59:20', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2016-03-11 18:00:17', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2016-03-14 15:44:31', '1', '未命名1', '1', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2016-03-14 16:18:24', '2', '未命名5', '1', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2016-03-14 16:18:37', '3', '未命名5', '1', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2016-03-15 17:36:51', '7', '赵四', '2', '已修改 avatar 。', '11', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2016-03-15 17:37:03', '6', '王麻子', '2', '已修改 avatar 。', '11', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2016-03-15 17:37:13', '5', '王二小', '2', '已修改 avatar 。', '11', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2016-03-15 17:37:23', '4', '张三', '2', '已修改 avatar 。', '11', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2016-03-16 11:14:11', '4', '汇盈1号', '1', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2016-03-16 15:36:25', '93', '查看机构图片', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('44', '2016-03-16 15:36:55', '94', '修改机构图片', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('45', '2016-03-16 15:37:17', '95', '删除机构图片', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('46', '2016-03-16 15:37:55', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('47', '2016-03-16 15:38:43', '17', '上海凡达', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('48', '2016-03-16 15:39:02', '20', '温州忽悠', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('49', '2016-03-16 15:39:14', '18', '浙江华硕', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('50', '2016-03-16 15:39:29', '25', '上海你猜', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('51', '2016-03-16 17:38:23', '3', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('52', '2016-03-16 17:43:41', '3', 'Announcement object', '2', '已修改 text 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('53', '2016-03-16 17:43:59', '3', 'Announcement object', '2', '没有字段被修改。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('54', '2016-03-16 17:45:03', '3', 'Announcement object', '2', '没有字段被修改。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('55', '2016-03-16 17:45:39', '4', 'Announcement object', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('56', '2016-03-16 17:45:57', '4', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('57', '2016-03-16 17:46:55', '4', 'Announcement object', '2', '已修改 text 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('58', '2016-03-16 17:47:06', '3', 'Announcement object', '2', '没有字段被修改。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('59', '2016-03-16 17:47:30', '5', 'Announcement object', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('60', '2016-03-16 17:48:30', '5', 'Announcement object', '2', '已修改 text 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('61', '2016-03-16 17:49:23', '6', 'Announcement object', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('62', '2016-03-16 17:50:27', '6', 'Announcement object', '2', '已修改 text 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('63', '2016-03-16 17:52:04', '7', 'Announcement object', '1', '', '24', '1');
INSERT INTO `django_admin_log` VALUES ('64', '2016-03-17 16:02:24', '30', '李志', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('65', '2016-03-17 16:15:28', '31', '李志', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('66', '2016-03-18 09:53:33', '1', 'CheckWork object', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('67', '2016-03-18 09:57:50', '2', '张三', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('68', '2016-03-18 09:58:16', '3', '王五字', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('69', '2016-03-18 09:58:47', '4', '灰机', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('70', '2016-03-18 10:00:58', '5', '赵四', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('71', '2016-03-18 10:02:15', '6', '立柱', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('72', '2016-03-18 10:02:56', '7', '王麻子', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('73', '2016-03-21 11:52:37', '7', '王麻子', '2', '已修改 check_business 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('74', '2016-03-21 11:52:42', '6', '立柱', '2', '已修改 check_business 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('75', '2016-03-21 11:52:47', '5', '赵四', '2', '已修改 check_business 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('76', '2016-03-21 11:52:54', '4', '灰机', '2', '已修改 check_business 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('77', '2016-03-21 11:52:59', '2', '张三', '2', '已修改 check_business 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('78', '2016-03-21 11:53:04', '1', '王二小', '2', '已修改 check_business 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('79', '2016-03-21 11:57:36', '3', '王五字', '2', '已修改 check_business 。', '25', '1');
INSERT INTO `django_admin_log` VALUES ('80', '2016-03-21 15:00:33', '8', '王麻子', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('81', '2016-03-21 15:11:08', '9', '赵四', '1', '', '25', '1');
INSERT INTO `django_admin_log` VALUES ('82', '2016-03-22 10:22:45', '8', '王麻子', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('83', '2016-03-22 10:22:53', '8', '王麻子', '2', '没有字段被修改。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('84', '2016-03-22 10:23:18', '9', '王麻子', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('85', '2016-03-22 10:23:56', '10', '王麻子', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('86', '2016-03-22 10:24:24', '11', '王麻子', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('87', '2016-03-22 10:24:59', '12', '王麻子', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('88', '2016-03-22 10:25:42', '13', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('89', '2016-03-22 10:26:06', '14', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('90', '2016-03-22 10:26:31', '15', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('91', '2016-03-22 10:26:53', '16', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('92', '2016-03-22 10:27:07', '6', '立柱', '2', '没有字段被修改。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('93', '2016-03-22 10:27:41', '17', '立柱', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('94', '2016-03-22 10:28:01', '18', '立柱', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('95', '2016-03-22 10:28:26', '19', '立柱', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('96', '2016-03-22 10:29:42', '20', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('97', '2016-03-22 10:30:15', '21', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('98', '2016-03-22 10:30:41', '22', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('99', '2016-03-22 10:30:51', '23', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('100', '2016-03-22 10:30:56', '12', '王麻子', '2', '没有字段被修改。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('101', '2016-03-22 10:31:19', '24', '王麻子', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('102', '2016-03-22 10:31:43', '25', '王麻子', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('103', '2016-03-22 14:48:17', '8', '黎明', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('104', '2016-03-22 14:48:54', '26', '黎明', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('105', '2016-03-22 16:45:24', '27', '黎明', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('106', '2016-03-22 17:04:56', '28', '立柱', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('107', '2016-03-29 11:16:50', '132', '出差审批', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('108', '2016-03-29 11:17:18', '133', '费用审批', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('109', '2016-03-29 11:17:39', '134', '请假审批', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('110', '2016-03-29 11:18:05', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('111', '2016-03-29 11:18:27', '17', '上海凡达', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('112', '2016-03-29 11:18:40', '20', '温州忽悠', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('113', '2016-03-29 11:19:08', '18', '浙江华硕', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('114', '2016-03-29 11:19:21', '25', '上海你猜', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('115', '2016-04-07 01:52:04', '165', '新增/删除公告(内部)', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('116', '2016-04-07 02:24:02', '93', '查看机构公告列表', '2', '已修改 name 和 codename 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('117', '2016-04-07 02:27:02', '80', '添加机构公告', '2', '已修改 name 和 codename 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('118', '2016-04-07 02:31:40', '95', '删除机构公告', '2', '已修改 name 和 codename 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('119', '2016-04-07 02:33:01', '94', '修改机构公告', '2', '已修改 name 和 codename 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('120', '2016-04-07 02:38:44', '165', '新增/删除公告(内部)', '2', '没有字段被修改。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('121', '2016-04-07 02:40:10', '25', '上海你猜', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('122', '2016-04-07 02:40:27', '17', '上海凡达', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('123', '2016-04-07 02:40:58', '17', '上海凡达', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('124', '2016-04-07 02:41:15', '17', '上海凡达', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('125', '2016-04-07 02:41:38', '18', '浙江华硕', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('126', '2016-04-07 02:41:49', '20', '温州忽悠', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('127', '2016-04-08 07:10:41', '169', '收款查询', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('128', '2016-04-08 07:12:41', '25', '上海你猜', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('129', '2016-04-08 07:12:53', '17', '上海凡达', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('130', '2016-04-08 07:13:06', '18', '浙江华硕', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('131', '2016-04-08 07:13:17', '20', '温州忽悠', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('132', '2016-04-15 11:23:56', '1', '黎明-18701789653', '2', '已修改 agents 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('133', '2016-04-15 15:27:45', '7', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('134', '2016-04-15 15:28:07', '11', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('135', '2016-04-15 15:28:26', '13', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('136', '2016-04-15 15:28:37', '12', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('137', '2016-04-15 15:29:10', '1', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('138', '2016-04-15 15:29:23', '2', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('139', '2016-04-15 15:30:00', '5', 'Announcement object', '2', '已修改 picture 。', '24', '1');
INSERT INTO `django_admin_log` VALUES ('140', '2016-04-15 15:51:18', '7', '上海你猜', '2', '已修改 logo 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('141', '2016-04-15 15:51:29', '4', '上海凡达', '2', '已修改 logo 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('142', '2016-04-18 15:09:48', '170', '修改机构基本信息', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('143', '2016-04-18 15:10:11', '25', '上海你猜', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('144', '2016-04-18 15:10:27', '33', 'zhejiang', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('145', '2016-04-18 15:10:38', '17', '上海凡达', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('146', '2016-04-18 15:10:50', '18', '浙江华硕', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('147', '2016-04-18 15:11:02', '20', '温州忽悠', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('148', '2016-04-20 16:53:09', '76', '修改客户密码', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('149', '2016-04-20 16:59:22', '174', '修改理财师手机号(账号)', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('150', '2016-04-20 17:00:01', '175', '修改员工手机号(账号)', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('151', '2016-04-20 17:00:36', '174', '修改理财师手机号', '2', '已修改 name 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('152', '2016-04-20 17:00:44', '175', '修改员工手机号', '2', '已修改 name 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('153', '2016-04-20 17:01:14', '25', '上海你猜', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('154', '2016-04-20 17:01:24', '33', 'zhejiang', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('155', '2016-04-20 17:01:34', '17', '上海凡达', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('156', '2016-04-20 17:01:47', '20', '温州忽悠', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('157', '2016-04-20 17:01:58', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('158', '2016-04-22 13:17:59', '69', '理财师添加', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('159', '2016-04-22 13:18:08', '60', '理财师隐私查看', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('160', '2016-04-22 13:18:19', '72', '理财师查看', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('161', '2016-04-22 13:18:30', '70', '理财师删除', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('162', '2016-04-22 13:18:41', '71', '理财师修改', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('163', '2016-04-22 13:18:51', '174', '修改理财师手机号', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('164', '2016-04-22 13:18:58', '75', '修改理财师密码', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('165', '2016-04-29 09:57:28', '59', '客户隐私查看(身份证号,手机,地址或其他)', '2', '已修改 name 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('166', '2016-04-29 10:04:24', '58', '员工隐私查看(身份证号,手机,地址或其他)', '2', '已修改 name 。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('167', '2016-05-09 15:26:46', '1', 'Lv_Announcement object', '1', '', '53', '1');
INSERT INTO `django_admin_log` VALUES ('168', '2016-05-09 15:55:23', '2', 'Lv_Announcement object', '1', '', '53', '1');
INSERT INTO `django_admin_log` VALUES ('169', '2016-05-09 15:57:25', '3', 'Lv_Announcement object', '1', '', '53', '1');
INSERT INTO `django_admin_log` VALUES ('170', '2016-05-09 15:57:40', '4', 'Lv_Announcement object', '1', '', '53', '1');
INSERT INTO `django_admin_log` VALUES ('171', '2016-05-09 15:57:56', '5', 'Lv_Announcement object', '1', '', '53', '1');
INSERT INTO `django_admin_log` VALUES ('172', '2016-05-09 16:39:19', '5', 'Lv_Announcement object', '2', '已修改 text 。', '53', '1');
INSERT INTO `django_admin_log` VALUES ('173', '2016-05-17 16:16:44', '1', '张三', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('174', '2016-05-17 16:19:47', '2', '张思', '1', '', '27', '1');
INSERT INTO `django_admin_log` VALUES ('175', '2016-05-18 10:34:25', '1', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('176', '2016-05-18 10:35:11', '2', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('177', '2016-05-18 15:23:57', '7', '上海你猜', '2', '已修改 note 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('178', '2016-05-18 15:24:13', '4', '上海凡达', '2', '已修改 logo 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('179', '2016-05-18 15:24:45', '7', '上海你猜', '2', '已修改 logo 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('180', '2016-05-18 15:33:26', '7', '上海凡达-撒旦撒旦撒', '2', '已修改 product_type，strategy 和 invest_scope 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('181', '2016-05-18 15:33:39', '6', '上海你猜-锦绣2号', '2', '已修改 strategy 和 invest_scope 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('182', '2016-05-18 15:33:47', '5', '上海凡达-金马349号', '2', '已修改 product_type，strategy 和 invest_scope 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('183', '2016-05-18 15:33:55', '3', '上海凡达-汇盈1号', '2', '已修改 product_type 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('184', '2016-05-18 15:34:03', '2', '上海凡达-锦绣3号', '2', '已修改 product_type 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('185', '2016-05-18 16:00:29', '8', '上海你猜-大苏打发送到', '1', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('186', '2016-05-18 16:01:13', '8', '上海你猜-大苏打发送到', '2', '已修改 return_expected 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('187', '2016-05-18 16:01:38', '6', '上海你猜-锦绣2号', '2', '已修改 product_sum 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('188', '2016-05-18 16:10:37', '6', '上海你猜-锦绣2号', '2', '已修改 product_type 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('189', '2016-05-19 16:51:31', '28', '灰机', '2', '已修改 password 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('190', '2016-05-23 12:00:17', '7', '上海你猜', '2', '已修改 business_phone 。', '10', '1');
INSERT INTO `django_admin_log` VALUES ('191', '2016-05-23 13:06:41', '1', '黎明-18701789653', '2', '已修改 portrait 和 note 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('192', '2016-05-23 13:10:06', '1', '黎明-18701789653', '2', '已修改 email 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('193', '2016-05-23 13:37:15', '1', '黎明-18701789653', '2', '已修改 product_target 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('194', '2016-05-23 13:37:46', '1', '黎明-18701789653', '2', '已修改 product_target 。', '13', '1');
INSERT INTO `django_admin_log` VALUES ('195', '2016-05-24 13:47:39', '2', '张三', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('196', '2016-05-24 13:47:45', '1', '张三', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('197', '2016-05-24 15:16:20', '3', '上海凡达', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('198', '2016-05-24 15:16:29', '3', '张三', '2', '已修改 check_history 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('199', '2016-05-24 15:17:12', '4', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('200', '2016-05-24 15:18:30', '5', '第三方', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('201', '2016-05-24 15:18:50', '6', '张思', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('202', '2016-05-24 15:46:27', '7', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('203', '2016-05-25 09:42:14', '3', '张三', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('204', '2016-05-25 09:42:20', '5', '第三方', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('205', '2016-05-31 14:57:34', '7', '张三', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('206', '2016-05-31 15:24:01', '6', '张思', '2', '没有字段被修改。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('207', '2016-05-31 16:10:08', '3', '张三', '2', '没有字段被修改。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('208', '2016-06-01 09:50:05', '7', '张三', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('209', '2016-06-01 09:50:16', '6', '张思', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('210', '2016-06-01 09:50:28', '5', '第三方', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('211', '2016-06-01 09:53:59', '3', '张三', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('212', '2016-06-01 17:27:29', '80', '添加机构公告', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('213', '2016-06-01 17:27:29', '165', '新增/删除公告(内部)', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('214', '2016-06-01 17:27:29', '65', '员工添加', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('215', '2016-06-01 17:27:29', '63', '产品添加', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('216', '2016-06-01 17:27:29', '95', '删除机构公告', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('217', '2016-06-01 17:27:29', '94', '修改机构公告', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('218', '2016-06-01 17:27:29', '93', '查看机构公告列表', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('219', '2016-06-01 17:27:29', '133', '费用审批', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('220', '2016-06-01 17:27:29', '59', '客户隐私查看(身份证号,手机,地址或其他)', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('221', '2016-06-01 17:27:29', '66', '员工删除', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('222', '2016-06-01 17:27:29', '64', '产品删除', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('223', '2016-06-01 17:27:29', '58', '员工隐私查看(身份证号,手机,地址或其他)', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('224', '2016-06-01 17:27:29', '73', '查看客户', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('225', '2016-06-01 17:27:29', '68', '员工查看', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('226', '2016-06-01 17:27:29', '61', '产品查看', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('227', '2016-06-01 17:27:29', '169', '收款查询', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('228', '2016-06-01 17:27:29', '134', '请假审批', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('229', '2016-06-01 17:27:29', '170', '修改机构基本信息', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('230', '2016-06-01 17:27:29', '67', '员工修改', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('231', '2016-06-01 17:27:29', '175', '修改员工手机号', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('232', '2016-06-01 17:27:29', '74', '修改员工密码', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('233', '2016-06-01 17:27:29', '62', '产品修改', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('234', '2016-06-01 17:27:29', '132', '出差审批', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('235', '2016-06-01 17:29:48', '218', '新增/修改/删除公司公告(外部)', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('236', '2016-06-01 17:32:22', '219', '新增/修改/删除产品', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('237', '2016-06-01 17:32:56', '220', '客户查看', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('238', '2016-06-01 17:34:02', '221', '新增/修改/删除公司公告(内部)', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('239', '2016-06-01 17:36:59', '221', '新增/修改/删除公司公告(内部)', '2', '没有字段被修改。', '2', '1');
INSERT INTO `django_admin_log` VALUES ('240', '2016-06-01 17:41:33', '222', '公司基本信息修改', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('241', '2016-06-01 17:42:09', '223', '财务管理', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('242', '2016-06-01 17:42:58', '224', '新增/修改/删除员工账户信息', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('243', '2016-06-01 17:43:23', '225', '员工查看', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('244', '2016-06-01 17:43:50', '226', '考勤管理', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('245', '2016-06-01 17:54:14', '47', '涠洲达华', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('246', '2016-06-01 17:54:37', '60', '发个梵蒂冈', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('247', '2016-06-01 17:55:01', '25', '上海你猜', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('248', '2016-06-01 17:55:32', '18', '浙江华硕', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('249', '2016-06-01 17:56:05', '17', '上海凡达', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('250', '2016-06-01 17:56:28', '20', '温州忽悠', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('251', '2016-06-01 17:56:47', '1', '律錳管理', '2', '已修改 user_permissions 和 last_login 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('252', '2016-06-02 13:41:00', '7', '张三', '2', '已修改 check_time 。', '28', '1');
INSERT INTO `django_admin_log` VALUES ('253', '2016-06-02 13:42:35', '8', '张三', '1', '', '28', '1');
INSERT INTO `django_admin_log` VALUES ('254', '2016-06-03 11:13:57', '26', '王麻子', '2', '已修改 password 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('255', '2016-06-22 14:23:45', '3', '上海凡达-汇盈1号', '2', '已修改 return_expected 。', '12', '1');
INSERT INTO `django_admin_log` VALUES ('256', '2016-07-25 11:46:24', '79', '11111', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('257', '2016-07-25 11:46:24', '80', '11111', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('258', '2016-07-25 11:46:24', '82', '11111', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('259', '2016-07-26 10:09:25', '83', '11111', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('260', '2016-07-26 10:25:05', '85', '上海力帆', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('261', '2016-07-26 14:04:15', '251', '考勤时间设定', '1', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('262', '2016-07-26 14:05:34', '17', '上海凡达', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('263', '2016-07-26 14:06:25', '87', '上海力帆', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('264', '2016-07-26 14:06:39', '25', '上海你猜', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('265', '2016-07-26 14:06:50', '18', '浙江华硕', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('266', '2016-07-26 14:07:19', '1', '律錳管理', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('267', '2016-07-26 14:07:34', '20', '温州忽悠', '2', '已修改 user_permissions 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('268', '2016-08-09 14:17:23', '95', '111', '2', '已修改 is_active 。', '4', '1');
INSERT INTO `django_admin_log` VALUES ('269', '2016-08-09 14:23:54', '94', '1111', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('270', '2016-08-09 14:24:04', '95', '111', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('271', '2016-08-11 17:30:43', '104', '77777', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('272', '2016-08-11 17:30:43', '109', '11111', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('273', '2016-08-11 17:30:43', '33', 'zhejiang', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('274', '2016-08-11 17:30:43', '88', '北京大华', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('275', '2016-08-11 17:30:43', '108', 'fdsfds', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('276', '2016-08-11 17:30:43', '91', '北京法人', '3', '', '4', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('49', 'agent_api', 'agent_version');
INSERT INTO `django_content_type` VALUES ('42', 'agent_api', 'cell_records_customer');
INSERT INTO `django_content_type` VALUES ('43', 'agent_api', 'cell_records_pcustomer');
INSERT INTO `django_content_type` VALUES ('66', 'agent_api', 'temporary_file');
INSERT INTO `django_content_type` VALUES ('25', 'aos', 'checkwork');
INSERT INTO `django_content_type` VALUES ('26', 'aos', 'checkwork_history');
INSERT INTO `django_content_type` VALUES ('52', 'api', 'attention');
INSERT INTO `django_content_type` VALUES ('19', 'api', 'checkin');
INSERT INTO `django_content_type` VALUES ('51', 'api', 'collection');
INSERT INTO `django_content_type` VALUES ('67', 'api', 'comment');
INSERT INTO `django_content_type` VALUES ('60', 'api', 'emailcode');
INSERT INTO `django_content_type` VALUES ('59', 'api', 'emailvalidsecond');
INSERT INTO `django_content_type` VALUES ('18', 'api', 'headline');
INSERT INTO `django_content_type` VALUES ('48', 'api', 'history_checkin');
INSERT INTO `django_content_type` VALUES ('61', 'api', 'point');
INSERT INTO `django_content_type` VALUES ('22', 'api', 'validsecond');
INSERT INTO `django_content_type` VALUES ('23', 'api', 'verificationcode');
INSERT INTO `django_content_type` VALUES ('16', 'api', 'version');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('7', 'authtoken', 'token');
INSERT INTO `django_content_type` VALUES ('35', 'captcha', 'captchastore');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('9', 'corsheaders', 'corsmodel');
INSERT INTO `django_content_type` VALUES ('63', 'easy_thumbnails', 'source');
INSERT INTO `django_content_type` VALUES ('64', 'easy_thumbnails', 'thumbnail');
INSERT INTO `django_content_type` VALUES ('65', 'easy_thumbnails', 'thumbnaildimensions');
INSERT INTO `django_content_type` VALUES ('11', 'erp', 'agent');
INSERT INTO `django_content_type` VALUES ('24', 'erp', 'announcement');
INSERT INTO `django_content_type` VALUES ('10', 'erp', 'business');
INSERT INTO `django_content_type` VALUES ('13', 'erp', 'customer');
INSERT INTO `django_content_type` VALUES ('41', 'erp', 'customer_pending');
INSERT INTO `django_content_type` VALUES ('71', 'erp', 'online_chat');
INSERT INTO `django_content_type` VALUES ('50', 'erp', 'position');
INSERT INTO `django_content_type` VALUES ('12', 'erp', 'product');
INSERT INTO `django_content_type` VALUES ('20', 'erp', 'product_type');
INSERT INTO `django_content_type` VALUES ('15', 'erp', 'purchase');
INSERT INTO `django_content_type` VALUES ('47', 'erp', 'real_purchase');
INSERT INTO `django_content_type` VALUES ('69', 'erp', 'redister_business');
INSERT INTO `django_content_type` VALUES ('55', 'oa', 'all_examine');
INSERT INTO `django_content_type` VALUES ('27', 'oa', 'checkwork');
INSERT INTO `django_content_type` VALUES ('28', 'oa', 'checkwork_history');
INSERT INTO `django_content_type` VALUES ('70', 'oa', 'check_time_setting');
INSERT INTO `django_content_type` VALUES ('32', 'oa', 'cost_application');
INSERT INTO `django_content_type` VALUES ('56', 'oa', 'cost_examine');
INSERT INTO `django_content_type` VALUES ('44', 'oa', 'daily_to_do');
INSERT INTO `django_content_type` VALUES ('31', 'oa', 'daily_work');
INSERT INTO `django_content_type` VALUES ('30', 'oa', 'internal_announcement');
INSERT INTO `django_content_type` VALUES ('57', 'oa', 'leave_examine');
INSERT INTO `django_content_type` VALUES ('33', 'oa', 'leave_management');
INSERT INTO `django_content_type` VALUES ('36', 'oa', 'read_message');
INSERT INTO `django_content_type` VALUES ('34', 'oa', 'travel_apply');
INSERT INTO `django_content_type` VALUES ('58', 'oa', 'travel_examine');
INSERT INTO `django_content_type` VALUES ('45', 'postman', 'message');
INSERT INTO `django_content_type` VALUES ('46', 'postman', 'pendingmessage');
INSERT INTO `django_content_type` VALUES ('8', 'registration', 'registrationprofile');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('62', 'web_customer', 'business_carousel');
INSERT INTO `django_content_type` VALUES ('53', 'web_customer', 'lv_announcement');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=328 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('4', 'erp', '0001_initial', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('5', 'erp', '0002_auto_20160205_1511', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('6', 'erp', '0003_business_name', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('7', 'erp', '0004_auto_20160212_1324', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('8', 'erp', '0005_agent_avatar', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('9', 'erp', '0006_auto_20160223_0843', '2016-03-08 16:34:53');
INSERT INTO `django_migrations` VALUES ('10', 'erp', '0007_product_on_top', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('11', 'erp', '0008_auto_20160223_1521', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('12', 'erp', '0009_auto_20160223_1549', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('13', 'contenttypes', '0002_remove_content_type_name', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0002_alter_permission_name_max_length', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0003_alter_user_email_max_length', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0004_alter_user_username_opts', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('17', 'auth', '0005_alter_user_last_login_null', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('18', 'auth', '0006_require_contenttypes_0002', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('19', 'erp', '0010_role', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('20', 'erp', '0011_auto_20160224_1603', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('21', 'erp', '0012_employee_role', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('22', 'erp', '0013_auto_20160224_1738', '2016-03-08 16:34:54');
INSERT INTO `django_migrations` VALUES ('23', 'erp', '0014_auto_20160225_1024', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('24', 'erp', '0015_auto_20160225_1607', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('25', 'erp', '0016_auto_20160225_1746', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('26', 'erp', '0017_agent_entry_person', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('27', 'erp', '0018_auto_20160226_1405', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('28', 'erp', '0019_auto_20160226_1538', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('29', 'erp', '0020_auto_20160226_1738', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('30', 'erp', '0021_auto_20160226_1740', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('31', 'erp', '0022_auto_20160229_0913', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('32', 'erp', '0023_auto_20160302_1029', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('33', 'erp', '0024_auto_20160302_1128', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('34', 'erp', '0025_auto_20160302_1348', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('35', 'api', '0001_initial', '2016-03-08 16:34:55');
INSERT INTO `django_migrations` VALUES ('36', 'api', '0002_auto_20160302_1551', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('37', 'authtoken', '0001_initial', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('38', 'erp', '0026_auto_20160302_1707', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('39', 'erp', '0027_business_logo', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('40', 'erp', '0028_auto_20160303_1711', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('41', 'erp', '0029_auto_20160304_0957', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('42', 'erp', '0030_auto_20160308_1453', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('43', 'erp', '0031_auto_20160308_1605', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('44', 'registration', '0001_initial', '2016-03-08 16:34:56');
INSERT INTO `django_migrations` VALUES ('45', 'registration', '0002_registrationprofile_activated', '2016-03-08 16:34:57');
INSERT INTO `django_migrations` VALUES ('46', 'registration', '0003_migrate_activatedstatus', '2016-03-08 16:34:57');
INSERT INTO `django_migrations` VALUES ('47', 'sessions', '0001_initial', '2016-03-08 16:34:57');
INSERT INTO `django_migrations` VALUES ('48', 'erp', '0032_auto_20160308_1717', '2016-03-08 17:17:10');
INSERT INTO `django_migrations` VALUES ('49', 'erp', '0033_auto_20160309_1512', '2016-03-09 15:12:32');
INSERT INTO `django_migrations` VALUES ('50', 'erp', '0034_auto_20160309_1513', '2016-03-09 15:13:37');
INSERT INTO `django_migrations` VALUES ('51', 'erp', '0035_auto_20160309_1550', '2016-03-09 15:50:18');
INSERT INTO `django_migrations` VALUES ('52', 'erp', '0036_auto_20160310_0913', '2016-03-10 09:13:57');
INSERT INTO `django_migrations` VALUES ('53', 'erp', '0037_auto_20160310_0919', '2016-03-10 09:19:18');
INSERT INTO `django_migrations` VALUES ('54', 'erp', '0038_auto_20160310_0932', '2016-03-10 09:32:35');
INSERT INTO `django_migrations` VALUES ('55', 'erp', '0039_auto_20160310_1346', '2016-03-10 13:47:20');
INSERT INTO `django_migrations` VALUES ('56', 'erp', '0040_announce_picture', '2016-03-11 14:50:26');
INSERT INTO `django_migrations` VALUES ('57', 'erp', '0041_auto_20160311_1625', '2016-03-11 16:26:07');
INSERT INTO `django_migrations` VALUES ('58', 'erp', '0042_auto_20160311_1736', '2016-03-11 17:36:11');
INSERT INTO `django_migrations` VALUES ('59', 'api', '0003_validsecond_verificationcode', '2016-03-11 17:46:21');
INSERT INTO `django_migrations` VALUES ('60', 'api', '0004_verificationcode_purpose', '2016-03-14 15:25:23');
INSERT INTO `django_migrations` VALUES ('61', 'erp', '0043_auto_20160314_1639', '2016-03-14 16:39:53');
INSERT INTO `django_migrations` VALUES ('62', 'erp', '0044_auto_20160316_0943', '2016-03-16 09:43:28');
INSERT INTO `django_migrations` VALUES ('63', 'erp', '0045_announcement_announce_business', '2016-03-16 09:47:41');
INSERT INTO `django_migrations` VALUES ('64', 'erp', '0046_announcement_is_active', '2016-03-16 11:13:11');
INSERT INTO `django_migrations` VALUES ('65', 'erp', '0047_auto_20160316_1113', '2016-03-16 11:13:12');
INSERT INTO `django_migrations` VALUES ('66', 'api', '0005_auto_20160316_1020', '2016-03-16 11:15:45');
INSERT INTO `django_migrations` VALUES ('67', 'erp', '0048_auto_20160316_1531', '2016-03-16 15:32:40');
INSERT INTO `django_migrations` VALUES ('68', 'aos', '0001_initial', '2016-03-18 09:41:09');
INSERT INTO `django_migrations` VALUES ('69', 'api', '0006_headline_picture', '2016-03-18 16:53:45');
INSERT INTO `django_migrations` VALUES ('70', 'aos', '0002_checkwork_check_business', '2016-03-21 11:51:12');
INSERT INTO `django_migrations` VALUES ('71', 'aos', '0003_auto_20160321_1705', '2016-03-21 17:05:13');
INSERT INTO `django_migrations` VALUES ('75', 'erp', '0049_auto_20160323_1757', '2016-03-23 17:57:56');
INSERT INTO `django_migrations` VALUES ('83', 'api', '0007_auto_20160324_1511', '2016-03-25 17:42:57');
INSERT INTO `django_migrations` VALUES ('84', 'api', '0008_version_context', '2016-03-25 17:42:57');
INSERT INTO `django_migrations` VALUES ('85', 'captcha', '0001_initial', '2016-03-25 17:42:57');
INSERT INTO `django_migrations` VALUES ('99', 'erp', '0050_auto_20160330_1541', '2016-03-31 16:51:53');
INSERT INTO `django_migrations` VALUES ('100', 'erp', '0051_auto_20160330_1800', '2016-03-31 16:51:53');
INSERT INTO `django_migrations` VALUES ('101', 'erp', '0052_auto_20160331_1022', '2016-03-31 16:51:53');
INSERT INTO `django_migrations` VALUES ('102', 'erp', '0053_auto_20160331_1246', '2016-03-31 16:51:54');
INSERT INTO `django_migrations` VALUES ('103', 'agent_api', '0001_initial', '2016-03-31 16:51:54');
INSERT INTO `django_migrations` VALUES ('111', 'postman', '0001_initial', '2016-04-05 07:32:28');
INSERT INTO `django_migrations` VALUES ('113', 'erp', '0054_auto_20160407_1702', '2016-04-07 09:02:35');
INSERT INTO `django_migrations` VALUES ('114', 'erp', '0055_real_purchase_brief', '2016-04-07 09:13:32');
INSERT INTO `django_migrations` VALUES ('115', 'erp', '0056_auto_20160407_1718', '2016-04-07 09:18:14');
INSERT INTO `django_migrations` VALUES ('116', 'erp', '0057_auto_20160407_1723', '2016-04-07 09:23:54');
INSERT INTO `django_migrations` VALUES ('117', 'erp', '0058_real_purchase_is_active', '2016-04-07 09:28:28');
INSERT INTO `django_migrations` VALUES ('118', 'erp', '0059_real_purchase_business', '2016-04-08 02:35:17');
INSERT INTO `django_migrations` VALUES ('119', 'erp', '0054_auto_20160411_1133', '2016-04-11 03:34:01');
INSERT INTO `django_migrations` VALUES ('120', 'erp', '0055_auto_20160411_1328', '2016-04-11 05:28:51');
INSERT INTO `django_migrations` VALUES ('121', 'erp', '0056_customer_customer_type', '2016-04-11 05:34:20');
INSERT INTO `django_migrations` VALUES ('122', 'erp', '0057_auto_20160411_1422', '2016-04-11 06:22:45');
INSERT INTO `django_migrations` VALUES ('123', 'erp', '0058_remove_customer_product_target', '2016-04-11 06:36:48');
INSERT INTO `django_migrations` VALUES ('124', 'erp', '0059_customer_product_target', '2016-04-11 06:37:13');
INSERT INTO `django_migrations` VALUES ('125', 'erp', '0060_auto_20160411_1453', '2016-04-11 06:54:08');
INSERT INTO `django_migrations` VALUES ('126', 'erp', '0061_customer_product_target', '2016-04-11 06:59:13');
INSERT INTO `django_migrations` VALUES ('127', 'erp', '0062_auto_20160411_1509', '2016-04-11 07:09:11');
INSERT INTO `django_migrations` VALUES ('128', 'erp', '0063_auto_20160411_1536', '2016-04-11 07:36:11');
INSERT INTO `django_migrations` VALUES ('129', 'erp', '0064_auto_20160411_1748', '2016-04-11 09:48:51');
INSERT INTO `django_migrations` VALUES ('130', 'erp', '0065_customer_avatar', '2016-04-12 15:14:08');
INSERT INTO `django_migrations` VALUES ('131', 'api', '0009_auto_20160413_0924', '2016-04-13 10:02:25');
INSERT INTO `django_migrations` VALUES ('133', 'api', '0010_auto_20160415_1538', '2016-04-15 15:52:52');
INSERT INTO `django_migrations` VALUES ('134', 'api', '0011_auto_20160415_1722', '2016-04-15 17:22:45');
INSERT INTO `django_migrations` VALUES ('135', 'api', '0012_checkin_continuous_days', '2016-04-18 11:46:59');
INSERT INTO `django_migrations` VALUES ('136', 'erp', '0066_auto_20160418_1741', '2016-04-18 17:41:47');
INSERT INTO `django_migrations` VALUES ('137', 'api', '0013_auto_20160419_1339', '2016-04-19 14:15:23');
INSERT INTO `django_migrations` VALUES ('138', 'erp', '0067_auto_20160421_1501', '2016-04-21 15:01:51');
INSERT INTO `django_migrations` VALUES ('139', 'erp', '0068_auto_20160421_1525', '2016-04-21 15:25:18');
INSERT INTO `django_migrations` VALUES ('140', 'erp', '0069_auto_20160422_1104', '2016-04-22 11:04:48');
INSERT INTO `django_migrations` VALUES ('141', 'erp', '0070_auto_20160422_1117', '2016-04-22 11:17:39');
INSERT INTO `django_migrations` VALUES ('142', 'erp', '0071_auto_20160422_1117', '2016-04-22 11:17:39');
INSERT INTO `django_migrations` VALUES ('143', 'erp', '0072_auto_20160422_1200', '2016-04-22 12:00:51');
INSERT INTO `django_migrations` VALUES ('144', 'erp', '0073_auto_20160422_1449', '2016-04-22 14:50:05');
INSERT INTO `django_migrations` VALUES ('145', 'agent_api', '0002_agent_version', '2016-04-25 13:21:32');
INSERT INTO `django_migrations` VALUES ('146', 'erp', '0074_auto_20160425_1447', '2016-04-25 14:47:39');
INSERT INTO `django_migrations` VALUES ('147', 'erp', '0075_agent_position', '2016-04-25 14:48:45');
INSERT INTO `django_migrations` VALUES ('148', 'erp', '0076_auto_20160425_1624', '2016-04-25 16:24:12');
INSERT INTO `django_migrations` VALUES ('149', 'erp', '0077_auto_20160426_1143', '2016-04-26 11:44:03');
INSERT INTO `django_migrations` VALUES ('150', 'erp', '0078_auto_20160426_1324', '2016-04-26 13:24:17');
INSERT INTO `django_migrations` VALUES ('151', 'erp', '0079_auto_20160426_1328', '2016-04-26 13:28:47');
INSERT INTO `django_migrations` VALUES ('152', 'erp', '0080_auto_20160426_1347', '2016-04-26 13:47:53');
INSERT INTO `django_migrations` VALUES ('153', 'erp', '0081_auto_20160426_1426', '2016-04-26 14:26:33');
INSERT INTO `django_migrations` VALUES ('154', 'erp', '0082_auto_20160426_1427', '2016-04-26 14:27:41');
INSERT INTO `django_migrations` VALUES ('155', 'erp', '0082_auto_20160426_1432', '2016-04-26 14:32:44');
INSERT INTO `django_migrations` VALUES ('156', 'erp', '0083_auto_20160426_1628', '2016-04-26 16:28:44');
INSERT INTO `django_migrations` VALUES ('157', 'erp', '0084_auto_20160426_1656', '2016-04-26 16:56:57');
INSERT INTO `django_migrations` VALUES ('158', 'erp', '0085_auto_20160426_1704', '2016-04-26 17:04:48');
INSERT INTO `django_migrations` VALUES ('159', 'erp', '0086_auto_20160426_1723', '2016-04-26 17:23:06');
INSERT INTO `django_migrations` VALUES ('160', 'erp', '0087_agent_qrcode', '2016-04-27 13:24:55');
INSERT INTO `django_migrations` VALUES ('161', 'api', '0014_attention_collection', '2016-04-27 16:18:57');
INSERT INTO `django_migrations` VALUES ('162', 'api', '0015_auto_20160427_1457', '2016-04-27 16:18:57');
INSERT INTO `django_migrations` VALUES ('163', 'erp', '0088_auto_20160427_1634', '2016-04-27 16:35:01');
INSERT INTO `django_migrations` VALUES ('164', 'erp', '0089_auto_20160428_0939', '2016-04-28 09:39:22');
INSERT INTO `django_migrations` VALUES ('165', 'erp', '0090_auto_20160429_1018', '2016-04-29 10:18:53');
INSERT INTO `django_migrations` VALUES ('166', 'erp', '0091_auto_20160429_1024', '2016-04-29 10:24:26');
INSERT INTO `django_migrations` VALUES ('167', 'erp', '0092_auto_20160429_1057', '2016-04-29 10:57:58');
INSERT INTO `django_migrations` VALUES ('168', 'agent_api', '0003_auto_20160503_0953', '2016-05-03 14:09:29');
INSERT INTO `django_migrations` VALUES ('169', 'erp', '0093_auto_20160504_0958', '2016-05-04 09:59:22');
INSERT INTO `django_migrations` VALUES ('170', 'erp', '0093_auto_20160504_1055', '2016-05-04 10:55:53');
INSERT INTO `django_migrations` VALUES ('171', 'erp', '0094_auto_20160504_1109', '2016-05-04 11:09:16');
INSERT INTO `django_migrations` VALUES ('172', 'erp', '0095_auto_20160504_1129', '2016-05-04 11:29:11');
INSERT INTO `django_migrations` VALUES ('173', 'erp', '0096_auto_20160506_1410', '2016-05-06 14:10:24');
INSERT INTO `django_migrations` VALUES ('174', 'erp', '0096_product_finished', '2016-05-06 15:41:44');
INSERT INTO `django_migrations` VALUES ('175', 'erp', '0093_auto_20160505_1623', '2016-05-06 17:11:47');
INSERT INTO `django_migrations` VALUES ('176', 'erp', '0097_merge', '2016-05-06 17:11:47');
INSERT INTO `django_migrations` VALUES ('177', 'web_customer', '0001_initial', '2016-05-09 15:26:01');
INSERT INTO `django_migrations` VALUES ('178', 'web_customer', '0002_auto_20160509_1558', '2016-05-09 15:58:49');
INSERT INTO `django_migrations` VALUES ('179', 'web_customer', '0003_auto_20160510_1411', '2016-05-10 14:11:38');
INSERT INTO `django_migrations` VALUES ('180', 'erp', '0098_auto_20160511_1349', '2016-05-11 13:49:39');
INSERT INTO `django_migrations` VALUES ('181', 'web_customer', '0004_auto_20160511_1352', '2016-05-11 13:52:15');
INSERT INTO `django_migrations` VALUES ('186', 'erp', '0098_product_contract', '2016-05-12 11:13:21');
INSERT INTO `django_migrations` VALUES ('190', 'erp', '0099_auto_20160512_1146', '2016-05-12 11:46:58');
INSERT INTO `django_migrations` VALUES ('192', 'erp', '0100_auto_20160513_0939', '2016-05-13 09:39:41');
INSERT INTO `django_migrations` VALUES ('193', 'erp', '0101_auto_20160513_1653', '2016-05-13 16:54:13');
INSERT INTO `django_migrations` VALUES ('195', 'erp', '0102_auto_20160516_1046', '2016-05-16 10:46:42');
INSERT INTO `django_migrations` VALUES ('198', 'erp', '0103_auto_20160516_1342', '2016-05-16 13:42:13');
INSERT INTO `django_migrations` VALUES ('221', 'oa', '0001_initial', '2016-05-17 13:30:46');
INSERT INTO `django_migrations` VALUES ('222', 'oa', '0002_checkwork_check_business', '2016-05-17 13:30:46');
INSERT INTO `django_migrations` VALUES ('223', 'oa', '0003_auto_20160321_1705', '2016-05-17 13:30:46');
INSERT INTO `django_migrations` VALUES ('224', 'oa', '0004_announcementemployee', '2016-05-17 13:30:46');
INSERT INTO `django_migrations` VALUES ('225', 'oa', '0005_auto_20160323_1759', '2016-05-17 13:30:47');
INSERT INTO `django_migrations` VALUES ('226', 'oa', '0006_internal_announcement_is_active', '2016-05-17 13:30:47');
INSERT INTO `django_migrations` VALUES ('227', 'oa', '0007_cost_application_daily_work_leave_management_travel_apply', '2016-05-17 13:30:48');
INSERT INTO `django_migrations` VALUES ('228', 'oa', '0008_auto_20160324_1630', '2016-05-17 13:30:48');
INSERT INTO `django_migrations` VALUES ('229', 'oa', '0009_auto_20160324_1728', '2016-05-17 13:30:50');
INSERT INTO `django_migrations` VALUES ('230', 'oa', '0010_auto_20160325_1546', '2016-05-17 13:30:50');
INSERT INTO `django_migrations` VALUES ('231', 'oa', '0011_read_message', '2016-05-17 13:30:50');
INSERT INTO `django_migrations` VALUES ('232', 'oa', '0012_auto_20160328_1720', '2016-05-17 13:30:50');
INSERT INTO `django_migrations` VALUES ('233', 'oa', '0013_auto_20160330_1136', '2016-05-17 13:30:51');
INSERT INTO `django_migrations` VALUES ('234', 'oa', '0014_auto_20160330_1521', '2016-05-17 13:30:53');
INSERT INTO `django_migrations` VALUES ('235', 'oa', '0015_auto_20160330_1638', '2016-05-17 13:30:53');
INSERT INTO `django_migrations` VALUES ('236', 'oa', '0016_auto_20160330_1648', '2016-05-17 13:30:53');
INSERT INTO `django_migrations` VALUES ('237', 'oa', '0017_auto_20160330_1650', '2016-05-17 13:30:54');
INSERT INTO `django_migrations` VALUES ('238', 'oa', '0018_auto_20160330_1759', '2016-05-17 13:30:55');
INSERT INTO `django_migrations` VALUES ('239', 'oa', '0019_auto_20160331_1030', '2016-05-17 13:30:56');
INSERT INTO `django_migrations` VALUES ('240', 'oa', '0020_cost_examine_is_active', '2016-05-17 13:30:56');
INSERT INTO `django_migrations` VALUES ('241', 'oa', '0021_leave_examine_travel_examine', '2016-05-17 13:30:56');
INSERT INTO `django_migrations` VALUES ('242', 'oa', '0022_daily_to_do', '2016-05-17 13:30:57');
INSERT INTO `django_migrations` VALUES ('243', 'oa', '0023_daily_to_do_to_do_time', '2016-05-17 13:30:57');
INSERT INTO `django_migrations` VALUES ('244', 'oa', '0024_auto_20160401_1515', '2016-05-17 13:30:57');
INSERT INTO `django_migrations` VALUES ('245', 'oa', '0025_auto_20160401_1517', '2016-05-17 13:30:58');
INSERT INTO `django_migrations` VALUES ('246', 'oa', '0026_auto_20160401_1525', '2016-05-17 13:30:58');
INSERT INTO `django_migrations` VALUES ('247', 'oa', '0027_auto_20160401_1639', '2016-05-17 13:30:58');
INSERT INTO `django_migrations` VALUES ('248', 'oa', '0028_auto_20160401_1712', '2016-05-17 13:30:58');
INSERT INTO `django_migrations` VALUES ('249', 'oa', '0029_auto_20160407_0936', '2016-05-17 13:30:58');
INSERT INTO `django_migrations` VALUES ('250', 'oa', '0030_auto_20160414_1459', '2016-05-17 13:30:59');
INSERT INTO `django_migrations` VALUES ('251', 'oa', '0031_all_examine', '2016-05-17 13:30:59');
INSERT INTO `django_migrations` VALUES ('252', 'oa', '0032_auto_20160512_1038', '2016-05-17 13:31:01');
INSERT INTO `django_migrations` VALUES ('253', 'oa', '0033_auto_20160512_1113', '2016-05-17 13:31:01');
INSERT INTO `django_migrations` VALUES ('254', 'oa', '0034_auto_20160512_1119', '2016-05-17 13:31:02');
INSERT INTO `django_migrations` VALUES ('255', 'oa', '0035_auto_20160512_1134', '2016-05-17 13:31:03');
INSERT INTO `django_migrations` VALUES ('256', 'oa', '0036_auto_20160512_1524', '2016-05-17 13:31:03');
INSERT INTO `django_migrations` VALUES ('257', 'oa', '0037_auto_20160513_1655', '2016-05-17 13:31:04');
INSERT INTO `django_migrations` VALUES ('258', 'oa', '0038_auto_20160516_1046', '2016-05-17 13:31:05');
INSERT INTO `django_migrations` VALUES ('259', 'oa', '0039_auto_20160516_1207', '2016-05-17 13:31:06');
INSERT INTO `django_migrations` VALUES ('260', 'oa', '0040_auto_20160517_1309', '2016-05-17 13:31:06');
INSERT INTO `django_migrations` VALUES ('261', 'api', '0016_auto_20160517_1449', '2016-05-17 14:49:54');
INSERT INTO `django_migrations` VALUES ('262', 'erp', '0104_auto_20160517_1449', '2016-05-17 14:49:54');
INSERT INTO `django_migrations` VALUES ('263', 'api', '0017_headline_read_num', '2016-05-19 11:20:03');
INSERT INTO `django_migrations` VALUES ('264', 'erp', '0105_auto_20160519_1119', '2016-05-19 11:20:03');
INSERT INTO `django_migrations` VALUES ('265', 'erp', '0106_auto_20160519_1356', '2016-05-19 13:57:02');
INSERT INTO `django_migrations` VALUES ('266', 'erp', '0107_announcement_read_num', '2016-05-19 14:44:52');
INSERT INTO `django_migrations` VALUES ('267', 'erp', '0108_auto_20160520_1519', '2016-05-20 15:19:31');
INSERT INTO `django_migrations` VALUES ('268', 'erp', '0109_auto_20160520_1728', '2016-05-20 17:28:52');
INSERT INTO `django_migrations` VALUES ('269', 'erp', '0110_auto_20160523_1429', '2016-05-23 14:30:09');
INSERT INTO `django_migrations` VALUES ('270', 'erp', '0111_auto_20160523_1657', '2016-05-23 16:58:22');
INSERT INTO `django_migrations` VALUES ('271', 'erp', '0112_auto_20160524_1416', '2016-05-24 14:17:04');
INSERT INTO `django_migrations` VALUES ('272', 'api', '0018_emailcode_emailvalidsecond', '2016-05-24 16:07:55');
INSERT INTO `django_migrations` VALUES ('273', 'erp', '0113_auto_20160524_1613', '2016-05-24 16:13:23');
INSERT INTO `django_migrations` VALUES ('274', 'erp', '0114_auto_20160524_1659', '2016-05-24 16:59:26');
INSERT INTO `django_migrations` VALUES ('275', 'api', '0019_auto_20160525_1058', '2016-05-25 13:09:46');
INSERT INTO `django_migrations` VALUES ('276', 'api', '0020_auto_20160525_1115', '2016-05-25 13:09:46');
INSERT INTO `django_migrations` VALUES ('277', 'api', '0021_point', '2016-05-25 14:56:19');
INSERT INTO `django_migrations` VALUES ('278', 'erp', '0115_auto_20160525_1508', '2016-05-25 15:10:07');
INSERT INTO `django_migrations` VALUES ('279', 'erp', '0116_auto_20160526_1314', '2016-05-26 13:14:41');
INSERT INTO `django_migrations` VALUES ('280', 'erp', '0117_auto_20160526_1321', '2016-05-26 13:21:44');
INSERT INTO `django_migrations` VALUES ('281', 'oa', '0041_auto_20160527_1601', '2016-05-27 16:01:13');
INSERT INTO `django_migrations` VALUES ('282', 'web_customer', '0005_business_carousel', '2016-05-27 16:38:29');
INSERT INTO `django_migrations` VALUES ('283', 'erp', '0118_auto_20160527_1658', '2016-05-27 16:58:09');
INSERT INTO `django_migrations` VALUES ('284', 'web_customer', '0006_auto_20160527_1745', '2016-05-27 17:45:20');
INSERT INTO `django_migrations` VALUES ('285', 'erp', '0119_position_department', '2016-05-31 10:27:07');
INSERT INTO `django_migrations` VALUES ('286', 'erp', '0120_auto_20160531_1135', '2016-05-31 11:35:55');
INSERT INTO `django_migrations` VALUES ('288', 'api', '0022_auto_20160531_1448', '2016-06-01 16:04:37');
INSERT INTO `django_migrations` VALUES ('293', 'oa', '0042_auto_20160602_1329', '2016-06-02 13:38:23');
INSERT INTO `django_migrations` VALUES ('294', 'oa', '0043_remove_checkwork_history_time_now', '2016-06-02 15:54:21');
INSERT INTO `django_migrations` VALUES ('295', 'oa', '0044_auto_20160602_1753', '2016-06-02 17:53:42');
INSERT INTO `django_migrations` VALUES ('296', 'oa', '0045_auto_20160603_1754', '2016-06-03 17:54:18');
INSERT INTO `django_migrations` VALUES ('297', 'erp', '0121_agent_wechat', '2016-06-06 17:15:35');
INSERT INTO `django_migrations` VALUES ('298', 'erp', '0122_agent_qq_number', '2016-06-06 17:15:43');
INSERT INTO `django_migrations` VALUES ('299', 'erp', '0123_auto_20160606_1723', '2016-06-06 17:23:19');
INSERT INTO `django_migrations` VALUES ('300', 'erp', '0124_auto_20160608_1349', '2016-06-08 14:00:32');
INSERT INTO `django_migrations` VALUES ('301', 'erp', '0125_auto_20160613_1739', '2016-06-13 17:39:25');
INSERT INTO `django_migrations` VALUES ('302', 'erp', '0126_agent_device_id', '2016-06-16 14:34:35');
INSERT INTO `django_migrations` VALUES ('303', 'erp', '0127_auto_20160616_1440', '2016-06-16 14:41:14');
INSERT INTO `django_migrations` VALUES ('304', 'oa', '0046_auto_20160616_1440', '2016-06-16 14:41:19');
INSERT INTO `django_migrations` VALUES ('305', 'erp', '0128_auto_20160617_1453', '2016-06-17 14:53:31');
INSERT INTO `django_migrations` VALUES ('306', 'api', '0023_auto_20160617_1500', '2016-06-20 15:08:39');
INSERT INTO `django_migrations` VALUES ('307', 'api', '0024_auto_20160617_1502', '2016-06-20 15:08:39');
INSERT INTO `django_migrations` VALUES ('308', 'api', '0025_auto_20160617_1554', '2016-06-20 15:08:39');
INSERT INTO `django_migrations` VALUES ('309', 'oa', '0047_auto_20160616_1729', '2016-06-20 17:04:37');
INSERT INTO `django_migrations` VALUES ('310', 'oa', '0048_auto_20160620_1404', '2016-06-20 17:04:37');
INSERT INTO `django_migrations` VALUES ('311', 'api', '0026_comment', '2016-06-21 09:43:36');
INSERT INTO `django_migrations` VALUES ('312', 'api', '0027_comment_is_valid', '2016-06-28 16:01:35');
INSERT INTO `django_migrations` VALUES ('313', 'agent_api', '0004_temporary_file', '2016-07-01 15:55:25');
INSERT INTO `django_migrations` VALUES ('314', 'agent_api', '0005_auto_20160620_1517', '2016-07-01 15:55:25');
INSERT INTO `django_migrations` VALUES ('315', 'easy_thumbnails', '0001_initial', '2016-07-05 10:30:55');
INSERT INTO `django_migrations` VALUES ('316', 'easy_thumbnails', '0002_thumbnaildimensions', '2016-07-05 10:30:55');
INSERT INTO `django_migrations` VALUES ('317', 'api', '0028_auto_20160707_1401', '2016-07-07 17:56:16');
INSERT INTO `django_migrations` VALUES ('318', 'erp', '0129_online_chat', '2016-07-20 15:58:50');
INSERT INTO `django_migrations` VALUES ('319', 'erp', '0130_online_chat_read', '2016-07-20 16:10:40');
INSERT INTO `django_migrations` VALUES ('320', 'erp', '0129_redister_business', '2016-07-25 11:27:32');
INSERT INTO `django_migrations` VALUES ('321', 'erp', '0130_auto_20160725_1406', '2016-07-25 14:07:02');
INSERT INTO `django_migrations` VALUES ('322', 'erp', '0131_auto_20160725_1517', '2016-07-25 15:17:34');
INSERT INTO `django_migrations` VALUES ('323', 'erp', '0131_redister_business_status', '2016-07-25 16:23:11');
INSERT INTO `django_migrations` VALUES ('324', 'oa', '0049_check_time_setting', '2016-07-26 14:00:13');
INSERT INTO `django_migrations` VALUES ('325', 'erp', '0132_merge', '2016-08-05 10:39:44');
INSERT INTO `django_migrations` VALUES ('326', 'api', '0029_auto_20160810_1514', '2016-08-11 09:51:39');
INSERT INTO `django_migrations` VALUES ('327', 'erp', '0133_auto_20160815_1737', '2016-08-15 17:37:32');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('00dit4lvz17xoj1smyuhhr8j7axwtt0j', 'OGUzOTIxNjQ0MzMyY2QwMjk5NmY4YmQ5NjM1MzEyYTQ3YTFiZGQ0Njp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk3ZTlmYWI5NTdlZjBmZWUzYjhhN2FmYWVjN2RhNDgxNzc3NmY3NzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyMiJ9', '2016-05-03 17:19:55');
INSERT INTO `django_session` VALUES ('06odc2soj2ez7bjxmz7oeukte64bo3u6', 'MmViMGFjYjI3YzZjMDU5ZmNkN2E5YmQ2YmM1ZjcyNGVmN2IyZjZhOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6MjB9', '2016-06-30 14:39:15');
INSERT INTO `django_session` VALUES ('0lhfse7wik126vu6gf339sh5wymvxr0m', 'ZjE4YWI4ZTRiNDMwZjk3ZGVjNzMyYWUzZjk0OWFkZWVhZDAzNjY0ZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImFjOTg3YTljNTQ3MjJkNzllYjYwNzU3MjNlODk3MjA1ZWVkYjAxNTYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyMCJ9', '2016-05-11 14:38:10');
INSERT INTO `django_session` VALUES ('0rdsjs5qbzxt3mazp49zjltooy2wemqa', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-08 11:45:11');
INSERT INTO `django_session` VALUES ('1e6ui98j6nm0vhpndh76sh7lq0a7m56m', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-12 19:22:06');
INSERT INTO `django_session` VALUES ('1i30aqw2wcniqaa4oqgi73bwfye26hb7', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 12:50:35');
INSERT INTO `django_session` VALUES ('1iel4ynumkj9ays8pilviu24s7v0lf34', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 17:32:35');
INSERT INTO `django_session` VALUES ('1ksvqgz8vr74trvdrgo7tqqojla9sbo1', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:34:24');
INSERT INTO `django_session` VALUES ('1nrvt0k6o5bun7tyr2zpsjudtkc0q5i8', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-27 19:27:28');
INSERT INTO `django_session` VALUES ('1p1aanqehzc22r8mj9uknqxfqjzsey3o', 'OGYzYjkyY2MzMThhYzJkZDYxNTMyMzdmMmMzYWM0NmFkZGNmNDE5Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWEwOWI2OTYzYzA5MjU5MTQ1MzE0YmY2MTFiOGMyZWJmODllOTUyMiIsIl9hdXRoX3VzZXJfaWQiOiI2NiIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-28 16:22:27');
INSERT INTO `django_session` VALUES ('1qbne0jgy58rb51xxf5xsz71txeh3pip', 'MTBhM2U3ZTRlMDA4NmFmMWQ2Zjk1MGY1ZGQyY2NkNGVmNmYyZjNiMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjA0ZjlkYTA4YjhmNzI5NDM5OWY4YjlmYzZhZmI3Y2I0ZDAxNDAzYzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSJ9', '2016-05-06 17:34:56');
INSERT INTO `django_session` VALUES ('1s7oidg3dr9q2j70vi03sfswwvizov8t', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:44:09');
INSERT INTO `django_session` VALUES ('1yz5fh0bfh40z7ehx2t4bbyfdmhal48j', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-06-30 16:49:15');
INSERT INTO `django_session` VALUES ('244eulqm5pa3dwbhqtn491lc45x05eq7', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 12:50:14');
INSERT INTO `django_session` VALUES ('27odupse4il8c5o0udxuwq14rfrsy1j0', 'OWY1Njc5ODE0MTg1MGY4MzFmNDhmMGZiNGE3Mjc5NjBiNDNhY2E2Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjVlMTQyNzhlOTY5NmM3YWU1ODI3ODUyOGIwNjU4NDc5Y2Y2MmEwNjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNyJ9', '2016-05-12 13:58:07');
INSERT INTO `django_session` VALUES ('2ger6unsfiwxzezkem9j3wm7jc02gqrp', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-07-01 19:47:28');
INSERT INTO `django_session` VALUES ('2r7vs62aacswnn65cjyml5fykvvwsqp1', 'MGE2MGE5NzQ2ODdjNWIxMGEwZDNjY2JlMDg2NGNmNjUzYTUxNmFhYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-31 16:02:13');
INSERT INTO `django_session` VALUES ('2svpw2ruz1istodtg0l0nzm6jd1c9c7s', 'NGViYmI0ZTY3OGU3M2JiZGU3MTA3MzBiN2M4ODY3YmNhNGVlYmY1Nzp7Il9hdXRoX3VzZXJfaGFzaCI6ImM3YjBmMGNiYjU5YTk3MWY1ZGMzZTAzMmYzMjg2NTc1NmZmYTY2MGQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyNiJ9', '2016-06-20 16:37:49');
INSERT INTO `django_session` VALUES ('3e1ltx4qouax9h8vv63yy6yidddpfqvq', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-27 11:27:41');
INSERT INTO `django_session` VALUES ('3ihfg7ogtl97ax66miqy6p51cwibyn5c', 'N2NmNzc1Njc3ZTNjODE2ZmMzNmM4MGZlZWVhNDZiMWI5MTM5OTk4NDp7Il9hdXRoX3VzZXJfaGFzaCI6IjUxNGI1YzQ0ZmE5YWUzMTExMTliMjFhY2ViMzliZGQyODZiNDVkYzMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyNSJ9', '2016-06-29 17:48:54');
INSERT INTO `django_session` VALUES ('3kn7ob7xyd2z4tgfyp1jhe109c7rpx7l', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 12:39:24');
INSERT INTO `django_session` VALUES ('44qwxku75rzx2gcy16jzgokg1pjpf6vf', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-03 11:48:28');
INSERT INTO `django_session` VALUES ('4wb4bbe52pdqlso7b2y9hf5676i5g5yu', 'NjQ2N2VkMDM0NGNiMDQ0ZjVmMGJiMTZhNmIyMWU2OTY2NWJlMzJjYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNmQzOTg1ZjA4NTg1YTk2ODQwMzc5ODZlMmM5ODhjYzg3MWNmZTgzOCIsIl9hdXRoX3VzZXJfaWQiOiI0MCIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-22 12:01:50');
INSERT INTO `django_session` VALUES ('50te55bj9ql2203r9ladw1must87u17h', 'MGE2MGE5NzQ2ODdjNWIxMGEwZDNjY2JlMDg2NGNmNjUzYTUxNmFhYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-30 18:07:07');
INSERT INTO `django_session` VALUES ('51mm84m4y6zyeogxgome583fzp9mg8nv', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-13 13:42:21');
INSERT INTO `django_session` VALUES ('53vznrvifl40qw4plthxy6h1ucffoj4w', 'YzNlMDE2ZTBiMjQ0M2JjNmRjYjliODQxZTg2NTNmMDlmYjQzNTVjYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImU3YTFmYTA5NmE0ZjhhYWNlNjA3ZDljYTA5ZWYzZWY4OWJhNWNkYTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyNCJ9', '2016-03-31 13:38:35');
INSERT INTO `django_session` VALUES ('54ezlpbx4g652h05xl1yqe9hhsbb1pct', 'OWY1Njc5ODE0MTg1MGY4MzFmNDhmMGZiNGE3Mjc5NjBiNDNhY2E2Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjVlMTQyNzhlOTY5NmM3YWU1ODI3ODUyOGIwNjU4NDc5Y2Y2MmEwNjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNyJ9', '2016-04-06 15:51:57');
INSERT INTO `django_session` VALUES ('576jdjvmjra5wcglts4v6lwlu9hklr7z', 'Y2I1NDhjNjg1NWY5YWU2MzAyOGFiYmM5ZWE1ODEyYjNjNWUxM2M4Mjp7Il9zZXNzaW9uX2V4cGlyeSI6MjB9', '2016-06-30 14:39:37');
INSERT INTO `django_session` VALUES ('5dtko7y2wmb9bfzg5kgcud1cznridb8c', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 17:24:08');
INSERT INTO `django_session` VALUES ('5osem884yyhc3qedzctxk2o7thzrrgtc', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-28 17:38:11');
INSERT INTO `django_session` VALUES ('5s3kxduc0n4bkj4ldt4xdnj84xntslzy', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-27 17:52:28');
INSERT INTO `django_session` VALUES ('5uf5q7p34lpehtqiqfdmkcanwa8xua1y', 'NjVmNDZkY2YyYzllY2ViNjgwMmQyZTczYWUwY2IwMDkxMjg3NzA1ODp7Il9hdXRoX3VzZXJfaGFzaCI6IjAzZGEzMThiYTdhNTA5ZmExYjFjOTkyMzM2YTk5MTQ5ZjU5NWIzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyMyJ9', '2016-04-15 14:03:26');
INSERT INTO `django_session` VALUES ('6csq89eewozuzgb24adgmndyssgj3idg', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 19:50:00');
INSERT INTO `django_session` VALUES ('6oidsz1up8trnqqvenuaw9dn0y6ei5kv', 'NDNhMGFkYTU0MTU1MjQzMDViNTE1MGZkMDIyNTNhZmI0NzRhZjY2ZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTBkZTU5Y2RjZTNlMDJhMDRhZWVhMGRkODdiNjIzN2IxYjUyYWVhNiIsIl9hdXRoX3VzZXJfaWQiOiIxNyIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-02 16:35:53');
INSERT INTO `django_session` VALUES ('6rug1pym0ngm5yb7qgaahg2k85q3l57y', 'MTI5YTNjZDBkN2QwZjY4MjgwNjk5ZTkyMWUwZWFlZGFkYjg1ZmJlODp7Il9hdXRoX3VzZXJfaGFzaCI6ImIwYTJjM2UyNmQ0MDUwNDQ1NGZlMWNiNWIzNWQwMzk3YWRjNWViZjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzMyJ9', '2016-04-26 17:59:02');
INSERT INTO `django_session` VALUES ('6w74rwuzykrleqhk2vmaif3vmoe7y6ht', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:12:37');
INSERT INTO `django_session` VALUES ('7c3p6atx1kfclppve6ft94hhznunf1k9', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 18:36:14');
INSERT INTO `django_session` VALUES ('7qqeloktev5usr3ei4e61ugkeq8nh6q6', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-22 19:16:00');
INSERT INTO `django_session` VALUES ('7so44ni916cn1aa8o3z975ull7gi6m0z', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-08 18:58:13');
INSERT INTO `django_session` VALUES ('85shz9xcbqw7ygdkk3s6xz2fd0oblqhz', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-17 13:41:40');
INSERT INTO `django_session` VALUES ('88tig74vl0hn2hr96413kxq5wq1jlswa', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-27 19:29:17');
INSERT INTO `django_session` VALUES ('89u5xs5fwt4dtqpjnp0pb41jcyymn3ab', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-08-09 19:38:01');
INSERT INTO `django_session` VALUES ('8ca4n34e3mnkwi4uvqj88dr8eotkd94k', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-07-05 12:33:11');
INSERT INTO `django_session` VALUES ('8fabd0519jt2lk1e45l6v2j9vprcqzph', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 13:49:25');
INSERT INTO `django_session` VALUES ('8lt54pzobyscorxi7qwckpjsevpapu6p', 'MGE2MGE5NzQ2ODdjNWIxMGEwZDNjY2JlMDg2NGNmNjUzYTUxNmFhYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-29 13:53:38');
INSERT INTO `django_session` VALUES ('8qwet7p9y9sbpm65826gn1ccshpchf89', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 15:24:00');
INSERT INTO `django_session` VALUES ('8r3983cl2bimmxl9xdnuh0052xzzjxrq', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-22 17:58:39');
INSERT INTO `django_session` VALUES ('8zbdfv09lqre09u44a4n4qbkfhlbkjkg', 'N2NlODI0N2M0MDVlMjAxMjAyYmIyYmNjYzAyZjk3ZWFkY2JlYTM2YTp7Il9hdXRoX3VzZXJfaGFzaCI6IjUwOTY2MmRjMjZmZDk5NDZhNTMwNjdmMDAyZjFkZTNiNzUyODBlMWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNyJ9', '2016-06-28 13:45:13');
INSERT INTO `django_session` VALUES ('9eotq3btgofx38gm7fbnl4yod31nm83h', 'Y2UyZmFlMmU5MTc5N2Y2MmZkMjdiYjJmNTQxNjA1NThkZTY0NjZmZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTA5NjYyZGMyNmZkOTk0NmE1MzA2N2YwMDJmMWRlM2I3NTI4MGUxYSIsIl9hdXRoX3VzZXJfaWQiOiIxNyIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-04 19:19:59');
INSERT INTO `django_session` VALUES ('9kpbtfk67quu807k0y10n10aadxh1xjo', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-28 20:00:09');
INSERT INTO `django_session` VALUES ('9z0b672epe1mm5pmhwh49mcx173mhxxh', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-15 13:55:49');
INSERT INTO `django_session` VALUES ('acomfbdc1xw91tjzkh80ntlm7eldsow0', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-01 11:15:38');
INSERT INTO `django_session` VALUES ('als9yfngy4cix50c1k1744o91z6lpinz', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-04 11:14:27');
INSERT INTO `django_session` VALUES ('aoylru9x9guha3lem2wk0ts4vbkqog3z', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-22 12:20:16');
INSERT INTO `django_session` VALUES ('arrvg4h6a2ykpfnscj5fvzvaadqvt6ck', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-08-01 19:40:01');
INSERT INTO `django_session` VALUES ('at160yn40ojp2arx8qjsv33137mr81xv', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-08-02 19:58:18');
INSERT INTO `django_session` VALUES ('atmw6dmjy0sjimm0t1t0fssxeyvazg8j', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-04 14:00:47');
INSERT INTO `django_session` VALUES ('axf46n4jgvnz3976vgh6mu50u3lfxs7u', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 19:58:09');
INSERT INTO `django_session` VALUES ('b3re4nfhlm9gudlm7190s2a584ox88j2', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-09-12 12:31:40');
INSERT INTO `django_session` VALUES ('ba36hkeiix3268vmkkouq7k5qy6pw5mo', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-08 11:10:57');
INSERT INTO `django_session` VALUES ('balhb92x8wiffhrffir5m0iqtvwz1jar', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 19:50:00');
INSERT INTO `django_session` VALUES ('bpjomxw61wak2ewhtz5yan2mc7ldre0x', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-08-03 19:57:54');
INSERT INTO `django_session` VALUES ('bruk76bi0d64gqn00nj0du252x3i319n', 'NGViYmI0ZTY3OGU3M2JiZGU3MTA3MzBiN2M4ODY3YmNhNGVlYmY1Nzp7Il9hdXRoX3VzZXJfaGFzaCI6ImM3YjBmMGNiYjU5YTk3MWY1ZGMzZTAzMmYzMjg2NTc1NmZmYTY2MGQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyNiJ9', '2016-06-17 17:36:12');
INSERT INTO `django_session` VALUES ('btnn33ejly9l8wfqki9js0oc8ay2d3e1', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-06-30 19:52:23');
INSERT INTO `django_session` VALUES ('bu2e4fcwjpnlavx220u5xaygjdl1bw1h', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-09-13 19:36:06');
INSERT INTO `django_session` VALUES ('cb1e6yrkv85yyk0xajf10mlhrciie4h4', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-28 12:57:07');
INSERT INTO `django_session` VALUES ('cii117pvvfpfxtuzyvz5q6tg1r7ztt1d', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-09-13 16:08:28');
INSERT INTO `django_session` VALUES ('cuxv3ela4w6wokh0q9ck2qvmvpvu22b8', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-20 20:03:24');
INSERT INTO `django_session` VALUES ('cvh1ir0re688bbv8b025qb6fzeg9vji5', 'NzVkYmIyMmEyMzMyYWYwZmYwMjE0ZGUwZjRiYjM2N2I5NDlkZmIxOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjBjMjcxM2EyOGE0MTYyZGNmOTUyMzg5MmM0YjFhYjg0N2RmNzc0YjAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNSJ9', '2016-03-23 17:23:55');
INSERT INTO `django_session` VALUES ('d8d819b5lj2qbwhdpgoukrvl6gc6i0z0', 'NzQ1MDRlZDE1NmE1ZDkzNTJlYmJkMTNkMDA5MjE5ZWQwMjc4YzZmYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjZkMzk4NWYwODU4NWE5Njg0MDM3OTg2ZTJjOTg4Y2M4NzFjZmU4MzgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0MCJ9', '2016-06-30 14:23:02');
INSERT INTO `django_session` VALUES ('d98gwgfijhi6xxiske93x37t0pbo8e4n', 'Y2UyZmFlMmU5MTc5N2Y2MmZkMjdiYjJmNTQxNjA1NThkZTY0NjZmZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTA5NjYyZGMyNmZkOTk0NmE1MzA2N2YwMDJmMWRlM2I3NTI4MGUxYSIsIl9hdXRoX3VzZXJfaWQiOiIxNyIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-18 19:45:49');
INSERT INTO `django_session` VALUES ('d9bg097n2ykvx0er9fdur1qhnu9yovx5', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-04 15:14:23');
INSERT INTO `django_session` VALUES ('di3nbb8vsml6d9ykoo7qfhr3njysg4cm', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 19:53:32');
INSERT INTO `django_session` VALUES ('dyf3mrtccwsbxn58gbu82lkjzyc31v5a', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-11 19:53:59');
INSERT INTO `django_session` VALUES ('e0afsae8qnhg3ltb14g7da5qzg47z2sb', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-08 13:52:56');
INSERT INTO `django_session` VALUES ('ec78h8l8v7301hn4zc85zdwezqt54mf4', 'MTAyMjY0OWQxNTdjOWIxZTE4ODJmNzhkODk0N2IwNzZiYjExM2MyYzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiNTA5NjYyZGMyNmZkOTk0NmE1MzA2N2YwMDJmMWRlM2I3NTI4MGUxYSIsIl9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-08-29 18:00:28');
INSERT INTO `django_session` VALUES ('er4wukurw50s9hyoyzmsnd4syfswnbo5', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-07-25 12:34:08');
INSERT INTO `django_session` VALUES ('ez2va7jjxwaa9ov1ltykcq4dq05o58sn', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-07-04 17:32:34');
INSERT INTO `django_session` VALUES ('f2bad0zfunzo711d293uytum6cthee65', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-19 19:43:14');
INSERT INTO `django_session` VALUES ('f3js6b1hsv1im7fz5awp2xb4qq7bqnii', 'OWY1Njc5ODE0MTg1MGY4MzFmNDhmMGZiNGE3Mjc5NjBiNDNhY2E2Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjVlMTQyNzhlOTY5NmM3YWU1ODI3ODUyOGIwNjU4NDc5Y2Y2MmEwNjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNyJ9', '2016-04-12 10:48:19');
INSERT INTO `django_session` VALUES ('fbgx2tqeigqiape8rwd3nykqy5r38in1', 'MmQ1ZmQ2MWNiOWY5OTEyZGQwNTUyYzFiMTJmOGUwOWVlNDEyYjMxOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOThhZjIyODBiNWYwNjdhZGQ1ODMwNmJkYjA5OWU0MDU1MGU2MjNkYyIsIl9hdXRoX3VzZXJfaWQiOiI4NyIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-26 17:11:21');
INSERT INTO `django_session` VALUES ('fiunp4dm48zcqfna4fvhfa41qyx69ppf', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-27 19:26:56');
INSERT INTO `django_session` VALUES ('fl3jbhkh55tkrer67rijy6kwpwq2rs73', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:33:48');
INSERT INTO `django_session` VALUES ('fxoobdqa6ei181xhv0o183cy9e74aoce', 'MGE2MGE5NzQ2ODdjNWIxMGEwZDNjY2JlMDg2NGNmNjUzYTUxNmFhYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-04-29 17:23:57');
INSERT INTO `django_session` VALUES ('gef116rvi5asnfyg92u5h7ghrq764sg4', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-02 12:57:22');
INSERT INTO `django_session` VALUES ('ggl5ds9lepu52zcus4ca2jjots0sw97y', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:04:08');
INSERT INTO `django_session` VALUES ('gq31kjqn3ebujyiilf1s3b6y1zmmm9bi', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:40:15');
INSERT INTO `django_session` VALUES ('gtohlcz9r7zke5n1qmngq19czfbazc3o', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-04 12:20:39');
INSERT INTO `django_session` VALUES ('gu6re1pl91gkna64eiz84jasydgxr9jx', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-08-08 17:05:56');
INSERT INTO `django_session` VALUES ('gxpyfyk4epcrpm9ttsm8wcxa0n2e5krt', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-27 19:30:39');
INSERT INTO `django_session` VALUES ('gyo3bgsrion5zhbyrm9wfzjeb4m101ty', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:33:55');
INSERT INTO `django_session` VALUES ('h7pvve6u6xg1rcve4lm4bsyr9i8txm93', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 15:38:34');
INSERT INTO `django_session` VALUES ('ha6y9gl4vsn8yfdxwsu4sx1jxx10rlh0', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-08 11:10:57');
INSERT INTO `django_session` VALUES ('hfk1xr8e4x5qaas2vyct85ea0ixgamjr', 'NDNhMGFkYTU0MTU1MjQzMDViNTE1MGZkMDIyNTNhZmI0NzRhZjY2ZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTBkZTU5Y2RjZTNlMDJhMDRhZWVhMGRkODdiNjIzN2IxYjUyYWVhNiIsIl9hdXRoX3VzZXJfaWQiOiIxNyIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-02 17:10:00');
INSERT INTO `django_session` VALUES ('hgtesjibc62fimnoossqllwvax8k1rui', 'N2NmNzc1Njc3ZTNjODE2ZmMzNmM4MGZlZWVhNDZiMWI5MTM5OTk4NDp7Il9hdXRoX3VzZXJfaGFzaCI6IjUxNGI1YzQ0ZmE5YWUzMTExMTliMjFhY2ViMzliZGQyODZiNDVkYzMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyNSJ9', '2016-06-02 16:54:06');
INSERT INTO `django_session` VALUES ('hisdasrojit4zl7mx5c6572wt498yfkh', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:05:04');
INSERT INTO `django_session` VALUES ('hwovdnvxhp6xd6iaop6byc5m82ij3gdd', 'MTAyMjY0OWQxNTdjOWIxZTE4ODJmNzhkODk0N2IwNzZiYjExM2MyYzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiNTA5NjYyZGMyNmZkOTk0NmE1MzA2N2YwMDJmMWRlM2I3NTI4MGUxYSIsIl9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-27 11:32:24');
INSERT INTO `django_session` VALUES ('ipvvttt3vpwrjy0y89eb4oi6tg6vnnhr', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-09 17:23:42');
INSERT INTO `django_session` VALUES ('iu2wgi0dozh91rucpog9ogtlyfb0duzi', 'NWJjYTdhNWY2Nzg0NTAzZDAwZWQ4MjEzZDc4YTNhYzk2NDFiMGUyYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiNmQzOTg1ZjA4NTg1YTk2ODQwMzc5ODZlMmM5ODhjYzg3MWNmZTgzOCIsIl9hdXRoX3VzZXJfaWQiOiI0MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-21 18:07:16');
INSERT INTO `django_session` VALUES ('j3tvhfuzedqq8bsfqnjrrhan0sz5zy49', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-05 18:31:39');
INSERT INTO `django_session` VALUES ('j4197tsnf9t732b552ffugvh3szw88dw', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-26 11:19:56');
INSERT INTO `django_session` VALUES ('j41blauotxwy1e2st7uqr6lz9u9gcxu3', 'NjQ2N2VkMDM0NGNiMDQ0ZjVmMGJiMTZhNmIyMWU2OTY2NWJlMzJjYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNmQzOTg1ZjA4NTg1YTk2ODQwMzc5ODZlMmM5ODhjYzg3MWNmZTgzOCIsIl9hdXRoX3VzZXJfaWQiOiI0MCIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-29 20:00:07');
INSERT INTO `django_session` VALUES ('jrflwg67qblpvm7opn5mv2v77nriecof', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-07-01 18:10:55');
INSERT INTO `django_session` VALUES ('jufzzjl2orx9pv6u0w59qxduicmon1fi', 'OWY1Njc5ODE0MTg1MGY4MzFmNDhmMGZiNGE3Mjc5NjBiNDNhY2E2Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjVlMTQyNzhlOTY5NmM3YWU1ODI3ODUyOGIwNjU4NDc5Y2Y2MmEwNjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNyJ9', '2016-03-30 17:54:29');
INSERT INTO `django_session` VALUES ('jyy06pgq2io06xecfrjyh5n8axi3vxgh', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-24 17:18:02');
INSERT INTO `django_session` VALUES ('k63c9aekkjc82sb7nq5tiow82526ee7t', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-14 12:08:33');
INSERT INTO `django_session` VALUES ('kdnls096hs3ts6dty7dr0dr4hni9jc7t', 'OWI5NjA2Nzc1NTgzZTc0MGI2ZDRiN2M3N2Q2MDY4NGZmZjIzNGRjNDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk4NGUyNWNkOTg3YThlNzkxNzEwMWQwZDAzNDIzMTdmMmQzNzZjY2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNyJ9', '2016-05-26 17:01:22');
INSERT INTO `django_session` VALUES ('klz9d5z0pu3z7rkzvajgtweo0jufewmp', 'NzQ1MDRlZDE1NmE1ZDkzNTJlYmJkMTNkMDA5MjE5ZWQwMjc4YzZmYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjZkMzk4NWYwODU4NWE5Njg0MDM3OTg2ZTJjOTg4Y2M4NzFjZmU4MzgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0MCJ9', '2016-06-30 14:21:32');
INSERT INTO `django_session` VALUES ('ldkl3jny9h4w00btrqoxltnag903chlk', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-06-30 18:45:57');
INSERT INTO `django_session` VALUES ('llckpy3hevx13kzzk0fx2wb785xv0ya0', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 12:39:29');
INSERT INTO `django_session` VALUES ('lml2nzpiq3p0se4gdt5x06zcll9qc9xo', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-09 17:40:49');
INSERT INTO `django_session` VALUES ('luf242v1i7moffrn9v1gsaz0xp1btzmy', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-05 19:47:19');
INSERT INTO `django_session` VALUES ('m0gjk3imrv2tis3a6dr8i1ufwrl38xjt', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:43:07');
INSERT INTO `django_session` VALUES ('m1l79ihf4xn88wo55svlc5ug1xtpnthp', 'MGE2MGE5NzQ2ODdjNWIxMGEwZDNjY2JlMDg2NGNmNjUzYTUxNmFhYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-04-22 05:51:05');
INSERT INTO `django_session` VALUES ('mc1oxmo11c5atsvofnbbyg98rddefpf2', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-07-26 19:23:23');
INSERT INTO `django_session` VALUES ('mkzqpod287l2takisc7ztwzhmdltfa6y', 'MTBhM2U3ZTRlMDA4NmFmMWQ2Zjk1MGY1ZGQyY2NkNGVmNmYyZjNiMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjA0ZjlkYTA4YjhmNzI5NDM5OWY4YjlmYzZhZmI3Y2I0ZDAxNDAzYzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSJ9', '2016-04-22 03:56:26');
INSERT INTO `django_session` VALUES ('mlcnvd4np2rp6plvy2kn8gl4qs8pjnpt', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-08 13:58:34');
INSERT INTO `django_session` VALUES ('mmrdmnuuctbq2a20yhef9n5d4yohdw1c', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-22 14:00:34');
INSERT INTO `django_session` VALUES ('mq2k22qszs6fhxgg4iraj0x737ad9wq4', 'YjlhOWE3MWE2Y2U2MzRhOTZlMWI0MzgzNDZjMDI0ZTM4MzBiYjQ3ZDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-03-31 16:48:11');
INSERT INTO `django_session` VALUES ('mwyvthwz2m6lp8gwb5ew1ztwaktlqhnt', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-21 19:57:32');
INSERT INTO `django_session` VALUES ('mxhrpfq1hvbjxsr6bk7uj3euhfwe6640', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 15:51:01');
INSERT INTO `django_session` VALUES ('n7wtp194z841f3riyp9e8ecgvtaobq02', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-11 13:30:17');
INSERT INTO `django_session` VALUES ('n9nt92d86lu7l6rqs2lnqwf89cfjiymj', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:13:26');
INSERT INTO `django_session` VALUES ('ndgoebhh6lztpmhawaapuihrttgpc0rx', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:34:19');
INSERT INTO `django_session` VALUES ('ngxafvx4702tg3t4rvwpedq2qic6sauh', 'NWJjYTdhNWY2Nzg0NTAzZDAwZWQ4MjEzZDc4YTNhYzk2NDFiMGUyYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiNmQzOTg1ZjA4NTg1YTk2ODQwMzc5ODZlMmM5ODhjYzg3MWNmZTgzOCIsIl9hdXRoX3VzZXJfaWQiOiI0MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-28 19:51:16');
INSERT INTO `django_session` VALUES ('nmjaumcmfycbr58byp6t2ruhux5a3l14', 'ZWI0OTUzYmFhNjczNmM0NWVkOTZkN2E1OTlkMDBjMGZjNWI0NmJhMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiOWEwOWI2OTYzYzA5MjU5MTQ1MzE0YmY2MTFiOGMyZWJmODllOTUyMiIsIl9hdXRoX3VzZXJfaWQiOiI2NiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-29 19:33:28');
INSERT INTO `django_session` VALUES ('nv2se56y3ea629p65b95jx451nhgmihu', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-07-26 12:42:54');
INSERT INTO `django_session` VALUES ('nyqi1pf2pyj9fkbwz5dxjncxea5k9wz0', 'MGE2MGE5NzQ2ODdjNWIxMGEwZDNjY2JlMDg2NGNmNjUzYTUxNmFhYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-05-04 16:51:58');
INSERT INTO `django_session` VALUES ('o8vd7o6axnyxar66033h8jk18n4xbgxg', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-26 13:25:52');
INSERT INTO `django_session` VALUES ('ocklcwxgpd4sstqa589obtonaq01wmju', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-18 11:20:21');
INSERT INTO `django_session` VALUES ('oi7di3pc0kmhkzum4gpdd3n4cf68sqnp', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 15:59:44');
INSERT INTO `django_session` VALUES ('ol7mfg13qy9ipwiun5s546850whw3tsl', 'NGVmNjI4YmEyZDBkNjMyMWE4ZDE0ODRkZDA1Y2UzOWY5MDM0Mzg4ZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjFlMDhiNDFmMjIyYWQzMjU4NTUyYWZkZWYwYzBkOTU4MDZhZTY1MDUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyOCJ9', '2016-03-30 16:00:26');
INSERT INTO `django_session` VALUES ('oo3rymgw2d740dnnfkwvt30wfne6c5x7', 'N2M2ODNjMWM4NWM5MjEwN2Q0ODI4MThiNjBjMzNmYTI3ODdmZTY0Zjp7fQ==', '2016-06-27 16:13:12');
INSERT INTO `django_session` VALUES ('oq31pec4ixjeme3rb12fucbf9gqsvtto', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-07 20:00:15');
INSERT INTO `django_session` VALUES ('orsi2umye6cqgpb7u2msf8chrn7jvbqt', 'YzNlMDE2ZTBiMjQ0M2JjNmRjYjliODQxZTg2NTNmMDlmYjQzNTVjYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImU3YTFmYTA5NmE0ZjhhYWNlNjA3ZDljYTA5ZWYzZWY4OWJhNWNkYTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyNCJ9', '2016-03-31 13:27:58');
INSERT INTO `django_session` VALUES ('otpsxmqm74gp2i1nlcsnrocy7umdixby', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-22 19:18:41');
INSERT INTO `django_session` VALUES ('ots14lhj0baxthpshqwrbam5t1tdh5gg', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-29 20:00:32');
INSERT INTO `django_session` VALUES ('ougtg1yyaifhx39p0sr8siszug5pt4or', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:44:33');
INSERT INTO `django_session` VALUES ('ox6hpf2cthci7mtmp84vzchw12oy2t35', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-02 18:39:59');
INSERT INTO `django_session` VALUES ('pfrw2og2t69dgqfo3b7aw4qb0sy71g4i', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-18 17:53:23');
INSERT INTO `django_session` VALUES ('pm5fiekahbcjalkv4is0bf6x6wgim34d', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-03 11:48:29');
INSERT INTO `django_session` VALUES ('ps1bku264xzmtq3tnk103egqstu68w4w', 'ZWI0OTUzYmFhNjczNmM0NWVkOTZkN2E1OTlkMDBjMGZjNWI0NmJhMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiOWEwOWI2OTYzYzA5MjU5MTQ1MzE0YmY2MTFiOGMyZWJmODllOTUyMiIsIl9hdXRoX3VzZXJfaWQiOiI2NiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-21 19:57:58');
INSERT INTO `django_session` VALUES ('qjxauzmedj0l0cyxp2ncq8o3n5cb111j', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 15:38:34');
INSERT INTO `django_session` VALUES ('qn091thggav3l6p51xdqp3910tuf1e32', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-07-25 19:57:47');
INSERT INTO `django_session` VALUES ('r03rqkpapfq5zpqo88idade4zp0tia4o', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-05 16:35:19');
INSERT INTO `django_session` VALUES ('ra2jstaylqfnqdeurma0z9hvzrbbuklo', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-16 12:21:19');
INSERT INTO `django_session` VALUES ('rggyt36kc1rjwyg9kqdao8fv0nf5w5ml', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-08 15:56:41');
INSERT INTO `django_session` VALUES ('rkzn7720ze3fkodta4pfnotn8jak7s7e', 'Y2UyZmFlMmU5MTc5N2Y2MmZkMjdiYjJmNTQxNjA1NThkZTY0NjZmZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTA5NjYyZGMyNmZkOTk0NmE1MzA2N2YwMDJmMWRlM2I3NTI4MGUxYSIsIl9hdXRoX3VzZXJfaWQiOiIxNyIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-01 19:42:47');
INSERT INTO `django_session` VALUES ('rn6x1szbg8lor3yrprkdwdjxkvmwlnr6', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-09-13 16:40:19');
INSERT INTO `django_session` VALUES ('rv8ccscok4admrogw1tw5rowjah09guj', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-08-12 13:21:09');
INSERT INTO `django_session` VALUES ('rzam0ssaxd2gnv8lfkk8izblc2xebwuz', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-25 15:45:01');
INSERT INTO `django_session` VALUES ('sdhwlvl9efoaihve5tvjcpxulf6wh7sr', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-24 15:01:04');
INSERT INTO `django_session` VALUES ('sv11g6v9tnbzt4hjdtz53mgxafy72qke', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-08-19 18:23:44');
INSERT INTO `django_session` VALUES ('sw9h1elfds9bjonwmhdpthm6okxj31mq', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 15:36:02');
INSERT INTO `django_session` VALUES ('t0vk0yj55xz24py3a3l9jfo2wi70rxg6', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 15:59:40');
INSERT INTO `django_session` VALUES ('t5mlvxv6pg39pzh1ftvdw8rvjktsfxc2', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-22 11:27:18');
INSERT INTO `django_session` VALUES ('t78mn81xenrqu59obkuekn80t8rc0w0o', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-08-17 17:32:28');
INSERT INTO `django_session` VALUES ('t9bmsvdq75m24h62exnpr8piudspao01', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-04 19:28:17');
INSERT INTO `django_session` VALUES ('ti1p0xecqzokjxqiixu1ezbn7j17jz96', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-11 19:59:37');
INSERT INTO `django_session` VALUES ('tjn17j0s5ip6fmwkkjsyyb0xosgselnn', 'MGE2MGE5NzQ2ODdjNWIxMGEwZDNjY2JlMDg2NGNmNjUzYTUxNmFhYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-05-13 17:22:19');
INSERT INTO `django_session` VALUES ('tk1kq3h1qhv1svhozatjdxrfja0gvzuk', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-25 11:28:08');
INSERT INTO `django_session` VALUES ('u4wlo9f35srecdkbao3wi36st2ixfp3f', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-28 11:33:46');
INSERT INTO `django_session` VALUES ('u9lwudr3iq9jyw7m025b6d9lsl3dwdbz', 'ZjE4YWI4ZTRiNDMwZjk3ZGVjNzMyYWUzZjk0OWFkZWVhZDAzNjY0ZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImFjOTg3YTljNTQ3MjJkNzllYjYwNzU3MjNlODk3MjA1ZWVkYjAxNTYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyMCJ9', '2016-03-30 18:02:07');
INSERT INTO `django_session` VALUES ('ub6p3b3r0clgqgw3bykjy8n9n423qipk', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-08-16 18:45:41');
INSERT INTO `django_session` VALUES ('ui23ser5bw45z2zw5h7ynpvicupkhze1', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-10 16:24:04');
INSERT INTO `django_session` VALUES ('v78zg866g75qa29r8l52r6b9gs6iaod7', 'M2I3YjhmN2Q1MTBiYjNhYmZkZjIzOGRkZmIzYzg1MGY4MmZjNDcwNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjA2MzcyOWY0YTQ5MjQ4MWIyNWU3ODgxZWVjMjU0YmQ1OTdjMGUzZCIsIl9hdXRoX3VzZXJfaWQiOiIyNCIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-03 13:55:07');
INSERT INTO `django_session` VALUES ('v7k63hou92rlx9hwo0ust8exo5h8pnws', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-07-04 18:56:23');
INSERT INTO `django_session` VALUES ('v91s4it3re23b9mumy13sb0pegrufrtt', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-26 17:58:52');
INSERT INTO `django_session` VALUES ('vdy5s56f1owq2kz9arcm3gtsbwpemv9e', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-01 11:15:38');
INSERT INTO `django_session` VALUES ('vowhiw5r8el447v8zdwzluxrm21oa33r', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-05 18:56:37');
INSERT INTO `django_session` VALUES ('w1j5fw00e0cvyxt9dor6cl44ygr46tke', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 12:40:19');
INSERT INTO `django_session` VALUES ('w7z7p3pon5oqit9e4cpph92c18kb9gha', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 15:35:55');
INSERT INTO `django_session` VALUES ('we3i6k8rdfd9akbqll1x07bqyb36ebj2', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-09 18:50:33');
INSERT INTO `django_session` VALUES ('ws1kntib6pu21124okdjhj7ick65fyck', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-07-25 17:58:09');
INSERT INTO `django_session` VALUES ('wuade71br18n4obhm4651wrtl6d1fube', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-15 19:30:04');
INSERT INTO `django_session` VALUES ('wyawla2myu2l8ndj0v0dvppnyza8x3xy', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-04 13:40:36');
INSERT INTO `django_session` VALUES ('xcckhlei7nzgi1pi42nvfeybigiggkah', 'ZWUyYjcxNjAyZGE3NGNiN2IwZTA3NWY2ZWFlNmQ0ZmY5MWMwMGYxZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjVlMTQyNzhlOTY5NmM3YWU1ODI3ODUyOGIwNjU4NDc5Y2Y2MmEwNjYiLCJfYXV0aF91c2VyX2lkIjoiMTciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9', '2016-04-06 15:49:29');
INSERT INTO `django_session` VALUES ('xhs90vkm0ng3x99ff3hkwgkpxz2zjdcf', 'ZDM1ZjNiNjE5NDdiNjQyMjg3M2ZkZmJhZTQ4ZWE0YTIyMTRhYmJjODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo3MjAwfQ==', '2016-08-05 14:11:57');
INSERT INTO `django_session` VALUES ('xqgfm0m88bj2verwxp9f6vz1tnmcx64s', 'Yjg0MTQ4ZDA3MGNjYWNlNWYzOTYzM2Y2NDRhNTc2MTk3YTcyZGUzYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiY2JjMWU4ZGVlYzI4MDFhNTk2ZGMyMTJiOGI3OTU4MThjMTUwNTdlYSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2016-08-16 12:29:30');
INSERT INTO `django_session` VALUES ('xydrpfoxtr2wa6z3otm4zod7flryenv4', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 15:37:54');
INSERT INTO `django_session` VALUES ('y1qdulumju1mnqbsowrf6gp8scukpwmd', 'YjlhOWE3MWE2Y2U2MzRhOTZlMWI0MzgzNDZjMDI0ZTM4MzBiYjQ3ZDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-04-06 15:12:51');
INSERT INTO `django_session` VALUES ('ydi3vo38dnmbysl9fz30ue94otkf3prs', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-27 19:27:48');
INSERT INTO `django_session` VALUES ('ygg9g08rfr4ycs5gfsykffzbk044r6gm', 'ZDZhZTk2NDUzZTZlNjgxNTIwMzI0YjE2OGFiYjZmY2M3OThiZGM2MTp7Il9hdXRoX3VzZXJfaGFzaCI6ImVmZGJkNmU5OTU4ZGEzMGZkZTgwMGUyMTY3NDIyMmJjYWNmOWE1NjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-25 17:12:20');
INSERT INTO `django_session` VALUES ('yvunt3mxlbkabseli7poeuj47p3egn85', 'NDJhYWVhNjk0ZDNmODQ1MzM3MzViZGQ3YjdkZWE4MWFkYjgyNmQ3NTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-01 11:42:42');
INSERT INTO `django_session` VALUES ('ywvt1icetpev0brrvxndg7pl9s44r8m8', 'OGYzYjkyY2MzMThhYzJkZDYxNTMyMzdmMmMzYWM0NmFkZGNmNDE5Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWEwOWI2OTYzYzA5MjU5MTQ1MzE0YmY2MTFiOGMyZWJmODllOTUyMiIsIl9hdXRoX3VzZXJfaWQiOiI2NiIsIl9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-07-29 12:15:43');
INSERT INTO `django_session` VALUES ('z327vpgsbfl8y7uyeubqpi7dz01m90mm', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-09-12 13:43:44');
INSERT INTO `django_session` VALUES ('za8n5bxrfhkvlf5wsk3mbbkqfwvz7wm8', 'MGE2MGE5NzQ2ODdjNWIxMGEwZDNjY2JlMDg2NGNmNjUzYTUxNmFhYjp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiYzFlOGRlZWMyODAxYTU5NmRjMjEyYjhiNzk1ODE4YzE1MDU3ZWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-31 09:18:48');
INSERT INTO `django_session` VALUES ('zc2f5goyx8ygjianrzuci5gq03e601w3', 'NzdjM2EwNTE3MTg2MjBlMjMwNTk5Y2VjZWU3YTU2YjVmZGQyZmNjMjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMH0=', '2016-08-05 11:23:42');
INSERT INTO `django_session` VALUES ('zo2py9189rnz1j2kt4h050tfd0so05ek', 'NWJjYTdhNWY2Nzg0NTAzZDAwZWQ4MjEzZDc4YTNhYzk2NDFiMGUyYjp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiNmQzOTg1ZjA4NTg1YTk2ODQwMzc5ODZlMmM5ODhjYzg3MWNmZTgzOCIsIl9hdXRoX3VzZXJfaWQiOiI0MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-28 12:57:11');
INSERT INTO `django_session` VALUES ('zqv3hgirmrtu98fd2e41qquxbeoqwrqc', 'ODQ5NmFjNjY0NjQxMzgzZWMyNTU3ZjI1YWU5YzM3ODdiNjg0NWY3ZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyZTAyNDYxNzA1NmQ5YjIwOGYxYmFhNzY3NzMwMmM0ZjYzZTY3NmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSJ9', '2016-07-08 15:50:30');
INSERT INTO `django_session` VALUES ('zu324ii9frmqwqtxupif5g7rqa5t2t8b', 'MTAyMjY0OWQxNTdjOWIxZTE4ODJmNzhkODk0N2IwNzZiYjExM2MyYzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiNTA5NjYyZGMyNmZkOTk0NmE1MzA2N2YwMDJmMWRlM2I3NTI4MGUxYSIsIl9hdXRoX3VzZXJfaWQiOiIxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-07-26 16:39:25');
INSERT INTO `django_session` VALUES ('zw55s8s4ed57h616m0dkxhby2j8ohmcr', 'ZTU4OWI3YzcxNjkxMTJhMWJkNmUyMDI1ZWE2NTIxMTM2ZGRhMjU1Mzp7Il9zZXNzaW9uX2V4cGlyeSI6NzIwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYTJlMDI0NjE3MDU2ZDliMjA4ZjFiYWE3Njc3MzAyYzRmNjNlNjc2ZCIsIl9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2016-08-10 13:36:48');

-- ----------------------------
-- Table structure for easy_thumbnails_source
-- ----------------------------
DROP TABLE IF EXISTS `easy_thumbnails_source`;
CREATE TABLE `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_source_storage_hash_3e1b0d13_uniq` (`storage_hash`,`name`),
  KEY `easy_thumbnails_source_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_source_b068931c` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of easy_thumbnails_source
-- ----------------------------
INSERT INTO `easy_thumbnails_source` VALUES ('1', '676509bd1d8bfde0e77f6f1049253382', 'business/logo/omprufp5ste5ur07fnc3c1vqdtjqvvjvr9tixrdpeceup9brzg8wd46kq9rz.jpg', '2016-08-11 17:34:05');
INSERT INTO `easy_thumbnails_source` VALUES ('2', '676509bd1d8bfde0e77f6f1049253382', 'business/qrcode/fyk9qdwving1nmgc8bwdyglyufize4oov7xjfrvlyvreodorotmwcgs43zon.jpg', '2016-08-11 17:34:05');
INSERT INTO `easy_thumbnails_source` VALUES ('3', '676509bd1d8bfde0e77f6f1049253382', 'business/license/qi9mrcpedq287sy1yxq1zllyezg2u0y13yujzeo3zbpwovrsbxwrr3u2gsl7.jpg', '2016-08-11 17:34:05');
INSERT INTO `easy_thumbnails_source` VALUES ('4', '676509bd1d8bfde0e77f6f1049253382', 'business/license/qqyaovfg0yi9ikx7ngp2unrgipxq2gqagg90fapxht4pxvgrgpyhxf9mbedt.jpg', '2016-08-11 17:34:05');
INSERT INTO `easy_thumbnails_source` VALUES ('5', '676509bd1d8bfde0e77f6f1049253382', 'idCard/image/nxrjh53qk12uvvrgiacbvjou842v5qdehizbk1rx1v9ueklqddxlcrzbmtzu.jpg', '2016-08-11 17:34:05');
INSERT INTO `easy_thumbnails_source` VALUES ('6', '676509bd1d8bfde0e77f6f1049253382', 'idCard/image/zf5z3yhswlylsasooykslje5a9hpsydoobj8wk2edv4fzsdckgxcynekjhdn.jpg', '2016-08-11 17:34:05');
INSERT INTO `easy_thumbnails_source` VALUES ('7', '676509bd1d8bfde0e77f6f1049253382', 'business/logo/aiptaik2hcp0mnoloxassmbtflsh96e8mbowtllysamzbdny2jb3fdtqjtvo.jpg', '2016-08-16 10:26:46');
INSERT INTO `easy_thumbnails_source` VALUES ('8', '676509bd1d8bfde0e77f6f1049253382', 'business/qrcode/xcihebral8qoksobm23th1risevl3y3ar7fro5zlpcjbg25tzbd1sliesfwi.png', '2016-08-16 10:26:46');
INSERT INTO `easy_thumbnails_source` VALUES ('9', '676509bd1d8bfde0e77f6f1049253382', 'business/license/si5zj9j1phbqqisa04tk7lo7uypjkrnlpai4jw6yhrltxi3xezc9uej9nlov.jpg', '2016-08-16 10:26:46');
INSERT INTO `easy_thumbnails_source` VALUES ('10', '676509bd1d8bfde0e77f6f1049253382', 'business/license/afuyopngvrpk6dzjy0hzrlcvpsoox3obnjpinkxt4axyswewyxyspb0hsapq.jpg', '2016-08-16 10:26:46');
INSERT INTO `easy_thumbnails_source` VALUES ('11', '676509bd1d8bfde0e77f6f1049253382', 'idCard/image/tnzmlrpuno4izsegcnybxybt19hz1bu4i4dzxs4rsbfksnkibr140egfvq2n.png', '2016-08-16 10:26:46');
INSERT INTO `easy_thumbnails_source` VALUES ('12', '676509bd1d8bfde0e77f6f1049253382', 'idCard/image/xassyogyi8lm4xloknwj2ckzbj7fofjyexy5f9zqpkhbks9390o0yh8moa4w.jpg', '2016-08-16 10:26:46');
INSERT INTO `easy_thumbnails_source` VALUES ('13', '676509bd1d8bfde0e77f6f1049253382', 'business/logo/dla8nbzypnylvvdl5qrjmmbt4t7czyijtomgcrbhdmds7re3edyregxrnzgk.jpg', '2016-08-16 14:18:04');
INSERT INTO `easy_thumbnails_source` VALUES ('14', '676509bd1d8bfde0e77f6f1049253382', 'business/qrcode/tn7oqzzhda2opgrf93uhjiu53gblh1nley4zzpfa0xup52yb97kxyzmgjlou.jpg', '2016-08-16 14:18:04');
INSERT INTO `easy_thumbnails_source` VALUES ('15', '676509bd1d8bfde0e77f6f1049253382', 'business/license/e3ma9x7kclyfsqj3v81hwoi7kuh4ngasfubvx9lchtla1uo7b8gix36ecfus.jpg', '2016-08-16 14:18:04');
INSERT INTO `easy_thumbnails_source` VALUES ('16', '676509bd1d8bfde0e77f6f1049253382', 'business/license/tvvnmpjdjf1fheh7nifequnxdnikg43esgs59erua04zpjgmyaooxeje3vgy.jpg', '2016-08-16 14:18:04');
INSERT INTO `easy_thumbnails_source` VALUES ('17', '676509bd1d8bfde0e77f6f1049253382', 'idCard/image/temv91naewpzos2rptj3imp6uailxtmdwtplfeghatzgec5dozc43g7motvs.jpg', '2016-08-16 14:18:04');
INSERT INTO `easy_thumbnails_source` VALUES ('18', '676509bd1d8bfde0e77f6f1049253382', 'idCard/image/p8fsypiwrtnp4e0yz1jzl1xnbkkiavlboxmnplnurflnfa1kal6plgn80jhv.jpg', '2016-08-16 14:18:04');
INSERT INTO `easy_thumbnails_source` VALUES ('19', '676509bd1d8bfde0e77f6f1049253382', 'business/logo/o4l9z63isq8zszf3ycvsuypjig6ofuv1qcbu6rl6wtqctat9wglpdjtspyl8.jpg', '2016-08-16 16:44:43');
INSERT INTO `easy_thumbnails_source` VALUES ('20', '676509bd1d8bfde0e77f6f1049253382', 'business/qrcode/entcwcypg5bue0ungceflhbbfj4zzlmatq3muokudn3ztnzmzpjxvdjixcm7.jpg', '2016-08-16 16:44:43');
INSERT INTO `easy_thumbnails_source` VALUES ('21', '676509bd1d8bfde0e77f6f1049253382', 'business/license/wsmfe8nllar9yj355yn6oydq3msautlh204qcks3ved01j8ihq8swoa7xqfc.jpg', '2016-08-16 16:44:43');
INSERT INTO `easy_thumbnails_source` VALUES ('22', '676509bd1d8bfde0e77f6f1049253382', 'business/license/a3wn7thcbvohtivjnjfd2oxj5sjsiu6k5lpgqvmfo0uezqizxbjhe0isnwyr.jpg', '2016-08-16 16:44:43');
INSERT INTO `easy_thumbnails_source` VALUES ('23', '676509bd1d8bfde0e77f6f1049253382', 'idCard/image/a5rwwjldvplrdu5r2h4c07hadfxa3mdvprju4etwq8wzqgoqopbhp8d2f9m5.jpg', '2016-08-16 16:44:43');
INSERT INTO `easy_thumbnails_source` VALUES ('24', '676509bd1d8bfde0e77f6f1049253382', 'idCard/image/xnovzviesiix8wsmm1rpafipsaeq6rryy4w19linw76rl2j3z6zma2xwvocz.jpg', '2016-08-16 16:44:43');

-- ----------------------------
-- Table structure for easy_thumbnails_thumbnail
-- ----------------------------
DROP TABLE IF EXISTS `easy_thumbnails_thumbnail`;
CREATE TABLE `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  `source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_thumbnail_storage_hash_7ef9fce_uniq` (`storage_hash`,`name`,`source_id`),
  KEY `easy_thumbnails__source_id_7106e1b7_fk_easy_thumbnails_source_id` (`source_id`),
  KEY `easy_thumbnails_thumbnail_b454e115` (`storage_hash`),
  KEY `easy_thumbnails_thumbnail_b068931c` (`name`),
  CONSTRAINT `easy_thumbnails__source_id_7106e1b7_fk_easy_thumbnails_source_id` FOREIGN KEY (`source_id`) REFERENCES `easy_thumbnails_source` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of easy_thumbnails_thumbnail
-- ----------------------------
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('1', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/logo\\omprufp5ste5ur07fnc3c1vqdtjqvvjvr9tixrdpeceup9brzg8wd46kq9rz.jpg.200x200_q85_crop.jpg', '2016-08-11 17:34:05', '1');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('2', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/qrcode\\fyk9qdwving1nmgc8bwdyglyufize4oov7xjfrvlyvreodorotmwcgs43zon.jpg.200x200_q85_crop.jpg', '2016-08-11 17:34:05', '2');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('3', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/license\\qi9mrcpedq287sy1yxq1zllyezg2u0y13yujzeo3zbpwovrsbxwrr3u2gsl7.jpg.200x200_q85_crop.jpg', '2016-08-11 17:34:05', '3');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('4', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/license\\qqyaovfg0yi9ikx7ngp2unrgipxq2gqagg90fapxht4pxvgrgpyhxf9mbedt.jpg.200x200_q85_crop.jpg', '2016-08-11 17:34:05', '4');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('5', 'd26becbf46ac48eda79c7a39a13a02dd', 'idCard/image\\nxrjh53qk12uvvrgiacbvjou842v5qdehizbk1rx1v9ueklqddxlcrzbmtzu.jpg.200x200_q85_crop.jpg', '2016-08-11 17:34:05', '5');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('6', 'd26becbf46ac48eda79c7a39a13a02dd', 'idCard/image\\zf5z3yhswlylsasooykslje5a9hpsydoobj8wk2edv4fzsdckgxcynekjhdn.jpg.200x200_q85_crop.jpg', '2016-08-11 17:34:05', '6');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('7', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/logo\\aiptaik2hcp0mnoloxassmbtflsh96e8mbowtllysamzbdny2jb3fdtqjtvo.jpg.200x200_q85_crop.jpg', '2016-08-16 10:26:46', '7');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('8', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/qrcode\\xcihebral8qoksobm23th1risevl3y3ar7fro5zlpcjbg25tzbd1sliesfwi.png.200x200_q85_crop.jpg', '2016-08-16 10:26:46', '8');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('9', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/license\\si5zj9j1phbqqisa04tk7lo7uypjkrnlpai4jw6yhrltxi3xezc9uej9nlov.jpg.200x200_q85_crop.jpg', '2016-08-16 10:26:46', '9');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('10', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/license\\afuyopngvrpk6dzjy0hzrlcvpsoox3obnjpinkxt4axyswewyxyspb0hsapq.jpg.200x200_q85_crop.jpg', '2016-08-16 10:26:46', '10');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('11', 'd26becbf46ac48eda79c7a39a13a02dd', 'idCard/image\\tnzmlrpuno4izsegcnybxybt19hz1bu4i4dzxs4rsbfksnkibr140egfvq2n.png.200x200_q85_crop.jpg', '2016-08-16 10:26:46', '11');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('12', 'd26becbf46ac48eda79c7a39a13a02dd', 'idCard/image\\xassyogyi8lm4xloknwj2ckzbj7fofjyexy5f9zqpkhbks9390o0yh8moa4w.jpg.200x200_q85_crop.jpg', '2016-08-16 10:26:46', '12');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('13', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/logo\\dla8nbzypnylvvdl5qrjmmbt4t7czyijtomgcrbhdmds7re3edyregxrnzgk.jpg.200x200_q85_crop.jpg', '2016-08-16 14:18:04', '13');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('14', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/qrcode\\tn7oqzzhda2opgrf93uhjiu53gblh1nley4zzpfa0xup52yb97kxyzmgjlou.jpg.200x200_q85_crop.jpg', '2016-08-16 14:18:04', '14');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('15', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/license\\e3ma9x7kclyfsqj3v81hwoi7kuh4ngasfubvx9lchtla1uo7b8gix36ecfus.jpg.200x200_q85_crop.jpg', '2016-08-16 14:18:04', '15');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('16', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/license\\tvvnmpjdjf1fheh7nifequnxdnikg43esgs59erua04zpjgmyaooxeje3vgy.jpg.200x200_q85_crop.jpg', '2016-08-16 14:18:04', '16');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('17', 'd26becbf46ac48eda79c7a39a13a02dd', 'idCard/image\\temv91naewpzos2rptj3imp6uailxtmdwtplfeghatzgec5dozc43g7motvs.jpg.200x200_q85_crop.jpg', '2016-08-16 14:18:04', '17');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('18', 'd26becbf46ac48eda79c7a39a13a02dd', 'idCard/image\\p8fsypiwrtnp4e0yz1jzl1xnbkkiavlboxmnplnurflnfa1kal6plgn80jhv.jpg.200x200_q85_crop.jpg', '2016-08-16 14:18:04', '18');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('19', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/logo\\o4l9z63isq8zszf3ycvsuypjig6ofuv1qcbu6rl6wtqctat9wglpdjtspyl8.jpg.200x200_q85_crop.jpg', '2016-08-16 16:44:43', '19');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('20', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/qrcode\\entcwcypg5bue0ungceflhbbfj4zzlmatq3muokudn3ztnzmzpjxvdjixcm7.jpg.200x200_q85_crop.jpg', '2016-08-16 16:44:43', '20');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('21', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/license\\wsmfe8nllar9yj355yn6oydq3msautlh204qcks3ved01j8ihq8swoa7xqfc.jpg.200x200_q85_crop.jpg', '2016-08-16 16:44:43', '21');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('22', 'd26becbf46ac48eda79c7a39a13a02dd', 'business/license\\a3wn7thcbvohtivjnjfd2oxj5sjsiu6k5lpgqvmfo0uezqizxbjhe0isnwyr.jpg.200x200_q85_crop.jpg', '2016-08-16 16:44:43', '22');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('23', 'd26becbf46ac48eda79c7a39a13a02dd', 'idCard/image\\a5rwwjldvplrdu5r2h4c07hadfxa3mdvprju4etwq8wzqgoqopbhp8d2f9m5.jpg.200x200_q85_crop.jpg', '2016-08-16 16:44:43', '23');
INSERT INTO `easy_thumbnails_thumbnail` VALUES ('24', 'd26becbf46ac48eda79c7a39a13a02dd', 'idCard/image\\xnovzviesiix8wsmm1rpafipsaeq6rryy4w19linw76rl2j3z6zma2xwvocz.jpg.200x200_q85_crop.jpg', '2016-08-16 16:44:43', '24');

-- ----------------------------
-- Table structure for easy_thumbnails_thumbnaildimensions
-- ----------------------------
DROP TABLE IF EXISTS `easy_thumbnails_thumbnaildimensions`;
CREATE TABLE `easy_thumbnails_thumbnaildimensions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thumbnail_id` int(11) NOT NULL,
  `width` int(10) unsigned DEFAULT NULL,
  `height` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `thumbnail_id` (`thumbnail_id`),
  CONSTRAINT `easy_thumb_thumbnail_id_314c3e84_fk_easy_thumbnails_thumbnail_id` FOREIGN KEY (`thumbnail_id`) REFERENCES `easy_thumbnails_thumbnail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of easy_thumbnails_thumbnaildimensions
-- ----------------------------

-- ----------------------------
-- Table structure for erp_agent
-- ----------------------------
DROP TABLE IF EXISTS `erp_agent`;
CREATE TABLE `erp_agent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sex` varchar(2) NOT NULL,
  `address` varchar(30) NOT NULL,
  `register_date` date DEFAULT NULL,
  `note` longtext,
  `user_id` int(11) DEFAULT NULL,
  `business_id` int(11) DEFAULT NULL,
  `name` varchar(30) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entry_person` varchar(20) NOT NULL,
  `agent_num` int(10) unsigned DEFAULT NULL,
  `idCard_num` varchar(30) DEFAULT NULL,
  `phoneNum` varchar(18) NOT NULL,
  `email` varchar(30) NOT NULL,
  `bank_account` varchar(30) DEFAULT NULL,
  `graduated_school` varchar(30) DEFAULT NULL,
  `graduated_time` date DEFAULT NULL,
  `job_type` varchar(2) DEFAULT NULL,
  `major` varchar(20) DEFAULT NULL,
  `salary_num` varchar(30) DEFAULT NULL,
  `position_id` int(11) DEFAULT NULL,
  `qrcode` varchar(100) DEFAULT NULL,
  `wechat` varchar(20) DEFAULT NULL,
  `qq_number` int(10) unsigned DEFAULT NULL,
  `first_pinyin` varchar(30) DEFAULT NULL,
  `pinyin` varchar(30) DEFAULT NULL,
  `device_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `erp_agent_2f4e4ac4` (`business_id`),
  KEY `erp_agent_bce5bd07` (`position_id`),
  CONSTRAINT `erp_agent_business_id_2fa7e7c4_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `erp_agent_user_id_33d5d4a7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_agent
-- ----------------------------
INSERT INTO `erp_agent` VALUES ('4', '2', '规定发光飞碟', '2016-03-10', '范甘迪发鬼地方i', '21', '4', 'ssss', 'agent/avatar/WzU5LCA1MjIsIDcxNiwgMTUwLCAxOTQsIDkwMSwgOTM2LCA3NjksIDg5NCwgMjY2XRYyMA8=.jpg', '1', '上海凡达', '1', '654002196904273824', '15825699658', '18701730286@163.com', '', '', null, null, '', '', '1', '', 'fdsf54245454', '1663830928', 'ssss', 'ssss', '');
INSERT INTO `erp_agent` VALUES ('5', '2', '发生范德萨', '2016-03-10', '发的规范的身份第三个', '22', '4', '王二小', 'agent/avatar/zqyuwfyrwwp7m1hlupftvrtft5otu9khdjlubg740c2zrtviya2tuulri2dy.jpg', '0', '律錳管理', '2', '342625199102082395', '18701752689', '1668380928@qq.com', '', '', null, null, '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('6', '1', '佛挡杀佛', '2016-03-14', '范德萨发斯蒂芬', '26', '7', '王麻子', 'agent/avatar/jo6gfd5hvanpdhiradqmlyi1t5cxdfr8ce4ilnt1p0vagyckjg3awcz0vfn4.jpg', '1', '上海你猜', '3', '342625199102082395', '18701730286', '18701730286@qq.com', '', '', null, null, '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('7', '1', '范德萨发生的', '2016-03-14', '给梵蒂冈梵蒂冈浮动', '29', '5', '赵四', 'agent/avatar/l75ojmirg12gdt566sckns5ynetr8bguxdhii6ztodviswhctv4rni1wjxiw.jpg', '1', '浙江华硕', '4', '342625199102082395', '18701730288', '3', null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('8', '1', '上海陆家嘴', '2016-04-22', '法第三方第三方第三方点睡', '34', '4', '小明', 'agent/avatar/zdkn1at0qgglebwg8kxrhmjjjujcjv2bwffp7a4dnnicvzzjurk8kny1cv8v.jpg', '0', '张三', '5', '342625199102082395', '18701766335', '1668380928@qq.com', '中国银行', '交大', '2016-04-23', '2', '金融管理', '125684586854', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('9', '1', '上海沪南路', '2016-04-22', '范德萨范德萨发的', '35', '4', '大话', '', '0', '张三', '6', '342625199102082395', '18701755896', '1668680928@qq.com', '招商银行', '电大', '2016-04-13', '2', '会计', '1254579564587', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('10', '1', '上海沪南路', '2016-04-22', '', '36', '4', '李大华', 'agent/avatar/Wzk1MywgNzU2LCAzMTAsIDk2NywgNzI5LCA5NTEsIDg2NywgODYyLCA1NzcsIDQ4NV0SMTgD.jpg', '0', '张三', '7', '342625199102082395', '18701755899', '166868022@qq.com', '招商银行', '电大', '2016-04-13', '2', '会计', '1254579564587', '1', '', '', null, 'ldh', 'lidahua', '');
INSERT INTO `erp_agent` VALUES ('11', '1', '上海沪南路', '2016-04-22', '范德萨范德萨发的发生的房顶上传销自残', '37', '4', '二华', 'agent/avatar/WzEwMCwgOTA5LCA0NiwgNTU4LCAzNDYsIDkwLCAxNTQsIDk2MCwgODQxLCAyMjddERcF.jpg', '0', '张三', '8', '342625199102082395', '18701755833', '1668680928@qq.com', '招商银行', '电大', '2016-04-13', '2', '会计', '1254579564587', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('12', '2', '上海沪南路', '2016-04-22', '', '38', '4', '三花', '', '0', '张三', '9', '342625199102082395', '18701755852', '1668380928@qq.com', '招商银行', '电大', '2016-04-13', '2', '会计', '1254579564587', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('13', '1', '上海沪南路', '2016-04-22', '', '39', '4', '四花', 'agent/avatar/jkwstl2jct0nz4rho5boqoxrumns55fnhpjhrrpkx8asdmusefjdvvbgnyxc.jpg', '0', '张三', '10', '342625199102082395', '18701755520', '1668380928@qq.com', '招商银行', '电大', '2016-04-13', '2', '会计', '1254579564587', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('14', '1', '发的发生的', '2016-04-22', '范德萨范德萨范德萨', '40', '4', '张思', 'agent/avatar/WzY3MCwgNTcxLCAzNTksIDIyNCwgMzgzLCAyNiwgOTkyLCAxNTgsIDYyNCwgMTQxXQsxMA4=.jpg', '1', '张三', '11', '342625199102082395', '15899658659', '1668380928@qq.com', '', '', null, '1', '', '45656532323', '1', '', '', null, 'zs', 'zhangsi', '22222');
INSERT INTO `erp_agent` VALUES ('15', '1', '发的发生的', '2016-04-22', '范德萨范德萨范德萨', '41', '4', '张思思', 'agent/avatar/qpexkpuiy9vb71y8yo3cpfpxdkemtwybvnnkjc6jjiv5r5jky7mlc5qdvopa.jpg', '0', '张三', '12', '342625199102082395', '18701730333', '1668380928@qq.com', '', '', null, '1', '', '45656532323', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('16', '1', '和规范化股份', '2016-04-22', '', '43', '4', '计划', 'agent/avatar/snycmyrdn5o9honi1tiixhjqgubobapkxzhogtji6g3jcy4bbpbzkhmlljfq.jpg', '0', '张三', '13', '342625199102082395', '18701755652', '18701730286@163.com', '', '', null, '1', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('17', '1', '发的范德萨', '2016-04-22', '范德萨范德萨', '44', '4', '几乎', 'agent/avatar/kfhteqciccvrcvyditltym4cpdxxw7eej0b1lyrk5audtqqelepktubibg4p.jpg', '0', '张三', '14', '342625199102082395', '18745865895', '18701730286@163.com', '', '', null, '2', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('18', '1', '发的发生的房顶上', '2016-04-22', '发生的范德萨范德萨', '46', '4', '更多的', 'agent/avatar/ar9qvweqtntfjfy2f9jjdsp0k0q9uwx28pfvyorty81xqxmwx3u3hez2b9qd.jpg', '0', '王二小', '15', '342625199102082395', '18701755555', '1668380928@qq.com', '', '', null, '2', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('19', '2', '大方的说法', '2016-04-26', '', '49', '4', '王菊', '', '0', '张三', '15', '342625199102082395', '13833558456', '1668380928@qq.com', '', '', null, '2', '', '', '1', '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('20', '1', 'fgfgfd ', '2016-04-27', '', '50', '4', '呵呵', 'agent/avatar/o72h75mxofknakguuyx6up3mcxtxmipfrfs5nzxmnxr42tkqmpbq78fac0go.jpg', '0', '上海凡达', '16', '342625199102082395', '18722566996', '18701730286@163.com', '', '', null, '2', '', '', '3', '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('21', '1', '的萨达', '2016-04-27', '', '51', '6', '回家', 'agent/avatar/hma5wpzztvjkirrxq2xtuiiqtvam0kf0cuhmuryyyt3e6v81ms8d1kbopq3p.jpg', '0', '温州忽悠', null, '342625199102082395', '13438385598', '1668380928@qq.com', '', '', null, '2', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('22', '1', '好几个', '2016-04-27', '', '52', '6', '回家', 'agent/avatar/lylce24ydvnzqt0aqlpy9xesldoq40hdtbrl3vseznev1qraqccxuosk4s59.jpg', '1', '温州忽悠', '1', '342625199102082395', '13838385569', '1668380928@qq.com', '', '', null, '2', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('23', '1', '发个梵蒂冈', '2016-04-27', '', '53', '6', '地方', 'agent/avatar/2oggajcc0tax4iq3c1hj1mgyjbpi4j9jt3ghpx9wf1xkt3swfytobm56ok6f.jpg', '1', '温州忽悠', '2', '342625199102082395', '15877885526', '1668380928@qq.com', '', '', null, '2', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('24', '1', 'fdsf ', '2016-04-27', '', '54', '6', '高的', 'agent/avatar/8gior6ngr1ku5tp4xpqesq2t4gyztvighnphog8ldpwntjxjk2azssuigsll.jpg', '1', '温州忽悠', '3', '342625199102082395', '18701766552', '18701730286@163.com', '', '', null, '2', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('25', '1', '给梵蒂冈梵蒂冈', '2016-04-27', '', '55', '6', '发个', 'agent/avatar/sbigkf5f4evtm1o0eeo6gmd5cbkxffeg1a0iidpsalyixoxm5a7zzjq1wxa2.jpg', '1', '温州忽悠', '4', '342625199102082395', '18707855256', '1668380928@qq.com', '', '', null, '2', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('26', '1', '高的', '2016-04-27', '', '56', '6', '链接', 'agent/avatar/rebmrza19k2itdly0fhhpfaieg9aaoit2ztztxcktslcjcknkdl36v2c1fta.jpg', '1', '温州忽悠', '5', '342625199102082395', '13838385548', '1668380928@qq.com', '', '', null, '2', '', '', null, '', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('27', '1', '佛挡杀佛', '2016-04-27', '', '57', '6', '丰东股份', 'agent/avatar/uev2mbcyttsadyclll2uy6iftzfn3yb1hhb1gh5flfqftvf5hs60v33ponco.jpg', '1', '温州忽悠', '6', '342625199102082395', '13434345586', '1668380928@qq.com', '', '', null, '2', '', '', null, 'agent/qrcode/B003None.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('28', '1', '发的发生的', '2016-04-27', '', '58', '5', '申达', 'agent/avatar/ufnkvauypkq2avj3mnbkigytpswpd9ikbdq2xsnv8el8x6cfllbhwaejrave.jpg', '1', '浙江华硕', '5', '342625199102082395', '18711458856', '1668380928@qq.com', '', '', null, '2', '', '', null, 'agent/qrcode/B0025.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('29', '2', '反对党生', '2016-04-28', '', '59', '4', '几句话', 'agent/avatar/c0vb9piyrv8fykkpuj0ei4l307wqk2pt6fy48ef2lffcprayx8oczenqqv23.jpg', '0', '上海凡达', '17', '342625199102082395', '18701788556', '1305251473@qq.com', '', '', null, '2', '', '', '1', 'agent/qrcode/B00117.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('30', '1', '重庆市渝北区', '2016-04-29', '的给梵蒂冈梵蒂冈', '61', '4', '李捷超', 'agent/avatar/vkow5s9bhamk2hik0avl88jij7qdenwhcyfbkrwcejyxnhoteke5ebpfogyq.jpg', '0', '张三', '18', '342625199102082395', '18755220123', '836518185@qq.com', '', '', null, '2', '', '', '1', 'agent/qrcode/B00118.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('31', '1', '的范德萨范德萨', '2016-04-29', '', '62', '4', '佘小龙', 'agent/avatar/8ljlwy2jdtzhdjiwz2vp5tmirhsarjfcrrjipotuuoinpd5ufbg0jhdnvjt3.jpg', '0', '张三', '19', '342625199102082395', '15866589652', '1668380928@qq.com', '', '', null, '2', '', '', '6', 'agent/qrcode/B00119.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('32', '1', '浙江省金华市武义县', '2016-05-09', '发大水发大水发', '63', '4', '恢复', 'agent/avatar/WzQzOSwgNTIzLCA0MTcsIDgxMCwgNTMxLCAyOTQsIDIwLCA1ODUsIDk2MCwgMzU3XRUABw==.jpg', '0', '上海凡达', '20', '342625199102082395', '13520404514', '1668380524@qq.com', '', '', null, '2', '', '', '3', 'agent/qrcode/B00120.png', null, null, 'hf', 'huifu', null);
INSERT INTO `erp_agent` VALUES ('33', '1', '河南省南阳市新野县', '2016-05-09', '', '64', '4', '但是', 'agent/avatar/WzM3LCAxMSwgMTU4LCAyODEsIDY1OSwgNjY4LCA3MDMsIDU2MSwgMjA1LCA5Nl0VDgo=.jpg', '0', '上海凡达', '21', '342625199102082395', '18755425568', '123123@qq.com', '', '', null, '2', '', '', '3', 'agent/qrcode/B00121.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('34', '1', '河北省秦皇岛市昌黎镇', '2016-05-12', '', '65', '4', '打算', 'agent/avatar/Wzg5OCwgMTMwLCAwLCA0NDUsIDQ1NSwgMzEwLCAyNjIsIDkzNCwgNjMyLCA4OF0FMTYQ.jpg', '0', '上海凡达', '22', '342625199102082395', '18701755632', '123@qq.com', '', '', null, '2', '', '', '3', 'agent/qrcode/B00122.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('35', '1', '重庆市巴南区', '2016-05-12', '', '66', '4', '第三方', 'agent/avatar/WzEyMCwgMzc3LCAxNzcsIDE0OCwgMjE2LCA1NzIsIDk2MCwgOTE3LCA4NjksIDUwOF0ZMTIX.jpg', '1', '上海凡达', '23', '342625199102082395', '18701455865', '666@qq.com', '', '', null, '2', '', '', '1', 'agent/qrcode/B00123.png', '', null, 'dsf', 'disanfang', '');
INSERT INTO `erp_agent` VALUES ('36', '1', '辽宁省辽阳市灯塔市', '2016-05-12', 'cscsacasc ', '67', '4', '方法第三方', 'agent/avatar/WzIwNCwgNTE2LCA0ODUsIDUwMCwgMzUwLCA1NTIsIDYzNSwgOTgxLCA4OTYsIDg4MV0OMjIM.jpg', '0', '上海凡达', '24', '342625199102082395', '18742522012', '888@qq.com', '', '', null, '2', '', '', '3', 'agent/qrcode/B00124.png', null, null, 'ffdsf', 'fangfadisanfang', null);
INSERT INTO `erp_agent` VALUES ('37', '1', '安徽省芜湖市南陵县', '2016-05-23', '', '69', '4', '任静', 'agent/avatar/WzU5NiwgNTgwLCA0MzQsIDcyNywgNzE0LCA0MDgsIDUyMSwgODIwLCAxNzQsIDMxN10DMTUV.jpg', '0', '上海凡达', '25', '342625199102082395', '13833558658', '1668380928@qq.com', '', '', null, '2', '', '', '1', 'agent/qrcode/B00125.png', '', null, 'rj', 'renjing', null);
INSERT INTO `erp_agent` VALUES ('38', '1', '湖北省荆州市郝穴镇', '2016-05-23', '', '70', '4', '火锅', 'agent/avatar/WzU0MCwgNDA1LCA2NjUsIDg0MywgODcyLCAzMzcsIDQ4MSwgMjMyLCAxOTgsIDU5N10KMTUZ.jpg', '0', '上海凡达', '26', '342625199102082395', '13855669568', '2860967941@qq.com', '', '', null, '2', '', '', '3', 'agent/qrcode/B00126.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('39', '1', '山东省莱芜市钢城区', '2016-05-24', '', '71', '4', '季虎刚', 'agent/avatar/WzgsIDI1NSwgODEsIDc5NiwgNDM5LCAxMjUsIDM2NSwgMzAwLCA2MzksIDUyMl0GMhE=.jpg', '0', '上海凡达', '27', '342625199102082395', '18744520023', '1668380928@qq.com', '', '', null, '2', '', '', '6', 'agent/qrcode/B00127.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('40', '1', '河南省信阳市罗山县', '2016-05-24', '', '72', '4', '举个', 'agent/avatar/Wzc1OSwgNjMwLCAzNiwgODIzLCAyNjQsIDI2LCAyMzYsIDY3OSwgMTA0LCAxMTddGDI1Bw==.jpg', '0', '上海凡达', '28', '342625199102082395', '13866556325', '1668380928@qq.com', '', '', null, '2', '', '', '1', 'agent/qrcode/B00128.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('41', '1', '河南省周口市沈丘县', '2016-05-24', '', '73', '4', '高的', 'agent/avatar/WzkxMSwgNzExLCA1OTgsIDE2MCwgNDQzLCAyMDcsIDU0NywgNzc0LCAxMTQsIDIxNV0QNBM=.jpg', '0', '上海凡达', '29', '342625199102082395', '18701720112', '1668380928@qq.com', '', '', null, '2', '', '', '1', 'agent/qrcode/B00129.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('42', '1', '安徽省淮南市潘集区', '2016-06-01', '', '74', '7', '个多月', 'agent/avatar/WzYzMywgNDc2LCA2MzIsIDIyMSwgNDYxLCA0NjMsIDUyMywgNTAyLCA2NDcsIDM3Nl0UMjMR.jpg', '0', '上海你猜', '4', '342625199102082395', '18701730286', '1668380928@qq.com', '', '', null, '2', '', '', null, 'agent/qrcode/B8884.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('43', '1', '湖北省襄樊市襄阳区', '2016-06-01', '', '75', '7', '几个点', 'agent/avatar/WzMwLCA2MjYsIDQwMSwgODU5LCA2NzgsIDgyOCwgMjA4LCA1ODUsIDk3NCwgNDc5XQA1BA==.jpg', '1', '上海你猜', '5', '342625199102082395', '18701730286', '1668380928@qq.com', '', '', null, '2', '', '', null, 'agent/qrcode/B8885.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('44', '1', '黑龙江省伊春市新青区', '2016-06-01', '', '76', '7', '改成才', 'agent/avatar/WzU1MSwgMjIwLCAzMDMsIDU5OSwgOTI5LCA1NTksIDI5MCwgODk5LCA1NDMsIDM2MF0WMjQO.jpg', '1', '上海你猜', '6', '342625199102082395', '18701730286', '1668380928@qq.com', '', '', null, '2', '', '', null, 'agent/qrcode/B8886.png', null, null, null, null, null);
INSERT INTO `erp_agent` VALUES ('45', '1', '江西省宜春市双溪镇', '2016-06-12', '', '77', '4', '111', 'agent/avatar/WzQ0NCwgMTUyLCAxNTAsIDM5MiwgMTY5LCAxOSwgNTY0LCA5OTIsIDczNiwgOTIzXQA0EA==.jpg', '0', '上海凡达', '30', '342625199102082395', '18701730286', '1668380928@qq.com', '', '', null, '2', '', '', '1', 'agent/qrcode/B00130.png', '', null, '111', '111', '');
INSERT INTO `erp_agent` VALUES ('46', '1', '重庆市江北区', '2016-06-24', '', null, '4', 'qqq', 'agent/avatar/WzkzMSwgMTA4LCA3OTQsIDcyMywgMjY5LCA0OTEsIDI2NSwgMTAsIDc2MywgMzg4XRYxNxU=.jpg', '0', '张三', '31', '342625199102082395', '18701730286', '55555@qq.com', '', '', null, '2', '', '', '3', 'agent/qrcode/B00131.png', '1111', '1111', 'qqq', 'qqq', null);
INSERT INTO `erp_agent` VALUES ('47', '1', '重庆市江北区', '2016-06-24', '', '78', '4', 'qqq', '', '0', '张三', '32', '342625199102082395', '18701730286', '55555@qq.com', '', '', null, '2', '', '', '3', 'agent/qrcode/B00132.png', '1111', '1111', 'qqq', 'qqq', null);
INSERT INTO `erp_agent` VALUES ('49', '1', '山西省忻州市五寨县', '2016-08-03', '', '93', '4', '11', '', '0', '张三', '34', '342625199102082395', '18701730256', '16683809282@qq.com', '', '', null, '2', '', '', '3', 'agent/qrcode/B00134.png', '', null, '11', '11', null);

-- ----------------------------
-- Table structure for erp_agent_permissions
-- ----------------------------
DROP TABLE IF EXISTS `erp_agent_permissions`;
CREATE TABLE `erp_agent_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agent_id` (`agent_id`,`permission_id`),
  KEY `erp_agent_permissio_permission_id_30bb7e1c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `erp_agent_permissions_agent_id_24806e8b_fk_erp_agent_id` FOREIGN KEY (`agent_id`) REFERENCES `erp_agent` (`id`),
  CONSTRAINT `erp_agent_permissio_permission_id_30bb7e1c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1781 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_agent_permissions
-- ----------------------------
INSERT INTO `erp_agent_permissions` VALUES ('1775', '4', '218');
INSERT INTO `erp_agent_permissions` VALUES ('1776', '4', '220');
INSERT INTO `erp_agent_permissions` VALUES ('1777', '4', '221');
INSERT INTO `erp_agent_permissions` VALUES ('1778', '4', '222');
INSERT INTO `erp_agent_permissions` VALUES ('1779', '4', '223');
INSERT INTO `erp_agent_permissions` VALUES ('1772', '4', '224');
INSERT INTO `erp_agent_permissions` VALUES ('1773', '4', '225');
INSERT INTO `erp_agent_permissions` VALUES ('1774', '4', '226');
INSERT INTO `erp_agent_permissions` VALUES ('1680', '6', '218');
INSERT INTO `erp_agent_permissions` VALUES ('1681', '6', '219');
INSERT INTO `erp_agent_permissions` VALUES ('1682', '6', '220');
INSERT INTO `erp_agent_permissions` VALUES ('1683', '6', '221');
INSERT INTO `erp_agent_permissions` VALUES ('1684', '6', '222');
INSERT INTO `erp_agent_permissions` VALUES ('1685', '6', '223');
INSERT INTO `erp_agent_permissions` VALUES ('1677', '6', '224');
INSERT INTO `erp_agent_permissions` VALUES ('1678', '6', '225');
INSERT INTO `erp_agent_permissions` VALUES ('1679', '6', '226');
INSERT INTO `erp_agent_permissions` VALUES ('1780', '14', '224');
INSERT INTO `erp_agent_permissions` VALUES ('1751', '35', '218');
INSERT INTO `erp_agent_permissions` VALUES ('1752', '35', '220');
INSERT INTO `erp_agent_permissions` VALUES ('1753', '35', '221');
INSERT INTO `erp_agent_permissions` VALUES ('1754', '35', '222');
INSERT INTO `erp_agent_permissions` VALUES ('1755', '35', '223');
INSERT INTO `erp_agent_permissions` VALUES ('1748', '35', '224');
INSERT INTO `erp_agent_permissions` VALUES ('1749', '35', '225');
INSERT INTO `erp_agent_permissions` VALUES ('1750', '35', '226');
INSERT INTO `erp_agent_permissions` VALUES ('1729', '46', '218');
INSERT INTO `erp_agent_permissions` VALUES ('1730', '46', '219');
INSERT INTO `erp_agent_permissions` VALUES ('1731', '46', '222');
INSERT INTO `erp_agent_permissions` VALUES ('1732', '46', '223');
INSERT INTO `erp_agent_permissions` VALUES ('1728', '46', '224');
INSERT INTO `erp_agent_permissions` VALUES ('1734', '47', '218');
INSERT INTO `erp_agent_permissions` VALUES ('1735', '47', '219');
INSERT INTO `erp_agent_permissions` VALUES ('1736', '47', '222');
INSERT INTO `erp_agent_permissions` VALUES ('1737', '47', '223');
INSERT INTO `erp_agent_permissions` VALUES ('1733', '47', '224');

-- ----------------------------
-- Table structure for erp_announcement
-- ----------------------------
DROP TABLE IF EXISTS `erp_announcement`;
CREATE TABLE `erp_announcement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `picture` varchar(500) DEFAULT NULL,
  `title` varchar(30) NOT NULL,
  `order` int(10) unsigned NOT NULL,
  `date` date NOT NULL,
  `show_text` tinyint(1) NOT NULL,
  `text` longtext,
  `announce_business_id` int(11) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `read_num` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `erp_announcement_bbee8096` (`announce_business_id`),
  CONSTRAINT `erp_announcement_announce_business_id_37321c6_fk_erp_business_id` FOREIGN KEY (`announce_business_id`) REFERENCES `erp_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_announcement
-- ----------------------------
INSERT INTO `erp_announcement` VALUES ('1', 'business/pictures/fu4h0wsr7mqbmnd80migcwwga9xgnk7nspqzq20wy0dcphb9w9htdrhbaoc7.jpg', '第一张', '1', '2016-03-16', '1', '发大水发大水发您好地方和法规贵航股份第三方荣飞无法第三方', '4', '0', '2');
INSERT INTO `erp_announcement` VALUES ('2', 'business/pictures/m394cbnqlga5jbouzm5x5zdkfqr8jdetoa29gowruonp5wdotbdq7xdkxxod.jpg', '第三张', '3', '2016-03-16', '1', '我们的服务宗旨是 一切为了客户  一切为了客户  一切为了客户，重要的事情说三次', '4', '0', '0');
INSERT INTO `erp_announcement` VALUES ('3', 'business/pictures/yupxh6nhws4hmifkautoknb5lol3bfmjl7mbdje8ae2b3dsusqfv8uwmyvvk.jpeg', '第一张', '1', '2016-03-16', '1', '秉承诚信引领发展，细节成就完美，服务打造品牌，给您不一般的体验', '7', '1', '10');
INSERT INTO `erp_announcement` VALUES ('4', 'business/pictures/c1mmreih1cmm8sgpdjfswihp7po4puo5yxkgi1i7zccbfyhosjp59fywxh7o.jpeg', '第二张', '2', '2016-03-16', '1', '新起点，新机遇，新挑战，加入我们从现在开始，开启不一样的人生', '7', '1', '5');
INSERT INTO `erp_announcement` VALUES ('5', 'business/pictures/whwu6xfd8qdjrm85wp9dd3z2hyxpubk2xr34fk4t6dc00euj3zsearq17uhg.jpg', '第三张', '3', '2016-03-16', '1', '让我们为世界金融界秩序化发展贡献诚信的力量', '7', '1', '2');
INSERT INTO `erp_announcement` VALUES ('6', 'business/pictures/w8mukohcinqq88hlfjpq3boyokuuc5wjucarwqkdpxkby03xubzsrakauvuf.jpeg', '第四张', '4', '2016-03-16', '1', '我们的服务宗旨是 一切为了客户  一切为了客户  一切为了客户，重要的事情说三次', '7', '1', '1');
INSERT INTO `erp_announcement` VALUES ('7', 'business/pictures/pvpouqkfamasefnfzjkorax7tk2cn1z0vonsng9fbjnt2asuqifttpl98tlr.jpg', '第五张', '5', '2016-03-16', '1', '牛基队，非同一般的队伍，不一般的team ，我就是我，不一样的烟火', '7', '1', '1');
INSERT INTO `erp_announcement` VALUES ('8', 'business/pictures/Wzg4NSwgNDEwLCAyMzgsIDk0MCwgMjI0LCA1NzgsIDI5NSwgNzMxLCA1ODYsIDg4Nl0DMjIT.jpg', '第二张', '2', '2016-03-16', '1', '<p><span>&nbsp; 50多年来，中赞两国人民结下了深厚的友谊，从中赞两国的友好合作当中得到了实实在在的好处。但始终有一些别有用心的人直到今天依然想破坏这种友谊。今天有一份地方小报公然造谣说中国人用人肉制成罐头牛肉在非洲销售。这完全是毫无根据的恶意中伤，是别有用心的诬蔑，其丑恶目的就是破坏中国人的形象，破坏中赞友谊，破坏中非友谊，这是我们坚决不能接受的。我们在此对这样的行为表示极大愤慨和强烈谴责。中国使馆将向赞比亚有关部门提出严正交涉，要求坚决彻查涉事报纸及其消息来源，还中国人以清白，给中国人一个公道！</span></p>', '4', '1', '4');
INSERT INTO `erp_announcement` VALUES ('9', 'business/pictures/WzYxNzEyLCA4OTAxNiwgODM0NzAsIDM5NTg5LCA1OTc0OCwgNTQwOCwgMzI5MjAsIDYxOTk1LCA5NjY2NSwgMjc1ODldChAU.jpg', '第四张', '4', '2016-03-16', '1', '让我们为世界金融界秩序化发展贡献诚信的力量', '4', '1', '1');
INSERT INTO `erp_announcement` VALUES ('10', 'business/pictures/WzY3NywgNDIsIDQ4MSwgNzIzLCAzNjIsIDk4LCA2OSwgMTAwLCA2MTcsIDEwN10ZBg0=.jpg', '第五张', '5', '2016-03-16', '1', '新起点，新机遇，新挑战，加入我们从现在开始，开启不一样的人生', '4', '1', '2');
INSERT INTO `erp_announcement` VALUES ('11', 'business/pictures/vbzd9ovi9wqcvatlprkd7h8loqx3indti3yifxtavfzvoydk5v5kfbheziva.jpg', '第一张', '1', '2016-03-16', '1', '新起点，新机遇，新挑战，加入我们从现在开始，开启不一样的人生', '5', '1', '0');
INSERT INTO `erp_announcement` VALUES ('12', 'business/pictures/mrsxglwuc34wgwaihfoswjzucrhzel1tluykwduxl7bgdyqbai4kidwtdkr6.jpg', '第二张', '2', '2016-03-16', '1', '牛基队，非同一般的队伍，不一般的team ，我就是我，不一样的烟火', '5', '1', '0');
INSERT INTO `erp_announcement` VALUES ('13', 'business/pictures/3acdenxiiosmbyqrcs3eunuc5phahmzoqclqze0ytvfbnogesz7lbezj3knz.jpg', '第一张', '2', '2016-03-16', '1', '牛基队，非同一般的队伍，不一般的team ，我就是我，不一样的烟火', '6', '1', '0');
INSERT INTO `erp_announcement` VALUES ('14', 'business/pictures/WzI0MywgNjI5LCAzNzQsIDY1NSwgMSwgNjgzLCA2ODYsIDE0NCwgMTUzLCAzMjZdBwgU.jpg', '第二张', '6', '2016-04-07', '1', '地方生发的', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('15', 'business/pictures/WzMyMiwgNjc0LCAxOTAsIDE4MiwgNDY4LCA3MDksIDcxMSwgNDA3LCAxODUsIDU0Ml0TEAs=.jpg', '第5张', '5', '2016-04-07', '1', '给人个梵蒂冈', '4', '0', '2');
INSERT INTO `erp_announcement` VALUES ('16', 'business/pictures/WzQyNiwgOTc3LCA1NTMsIDE2MywgMTY3LCA4MDgsIDE0MCwgODMsIDg5MiwgOTk2XQg0Bw==.jpg', '到底', '1', '2016-04-21', '1', '<p><span>&nbsp; 张德江说，为山九仞非一日之功。香港特别行政区的成立还不到19年，&ldquo;一国两制&rdquo;实践没有任何先例可循，各方面的制度和体制机制尚需完善。一些深层次矛盾总要经过一段时间才会逐渐显现出来，这有其客观必然性。今天暴露的许多问题有些是多年累积而来的，有些是新出现的，解决起来也绝非朝夕之功。我们不能因此就对&ldquo;一国两制&rdquo;产生怀疑、动摇甚至否定。没有过不去的火焰山。我们有智慧有能力解决&ldquo;一国两制&rdquo;实践中的问题。</span></p>', '4', '1', '3');
INSERT INTO `erp_announcement` VALUES ('54', 'business/pictures/Wzc2NywgOTE4LCA2MjMsIDE3MCwgOTk5LCAzMjAsIDMwOCwgNzA3LCA1MzMsIDk1Nl0GOAI=.jpg', '二反倒是', '44', '2016-05-06', '1', '<p>据介绍，中铁装备在展览会上主要展示了自主研发的新产品模型：已应用于新加坡汤申线地铁项目的矩形盾构机、将应用于蒙华铁路白城隧道的马蹄形盾构机，以及应用于黎巴嫩大贝鲁特供水项目的世界最小直径（3.5米）的硬岩掘进机等。 　　与国际上常规的圆形盾构机不同，中铁装备的异形盾构机不仅是断面的&ldquo;变形&rdquo;，更是工法、技术的&ldquo;变形&rdquo;。它不仅可以在保证施工安全的前提下，在离地面仅3米的地下开山掘土，而且比圆形截面减少20%&mdash;30%的开挖面积，最大程度地提高空间利用率，同时通过底部找平，节省大量的工期和后期施工成本。</p>', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('55', 'business/pictures/WzYzNiwgMTU0LCA3NTUsIDI5MSwgNzMxLCAzMzksIDQ2MywgNjY4LCA4MDIsIDg3Ml0TMjMQ.jpg', '热热我', '23', '2016-05-06', '1', '<p>233都是非法的</p>', '4', '1', '1');
INSERT INTO `erp_announcement` VALUES ('56', 'business/pictures/WzQ0NywgMTYsIDgyNywgNTQyLCAyNzcsIDcyMywgMTc2LCA3NDAsIDYyNSwgN10SMTkB.jpg', '计划', '90', '2016-05-06', '1', '<p>规范和规范化</p>', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('57', 'business/pictures/WzIwMywgMzYxLCA4MjAsIDYyMiwgODg1LCAzNywgMTIyLCA3MDgsIDkyNywgMzA4XQA=.jpg', '88', '88', '2016-05-06', '1', '88', '4', '0', '0');
INSERT INTO `erp_announcement` VALUES ('58', 'business/pictures/Wzg1OCwgODE2LCA4MTAsIDU4MCwgNjQxLCA3NjksIDY4NywgODMyLCAzMjEsIDk2XQY=.jpg', '客户', '65', '2016-05-06', '1', '与他人也太容易', '4', '0', '0');
INSERT INTO `erp_announcement` VALUES ('59', 'business/pictures/Wzg1NywgMjc5LCA3NTgsIDc0OSwgMzI1LCAzNTAsIDQyNCwgMTYsIDkyOSwgNzU1XRY=.jpg', '87', '87', '2016-05-06', '1', '87', '4', '0', '0');
INSERT INTO `erp_announcement` VALUES ('60', 'business/pictures/WzExNSwgNzU4LCAyOTYsIDE4NSwgNzQ1LCAzOTQsIDUyNiwgMjk5LCA3NjcsIDIxNl0T.jpg', '格瑞特', '34', '2016-05-06', '1', '而额外热舞人', '4', '1', '1');
INSERT INTO `erp_announcement` VALUES ('61', 'business/pictures/WzU5OSwgNTQwLCA1MzksIDE5NiwgNzMsIDE4OCwgMTY0LCAzMzAsIDg2OSwgNDU0XQM=.jpg', '发个', '45', '2016-05-06', '1', '如同仁堂', '4', '0', '0');
INSERT INTO `erp_announcement` VALUES ('62', '', '官方', '54', '2016-05-06', '1', '天热腾腾', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('63', 'business/pictures/WzE0NSwgMjA5LCA0NDIsIDE2OCwgMzc5LCA0MzUsIDU3LCA2MDgsIDc0OCwgNjExXRI=.jpg', '查询', '34', '2016-05-06', '1', '范德萨范德萨', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('64', 'business/pictures/WzQ1MywgODU3LCA1MjMsIDE5MywgNTE0LCA2NjQsIDg4OSwgNzk0LCA0MjEsIDYwNF0N.jpg', '辅导费', '43', '2016-05-06', '1', '的发生的房顶上', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('65', 'business/pictures/WzY1NywgNjQwLCA2NzIsIDkzNywgNzE2LCAxNjcsIDQsIDczNSwgOTksIDQ5Nl0Z.jpg', '格斗', '56', '2016-05-06', '1', '太热', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('66', 'business/pictures/Wzk4MSwgNDYxLCAzOTIsIDg3OSwgMjQ5LCA3MzMsIDQzNiwgMjI1LCA4NDMsIDI0M10PNQg=.jpg', '鬼地方个地方', '44', '2016-06-12', '1', '<p>和法国和法国合肥规划</p>', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('67', 'business/pictures/Wzc3MSwgNTkyLCA4ODMsIDIzOSwgODMzLCA5NTQsIDE2OCwgNzE3LCA3MjUsIDQxNF0ZMTUN.jpg', '1111', '2288', '2016-06-17', '1', '<p>222</p>', '4', '1', '0');
INSERT INTO `erp_announcement` VALUES ('68', '', '111', '111', '2016-07-18', '1', '', '4', '0', '0');
INSERT INTO `erp_announcement` VALUES ('69', '', '55', '555', '2016-07-18', '1', '<p>555</p>', '4', '0', '0');
INSERT INTO `erp_announcement` VALUES ('70', '', '22222', '22222', '2016-08-04', '1', '<p>222222</p>', '4', '0', '0');
INSERT INTO `erp_announcement` VALUES ('71', '', '1111111', '1111', '2016-08-05', '1', '<p>1111</p>', '4', '0', '0');

-- ----------------------------
-- Table structure for erp_business
-- ----------------------------
DROP TABLE IF EXISTS `erp_business`;
CREATE TABLE `erp_business` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(30) NOT NULL,
  `register_date` date DEFAULT NULL,
  `note` longtext,
  `user_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `entry_person` varchar(20) DEFAULT NULL,
  `business_num` varchar(20) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `brief_introduction` varchar(15) DEFAULT NULL,
  `phoneNum` varchar(18) NOT NULL,
  `business_license_copy` varchar(100) DEFAULT NULL,
  `business_license_original` varchar(100) DEFAULT NULL,
  `contact_name` varchar(20) DEFAULT NULL,
  `contact_position` varchar(20) DEFAULT NULL,
  `idCard_negative` varchar(100) DEFAULT NULL,
  `idCard_positive` varchar(100) DEFAULT NULL,
  `due_time` date DEFAULT NULL,
  `business_email` varchar(254) DEFAULT NULL,
  `business_phone` varchar(18) NOT NULL,
  `business_qrcode` varchar(100) DEFAULT NULL,
  `work_address` varchar(18) NOT NULL,
  `business_type` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `erp_business_business_num_4935bbde_uniq` (`business_num`),
  CONSTRAINT `erp_business_user_id_59e3f71_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_business
-- ----------------------------
INSERT INTO `erp_business` VALUES ('4', '上海陆家嘴', '2016-03-10', '<p><em><strong>Hello, World!</strong></em></p>', '17', '上海凡达', '1668380928@qq.com', '1', '律錳管理', 'B001', 'business/logo/WzEwMSwgMTQ1LCAxMjIsIDg5LCA5NjIsIDc5OSwgNjI0LCA1NTMsIDc2OSwgNzkyXQAwFw==.jpg', '法国的双方根据第三方根据第三方', '18701733569', 'business/license/kt6ksoph78zaakmilijzfroykm9stfjdp0xd6zxgyz9wjlwptce5xy4gyepd.jpg', 'business/license/x7jos2vkumsarrvv1qzunlji8jfepnrllckrhjbjx70nzvdfx7xfge6lzjkr.jpg', '奥巴马', '总统', 'idCard/image/1madioll0awmap0wodegux28yxk5ylz2hzdrieamw4u4zlzi69mmaumk0zb8.jpg', 'idCard/image/htrjcvjtal3ezhzmu9xorsoug1lnjzadagl6cvjnlcjsutt2zx2e2tr90e23.jpg', '2016-05-13', '1232132@qq.com', '4001-2545-5235', 'business/qrcode/WzI1LCAzNzYsIDU5OCwgODg4LCA5OTEsIDE4NywgNzQ3LCA2NCwgNTY1LCA1MTldGTQY.jpg', '上海市浦东新区沪南路1000号', '1');
INSERT INTO `erp_business` VALUES ('5', '浙江吴中路', '2016-03-10', '规划法规和很反感', '18', '浙江华硕', '819493212@qq.com', '1', '律錳管理', 'B002', 'business/logo/hj23jfgjmmjlkizeqjbkczhwngskhywoteoukyni4jntvdatapojbocqozuh.jpg', '给梵蒂冈梵蒂冈浮动', '18725698756', null, null, null, null, null, null, null, null, '1', null, '1', '1');
INSERT INTO `erp_business` VALUES ('6', '温州吴中路', '2016-03-10', '规划法规和很反感', '20', '温州忽悠', '819493212@qq.com', '1', '律錳管理', 'B003', 'business/logo/xkgujucmvmjjrnvohnk3ulxzcwg9ygijaeife0mjtsdheuslew029kem3lcg.jpg', '给梵蒂冈梵蒂冈浮动', '18725698758', null, null, null, null, null, null, null, null, '1', null, '1', '1');
INSERT INTO `erp_business` VALUES ('7', '环境还是多家分店', '2016-03-14', '<p>鬼地方个梵蒂冈浮动</p>', '25', '上海你猜', '1668380928@qq.com', '1', '律錳管理', 'B888', 'business/logo/oxfn3rvr34korcpbuy4o3yaheggfksums0j2ndb2geygiamlzcet4flsckkp.jpeg', '斯蒂芬胜多负少的', '18701730556', '', '', '', '', '', '', null, '', '400-555-666', '', '', '1');
INSERT INTO `erp_business` VALUES ('9', '山西省忻州市繁城镇', '2016-04-22', '', '45', '浙江沪和', '55555@qq.com', '1', '律錳管理', 'Bjjj', 'business/logo/a85oaka0saog4bgmtglqnpztlctqlhbwmmcjf4wgp5kzywaygg0fadh2l4lv.jpg', 'DVD三vsdvsdvsd', '18745865235', '', '', '', '', '', '', '2016-06-04', null, '1', '', '1', '1');
INSERT INTO `erp_business` VALUES ('10', '三的撒打算', '2016-04-26', '<p>vdvdsvdsvdsvdsv</p>', '47', '涠洲达华', '727053701@qq.com', '1', '律錳管理', 'B145', 'business/logo/awzeluokhhlqagc4sz8fqorfhkmy8pi6eso9fv3wdutdhxqq6v2mggg4a2r8.jpg', '分的佛挡杀佛', '18701730255', 'business/license/4gscgs48bzcpw9ew51bbnzhw0js0bfbmqioijz2vmmba6vwta9xp6t0aaxii.jpg', '', '', '', '', '', '2016-05-07', '', '1', '', '11', '1');
INSERT INTO `erp_business` VALUES ('11', '佛挡杀佛', '2016-04-28', '', '60', '发个梵蒂冈', '1305251473@qq.com', '0', '律錳管理', 'B550', 'business/logo/nnfujein8ph56g5ie4nboju358isj8riljoqk3ldn56rgtaxcvpkbqdmznw1.jpg', '', '18744585568', '', '', 'vcx', '发的规范的', '', '', null, null, '1', null, '1', '1');
INSERT INTO `erp_business` VALUES ('13', '吉林省白山市靖宇县', '2016-07-26', '', '87', '上海力帆', '1668380928@qq.com', '1', '律錳管理', 'B1122', '', '', '18701730286', '', '', '', '', '', '', null, '2121212@qq.com', '21212121', '', 'ddweqdewdew', '1');
INSERT INTO `erp_business` VALUES ('16', '江西省新余市分宜镇', '2016-08-11', '', '114', '11111', '1668380928@qq.com', '1', '律錳管理', 'B0099', '', '', '18701730286', '', '', '', '', '', '', null, '', '400-333-5678', '', '江西省新余市分宜镇', '1');
INSERT INTO `erp_business` VALUES ('17', '安徽省铜陵市郊区', '2016-08-12', '', '115', '防守打法', '1668380928@qq.com', '1', '律錳管理', 'G2299', '', '', '18701730286', '', '', '', '', '', '', null, '', '400-234-7687', '', '发生地方第三方', '1');

-- ----------------------------
-- Table structure for erp_customer
-- ----------------------------
DROP TABLE IF EXISTS `erp_customer`;
CREATE TABLE `erp_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sex` varchar(2) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `register_date` date NOT NULL,
  `note` longtext,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(30) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `idCard_num` varchar(30) DEFAULT NULL,
  `phoneNum` varchar(18) NOT NULL,
  `city` varchar(30) DEFAULT NULL,
  `industry` varchar(30) DEFAULT NULL,
  `calling_card` varchar(100) DEFAULT NULL,
  `company` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `risk_preference` varchar(5) DEFAULT NULL,
  `customer_type` varchar(2) NOT NULL,
  `portrait` varchar(100) DEFAULT NULL,
  `first_pinyin` varchar(30) DEFAULT NULL,
  `pinyin` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `erp_customer_user_id_79e51877_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_customer
-- ----------------------------
INSERT INTO `erp_customer` VALUES ('1', '1', '山东省第三', '2016-03-11', '<p>范德萨范德萨</p>', '24', '黎明', '1', '342625199102082395', '18701789653', '', '', '', '', '12346@qq.com', null, '1', 'customer/avatar/rdhiy9r70tprnrlboyz54wreyqy21wxzy5mnhph4zrlh1mzndpjvjinwjylo.jpg', null, null);
INSERT INTO `erp_customer` VALUES ('2', '1', '发的范德萨', '2016-03-14', 'DVD上vvd水电工广泛地', '28', '灰机', '1', '342625199102082395', '18701736526', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `erp_customer` VALUES ('5', '1', null, '2016-03-17', null, '32', '李志', '1', '440804199303081613', '13520404512', null, null, null, null, null, null, '1', null, null, null);
INSERT INTO `erp_customer` VALUES ('6', '1', '发的范德萨', '2016-04-11', '的身份地方', null, '张三三', '1', '342625199102082395', '18701766589', '上海', '金融', '', 'vcx', '123456@qq.com', '2', '2', null, null, null);
INSERT INTO `erp_customer` VALUES ('7', '1', '的地方', '2016-04-11', '规范的广泛地', null, '王麻爱', '1', '342625199102082395', '18701730864', '更丰富', '高度', '', '浮动', '342@qq.com', '6', '2', null, null, null);
INSERT INTO `erp_customer` VALUES ('8', '1', '的地方', '2016-04-11', '规范的广泛地', null, '王麻爱', '1', '342625199102082395', '18701730864', '更丰富', '高度', '', '浮动', '342@qq.com', '6', '2', null, null, null);
INSERT INTO `erp_customer` VALUES ('9', '1', '个蛋糕房', '2016-04-11', '发的发生的', null, '浮动', '1', '342625199102082395', '18701765896', '发送到', '高度', '', '给对方', '53543@qq.com', '3', '1', null, null, null);
INSERT INTO `erp_customer` VALUES ('10', '1', '恢复', '2016-04-11', '', null, '和规范化', '1', '342625199102082395', '18701733332', '', '', '', '法国恢复', '', null, '2', null, null, null);
INSERT INTO `erp_customer` VALUES ('11', '1', '恢复', '2016-04-11', '的发个梵蒂冈', null, '和规范化', '1', '342625199102082395', '18701733332', '高度', '给对方', 'customer/calling_card/3xxywof5gvsp9lsc4x3zriktprlky9buywlqxzagsoyhjmnvkuxeci3t5wl9.jpg', '法国恢复', '1111@qq.com', null, '2', null, null, null);
INSERT INTO `erp_customer` VALUES ('12', '1', '浮动', '2016-04-11', '和规范化股份', null, '高度', '1', '342625199102082395', '18701725695', '今天加合法', '给对方', 'customer/calling_card/zncinbyvuhyefve8jvubvgsqlhubi49v44rmrn0d2tuiuonklzvgzv0f8vos.jpg', '给对方', '123445@qq.com', '3', '2', null, null, null);
INSERT INTO `erp_customer` VALUES ('13', '1', '浮动', '2016-04-11', '和规范化股份', null, '高度', '1', '342625199102082395', '18701725695', '今天加合法', '给对方梵蒂冈梵蒂冈', 'customer/calling_card/kjhwe9efulmlirzl1gztqwuhf1xfpql9rmdm9wcnwlkcgdw1ydppwkkw0pzr.jpg', '给对方', '123445@qq.com', '3', '2', 'customer/avatar/WzM0NiwgNzY0LCA2OTYsIDIyLCA1MjIsIDU5MCwgNDAzLCA3NzEsIDE4MSwgOTczXRcxMAw=.jpg', 'gd', 'gaodu');
INSERT INTO `erp_customer` VALUES ('14', '1', '规范的广泛地', '2016-04-22', '', null, '地方', '1', '342625199102082395', '18765478524', '', '', '', '', '', '2', '2', '', 'df', 'difang');
INSERT INTO `erp_customer` VALUES ('15', '1', '形成行政村', '2016-04-26', '发大水发大水发', null, '里散户', '1', '342625199102082395', '18745625548', '', '', 'customer/calling_card/gbrmzar3onc2iviilnytky9g9trupjithiktmimz7nvaztsl2ndkfvk6u1pi.jpg', '', '', '3', '2', 'customer/avatar/WzcyMCwgMzY2LCA4NTgsIDMyNCwgODU5LCAyOTcsIDE1MCwgMTc2LCA0MjQsIDE3XQcyMAA=.jpg', null, null);
INSERT INTO `erp_customer` VALUES ('16', '1', '形成行政村', '2016-04-26', '发大水发大水发', null, '从现在', '0', '342625199102082395', '18745625548', '', '', '', '', '', '3', '2', '', null, null);
INSERT INTO `erp_customer` VALUES ('17', '1', '东方大道', '2016-05-13', '', null, '浮动', '1', '', '18701755003', '', '', '', '', '', '5', '2', 'customer/avatar/WzQ4NSwgNzgzLCA2MjYsIDQwMSwgMzQ0LCAyMywgOTQwLCA4MjYsIDQzMSwgNjU4XQ8xNhE=.jpg', null, null);
INSERT INTO `erp_customer` VALUES ('18', '1', '发顺丰', '2016-05-13', '', null, '高度', '1', '', '18701566231', '', '', '', '', '', '4', '2', 'customer/avatar/WzUzMCwgNTU4LCAzMTcsIDQ0NCwgNTI0LCA2MjcsIDY2MiwgNjI2LCA4ODQsIDI1M10KMTgJ.jpg', null, null);
INSERT INTO `erp_customer` VALUES ('19', '1', '和规范化', '2016-05-16', '', null, '黄飞鸿', '0', '', '18701145245', '', '', '', '', '', '3', '2', 'customer/avatar/WzIxNiwgNzcxLCA5MTAsIDYzNCwgNTU4LCA0MTgsIDMxMSwgOTM4LCA5MjIsIDY5XQMwCQ==.jpg', 'hfh', 'huangfeihong');
INSERT INTO `erp_customer` VALUES ('20', '1', '', '2016-05-16', '', null, '123', '1', '', '13800138000', '', '', '', '', '', '1', '2', '', null, null);
INSERT INTO `erp_customer` VALUES ('21', '1', '', '2016-05-16', '', null, '123', '1', '', '18701522356', '', '', '', '', '', '3', '2', 'customer/avatar/WzgxNSwgNzIxLCA5MzgsIDg4MSwgNjA2LCA2NzAsIDY3NywgNjM3LCA3MTEsIDU2OF0IMBg=.jpg', null, null);
INSERT INTO `erp_customer` VALUES ('22', '2', '给梵蒂冈梵蒂冈浮动', '2016-06-06', '放松法第三方', null, '反倒是', '1', '342625199102082395', '18701730286', '范德萨发生', '辅导费', '', '发的规范的', '1668380928@qq.com', '4', '2', 'customer/avatar/Wzg2MCwgNzM3LCAxMzIsIDg1NSwgNTY3LCA1MzIsIDQ2NSwgNDA1LCAyODIsIDM1MF0QMTcZ.jpg', null, null);
INSERT INTO `erp_customer` VALUES ('23', '1', '', '2016-06-13', '', null, '111', '0', '', '18701730286', '', '', '', '', '', null, '2', 'customer/avatar/WzEzNiwgOTIzLCA5NDksIDk5NywgNjM2LCAzMDMsIDYxNSwgOTk4LCA5MjEsIDMxOF0ZMjQB.jpg', '111', '111');
INSERT INTO `erp_customer` VALUES ('24', '1', '1111', '2016-06-30', '111', null, '111', '1', '342625199102082395', '18701730586', '111', '111', '', '111', '111@qq.com', '4', '2', 'customer/avatar/WzEzOSwgOTUxLCA4NzEsIDIzOCwgMTI1LCA0MDYsIDg0NywgMzY1LCAzNjYsIDk4Nl0IOBM=.jpg', '111', '111');
INSERT INTO `erp_customer` VALUES ('25', '1', '222', '2016-06-30', '', null, '222', '1', '342625199102082395', '18701730226', '', '', '', '222', '222@qq.com', '3', '2', 'customer/avatar/WzE1OCwgMTE2LCAzNDcsIDEzOSwgNzI0LCA0OTksIDMzOSwgNzY4LCA3MDYsIDE0MF0EMTYG.jpg', '222', '222');
INSERT INTO `erp_customer` VALUES ('26', '1', '333', '2016-06-30', '', null, '333', '1', '342625199102082395', '18701730225', '', '', '', '333', '333@qq.com', '3', '2', 'customer/avatar/WzE2MiwgNzc2LCA4OTEsIDQ3OCwgODE3LCA5OSwgNDA1LCA5MTYsIDEwLCA1N10LNQE=.jpg', '333', '333');
INSERT INTO `erp_customer` VALUES ('27', '1', '111', '2016-07-19', '', null, '111', '1', '342625199102082395', '18701730286', '', '', '', '', '', null, '2', '', '111', '111');
INSERT INTO `erp_customer` VALUES ('28', '1', '5555', '2016-08-04', '', null, '5555', '0', '342625199102082395', '18701730256', '', '', '', '555', '', '4', '2', '', '5555', '5555');
INSERT INTO `erp_customer` VALUES ('29', '1', null, '2016-08-10', null, '106', 'fdsf', '1', null, '17722493271', null, null, '', null, '1668380928@qq.com', null, '2', '', 'fdsf', 'fdsf');
INSERT INTO `erp_customer` VALUES ('30', '1', null, '2016-08-10', null, '107', 'fdsfdsfd', '1', null, '17722493271', null, null, '', null, '1668380928@qq.com', null, '1', '', 'fdsfdsfd', 'fdsfdsfd');
INSERT INTO `erp_customer` VALUES ('31', '1', null, '2016-08-10', null, '110', 'fdfdfdfd', '1', null, '18701730286', null, null, '', null, '18701730286@163.com', null, '1', '', 'fdfdfdfd', 'fdfdfdfd');
INSERT INTO `erp_customer` VALUES ('32', '1', null, '2016-08-10', null, '111', '发送到', '1', null, '18221888969', null, null, '', null, '1668380928@qq.com', null, '1', '', 'fsd', 'fasongdao');
INSERT INTO `erp_customer` VALUES ('33', '1', null, '2016-08-11', null, '112', 'dfds', '1', null, '18701730286', null, null, '', null, '1668380928@qq.com', null, '1', '', 'dfds', 'dfds');
INSERT INTO `erp_customer` VALUES ('34', '1', null, '2016-08-11', null, '113', 'dfds', '1', null, '18701730286', null, null, '', null, '1668380928@qq.com', null, '1', '', 'dfds', 'dfds');

-- ----------------------------
-- Table structure for erp_customer_agents
-- ----------------------------
DROP TABLE IF EXISTS `erp_customer_agents`;
CREATE TABLE `erp_customer_agents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `agent_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_id` (`customer_id`,`agent_id`),
  KEY `erp_customer_agents_agent_id_6c9707cc_fk_erp_agent_id` (`agent_id`),
  CONSTRAINT `erp_customer_agents_agent_id_6c9707cc_fk_erp_agent_id` FOREIGN KEY (`agent_id`) REFERENCES `erp_agent` (`id`),
  CONSTRAINT `erp_customer_agents_customer_id_7530a26_fk_erp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `erp_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_customer_agents
-- ----------------------------
INSERT INTO `erp_customer_agents` VALUES ('38', '1', '4');
INSERT INTO `erp_customer_agents` VALUES ('39', '1', '6');
INSERT INTO `erp_customer_agents` VALUES ('2', '2', '6');
INSERT INTO `erp_customer_agents` VALUES ('13', '5', '4');
INSERT INTO `erp_customer_agents` VALUES ('6', '6', '7');
INSERT INTO `erp_customer_agents` VALUES ('7', '7', '7');
INSERT INTO `erp_customer_agents` VALUES ('8', '8', '7');
INSERT INTO `erp_customer_agents` VALUES ('9', '9', '7');
INSERT INTO `erp_customer_agents` VALUES ('10', '13', '4');
INSERT INTO `erp_customer_agents` VALUES ('46', '14', '4');
INSERT INTO `erp_customer_agents` VALUES ('52', '14', '35');
INSERT INTO `erp_customer_agents` VALUES ('15', '15', '4');
INSERT INTO `erp_customer_agents` VALUES ('16', '16', '4');
INSERT INTO `erp_customer_agents` VALUES ('26', '17', '4');
INSERT INTO `erp_customer_agents` VALUES ('27', '18', '14');
INSERT INTO `erp_customer_agents` VALUES ('28', '19', '4');
INSERT INTO `erp_customer_agents` VALUES ('29', '21', '4');
INSERT INTO `erp_customer_agents` VALUES ('44', '22', '6');
INSERT INTO `erp_customer_agents` VALUES ('47', '23', '4');
INSERT INTO `erp_customer_agents` VALUES ('48', '24', '4');
INSERT INTO `erp_customer_agents` VALUES ('49', '25', '4');
INSERT INTO `erp_customer_agents` VALUES ('50', '26', '4');
INSERT INTO `erp_customer_agents` VALUES ('51', '27', '4');
INSERT INTO `erp_customer_agents` VALUES ('53', '28', '4');

-- ----------------------------
-- Table structure for erp_customer_pending
-- ----------------------------
DROP TABLE IF EXISTS `erp_customer_pending`;
CREATE TABLE `erp_customer_pending` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `phoneNum` varchar(18) NOT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `register_date` date DEFAULT NULL,
  `idCard_num` varchar(30) DEFAULT NULL,
  `note` longtext,
  `industry` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `agents_id` int(11) DEFAULT NULL,
  `calling_card` varchar(100) DEFAULT NULL,
  `company` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `estimate_purchase_total` int(11) DEFAULT NULL,
  `risk_preference` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `erp_customer_pending_agents_id_7b437c4c_fk_erp_agent_id` (`agents_id`),
  CONSTRAINT `erp_customer_pending_agents_id_7b437c4c_fk_erp_agent_id` FOREIGN KEY (`agents_id`) REFERENCES `erp_agent` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_customer_pending
-- ----------------------------

-- ----------------------------
-- Table structure for erp_customer_pending_product_target
-- ----------------------------
DROP TABLE IF EXISTS `erp_customer_pending_product_target`;
CREATE TABLE `erp_customer_pending_product_target` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_pending_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_pending_id` (`customer_pending_id`,`product_id`),
  KEY `erp_customer_pending_produ_product_id_12491fdf_fk_erp_product_id` (`product_id`),
  CONSTRAINT `erp_customer_pending_produ_product_id_12491fdf_fk_erp_product_id` FOREIGN KEY (`product_id`) REFERENCES `erp_product` (`id`),
  CONSTRAINT `erp_cust_customer_pending_id_35384e69_fk_erp_customer_pending_id` FOREIGN KEY (`customer_pending_id`) REFERENCES `erp_customer_pending` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_customer_pending_product_target
-- ----------------------------

-- ----------------------------
-- Table structure for erp_customer_product_target
-- ----------------------------
DROP TABLE IF EXISTS `erp_customer_product_target`;
CREATE TABLE `erp_customer_product_target` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_id` (`customer_id`,`product_id`),
  KEY `erp_customer_product_targe_product_id_6e7ba555_fk_erp_product_id` (`product_id`),
  CONSTRAINT `erp_customer_product_targe_product_id_6e7ba555_fk_erp_product_id` FOREIGN KEY (`product_id`) REFERENCES `erp_product` (`id`),
  CONSTRAINT `erp_customer_product_tar_customer_id_30a72087_fk_erp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `erp_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_customer_product_target
-- ----------------------------
INSERT INTO `erp_customer_product_target` VALUES ('24', '1', '2');
INSERT INTO `erp_customer_product_target` VALUES ('25', '1', '3');
INSERT INTO `erp_customer_product_target` VALUES ('26', '1', '6');
INSERT INTO `erp_customer_product_target` VALUES ('1', '12', '3');
INSERT INTO `erp_customer_product_target` VALUES ('2', '12', '5');
INSERT INTO `erp_customer_product_target` VALUES ('3', '12', '6');
INSERT INTO `erp_customer_product_target` VALUES ('34', '13', '3');
INSERT INTO `erp_customer_product_target` VALUES ('35', '13', '5');
INSERT INTO `erp_customer_product_target` VALUES ('33', '14', '2');
INSERT INTO `erp_customer_product_target` VALUES ('14', '15', '5');
INSERT INTO `erp_customer_product_target` VALUES ('15', '15', '6');
INSERT INTO `erp_customer_product_target` VALUES ('10', '16', '5');
INSERT INTO `erp_customer_product_target` VALUES ('11', '16', '6');
INSERT INTO `erp_customer_product_target` VALUES ('19', '19', '3');
INSERT INTO `erp_customer_product_target` VALUES ('21', '21', '3');
INSERT INTO `erp_customer_product_target` VALUES ('28', '22', '6');
INSERT INTO `erp_customer_product_target` VALUES ('27', '22', '8');
INSERT INTO `erp_customer_product_target` VALUES ('32', '24', '7');
INSERT INTO `erp_customer_product_target` VALUES ('30', '25', '7');
INSERT INTO `erp_customer_product_target` VALUES ('31', '26', '9');

-- ----------------------------
-- Table structure for erp_online_chat
-- ----------------------------
DROP TABLE IF EXISTS `erp_online_chat`;
CREATE TABLE `erp_online_chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(500) NOT NULL,
  `send_time` datetime NOT NULL,
  `business_id` int(11) NOT NULL,
  `recipient_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `read` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `erp_online_chat_business_id_1094fccd_fk_erp_business_id` (`business_id`),
  KEY `erp_online_chat_recipient_id_1da90dc9_fk_auth_user_id` (`recipient_id`),
  KEY `erp_online_chat_sender_id_27517150_fk_auth_user_id` (`sender_id`),
  CONSTRAINT `erp_online_chat_business_id_1094fccd_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `erp_online_chat_recipient_id_1da90dc9_fk_auth_user_id` FOREIGN KEY (`recipient_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `erp_online_chat_sender_id_27517150_fk_auth_user_id` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=210 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_online_chat
-- ----------------------------
INSERT INTO `erp_online_chat` VALUES ('40', '男方法', '2016-07-21 14:15:37', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('41', '南方女方给男方', '2016-07-21 14:15:40', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('42', '弄饭饭', '2016-07-21 14:15:42', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('43', '个人郭德纲', '2016-07-21 14:26:05', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('44', '顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶', '2016-07-21 14:45:31', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('45', '本规范办官方吧官方', '2016-07-21 15:06:47', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('48', '发生的发生地方', '2016-07-21 15:09:41', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('49', '给发个梵蒂冈发', '2016-07-21 15:09:44', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('50', '很反感', '2016-07-21 15:10:41', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('51', '个地方官', '2016-07-21 15:10:59', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('52', '和符合规范', '2016-07-21 15:19:01', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('53', '本规范干部', '2016-07-21 15:21:25', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('54', '你在哪里啊？\n\n', '2016-07-21 15:21:39', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('55', '我在上海', '2016-07-21 15:21:52', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('56', '的说法是否', '2016-07-21 15:27:27', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('57', 'v发v凡达', '2016-07-21 15:27:34', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('58', '防守打法', '2016-07-21 15:44:25', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('60', 'v虚线 ', '2016-07-21 15:44:53', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('61', 'vxvxv', '2016-07-21 15:45:06', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('62', '刚刚的规范的刚', '2016-07-21 15:45:18', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('63', '$(\".chat01_content\").scrollTop($(\".mes3\").height()*10000)$(\".chat01_content\").scrollTop($(\".mes3\").height()*10000)', '2016-07-21 15:46:34', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('64', '刚刚梵蒂冈梵蒂冈', '2016-07-21 15:52:31', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('65', '和法国恢复恢复', '2016-07-21 15:56:23', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('66', '发的发生地方', '2016-07-21 16:18:47', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('67', 'v是的v是v ', '2016-07-21 16:18:54', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('68', '和法国和法国', '2016-07-21 16:20:48', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('69', 'GDGFGD', '2016-07-21 16:37:12', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('70', 'vfdvfd ', '2016-07-21 16:44:57', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('71', 'dgahsdgad', '2016-07-21 16:50:14', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('72', '发的发生法', '2016-07-21 16:50:24', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('73', 'vfdvdfvf', '2016-07-21 16:50:38', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('74', 'v凡达v发v ', '2016-07-21 16:50:44', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('75', '我靠\n', '2016-07-21 16:50:52', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('76', '去死', '2016-07-21 16:51:01', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('77', '发生的发生的发生', '2016-07-21 17:00:03', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('78', '什么时候吃饭？\n', '2016-07-21 17:52:05', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('79', '什么时候吃饭？\n', '2016-07-21 17:52:30', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('80', '十二点左右\n', '2016-07-21 17:52:54', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('81', '在哪里吃？', '2016-07-21 17:56:35', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('82', 'gfdgdfg ', '2016-07-22 09:33:03', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('83', 'ytrytrytry', '2016-07-22 09:33:15', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('84', '华鼎奖阿什顿看撒谎的\n', '2016-07-25 13:41:41', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('85', '干嘛？', '2016-07-25 13:42:05', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('86', '吃饭', '2016-07-25 13:42:14', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('87', '早晨打卡了吗？', '2016-07-28 09:42:42', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('88', '打过了\n', '2016-07-28 09:42:51', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('89', 'fdsfs\n', '2016-07-28 09:48:37', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('90', '急急急', '2016-07-28 09:55:11', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('91', 'v的v', '2016-07-28 09:57:48', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('92', '啥意思啊？', '2016-07-28 09:58:22', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('93', '\n', '2016-07-28 09:58:59', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('94', '\n发v大幅度', '2016-07-28 10:05:14', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('95', 'hi', '2016-07-28 10:40:41', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('96', '发生地方第三方', '2016-07-28 10:42:15', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('97', '玛尼？', '2016-07-28 10:55:49', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('98', '要你管！！！！', '2016-07-28 10:56:09', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('99', '吃的少吃的少', '2016-07-28 13:38:58', '4', '40', '17', '1');
INSERT INTO `erp_online_chat` VALUES ('100', '干嘛你？', '2016-07-28 14:00:45', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('101', '你几点睡呢常见的', '2016-07-28 14:03:06', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('102', '逗逼！！！', '2016-07-28 14:04:13', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('103', 'dasddasd', '2016-07-28 14:15:44', '4', '40', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('104', '年该行河南话', '2016-07-28 14:15:53', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('105', '我靠', '2016-07-28 14:17:09', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('106', '下午去，阿里', '2016-07-28 14:22:25', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('107', '你去哪？', '2016-07-28 14:23:38', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('108', '要你管，╭(╯^╰)╮\n', '2016-07-28 14:23:54', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('109', '下班', '2016-07-28 15:19:36', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('110', '这么早', '2016-07-28 15:19:56', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('111', '哎', '2016-07-28 15:40:14', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('112', '大苏打', '2016-07-28 15:47:50', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('113', '鼎折覆餗', '2016-07-28 16:07:05', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('114', '不过分不高', '2016-07-28 17:43:58', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('115', '\n给合肥合肥', '2016-07-28 17:44:16', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('116', '防辐射', '2016-07-28 17:44:32', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('117', '佛挡杀佛', '2016-07-28 17:44:42', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('118', '不过分不高', '2016-07-28 17:45:48', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('119', '\n', '2016-07-28 17:45:51', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('120', '\n', '2016-07-28 17:45:52', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('121', '\n', '2016-07-28 17:45:53', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('122', '规范化股份', '2016-07-28 17:46:38', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('123', '\n', '2016-07-28 17:46:42', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('124', '\n', '2016-07-28 17:46:44', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('125', '\n', '2016-07-28 17:46:46', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('126', '\n', '2016-07-28 17:46:48', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('127', '\n', '2016-07-28 17:47:53', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('128', '\n', '2016-07-28 17:47:54', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('129', '\n', '2016-07-28 17:47:55', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('130', '\n', '2016-07-28 17:47:56', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('131', '\n', '2016-07-28 17:48:03', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('132', '\n', '2016-07-28 17:48:05', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('133', '\n法规的法规', '2016-07-28 17:48:20', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('134', '\n', '2016-07-28 17:48:30', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('135', '\n', '2016-07-29 09:08:26', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('136', '\n', '2016-07-29 09:08:29', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('137', '\n', '2016-07-29 09:08:32', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('138', '\n', '2016-07-29 09:08:38', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('139', '\n', '2016-07-29 09:08:40', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('140', '\n', '2016-07-29 09:08:45', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('141', 'hfgh ', '2016-07-29 09:08:54', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('142', '\n', '2016-07-29 09:08:57', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('143', 'hjgjghjg\n\n\n\n\n\n', '2016-07-29 09:10:27', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('144', 'hi', '2016-07-29 09:50:19', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('145', '\nvfdvf', '2016-07-29 09:51:15', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('146', '好久好久', '2016-07-29 09:53:25', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('147', '哈哈哈', '2016-07-29 10:00:55', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('148', '\n画虎刻鹄', '2016-07-29 10:01:17', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('149', '\n六角恐龙', '2016-07-29 10:01:21', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('150', '太热特然\n', '2016-07-29 10:01:29', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('151', '\n个人个人', '2016-07-29 10:01:36', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('152', '干嘛呢？', '2016-07-29 10:02:17', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('153', '靠\n', '2016-07-29 10:02:30', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('154', '我靠', '2016-07-29 10:03:00', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('155', '我靠\n', '2016-07-29 10:03:09', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('156', '已\n\n', '2016-07-29 10:03:25', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('157', '放松放松的三\n', '2016-07-29 10:03:37', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('158', '范德萨范德萨', '2016-07-29 10:03:50', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('159', '借款借款', '2016-07-29 10:04:06', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('160', '发生范德萨\n', '2016-07-29 10:04:18', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('161', '鬼地方个地方\n\n\n', '2016-07-29 10:05:23', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('162', '发生的发生地方\n\n\n', '2016-07-29 10:05:28', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('163', '\n几款空间打开', '2016-07-29 10:05:45', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('164', '和监管局', '2016-07-29 10:09:20', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('165', '和卡卡和\n', '2016-07-29 10:09:43', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('166', '将军令蓝精灵\n', '2016-07-29 10:10:09', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('167', '\n从第三次的', '2016-07-29 10:10:15', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('168', '在吗？', '2016-07-29 10:11:02', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('169', '在的', '2016-07-29 10:11:47', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('170', '\n干嘛？', '2016-07-29 10:11:56', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('171', '好久好久', '2016-07-29 13:41:53', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('172', '\n范德萨发的', '2016-07-29 13:43:10', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('173', '借款借款', '2016-07-29 13:44:49', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('174', '\n好久好久', '2016-07-29 13:47:54', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('175', '你在干那？\n', '2016-07-29 13:48:05', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('176', '怎么了？', '2016-07-29 13:51:28', '4', '40', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('177', '恢复规划', '2016-07-29 13:52:45', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('178', '范德萨发生', '2016-07-29 13:55:45', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('179', '\nvfdvf', '2016-07-29 13:56:17', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('180', '很反感', '2016-07-29 13:56:36', '4', '21', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('192', '和积分换房间快速', '2016-07-29 15:14:48', '4', '66', '40', '1');
INSERT INTO `erp_online_chat` VALUES ('195', '可好看', '2016-07-29 16:21:41', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('196', '\n太热太热特太热特然他', '2016-07-29 16:21:49', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('197', '空间和卡卡和空', '2016-07-29 16:21:59', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('198', '\n借款借款', '2016-07-29 17:02:36', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('199', '\n好久好久', '2016-07-29 17:06:47', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('200', 'HI', '2016-08-01 09:56:38', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('201', '干嘛？', '2016-08-01 09:56:57', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('202', '\nxiangnile', '2016-08-01 09:57:04', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('203', '草，说中文\n', '2016-08-01 09:57:18', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('204', '你打我啊\n', '2016-08-01 09:57:28', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('205', '打不死你\n', '2016-08-01 09:57:34', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('206', '\n', '2016-08-01 10:07:46', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('207', '\n', '2016-08-01 10:08:02', '4', '21', '66', '1');
INSERT INTO `erp_online_chat` VALUES ('208', '你啥意思啊\n\n', '2016-08-01 10:08:19', '4', '66', '21', '1');
INSERT INTO `erp_online_chat` VALUES ('209', 'efewfw ', '2016-08-05 09:36:12', '4', '40', '21', '0');

-- ----------------------------
-- Table structure for erp_position
-- ----------------------------
DROP TABLE IF EXISTS `erp_position`;
CREATE TABLE `erp_position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `register_date` date DEFAULT NULL,
  `entry_person` varchar(20) NOT NULL,
  `business_id` int(11) DEFAULT NULL,
  `department` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `erp_position_business_id_15c199a3_fk_erp_business_id` (`business_id`),
  CONSTRAINT `erp_position_business_id_15c199a3_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_position
-- ----------------------------
INSERT INTO `erp_position` VALUES ('1', '理财师', '2016-04-25', '张三', '4', '市场部');
INSERT INTO `erp_position` VALUES ('3', '会计', '2016-04-25', '张三', '4', '财务部');
INSERT INTO `erp_position` VALUES ('4', '经理', '2016-04-26', '张三', null, '1');
INSERT INTO `erp_position` VALUES ('5', '经理', '2016-04-26', '张三', null, '1');
INSERT INTO `erp_position` VALUES ('6', '经理', '2016-04-26', '张三', '4', '技术部');
INSERT INTO `erp_position` VALUES ('8', '网络营销', '2016-09-13', 'ssss', '4', '销售');

-- ----------------------------
-- Table structure for erp_position_permissions
-- ----------------------------
DROP TABLE IF EXISTS `erp_position_permissions`;
CREATE TABLE `erp_position_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `position_id` (`position_id`,`permission_id`),
  KEY `erp_position_permis_permission_id_77bcdd6d_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `erp_position_permissions_position_id_848ab53_fk_erp_position_id` FOREIGN KEY (`position_id`) REFERENCES `erp_position` (`id`),
  CONSTRAINT `erp_position_permis_permission_id_77bcdd6d_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_position_permissions
-- ----------------------------
INSERT INTO `erp_position_permissions` VALUES ('47', '1', '218');
INSERT INTO `erp_position_permissions` VALUES ('48', '1', '220');
INSERT INTO `erp_position_permissions` VALUES ('49', '1', '221');
INSERT INTO `erp_position_permissions` VALUES ('50', '1', '222');
INSERT INTO `erp_position_permissions` VALUES ('51', '1', '223');
INSERT INTO `erp_position_permissions` VALUES ('44', '1', '224');
INSERT INTO `erp_position_permissions` VALUES ('45', '1', '225');
INSERT INTO `erp_position_permissions` VALUES ('46', '1', '226');
INSERT INTO `erp_position_permissions` VALUES ('22', '3', '218');
INSERT INTO `erp_position_permissions` VALUES ('23', '3', '219');
INSERT INTO `erp_position_permissions` VALUES ('24', '3', '222');
INSERT INTO `erp_position_permissions` VALUES ('25', '3', '223');
INSERT INTO `erp_position_permissions` VALUES ('21', '3', '224');
INSERT INTO `erp_position_permissions` VALUES ('27', '6', '218');
INSERT INTO `erp_position_permissions` VALUES ('28', '6', '219');
INSERT INTO `erp_position_permissions` VALUES ('29', '6', '220');
INSERT INTO `erp_position_permissions` VALUES ('30', '6', '221');
INSERT INTO `erp_position_permissions` VALUES ('26', '6', '224');
INSERT INTO `erp_position_permissions` VALUES ('56', '8', '220');

-- ----------------------------
-- Table structure for erp_product
-- ----------------------------
DROP TABLE IF EXISTS `erp_product`;
CREATE TABLE `erp_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `abbreviation` varchar(100) NOT NULL,
  `strategy` longtext,
  `custodian` varchar(100) DEFAULT NULL,
  `term_footnote` varchar(2000) DEFAULT NULL,
  `manager` varchar(30) NOT NULL,
  `begin_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `period` int(11) NOT NULL,
  `mini_sub` bigint(20) NOT NULL,
  `addition` bigint(20) DEFAULT NULL,
  `invest_scope` longtext,
  `alert_line` decimal(6,4) DEFAULT NULL,
  `clearance_line` decimal(6,4) DEFAULT NULL,
  `risk_preference` varchar(10) NOT NULL,
  `return_expected` decimal(6,4) NOT NULL,
  `subscription_fee` decimal(6,4) DEFAULT NULL,
  `custody_fee` decimal(6,4) DEFAULT NULL,
  `service_fee` decimal(6,4) DEFAULT NULL,
  `redemption_fee` decimal(6,4) DEFAULT NULL,
  `management_fee` decimal(6,4) DEFAULT NULL,
  `compensation` decimal(6,4) DEFAULT NULL,
  `compensation_distribution` varchar(2000) DEFAULT NULL,
  `business_id` int(11) DEFAULT NULL,
  `on_top` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `product_type_id` int(11) NOT NULL,
  `ahead_end` tinyint(1) NOT NULL,
  `product_sum` int(10) unsigned DEFAULT NULL,
  `finished` tinyint(1) NOT NULL,
  `contract` varchar(100) DEFAULT NULL,
  `province` varchar(30) DEFAULT NULL,
  `structure` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `erp_product_2f4e4ac4` (`business_id`),
  KEY `erp_product_d9862cd8` (`product_type_id`),
  CONSTRAINT `erp_product_business_id_42978b48_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `erp_product_product_type_id_3596e22e_fk_erp_product_type_id` FOREIGN KEY (`product_type_id`) REFERENCES `erp_product_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_product
-- ----------------------------
INSERT INTO `erp_product` VALUES ('2', '锦绣3号', '锦绣3号', '<p>的范德萨发生的房顶上</p>', '中国银行', '划分贵航股份', '张三', '2016-11-10', '2016-03-10', '1200', '150', '126', '<p>发斯蒂芬斯蒂芬斯蒂芬身份</p>', '12.0000', '0.0120', '5', '1.0011', '12.0000', '12.0000', '12.0000', '12.0000', '12.0000', '12.0000', '12', '4', '1', '1', '6', '0', '888888', '0', 'product/contract/ots1entxvgjocp2i8iz7imddkacqxetais71dyvghuwghnjf4j30kjhq7wjf.jpg', '官方大哥大法官', '0');
INSERT INTO `erp_product` VALUES ('3', '汇盈1号', '汇盈1号', '<p>而额外热舞大方的说法</p>', '中国工商银行', '绯闻绯闻v', '陈晓', '2016-03-05', '2616-05-18', '1200', '127', '12', '<p>额外企鹅请问</p>', '12.0000', '12.0000', '3', '1.2200', '12.0000', '12.0000', '12.0000', '12.0000', '12.0000', '12.0000', '12', '4', '1', '1', '4', '0', '11', '0', '1', '', '0');
INSERT INTO `erp_product` VALUES ('5', '金马349号', '金马349号', '<p>regret</p>', '建设银行', 'tertiary', '李文', '2016-03-19', '2016-03-25', '4', '5', '4', '<p>梵蒂冈梵蒂冈</p>', '4.0000', '4.0000', '4', '2.0000', '4.0000', '4.0000', '4.0000', '4.0000', '4.0000', '4.0000', '4', '4', '1', '1', '5', '0', null, '0', '1', '', '0');
INSERT INTO `erp_product` VALUES ('6', '锦绣2号', '锦绣2号', '<p>发生范德萨</p>', '范德萨范德萨', '发生范德萨', '范德萨发的', '2016-03-11', '2016-03-26', '21', '22', '23', '<p>问问我去</p>', '22.0000', '22.0000', '2', '22.0000', '22.0000', '21.9999', '22.0000', '22.0000', '22.0000', '22.0000', '22', '7', '1', '1', '1', '0', '1366', '0', '1', '', '0');
INSERT INTO `erp_product` VALUES ('7', '华为888', '撒旦撒旦撒', '<p>环境和关键</p>', '刚和规范合格', '规范的广泛地', '门口那么', '2016-04-01', '2016-04-08', '100', '1000', '8883', '<p>，老看见了看见了</p>', '10.0000', '10.0000', '1', '10.0000', '10.0000', '10.0000', '10.0000', '10.0000', '10.0000', '10.0000', '件合格机构', '4', '1', '1', '1', '0', '1110998', '0', '1', '', '0');
INSERT INTO `erp_product` VALUES ('8', '金融8号', '大苏打发送到', '<p>发给梵蒂冈梵蒂冈发鬼地方发过个梵蒂冈范甘迪发鬼地方给梵蒂冈梵蒂冈地方</p>', '个梵蒂冈', '', '反倒是', '2016-05-18', '2016-05-18', '24', '10', '1000', '<p>鬼地方给梵蒂冈梵蒂冈就和规范和规范化规范和规范化天鬼地方个梵蒂冈分国芳蛋糕房的</p>', '0.1000', '0.1000', '2', '0.2000', '0.1000', '0.1000', '0.1000', '0.1000', '0.1000', '0.1000', '', '7', '0', '1', '1', '0', '2000', '0', 'product/contract/ivovtpvujm54dyssjyni9ovb1lvotq0viurztczheqrl5sedawqhfral9d9g.jpg', '', '0');
INSERT INTO `erp_product` VALUES ('9', '三星金融', '发范德萨范德萨', '<p><span style=\"font-size: large;\"><em><strong>&nbsp; 刚梵蒂冈地方刚发的规范的广泛地个梵蒂</strong></em></span></p>\r\n<p><span style=\"font-size: large;\"><em><strong>&nbsp; &nbsp; 冈地方鬼地方个梵蒂冈地方官规定规范的官方给梵蒂冈梵蒂冈浮动规范的给梵蒂冈梵蒂冈浮动官方</strong></em></span></p>\r\n<p>&nbsp;</p>\r\n<p><span style=\"font-size: medium;\"><strong>房间的划分及安防和福建省的房间第三方和空间的房间看电视</strong></span></p>\r\n<p><span style=\"font-size: medium;\"><strong>看到房间都流口水放假了肯定是房间的</strong></span></p>\r\n<p><span style=\"font-size: medium;\"><strong>房间看第三方尽快蓝水晶发了多少</strong></span></p>\r\n<p><span style=\"font-size: medium;\"><strong>房间的看来是福建省的空间发牢骚的</strong></span></p>\r\n<p><span style=\"font-size: medium;\"><strong>付款了第三方计算机法律</strong></span></p>', '及环境规划及', '股份的股份的股份', '公告高度', '2016-05-05', '2016-05-06', '36', '10000', '1000', '<p><span><em><strong>&nbsp;<img title=\"酷\" src=\"../../static/tiny_mce/plugins/emotions/img/smiley-cool.gif\" alt=\"酷\" border=\"0\" /><span style=\"font-size: large; background-color: #ff9900;\">刚梵蒂冈地方刚发的规范的广泛地个梵蒂</span></strong></em></span></p>\r\n<p><span style=\"font-size: large; background-color: #ff9900;\"><em><strong>&nbsp; &nbsp; 冈地方鬼地方个梵蒂冈地方官规定规范的官方给梵蒂冈梵蒂冈浮动规范的给梵蒂冈梵蒂冈浮动官方</strong></em></span></p>\r\n<p>&nbsp;</p>\r\n<p><span style=\"background-color: #993366;\"><strong>房间的划分及安防和福建省的房间第三方和空间的房间看电视</strong></span></p>\r\n<p><span style=\"background-color: #993366;\"><strong>看到房间都流口水放假了肯定是房间的</strong></span></p>\r\n<p><span style=\"background-color: #993366;\"><strong>房间看第三方尽快蓝水晶发了多少</strong></span></p>\r\n<p><span style=\"background-color: #993366;\"><strong>房间的看来是福建省的空间发牢骚的</strong></span></p>\r\n<p><span><strong><span style=\"background-color: #993366;\">付款了第三方计算机法律</span><img title=\"发财\" src=\"../../static/tiny_mce/plugins/emotions/img/smiley-money-mouth.gif\" alt=\"发财\" border=\"0\" /></strong></span></p>', '0.2200', '0.2200', '1', '0.1140', '0.2200', '0.2200', '0.2200', '0.2160', '0.2200', '0.2200', '股份大股东', '4', '0', '1', '2', '0', '99998', '0', 'product/contract/bleh33qbawzx87s6i4rl73mbiyui56z5hulv4qfnnofatzf20dmm85uq9akq.jpg', '范德萨范德萨发生', '0');
INSERT INTO `erp_product` VALUES ('10', '未命名', '111', '', '11', '', '11', null, null, '1', '1', null, '', null, null, '3', '1.0000', null, null, null, null, null, null, '', '4', '1', '0', '3', '0', '1', '0', '', '', '0');
INSERT INTO `erp_product` VALUES ('11', '未命名', '111', '', '', '', '11', null, null, '11', '11', null, '', null, null, '3', '11.0000', null, null, null, null, null, null, '', '4', '0', '0', '3', '0', '8', '0', '', '', '0');
INSERT INTO `erp_product` VALUES ('12', '2222', '2222', '<p>222</p>', '222', '222', '222', '1899-11-28', '2016-08-16', '22', '22', '22', '<p>222</p>', '22.0000', '2.0000', '3', '2.0000', '2.0000', '2.0000', '1.0000', '2.0000', '2.0000', '2.0000', '222', '4', '1', '0', '4', '1', '20', '0', '', '222', '0');
INSERT INTO `erp_product` VALUES ('13', '2', '2', '<p>2</p>', '2', '2', '2', '1899-12-31', '1899-11-28', '2', '2', '2', '<p>2</p>', '2.0000', '2.0000', '3', '2.0000', '2.0000', '2.0000', '2.0000', '2.0000', '2.0000', '2.0000', '2', '4', '1', '0', '3', '1', '2', '0', '', '2', '0');
INSERT INTO `erp_product` VALUES ('14', '2', '2', '', '2', '', '2', null, null, '2', '2', null, '', null, null, '3', '2.0000', null, null, null, null, null, null, '', '4', '1', '0', '3', '0', '2', '0', '', '', '0');
INSERT INTO `erp_product` VALUES ('15', '未命名', '2', '', '9990', '', '8880', null, null, '2', '2', null, '', null, null, '3', '2.0000', null, null, null, null, null, null, '', '4', '1', '0', '3', '0', null, '0', '', '', '0');
INSERT INTO `erp_product` VALUES ('16', '111', '11', '', '2228', '', '1115', '2016-08-01', '2016-08-17', '1', '1', null, '', null, null, '3', '1.0000', null, null, null, null, null, null, '', '4', '1', '0', '3', '0', '1', '0', '', '', '0');
INSERT INTO `erp_product` VALUES ('17', '444', '44', '', '44', '', '44', '2016-08-16', '2016-08-22', '44', '44', null, '', null, null, '3', '44.0000', null, null, null, null, null, null, '', '4', '1', '0', '3', '0', '41', '0', '', '', '0');
INSERT INTO `erp_product` VALUES ('18', '77', '77', '', '77', '', '77', '2016-08-10', '2016-08-25', '77', '77', null, '', null, null, '3', '77.0000', null, null, null, null, null, null, '', '4', '1', '0', '3', '0', '77', '0', '', '', '0');
INSERT INTO `erp_product` VALUES ('19', '未命名', '111', '', '', '', '1', null, null, '1', '1', null, '', null, null, '3', '1.0000', null, null, null, null, null, null, '', '4', '0', '0', '3', '0', '1', '0', '', '', '0');

-- ----------------------------
-- Table structure for erp_product_type
-- ----------------------------
DROP TABLE IF EXISTS `erp_product_type`;
CREATE TABLE `erp_product_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeName` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_product_type
-- ----------------------------
INSERT INTO `erp_product_type` VALUES ('1', '股权板块');
INSERT INTO `erp_product_type` VALUES ('2', '创投板块');
INSERT INTO `erp_product_type` VALUES ('3', '债权板块');
INSERT INTO `erp_product_type` VALUES ('4', '证券板块');
INSERT INTO `erp_product_type` VALUES ('5', '信托板块');
INSERT INTO `erp_product_type` VALUES ('6', '资管板块');
INSERT INTO `erp_product_type` VALUES ('7', '基金理财');

-- ----------------------------
-- Table structure for erp_purchase
-- ----------------------------
DROP TABLE IF EXISTS `erp_purchase`;
CREATE TABLE `erp_purchase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `register_time` datetime NOT NULL,
  `brief` longtext,
  PRIMARY KEY (`id`),
  KEY `erp_purchase_customer_id_aab305_fk_erp_customer_id` (`customer_id`),
  KEY `erp_purchase_product_id_e86e297_fk_erp_product_id` (`product_id`),
  CONSTRAINT `erp_purchase_customer_id_aab305_fk_erp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `erp_customer` (`id`),
  CONSTRAINT `erp_purchase_product_id_e86e297_fk_erp_product_id` FOREIGN KEY (`product_id`) REFERENCES `erp_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_purchase
-- ----------------------------
INSERT INTO `erp_purchase` VALUES ('3', '43243', '2016-03-14', '2016-03-14', '1', '5', '2016-03-14 16:18:00', null);
INSERT INTO `erp_purchase` VALUES ('11', '20000', '2016-03-01', '2016-03-31', '2', '2', '2016-03-17 09:16:37', null);
INSERT INTO `erp_purchase` VALUES ('12', '4000012', '2016-03-01', '2016-03-30', '2', '3', '2016-03-17 09:51:56', null);

-- ----------------------------
-- Table structure for erp_real_purchase
-- ----------------------------
DROP TABLE IF EXISTS `erp_real_purchase`;
CREATE TABLE `erp_real_purchase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) NOT NULL,
  `income_date` date NOT NULL,
  `end_date` date NOT NULL,
  `pay_type` varchar(3) NOT NULL,
  `department` varchar(10) DEFAULT NULL,
  `bill_number` varchar(50) DEFAULT NULL,
  `register_time` datetime NOT NULL,
  `brief` longtext,
  `is_active` tinyint(1) NOT NULL,
  `business_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `real_agent_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `erp_real_purchase_business_id_40c84bc5_fk_erp_business_id` (`business_id`),
  KEY `erp_real_purchase_cb24373b` (`customer_id`),
  KEY `erp_real_purchase_9bea82de` (`product_id`),
  KEY `erp_real_purchase_a0b0f6a2` (`real_agent_id`),
  CONSTRAINT `erp_real_purchase_business_id_40c84bc5_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `erp_real_purchase_customer_id_1291fb0f_fk_erp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `erp_customer` (`id`),
  CONSTRAINT `erp_real_purchase_product_id_72496c33_fk_erp_product_id` FOREIGN KEY (`product_id`) REFERENCES `erp_product` (`id`),
  CONSTRAINT `erp_real_purchase_real_agent_id_62cb6837_fk_erp_agent_id` FOREIGN KEY (`real_agent_id`) REFERENCES `erp_agent` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_real_purchase
-- ----------------------------
INSERT INTO `erp_real_purchase` VALUES ('1', '10000', '2016-04-11', '2016-04-15', '1', '高度', 'eternal', '2016-04-11 07:43:42', '的个非官方个地方官', '1', '4', '13', '2', '4');
INSERT INTO `erp_real_purchase` VALUES ('2', '2568965', '2016-04-01', '2016-04-29', '1', '交换机和房间', '规范的广泛地', '2016-04-11 07:46:54', '规范的广泛地', '1', '4', '13', '5', '4');
INSERT INTO `erp_real_purchase` VALUES ('7', '88888', '2016-04-15', '2016-04-16', '1', '法规的法规', 'hghgfh5464', '2016-04-15 13:54:33', '的范德萨发的', '1', '7', '2', '6', '6');
INSERT INTO `erp_real_purchase` VALUES ('8', '10000', '2016-04-14', '2016-04-30', '1', '', '', '2016-04-22 16:11:57', '', '1', '4', '14', '3', '5');
INSERT INTO `erp_real_purchase` VALUES ('9', '100000', '2016-04-13', '2016-04-23', '1', '', '', '2016-04-26 13:58:58', '', '1', '4', '15', '3', '4');
INSERT INTO `erp_real_purchase` VALUES ('10', '20000', '2016-03-30', '2016-04-23', '1', '', '', '2016-04-26 14:56:41', '', '1', '4', '15', '5', '4');
INSERT INTO `erp_real_purchase` VALUES ('11', '55555', '2016-04-06', '2016-04-16', '1', '', '', '2016-04-26 15:26:13', '', '1', '4', '16', '5', '4');
INSERT INTO `erp_real_purchase` VALUES ('12', '88888', '2016-03-29', '2016-05-07', '1', '', '', '2016-04-26 15:26:42', '', '1', '4', '5', '5', '4');
INSERT INTO `erp_real_purchase` VALUES ('13', '10000', '2016-05-04', '2016-05-20', '1', '', '', '2016-05-13 09:54:49', '', '1', '4', '18', '5', '14');
INSERT INTO `erp_real_purchase` VALUES ('14', '10000', '2016-05-11', '2016-05-12', '1', '', '', '2016-05-16 10:47:40', '', '1', '4', '15', '5', '4');
INSERT INTO `erp_real_purchase` VALUES ('15', '10000', '2016-05-10', '2016-05-12', '1', '', '', '2016-05-25 16:44:34', '', '1', '4', '1', '3', '4');
INSERT INTO `erp_real_purchase` VALUES ('16', '10000', '2016-06-09', '2016-06-17', '3', '', '', '2016-06-07 17:13:44', '', '1', '4', '21', '5', '4');
INSERT INTO `erp_real_purchase` VALUES ('17', '10020', '2016-06-07', '2016-06-09', '2', '', '', '2016-06-07 17:14:26', '', '1', '4', '21', '5', '4');
INSERT INTO `erp_real_purchase` VALUES ('18', '10000', '2016-07-12', '2016-07-07', '1', '', '', '2016-07-19 10:28:21', '', '1', '4', '27', '6', '4');
INSERT INTO `erp_real_purchase` VALUES ('19', '10000', '2016-07-12', '2016-07-13', '1', '', '', '2016-07-19 10:29:14', '', '1', '4', '27', '5', '4');
INSERT INTO `erp_real_purchase` VALUES ('20', '111', '2016-08-04', '2016-08-11', '1', '', '', '2016-08-04 14:59:30', '', '1', '4', '15', '10', '4');
INSERT INTO `erp_real_purchase` VALUES ('21', '11', '2016-08-10', '2016-08-25', '1', '', '', '2016-08-04 14:59:54', '', '1', '4', '27', '10', '4');

-- ----------------------------
-- Table structure for erp_redister_business
-- ----------------------------
DROP TABLE IF EXISTS `erp_redister_business`;
CREATE TABLE `erp_redister_business` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `logo` varchar(100) DEFAULT NULL,
  `business_qrcode` varchar(100) DEFAULT NULL,
  `business_license_original` varchar(100) DEFAULT NULL,
  `business_license_copy` varchar(100) DEFAULT NULL,
  `idCard_positive` varchar(100) DEFAULT NULL,
  `idCard_negative` varchar(100) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `phoneNum` varchar(18) NOT NULL,
  `business_phone` varchar(18) NOT NULL,
  `email` varchar(254) NOT NULL,
  `business_email` varchar(254) DEFAULT NULL,
  `address` varchar(30) NOT NULL,
  `work_address` varchar(18) NOT NULL,
  `register_date` date DEFAULT NULL,
  `contact_name` varchar(20) DEFAULT NULL,
  `contact_position` varchar(20) DEFAULT NULL,
  `brief_introduction` varchar(15) DEFAULT NULL,
  `note` longtext,
  `is_active` tinyint(1) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` varchar(2) NOT NULL,
  `business_type` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `erp_redister_business_user_id_3675fac5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of erp_redister_business
-- ----------------------------
INSERT INTO `erp_redister_business` VALUES ('4', 'business/logo/o4l9z63isq8zszf3ycvsuypjig6ofuv1qcbu6rl6wtqctat9wglpdjtspyl8.jpg', 'business/qrcode/entcwcypg5bue0ungceflhbbfj4zzlmatq3muokudn3ztnzmzpjxvdjixcm7.jpg', 'business/license/wsmfe8nllar9yj355yn6oydq3msautlh204qcks3ved01j8ihq8swoa7xqfc.jpg', 'business/license/a3wn7thcbvohtivjnjfd2oxj5sjsiu6k5lpgqvmfo0uezqizxbjhe0isnwyr.jpg', 'idCard/image/a5rwwjldvplrdu5r2h4c07hadfxa3mdvprju4etwq8wzqgoqopbhp8d2f9m5.jpg', 'idCard/image/xnovzviesiix8wsmm1rpafipsaeq6rryy4w19linw76rl2j3z6zma2xwvocz.jpg', '上海力帆', '18701730286', '21212121', '1668380928@qq.com', '2121212@qq.com', '吉林省白山市靖宇县', 'ddweqdewdew', '2016-07-26', '', '', '', '', '1', '87', '1', '1');
INSERT INTO `erp_redister_business` VALUES ('7', '', '', '', '', '', '', '深圳虎就', '18701730286', '321321321', '1668380928@qq.com', '3213123@qq.com', '内蒙古乌兰察布市商都镇', 'dsadad', '2016-07-26', '', '', '', '', '0', '90', '2', '1');
INSERT INTO `erp_redister_business` VALUES ('11', 'business/logo/omprufp5ste5ur07fnc3c1vqdtjqvvjvr9tixrdpeceup9brzg8wd46kq9rz.jpg', 'business/qrcode/fyk9qdwving1nmgc8bwdyglyufize4oov7xjfrvlyvreodorotmwcgs43zon.jpg', 'business/license/qi9mrcpedq287sy1yxq1zllyezg2u0y13yujzeo3zbpwovrsbxwrr3u2gsl7.jpg', 'business/license/qqyaovfg0yi9ikx7ngp2unrgipxq2gqagg90fapxht4pxvgrgpyhxf9mbedt.jpg', 'idCard/image/nxrjh53qk12uvvrgiacbvjou842v5qdehizbk1rx1v9ueklqddxlcrzbmtzu.jpg', 'idCard/image/zf5z3yhswlylsasooykslje5a9hpsydoobj8wk2edv4fzsdckgxcynekjhdn.jpg', '11111', '18701730286', '400-333-5678', '1668380928@qq.com', null, '江西省新余市分宜镇', '江西省新余市分宜镇', '2016-08-11', null, null, null, null, '1', '114', '1', '1');
INSERT INTO `erp_redister_business` VALUES ('12', 'business/logo/dla8nbzypnylvvdl5qrjmmbt4t7czyijtomgcrbhdmds7re3edyregxrnzgk.jpg', 'business/qrcode/tn7oqzzhda2opgrf93uhjiu53gblh1nley4zzpfa0xup52yb97kxyzmgjlou.jpg', 'business/license/e3ma9x7kclyfsqj3v81hwoi7kuh4ngasfubvx9lchtla1uo7b8gix36ecfus.jpg', 'business/license/tvvnmpjdjf1fheh7nifequnxdnikg43esgs59erua04zpjgmyaooxeje3vgy.jpg', 'idCard/image/temv91naewpzos2rptj3imp6uailxtmdwtplfeghatzgec5dozc43g7motvs.jpg', 'idCard/image/p8fsypiwrtnp4e0yz1jzl1xnbkkiavlboxmnplnurflnfa1kal6plgn80jhv.jpg', '防守打法', '18701730286', '400-234-7687', '1668380928@qq.com', null, '安徽省铜陵市郊区', '发生地方第三方', '2016-08-12', null, null, null, null, '1', '115', '1', '1');
INSERT INTO `erp_redister_business` VALUES ('14', 'business/logo/j4upx9az2tx1kabdgls3djotyyalzz1k7fajlgjphbcbcspc65ypiwhpcwct.jpg', 'business/qrcode/rh3lmtxhviik2nut2rxb0ezlqp9k9sbt2cagydmaz1swd5dojcguztxi1wu7.jpg', 'business/license/rujxjvclo77e5xfdvkix5pfwckgk2m0yujrqkfbdfyidd34aiemiei5gkyvj.jpg', 'business/license/jvqwgd3sitqsifc8i542uvdtcp0knkn2w3gi72oowmjp1fto0x3xkiw8w0yv.jpg', 'idCard/image/atip0xlvkfqsi4dqqffivfctm6jzs6gblxwmc0aj9dpefhr3z2ukhpxw6v2f.png', 'idCard/image/ybzw93m0fv5qi3oqabu56mqxb9hkj637if0r1nuviq9ysods2aavsae6fioq.jpg', 'dfds', '18701730286', '400-34324-432', 'fsdfdsf@qq.com', null, '湖北省恩施州翔凤镇', 'erewrew', '2016-08-15', null, null, null, null, '0', '119', '3', '1');
INSERT INTO `erp_redister_business` VALUES ('15', 'business/logo/aiptaik2hcp0mnoloxassmbtflsh96e8mbowtllysamzbdny2jb3fdtqjtvo.jpg', 'business/qrcode/xcihebral8qoksobm23th1risevl3y3ar7fro5zlpcjbg25tzbd1sliesfwi.png', 'business/license/si5zj9j1phbqqisa04tk7lo7uypjkrnlpai4jw6yhrltxi3xezc9uej9nlov.jpg', 'business/license/afuyopngvrpk6dzjy0hzrlcvpsoox3obnjpinkxt4axyswewyxyspb0hsapq.jpg', 'idCard/image/tnzmlrpuno4izsegcnybxybt19hz1bu4i4dzxs4rsbfksnkibr140egfvq2n.png', 'idCard/image/xassyogyi8lm4xloknwj2ckzbj7fofjyexy5f9zqpkhbks9390o0yh8moa4w.jpg', '的萨达', '18701730286', '400-2345-654', 'dsds@qq.com', null, '浙江省舟山市岱山县', 'rerewrwerwr', '2016-08-16', null, null, null, null, '0', '120', '3', '2');

-- ----------------------------
-- Table structure for oa_all_examine
-- ----------------------------
DROP TABLE IF EXISTS `oa_all_examine`;
CREATE TABLE `oa_all_examine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(10) unsigned NOT NULL,
  `examine_status` varchar(1) NOT NULL,
  `read_status` varchar(1) NOT NULL,
  `examine_message` longtext,
  `is_active` tinyint(1) NOT NULL,
  `examine_time` datetime DEFAULT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `examine_business_id` int(11) DEFAULT NULL,
  `examine_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_all_examin_content_type_id_33721862_fk_django_content_type_id` (`content_type_id`),
  KEY `oa_all_examine_examine_business_id_361913f2_fk_erp_business_id` (`examine_business_id`),
  KEY `oa_all_examine_examine_user_id_7e7802c7_fk_auth_user_id` (`examine_user_id`),
  CONSTRAINT `oa_all_examine_examine_business_id_361913f2_fk_erp_business_id` FOREIGN KEY (`examine_business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_all_examine_examine_user_id_7e7802c7_fk_auth_user_id` FOREIGN KEY (`examine_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `oa_all_examin_content_type_id_33721862_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_all_examine
-- ----------------------------
INSERT INTO `oa_all_examine` VALUES ('8', '1', '3', '1', null, '1', '2016-05-27 16:01:06', '31', '4', '17');
INSERT INTO `oa_all_examine` VALUES ('9', '1', '3', '1', '匹配', '1', '2016-07-19 14:16:42', '31', '4', '21');
INSERT INTO `oa_all_examine` VALUES ('14', '1', '1', '2', '给对方', '1', '2016-07-28 15:50:27', '34', '4', '21');
INSERT INTO `oa_all_examine` VALUES ('15', '1', '3', '1', null, '1', '2016-05-27 16:01:06', '34', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('16', '2', '2', '2', 'weweqe', '1', '2016-08-05 10:37:57', '32', '4', '21');
INSERT INTO `oa_all_examine` VALUES ('17', '2', '3', '1', null, '1', '2016-05-27 16:01:06', '32', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('18', '3', '3', '1', null, '1', '2016-05-27 16:01:06', '32', '6', '52');
INSERT INTO `oa_all_examine` VALUES ('19', '3', '3', '1', null, '1', '2016-05-27 16:01:06', '32', '6', '53');
INSERT INTO `oa_all_examine` VALUES ('22', '4', '3', '1', null, '1', '2016-06-03 11:14:47', '31', '7', '75');
INSERT INTO `oa_all_examine` VALUES ('23', '4', '3', '1', null, '1', '2016-06-03 11:14:47', '31', '7', '76');
INSERT INTO `oa_all_examine` VALUES ('24', '4', '3', '1', null, '1', '2016-06-03 17:36:28', '32', '7', '75');
INSERT INTO `oa_all_examine` VALUES ('25', '4', '3', '1', null, '1', '2016-06-03 17:36:28', '32', '7', '76');
INSERT INTO `oa_all_examine` VALUES ('26', '2', '3', '1', null, '1', '2016-06-03 17:43:26', '34', '7', '75');
INSERT INTO `oa_all_examine` VALUES ('27', '2', '3', '1', null, '1', '2016-06-03 17:43:26', '34', '7', '76');
INSERT INTO `oa_all_examine` VALUES ('28', '2', '3', '1', null, '1', '2016-06-03 17:44:26', '33', '7', '75');
INSERT INTO `oa_all_examine` VALUES ('29', '2', '3', '1', null, '1', '2016-06-03 17:44:26', '33', '7', '76');
INSERT INTO `oa_all_examine` VALUES ('31', '3', '3', '1', 'fsdfsd', '1', '2016-06-27 09:47:03', '33', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('32', '5', '3', '1', '个梵蒂冈地方', '1', '2016-06-03 17:59:52', '32', '4', '21');
INSERT INTO `oa_all_examine` VALUES ('36', '6', '3', '1', null, '1', null, '31', '4', '66');
INSERT INTO `oa_all_examine` VALUES ('37', '6', '3', '1', null, '1', null, '32', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('39', '3', '3', '1', null, '1', null, '34', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('40', '7', '3', '1', '', '1', '2016-06-24 16:05:15', '32', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('41', '7', '3', '1', null, '1', null, '32', '4', '66');
INSERT INTO `oa_all_examine` VALUES ('42', '4', '3', '1', null, '1', null, '33', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('43', '4', '3', '1', null, '1', null, '34', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('44', '7', '3', '1', null, '1', null, '31', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('45', '8', '3', '1', null, '1', null, '31', '4', '40');
INSERT INTO `oa_all_examine` VALUES ('46', '5', '3', '1', null, '1', null, '33', '4', '40');

-- ----------------------------
-- Table structure for oa_checkwork
-- ----------------------------
DROP TABLE IF EXISTS `oa_checkwork`;
CREATE TABLE `oa_checkwork` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abscissa` varchar(30) NOT NULL,
  `ordinate` varchar(30) NOT NULL,
  `check_time` datetime NOT NULL,
  `check_user_id` int(11) NOT NULL,
  `check_business_id` int(11) NOT NULL,
  `address` varchar(300) DEFAULT NULL,
  `area` varchar(300) DEFAULT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oa_checkwork_check_user_id_85979d0_uniq` (`check_user_id`),
  KEY `oa_checkwork_31c9cbe0` (`check_business_id`),
  CONSTRAINT `oa_checkwork_check_business_id_3a32c5c5_fk_erp_business_id` FOREIGN KEY (`check_business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_checkwork_check_user_id_85979d0_fk_auth_user_id` FOREIGN KEY (`check_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_checkwork
-- ----------------------------
INSERT INTO `oa_checkwork` VALUES ('1', '121.525372', '31.233468', '2016-05-24 16:16:00', '21', '4', '上海市浦东新区张杨路630号', '八佰伴,东方路,潍坊', '1');
INSERT INTO `oa_checkwork` VALUES ('2', '121.525362', '31.233489', '2016-05-17 16:19:00', '40', '4', '上海市浦东新区张杨路630号', '八佰伴,东方路,潍坊', '1');

-- ----------------------------
-- Table structure for oa_checkwork_history
-- ----------------------------
DROP TABLE IF EXISTS `oa_checkwork_history`;
CREATE TABLE `oa_checkwork_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abscissa` varchar(30) NOT NULL,
  `ordinate` varchar(30) NOT NULL,
  `check_time` datetime NOT NULL,
  `check_business_history_id` int(11) NOT NULL,
  `check_history_id` int(11) NOT NULL,
  `address` varchar(300) DEFAULT NULL,
  `area` varchar(300) DEFAULT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_checkwo_check_business_history_id_5282e001_fk_erp_business_id` (`check_business_history_id`),
  KEY `oa_checkwork_history_check_history_id_75f79ee9_fk_auth_user_id` (`check_history_id`),
  CONSTRAINT `oa_checkwork_history_check_history_id_75f79ee9_fk_auth_user_id` FOREIGN KEY (`check_history_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `oa_checkwo_check_business_history_id_5282e001_fk_erp_business_id` FOREIGN KEY (`check_business_history_id`) REFERENCES `erp_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_checkwork_history
-- ----------------------------
INSERT INTO `oa_checkwork_history` VALUES ('1', '121.525345', '31.233489', '2016-05-24 03:57:00', '4', '21', '上海市浦东新区张杨路630号', '八佰伴,东方路,潍坊', '1');
INSERT INTO `oa_checkwork_history` VALUES ('2', '121.525862', '31.257889', '2016-05-24 08:55:00', '4', '21', '上海市浦东新区张杨路630号', '八佰伴,东方路,潍坊', '1');
INSERT INTO `oa_checkwork_history` VALUES ('3', '121.524562', '31.233489', '2016-06-01 00:00:00', '4', '21', '地方地方', '个非官方个', '1');
INSERT INTO `oa_checkwork_history` VALUES ('4', '121.525362', '31.233489', '2016-05-24 00:00:00', '4', '21', '佛挡杀佛', '会很反感', '1');
INSERT INTO `oa_checkwork_history` VALUES ('5', '121.525362', '121.525362', '2016-06-01 00:00:00', '4', '66', '发烧', '公告', '1');
INSERT INTO `oa_checkwork_history` VALUES ('6', '121.525362', '121.525362', '2016-06-01 09:01:00', '4', '40', '发生大幅度', '郭德纲', '0');
INSERT INTO `oa_checkwork_history` VALUES ('7', '121.525362', '121.525362', '2016-07-01 03:04:00', '4', '21', '佛挡杀佛幅度', '范德萨发生', '1');
INSERT INTO `oa_checkwork_history` VALUES ('8', '121.525362', '31.233489', '2016-06-02 13:41:00', '4', '21', '海市浦东新区张杨路630号', '八佰伴,东方路,潍坊', '0');

-- ----------------------------
-- Table structure for oa_check_time_setting
-- ----------------------------
DROP TABLE IF EXISTS `oa_check_time_setting`;
CREATE TABLE `oa_check_time_setting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `check_in_time` time NOT NULL,
  `check_out_time` time NOT NULL,
  `check_in_remind` time NOT NULL,
  `check_out_remind` time NOT NULL,
  `business_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_check_time_setting_business_id_5ef5dd5f_fk_erp_business_id` (`business_id`),
  CONSTRAINT `oa_check_time_setting_business_id_5ef5dd5f_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_check_time_setting
-- ----------------------------
INSERT INTO `oa_check_time_setting` VALUES ('1', '15:00:00', '18:44:00', '07:50:00', '17:50:00', '4');
INSERT INTO `oa_check_time_setting` VALUES ('2', '06:30:16', '09:00:16', '07:55:16', '04:25:16', '7');
INSERT INTO `oa_check_time_setting` VALUES ('11', '09:00:02', '17:30:02', '13:30:02', '12:50:02', '13');

-- ----------------------------
-- Table structure for oa_cost_application
-- ----------------------------
DROP TABLE IF EXISTS `oa_cost_application`;
CREATE TABLE `oa_cost_application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(20) NOT NULL,
  `content` varchar(100) NOT NULL,
  `cost` bigint(20) NOT NULL,
  `time` datetime NOT NULL,
  `business_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_cost_application_business_id_437894b4_fk_erp_business_id` (`business_id`),
  KEY `oa_cost_application_user_id_91f8f09_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oa_cost_application_business_id_437894b4_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_cost_application_user_id_91f8f09_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_cost_application
-- ----------------------------
INSERT INTO `oa_cost_application` VALUES ('2', '发生的发生法', '发送到发送到', '10000', '2016-05-26 14:04:32', '4', '40', '1');
INSERT INTO `oa_cost_application` VALUES ('3', '发大水发大水发', '范德萨发斯蒂芬', '10000', '2016-05-26 14:30:59', '6', '52', '1');
INSERT INTO `oa_cost_application` VALUES ('4', '给梵蒂冈梵蒂冈浮动', '梵蒂冈梵蒂冈地方官', '10000', '2016-06-03 17:36:28', '7', '26', '1');
INSERT INTO `oa_cost_application` VALUES ('5', '范德萨发生的', '范德萨发斯蒂芬', '1111', '2016-06-03 17:57:48', '4', '40', '1');
INSERT INTO `oa_cost_application` VALUES ('6', '发生的发生', '放松放松的放松的', '11111', '2016-06-07 14:05:34', '4', '21', '1');
INSERT INTO `oa_cost_application` VALUES ('7', '第三方第三方', '发生的房顶上', '1111', '2016-06-15 15:08:20', '4', '21', '1');

-- ----------------------------
-- Table structure for oa_cost_application_examine_user
-- ----------------------------
DROP TABLE IF EXISTS `oa_cost_application_examine_user`;
CREATE TABLE `oa_cost_application_examine_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cost_application_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cost_application_id` (`cost_application_id`,`user_id`),
  KEY `oa_cost_application_examine_use_user_id_18963890_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oa_cost_application_examine_use_user_id_18963890_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `oa_cost_a_cost_application_id_565cc8ab_fk_oa_cost_application_id` FOREIGN KEY (`cost_application_id`) REFERENCES `oa_cost_application` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_cost_application_examine_user
-- ----------------------------
INSERT INTO `oa_cost_application_examine_user` VALUES ('4', '2', '21');
INSERT INTO `oa_cost_application_examine_user` VALUES ('3', '2', '40');
INSERT INTO `oa_cost_application_examine_user` VALUES ('5', '3', '52');
INSERT INTO `oa_cost_application_examine_user` VALUES ('6', '3', '53');
INSERT INTO `oa_cost_application_examine_user` VALUES ('7', '4', '75');
INSERT INTO `oa_cost_application_examine_user` VALUES ('8', '4', '76');
INSERT INTO `oa_cost_application_examine_user` VALUES ('9', '5', '21');
INSERT INTO `oa_cost_application_examine_user` VALUES ('10', '6', '40');
INSERT INTO `oa_cost_application_examine_user` VALUES ('11', '7', '40');
INSERT INTO `oa_cost_application_examine_user` VALUES ('12', '7', '66');

-- ----------------------------
-- Table structure for oa_cost_examine
-- ----------------------------
DROP TABLE IF EXISTS `oa_cost_examine`;
CREATE TABLE `oa_cost_examine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `examine_status` varchar(1) NOT NULL,
  `examine_message` longtext,
  `examine_time` datetime DEFAULT NULL,
  `cost_examine_id` int(11) NOT NULL,
  `examine_business_id` int(11) DEFAULT NULL,
  `examine_user_id` int(11) DEFAULT NULL,
  `read_status` varchar(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_cost_examine_f63c3eaf` (`cost_examine_id`),
  KEY `oa_cost_examine_1125bdbb` (`examine_business_id`),
  KEY `oa_cost_examine_236973b7` (`examine_user_id`),
  CONSTRAINT `oa_cost_examine_examine_business_id_e038c19_fk_erp_business_id` FOREIGN KEY (`examine_business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_cost_examine_examine_user_id_735318ec_fk_auth_user_id` FOREIGN KEY (`examine_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `oa_cost_exami_cost_examine_id_2b19a192_fk_oa_cost_application_id` FOREIGN KEY (`cost_examine_id`) REFERENCES `oa_cost_application` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_cost_examine
-- ----------------------------

-- ----------------------------
-- Table structure for oa_daily_to_do
-- ----------------------------
DROP TABLE IF EXISTS `oa_daily_to_do`;
CREATE TABLE `oa_daily_to_do` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(30) NOT NULL,
  `content` varchar(100) NOT NULL,
  `remark` longtext,
  `add_time` datetime NOT NULL,
  `todo_user_id` int(11) DEFAULT NULL,
  `to_do_time` datetime NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_daily_to_do_todo_user_id_5c8a1cc5_fk_auth_user_id` (`todo_user_id`),
  CONSTRAINT `oa_daily_to_do_todo_user_id_5c8a1cc5_fk_auth_user_id` FOREIGN KEY (`todo_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_daily_to_do
-- ----------------------------
INSERT INTO `oa_daily_to_do` VALUES ('1', '分国芳蛋糕房的', '和电话法国和法国', '<p>爆发的规划梵蒂冈地方和奋斗</p>', '2016-06-02 17:53:46', '17', '2016-06-01 10:15:00', '1');
INSERT INTO `oa_daily_to_do` VALUES ('2', '太阳太阳日太阳', '鬼地方三国杀', '<p>发的发生的发生的发生</p>', '2016-06-02 17:54:00', '17', '2016-06-01 09:30:00', '1');
INSERT INTO `oa_daily_to_do` VALUES ('3', '规范和规划', '和法国和法国', '<p>和法国和法国火锅</p>', '2016-06-02 17:55:21', '17', '2016-06-09 04:10:00', '0');
INSERT INTO `oa_daily_to_do` VALUES ('4', '规定发光飞碟', '鬼地方个地方', '<p>个梵蒂冈地方</p>', '2016-06-02 18:01:02', '17', '2016-06-13 07:00:00', '1');
INSERT INTO `oa_daily_to_do` VALUES ('5', '和法国和法国', '的范德萨范德萨', '<p>发生的房顶上</p>', '2016-06-02 18:02:00', '17', '2016-05-30 00:00:00', '1');
INSERT INTO `oa_daily_to_do` VALUES ('6', '规范的广泛地梵蒂冈', '地大声大声道', '<p>的撒的撒打算</p>', '2016-06-03 10:19:56', '25', '2016-06-07 02:05:00', '1');
INSERT INTO `oa_daily_to_do` VALUES ('7', '分地方v', '佛挡杀佛好', '<p>发生地方地方</p>', '2016-06-12 16:56:32', '21', '2016-05-31 01:00:00', '1');
INSERT INTO `oa_daily_to_do` VALUES ('8', '发大水发大水发', '范德萨范德萨发生的', '<p>发生的发生地方的</p>', '2016-06-15 13:50:57', '21', '2016-06-09 04:10:00', '0');
INSERT INTO `oa_daily_to_do` VALUES ('9', '和规范化法', '发生发生地方', '<p>范德萨发生的</p>', '2016-06-15 14:04:10', '21', '2016-05-31 01:00:00', '1');
INSERT INTO `oa_daily_to_do` VALUES ('10', '发生的发生', '发送到发送到', '<p>发的发生地方</p>', '2016-06-15 14:11:18', '1', '2016-05-30 01:45:00', '1');
INSERT INTO `oa_daily_to_do` VALUES ('11', '111', '111', '<p>111</p>', '2016-06-27 11:51:31', '21', '2016-06-01 03:10:00', '0');
INSERT INTO `oa_daily_to_do` VALUES ('12', '1111', '111', '<p>111</p>', '2016-06-27 11:56:08', '21', '2016-06-21 08:25:00', '0');
INSERT INTO `oa_daily_to_do` VALUES ('13', '11', '111', '', '2016-07-19 11:25:13', '21', '2016-06-27 01:05:05', '0');
INSERT INTO `oa_daily_to_do` VALUES ('14', '44444', '44444', '<p>444</p>', '2016-08-04 15:27:08', '21', '2016-08-10 02:05:59', '0');

-- ----------------------------
-- Table structure for oa_daily_work
-- ----------------------------
DROP TABLE IF EXISTS `oa_daily_work`;
CREATE TABLE `oa_daily_work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `business_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `content` varchar(300) NOT NULL,
  `topic` varchar(300) NOT NULL,
  `work_type` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_daily_work_business_id_7839625f_fk_erp_business_id` (`business_id`),
  KEY `oa_daily_work_user_id_10e35e84_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oa_daily_work_business_id_7839625f_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_daily_work_user_id_10e35e84_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_daily_work
-- ----------------------------
INSERT INTO `oa_daily_work` VALUES ('1', '2016-05-25 13:43:17', '4', '17', '1', '发的范德萨范德萨', '给梵蒂冈梵蒂冈', '1');
INSERT INTO `oa_daily_work` VALUES ('4', '2016-06-03 11:14:47', '7', '26', '1', '发地方第三方第三方', '第三方第三方斯蒂芬', '2');
INSERT INTO `oa_daily_work` VALUES ('6', '2016-06-07 13:25:27', '4', '21', '1', '发生地方第三方', '发的发生的', '1');
INSERT INTO `oa_daily_work` VALUES ('7', '2016-06-24 10:08:51', '4', '21', '1', '54535555555555555555555555555555555555555555555555555555555555555555', '454354543555555555555555555555555555555555555555555555555555555555', '1');
INSERT INTO `oa_daily_work` VALUES ('8', '2016-06-24 11:54:06', '4', '21', '1', '热热热热污染物热热我惹我热热', '热热污染费绯闻绯闻访问费绯闻绯闻绯闻绯闻绯闻', '1');

-- ----------------------------
-- Table structure for oa_daily_work_examine_user
-- ----------------------------
DROP TABLE IF EXISTS `oa_daily_work_examine_user`;
CREATE TABLE `oa_daily_work_examine_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `daily_work_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `daily_work_id` (`daily_work_id`,`user_id`),
  KEY `oa_daily_work_examine_user_user_id_24b001e9_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oa_daily_work_examine_daily_work_id_416fe555_fk_oa_daily_work_id` FOREIGN KEY (`daily_work_id`) REFERENCES `oa_daily_work` (`id`),
  CONSTRAINT `oa_daily_work_examine_user_user_id_24b001e9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_daily_work_examine_user
-- ----------------------------
INSERT INTO `oa_daily_work_examine_user` VALUES ('1', '1', '17');
INSERT INTO `oa_daily_work_examine_user` VALUES ('2', '1', '21');
INSERT INTO `oa_daily_work_examine_user` VALUES ('7', '4', '75');
INSERT INTO `oa_daily_work_examine_user` VALUES ('8', '4', '76');
INSERT INTO `oa_daily_work_examine_user` VALUES ('11', '6', '66');
INSERT INTO `oa_daily_work_examine_user` VALUES ('12', '7', '40');
INSERT INTO `oa_daily_work_examine_user` VALUES ('13', '8', '40');

-- ----------------------------
-- Table structure for oa_internal_announcement
-- ----------------------------
DROP TABLE IF EXISTS `oa_internal_announcement`;
CREATE TABLE `oa_internal_announcement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(30) NOT NULL,
  `content` longtext,
  `on_top` varchar(1) NOT NULL,
  `onTop_start` date DEFAULT NULL,
  `onTop_end` date DEFAULT NULL,
  `publish` varchar(1) NOT NULL,
  `publish_start` date DEFAULT NULL,
  `publish_end` date DEFAULT NULL,
  `add_time` date NOT NULL,
  `announcement_business_id` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_internal_announcement_business_id_1cb811ab_fk_erp_business_id` (`announcement_business_id`),
  CONSTRAINT `oa_internal_announcement_business_id_1cb811ab_fk_erp_business_id` FOREIGN KEY (`announcement_business_id`) REFERENCES `erp_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_internal_announcement
-- ----------------------------
INSERT INTO `oa_internal_announcement` VALUES ('1', '给对方', '<p>vvcvxcv</p>', '1', '2016-06-08', '2016-07-01', '1', '2016-06-15', '2016-06-17', '2016-06-02', '4', '1');
INSERT INTO `oa_internal_announcement` VALUES ('2', '范德萨发生的', '<p>的发生的发生的发生</p>', '1', '2016-06-02', '2016-06-17', '1', '2016-06-15', '2016-06-25', '2016-06-03', '4', '1');
INSERT INTO `oa_internal_announcement` VALUES ('3', '看环境空间和', '<p>vfdvfd</p>', '1', '2016-05-31', '2016-06-09', '1', '2016-06-01', '2016-07-08', '2016-06-03', '7', '1');
INSERT INTO `oa_internal_announcement` VALUES ('4', '111', '<p>111</p>', '1', '2016-06-07', '2016-06-07', '1', '1899-12-13', '2016-06-20', '2016-06-12', '4', '1');
INSERT INTO `oa_internal_announcement` VALUES ('5', '1111', '', '1', '2016-06-22', '2016-06-29', '1', '2016-06-22', '2016-06-15', '2016-06-15', '4', '1');
INSERT INTO `oa_internal_announcement` VALUES ('6', '333', '', '1', '2016-06-08', '2016-06-08', '1', '1899-11-28', '2016-06-07', '2016-06-15', '4', '1');
INSERT INTO `oa_internal_announcement` VALUES ('7', '但是', '', '1', '2016-07-13', '2016-07-22', '1', '2016-07-13', '2016-07-14', '2016-06-24', '4', '1');
INSERT INTO `oa_internal_announcement` VALUES ('8', '111', '', '1', null, null, '1', null, null, '2016-07-19', '4', '0');
INSERT INTO `oa_internal_announcement` VALUES ('9', '88888', '<p>88888</p>', '1', '2016-08-22', '2016-09-01', '1', '2016-08-09', '2016-08-24', '2016-08-04', '4', '0');
INSERT INTO `oa_internal_announcement` VALUES ('10', '787878', '<p>878787</p>', '1', '1899-12-05', '2016-08-09', '1', '2016-08-14', '2016-08-24', '2016-08-04', '4', '0');

-- ----------------------------
-- Table structure for oa_leave_examine
-- ----------------------------
DROP TABLE IF EXISTS `oa_leave_examine`;
CREATE TABLE `oa_leave_examine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `examine_status` varchar(1) NOT NULL,
  `read_status` varchar(1) NOT NULL,
  `examine_message` longtext,
  `is_active` tinyint(1) NOT NULL,
  `examine_time` datetime DEFAULT NULL,
  `examine_business_id` int(11) DEFAULT NULL,
  `examine_user_id` int(11) DEFAULT NULL,
  `leave_examine_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_leave_examine_examine_business_id_7b1eda68_fk_erp_business_id` (`examine_business_id`),
  KEY `oa_leave_examine_examine_user_id_392de42d_fk_auth_user_id` (`examine_user_id`),
  KEY `oa_leave_exa_leave_examine_id_7f57ceb6_fk_oa_leave_management_id` (`leave_examine_id`),
  CONSTRAINT `oa_leave_examine_examine_business_id_7b1eda68_fk_erp_business_id` FOREIGN KEY (`examine_business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_leave_examine_examine_user_id_392de42d_fk_auth_user_id` FOREIGN KEY (`examine_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `oa_leave_exa_leave_examine_id_7f57ceb6_fk_oa_leave_management_id` FOREIGN KEY (`leave_examine_id`) REFERENCES `oa_leave_management` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_leave_examine
-- ----------------------------

-- ----------------------------
-- Table structure for oa_leave_management
-- ----------------------------
DROP TABLE IF EXISTS `oa_leave_management`;
CREATE TABLE `oa_leave_management` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(20) NOT NULL,
  `content` varchar(100) NOT NULL,
  `start` date NOT NULL,
  `end` date NOT NULL,
  `time` datetime NOT NULL,
  `business_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_leave_management_business_id_259b30bd_fk_erp_business_id` (`business_id`),
  KEY `oa_leave_management_user_id_f8fb2ee_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oa_leave_management_business_id_259b30bd_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_leave_management_user_id_f8fb2ee_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_leave_management
-- ----------------------------
INSERT INTO `oa_leave_management` VALUES ('2', '和法国恢复', '和法国和法国合肥', '2016-05-31', '2016-06-10', '2016-06-03 17:44:26', '7', '26', '1');
INSERT INTO `oa_leave_management` VALUES ('3', '范德萨范德萨', '交换机和国际刚', '2016-06-08', '2016-06-18', '2016-06-03 17:49:44', '4', '21', '1');
INSERT INTO `oa_leave_management` VALUES ('4', '大幅度', '发地方地方', '2016-06-05', '2016-06-10', '2016-06-15 15:24:33', '4', '21', '1');
INSERT INTO `oa_leave_management` VALUES ('5', '的撒打算', '的撒大大', '2016-05-30', '2016-06-08', '2016-06-24 16:03:46', '4', '21', '1');

-- ----------------------------
-- Table structure for oa_leave_management_examine_user
-- ----------------------------
DROP TABLE IF EXISTS `oa_leave_management_examine_user`;
CREATE TABLE `oa_leave_management_examine_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `leave_management_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `leave_management_id` (`leave_management_id`,`user_id`),
  KEY `oa_leave_management_examine_use_user_id_42da893b_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oa_leave_management_examine_use_user_id_42da893b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `oa_leave__leave_management_id_36e9e667_fk_oa_leave_management_id` FOREIGN KEY (`leave_management_id`) REFERENCES `oa_leave_management` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_leave_management_examine_user
-- ----------------------------
INSERT INTO `oa_leave_management_examine_user` VALUES ('4', '2', '75');
INSERT INTO `oa_leave_management_examine_user` VALUES ('5', '2', '76');
INSERT INTO `oa_leave_management_examine_user` VALUES ('6', '3', '40');
INSERT INTO `oa_leave_management_examine_user` VALUES ('8', '4', '40');
INSERT INTO `oa_leave_management_examine_user` VALUES ('9', '5', '40');

-- ----------------------------
-- Table structure for oa_read_message
-- ----------------------------
DROP TABLE IF EXISTS `oa_read_message`;
CREATE TABLE `oa_read_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model_name` varchar(30) DEFAULT NULL,
  `record_id` int(11) DEFAULT NULL,
  `read_time` datetime NOT NULL,
  `read_business_id` int(11) DEFAULT NULL,
  `read_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_read_message_read_business_id_20a5bfb6_fk_erp_business_id` (`read_business_id`),
  KEY `oa_read_message_read_user_id_15c4c825_fk_auth_user_id` (`read_user_id`),
  CONSTRAINT `oa_read_message_read_business_id_20a5bfb6_fk_erp_business_id` FOREIGN KEY (`read_business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_read_message_read_user_id_15c4c825_fk_auth_user_id` FOREIGN KEY (`read_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_read_message
-- ----------------------------
INSERT INTO `oa_read_message` VALUES ('1', 'announcement', '16', '2016-05-20 13:30:27', '4', '17');
INSERT INTO `oa_read_message` VALUES ('2', 'announcement', '1', '2016-05-20 13:31:57', '4', '17');
INSERT INTO `oa_read_message` VALUES ('3', 'announcement', '3', '2016-05-20 13:32:02', '4', '17');
INSERT INTO `oa_read_message` VALUES ('4', 'announcement', '3', '2016-05-26 14:38:47', null, '1');
INSERT INTO `oa_read_message` VALUES ('5', 'announcement', '55', '2016-06-01 16:42:42', '4', '21');
INSERT INTO `oa_read_message` VALUES ('6', 'announcement', '58', '2016-06-01 16:44:16', '4', '21');
INSERT INTO `oa_read_message` VALUES ('7', 'announcement', '8', '2016-06-02 10:29:32', null, '1');
INSERT INTO `oa_read_message` VALUES ('8', 'internal_announcement', '1', '2016-06-02 10:49:09', '4', '17');
INSERT INTO `oa_read_message` VALUES ('9', 'internal_announcement', '1', '2016-06-02 11:06:16', '4', '21');
INSERT INTO `oa_read_message` VALUES ('10', 'announcement', '54', '2016-06-02 13:24:31', '4', '17');
INSERT INTO `oa_read_message` VALUES ('11', 'announcement', '7', '2016-06-02 15:17:05', null, '1');
INSERT INTO `oa_read_message` VALUES ('12', 'announcement', '55', '2016-06-03 09:45:29', '4', '17');
INSERT INTO `oa_read_message` VALUES ('13', 'announcement', '4', '2016-06-03 09:45:40', '7', '25');
INSERT INTO `oa_read_message` VALUES ('14', 'announcement', '55', '2016-06-03 09:45:49', '7', '25');
INSERT INTO `oa_read_message` VALUES ('15', 'announcement', '6', '2016-06-03 09:54:08', '7', '25');
INSERT INTO `oa_read_message` VALUES ('16', 'announcement', '6', '2016-06-03 09:56:50', null, '1');
INSERT INTO `oa_read_message` VALUES ('17', 'announcement', '16', '2016-06-03 09:56:59', null, '1');
INSERT INTO `oa_read_message` VALUES ('18', 'internal_announcement', '3', '2016-06-03 10:07:07', '7', '25');
INSERT INTO `oa_read_message` VALUES ('19', 'internal_announcement', '3', '2016-06-03 10:07:31', null, '1');
INSERT INTO `oa_read_message` VALUES ('20', 'internal_announcement', '1', '2016-06-03 10:07:34', null, '1');
INSERT INTO `oa_read_message` VALUES ('21', 'internal_announcement', '2', '2016-06-06 15:59:01', '4', '21');
INSERT INTO `oa_read_message` VALUES ('22', 'internal_announcement', '2', '2016-06-07 11:38:44', '4', '17');
INSERT INTO `oa_read_message` VALUES ('23', 'announcement', '66', '2016-06-13 13:24:12', '4', '21');
INSERT INTO `oa_read_message` VALUES ('24', 'announcement', '54', '2016-06-13 17:06:54', '4', '21');
INSERT INTO `oa_read_message` VALUES ('25', 'internal_announcement', '6', '2016-06-15 14:48:48', '4', '21');
INSERT INTO `oa_read_message` VALUES ('26', 'announcement', '7', '2016-06-16 11:25:59', '7', '25');
INSERT INTO `oa_read_message` VALUES ('27', 'announcement', '16', '2016-06-16 14:14:17', '4', '21');
INSERT INTO `oa_read_message` VALUES ('28', 'announcement', '67', '2016-06-22 15:57:57', '4', '21');
INSERT INTO `oa_read_message` VALUES ('29', 'announcement', '67', '2016-07-18 11:12:32', '4', '17');
INSERT INTO `oa_read_message` VALUES ('30', 'announcement', '67', '2016-07-28 14:13:46', '4', '40');
INSERT INTO `oa_read_message` VALUES ('31', 'announcement', '66', '2016-07-28 14:33:36', '4', '40');
INSERT INTO `oa_read_message` VALUES ('32', 'announcement', '54', '2016-07-28 14:42:32', '4', '40');
INSERT INTO `oa_read_message` VALUES ('33', 'announcement', '67', '2016-09-02 10:47:37', null, '1');
INSERT INTO `oa_read_message` VALUES ('34', 'announcement', '66', '2016-09-02 15:09:49', '4', '17');
INSERT INTO `oa_read_message` VALUES ('35', 'announcement', '56', '2016-09-02 15:09:57', '4', '17');

-- ----------------------------
-- Table structure for oa_travel_apply
-- ----------------------------
DROP TABLE IF EXISTS `oa_travel_apply`;
CREATE TABLE `oa_travel_apply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(30) NOT NULL,
  `content` varchar(30) NOT NULL,
  `cost` bigint(20) NOT NULL,
  `start` date NOT NULL,
  `end` date NOT NULL,
  `time` datetime NOT NULL,
  `business_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_travel_apply_business_id_2ec3011b_fk_erp_business_id` (`business_id`),
  KEY `oa_travel_apply_user_id_4688fe8a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oa_travel_apply_business_id_2ec3011b_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_travel_apply_user_id_4688fe8a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_travel_apply
-- ----------------------------
INSERT INTO `oa_travel_apply` VALUES ('1', '放松放松的', '范德萨发生的', '10000', '2016-05-04', '2016-05-12', '2016-05-26 13:56:51', '4', '40', '1');
INSERT INTO `oa_travel_apply` VALUES ('2', '官方大哥大法官', '个梵蒂冈地方鬼地方', '1000', '2016-06-02', '2016-06-11', '2016-06-03 17:43:26', '7', '26', '1');
INSERT INTO `oa_travel_apply` VALUES ('3', '范德萨发生的', '符合规范化股份', '11111', '2016-05-31', '2016-06-23', '2016-06-07 15:23:12', '4', '21', '1');
INSERT INTO `oa_travel_apply` VALUES ('4', '的三大山东省', '大大大叔', '1111', '2016-06-01', '2016-06-15', '2016-06-15 15:44:18', '4', '21', '1');

-- ----------------------------
-- Table structure for oa_travel_apply_examine_user
-- ----------------------------
DROP TABLE IF EXISTS `oa_travel_apply_examine_user`;
CREATE TABLE `oa_travel_apply_examine_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `travel_apply_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `travel_apply_id` (`travel_apply_id`,`user_id`),
  KEY `oa_travel_apply_examine_user_user_id_7cc9b0b5_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oa_travel_apply_examine_user_user_id_7cc9b0b5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `oa_travel_apply_e_travel_apply_id_13218ef9_fk_oa_travel_apply_id` FOREIGN KEY (`travel_apply_id`) REFERENCES `oa_travel_apply` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_travel_apply_examine_user
-- ----------------------------
INSERT INTO `oa_travel_apply_examine_user` VALUES ('2', '1', '21');
INSERT INTO `oa_travel_apply_examine_user` VALUES ('1', '1', '40');
INSERT INTO `oa_travel_apply_examine_user` VALUES ('3', '2', '75');
INSERT INTO `oa_travel_apply_examine_user` VALUES ('4', '2', '76');
INSERT INTO `oa_travel_apply_examine_user` VALUES ('5', '3', '40');
INSERT INTO `oa_travel_apply_examine_user` VALUES ('6', '4', '40');

-- ----------------------------
-- Table structure for oa_travel_examine
-- ----------------------------
DROP TABLE IF EXISTS `oa_travel_examine`;
CREATE TABLE `oa_travel_examine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `examine_status` varchar(1) NOT NULL,
  `read_status` varchar(1) NOT NULL,
  `examine_message` longtext,
  `is_active` tinyint(1) NOT NULL,
  `examine_time` datetime DEFAULT NULL,
  `examine_business_id` int(11) DEFAULT NULL,
  `examine_user_id` int(11) DEFAULT NULL,
  `travel_examine_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oa_travel_examine_examine_business_id_14c925a_fk_erp_business_id` (`examine_business_id`),
  KEY `oa_travel_examine_examine_user_id_4c26aba1_fk_auth_user_id` (`examine_user_id`),
  KEY `oa_travel_examin_travel_examine_id_2209caa_fk_oa_travel_apply_id` (`travel_examine_id`),
  CONSTRAINT `oa_travel_examine_examine_business_id_14c925a_fk_erp_business_id` FOREIGN KEY (`examine_business_id`) REFERENCES `erp_business` (`id`),
  CONSTRAINT `oa_travel_examine_examine_user_id_4c26aba1_fk_auth_user_id` FOREIGN KEY (`examine_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `oa_travel_examin_travel_examine_id_2209caa_fk_oa_travel_apply_id` FOREIGN KEY (`travel_examine_id`) REFERENCES `oa_travel_apply` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oa_travel_examine
-- ----------------------------

-- ----------------------------
-- Table structure for postman_message
-- ----------------------------
DROP TABLE IF EXISTS `postman_message`;
CREATE TABLE `postman_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(120) NOT NULL,
  `body` longtext NOT NULL,
  `email` varchar(254) NOT NULL,
  `sent_at` datetime NOT NULL,
  `read_at` datetime DEFAULT NULL,
  `replied_at` datetime DEFAULT NULL,
  `sender_archived` tinyint(1) NOT NULL,
  `recipient_archived` tinyint(1) NOT NULL,
  `sender_deleted_at` datetime DEFAULT NULL,
  `recipient_deleted_at` datetime DEFAULT NULL,
  `moderation_status` varchar(1) NOT NULL,
  `moderation_date` datetime DEFAULT NULL,
  `moderation_reason` varchar(120) NOT NULL,
  `moderation_by_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `recipient_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `thread_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `postman_message_moderation_by_id_2b7e279e_fk_auth_user_id` (`moderation_by_id`),
  KEY `postman_message_parent_id_5b8df4a5_fk_postman_message_id` (`parent_id`),
  KEY `postman_message_recipient_id_d52aeab_fk_auth_user_id` (`recipient_id`),
  KEY `postman_message_sender_id_2c020912_fk_auth_user_id` (`sender_id`),
  KEY `postman_message_thread_id_36e2f405_fk_postman_message_id` (`thread_id`),
  CONSTRAINT `postman_message_moderation_by_id_2b7e279e_fk_auth_user_id` FOREIGN KEY (`moderation_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `postman_message_parent_id_5b8df4a5_fk_postman_message_id` FOREIGN KEY (`parent_id`) REFERENCES `postman_message` (`id`),
  CONSTRAINT `postman_message_recipient_id_d52aeab_fk_auth_user_id` FOREIGN KEY (`recipient_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `postman_message_sender_id_2c020912_fk_auth_user_id` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `postman_message_thread_id_36e2f405_fk_postman_message_id` FOREIGN KEY (`thread_id`) REFERENCES `postman_message` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of postman_message
-- ----------------------------

-- ----------------------------
-- Table structure for registration_registrationprofile
-- ----------------------------
DROP TABLE IF EXISTS `registration_registrationprofile`;
CREATE TABLE `registration_registrationprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activation_key` varchar(40) NOT NULL,
  `user_id` int(11) NOT NULL,
  `activated` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `registration_registrationprofil_user_id_3f7685bb_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of registration_registrationprofile
-- ----------------------------

-- ----------------------------
-- Table structure for web_customer_business_carousel
-- ----------------------------
DROP TABLE IF EXISTS `web_customer_business_carousel`;
CREATE TABLE `web_customer_business_carousel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `carousel` varchar(100) DEFAULT NULL,
  `add_time` datetime NOT NULL,
  `add_user_id` int(11) DEFAULT NULL,
  `business_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `web_customer_business_carou_add_user_id_3cdd570e_fk_auth_user_id` (`add_user_id`),
  KEY `web_customer_business_ca_business_id_3e00bb5f_fk_erp_business_id` (`business_id`),
  CONSTRAINT `web_customer_business_carou_add_user_id_3cdd570e_fk_auth_user_id` FOREIGN KEY (`add_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `web_customer_business_ca_business_id_3e00bb5f_fk_erp_business_id` FOREIGN KEY (`business_id`) REFERENCES `erp_business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of web_customer_business_carousel
-- ----------------------------
INSERT INTO `web_customer_business_carousel` VALUES ('3', 'business/carousel/WzQyNywgMzA4LCA3NTQsIDEzMiwgMTksIDM1OCwgMjE2LCA4NDYsIDYwMywgODk5XQ03Fg==.jpg', '2016-06-01 13:49:50', '21', '4');
INSERT INTO `web_customer_business_carousel` VALUES ('4', 'business/carousel/Wzc3LCA4MjYsIDUyOSwgNzEyLCA3NTEsIDgyLCA1NjcsIDM1OSwgMzUzLCA3NTJdBDgE.jpg', '2016-06-08 13:48:04', '21', '4');
INSERT INTO `web_customer_business_carousel` VALUES ('6', '', '2016-07-18 15:43:08', '17', '4');

-- ----------------------------
-- Table structure for web_customer_lv_announcement
-- ----------------------------
DROP TABLE IF EXISTS `web_customer_lv_announcement`;
CREATE TABLE `web_customer_lv_announcement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lv_picture` varchar(100) DEFAULT NULL,
  `title` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `text` longtext,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of web_customer_lv_announcement
-- ----------------------------
INSERT INTO `web_customer_lv_announcement` VALUES ('1', 'lvmeng/announcement/WzU2MiwgNDA0LCA5OTQsIDk5MCwgODUwLCA0OTMsIDE4OSwgODExLCA2MjAsIDkxNF0HMjUW.jpg', '呵呵1', '2016-05-09', '<p>&nbsp; &nbsp; &nbsp; <span style=\"font-size: large;\"><strong>原标题：办辽宁老虎，集中了四员大将<img title=\"大叫\" src=\"../../static/tiny_mce/plugins/emotions/img/smiley-yell.gif\" alt=\"大叫\" border=\"0\" /> </strong></span>　　</p>\r\n<p>　　这两个月，辽宁上头条的频次让人震撼了。</p>\r\n<p>　　在林铎转任甘肃代省长后，中纪委宣传部长陈小江&ldquo;空降&rdquo;辽宁出任纪委书记。</p>\r\n<p>&nbsp; &nbsp; &nbsp;&nbsp;</p>\r\n<p>　　这可不是一条普通的人事任免消息，因为消息中的人物和地点，都具有足够抢眼的新闻性。</p>\r\n<p>　　长安街知事（微信ID:Capitalnews）发现，辽宁当前的&ldquo;打虎&rdquo;工作，已经云集了四位重量级人物。</p>\r\n<p>　　今年二月底，中央第三巡视组进驻辽宁，该省成为中央巡视首批&ldquo;回头看&rdquo;的地方。在这个巡视组中，组长是北京市纪委原书记叶青纯，副组长是云南省委组织部原部长刘维佳，两名部级大员坐镇，震撼力十足。</p>', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('2', 'lvmeng/announcement/WzQwNCwgMjE5LCA4MzUsIDg5NywgNTUyLCA4NDcsIDkwMSwgNjMwLCA0MDMsIDE5XQ4yMw0=.jpg', '刚刚的规范的', '2016-05-09', '<p><span style=\"font-size: x-small;\">发鬼地方个梵蒂冈</span></p>', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('3', 'lvmeng/announcement/0th0h3i7b6tvhjmtw9cuq0ukicm8t0nj8ip59ivxs7bz63lekpafbavu9csl.jpg', '发的规范的官方', '2016-05-09', '地方给梵蒂冈梵蒂冈浮动', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('4', 'lvmeng/announcement/bpszuujlruunvohumxmskhnjk3hm0bzqgtopysmewotertyz7bybxmvm8ia6.jpg', '给发个梵蒂冈', '2016-05-09', '<p><span style=\"font-size: medium;\">h几大块的哈萨克道德经</span></p>', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('5', 'lvmeng/announcement/WzgzNCwgNzg3LCA2NTgsIDg4LCAxNDIsIDE1NywgNDUxLCA3NzUsIDY0NiwgNzQ4XQ0EAA==.jpg', '和规范和规范化和规范和规范化和规范和规范化和规范和规范化', '2016-05-09', '    中新网5月9日电 据教育部网站消息，日前，国务院教育督导委员会办公室向各地印发《关于开展校园欺凌专项治理的通知》(以下简称《通知》)，要求各地各中小学校针对发生在学生之间，蓄意或恶意通过肢体、语言及网络等手段，实施欺负、侮辱造成伤害的校园欺凌进行专项治理', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('6', 'lvmeng/announcement/ve4asvnpnea6yxulyx4vqeqqd8er0vocpjeek9ty3afq7u7pzqvgxgwwfdsz.jpg', '大概', '2016-05-10', '发的范德萨范德萨', '0');
INSERT INTO `web_customer_lv_announcement` VALUES ('7', 'lvmeng/announcement/WzE3MiwgOTY3LCA3NzIsIDUzMSwgMzksIDMyLCAyMDYsIDQyNywgNTAwLCA1MTFdBhMF.jpg', '但是', '2016-05-10', '发生地方第三方', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('8', 'lvmeng/announcement/Wzg2OSwgNDg1LCA5LCA4NTAsIDMwOCwgMTI3LCAyOTAsIDI0MCwgNTQ4LCAxODldEAkH.jpg', '个梵蒂冈', '2016-05-10', '国芳蛋糕房给发个梵蒂冈发给梵蒂冈梵蒂冈梵蒂冈非官方的个非官方个地方官', '0');
INSERT INTO `web_customer_lv_announcement` VALUES ('9', 'lvmeng/announcement/WzE0NCwgOTI0LCA1NzIsIDYwMywgMywgODI0LCAzMTIsIDk0NiwgNTgxLCA3MDNdCzIA.jpg', '11111', '2016-05-16', '<p>sadsadasd</p>', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('10', '', '1111', '2016-05-16', '<p>dsdsadsadsd</p>', '0');
INSERT INTO `web_customer_lv_announcement` VALUES ('11', '', '333', '2016-05-16', '<p>333</p>', '0');
INSERT INTO `web_customer_lv_announcement` VALUES ('12', 'lvmeng/announcement/WzY0MCwgODYwLCA4NjMsIDEzMCwgNTE1LCAyMDgsIDg1MywgODE4LCA0MDUsIDI0OV0ANgs=.jpg', '第三方第三方的三', '2016-06-01', '<p>范德萨范德萨范德萨</p>', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('13', 'lvmeng/announcement/WzY1NywgMjY5LCAzNzcsIDE1MCwgOTA1LCA2ODIsIDQzNywgMjEzLCA2MSwgMTIyXRgwBg==.jpg', '第三方第三方第三方', '2016-06-06', '<p>发生的发生的发生的发生的</p>', '1');
INSERT INTO `web_customer_lv_announcement` VALUES ('14', 'lvmeng/announcement/Wzg2NCwgNDk1LCA3MDAsIDExMiwgODMyLCAzNzgsIDk4NywgMTksIDg1OCwgNTE4XQsxDA==.jpg', '111', '2016-06-13', '<p>111</p>', '0');
INSERT INTO `web_customer_lv_announcement` VALUES ('15', 'lvmeng/announcement/WzQ1NSwgNjM3LCA2NjMsIDk3OCwgMjQsIDE4NCwgNjE2LCA1NDQsIDQwNCwgMTc4XQs3Dg==.jpg', 'pppppp', '2016-07-19', '', '0');
SET FOREIGN_KEY_CHECKS=1;
