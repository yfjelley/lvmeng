-- MySQL dump 10.13  Distrib 6.0.11-alpha, for Win32 (ia32)
--
-- Host: localhost    Database: lvmeng
-- ------------------------------------------------------
-- Server version	6.0.11-alpha-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(49,'agent_api','agent_version'),(42,'agent_api','cell_records_customer'),(43,'agent_api','cell_records_pcustomer'),(25,'aos','checkwork'),(26,'aos','checkwork_history'),(52,'api','attention'),(19,'api','checkin'),(51,'api','collection'),(18,'api','headline'),(48,'api','history_checkin'),(22,'api','validsecond'),(23,'api','verificationcode'),(16,'api','version'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'authtoken','token'),(35,'captcha','captchastore'),(5,'contenttypes','contenttype'),(9,'corsheaders','corsmodel'),(11,'erp','agent'),(24,'erp','announcement'),(10,'erp','business'),(13,'erp','customer'),(41,'erp','customer_pending'),(50,'erp','position'),(12,'erp','product'),(20,'erp','product_type'),(15,'erp','purchase'),(47,'erp','real_purchase'),(27,'oa','checkwork'),(28,'oa','checkwork_history'),(32,'oa','cost_application'),(38,'oa','cost_examine'),(44,'oa','daily_to_do'),(31,'oa','daily_work'),(30,'oa','internal_announcement'),(39,'oa','leave_examine'),(33,'oa','leave_management'),(36,'oa','read_message'),(34,'oa','travel_apply'),(40,'oa','travel_examine'),(45,'postman','message'),(46,'postman','pendingmessage'),(8,'registration','registrationprofile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-06  7:46:21
