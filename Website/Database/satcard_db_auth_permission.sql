-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: satcard_db
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add email address',7,'add_emailaddress'),(26,'Can change email address',7,'change_emailaddress'),(27,'Can delete email address',7,'delete_emailaddress'),(28,'Can view email address',7,'view_emailaddress'),(29,'Can add email confirmation',8,'add_emailconfirmation'),(30,'Can change email confirmation',8,'change_emailconfirmation'),(31,'Can delete email confirmation',8,'delete_emailconfirmation'),(32,'Can view email confirmation',8,'view_emailconfirmation'),(33,'Can add raw payload',9,'add_rawpayload'),(34,'Can change raw payload',9,'change_rawpayload'),(35,'Can delete raw payload',9,'delete_rawpayload'),(36,'Can view raw payload',9,'view_rawpayload'),(37,'Can add device',10,'add_device'),(38,'Can change device',10,'change_device'),(39,'Can delete device',10,'delete_device'),(40,'Can view device',10,'view_device'),(41,'Can add data',11,'add_data'),(42,'Can change data',11,'change_data'),(43,'Can delete data',11,'delete_data'),(44,'Can view data',11,'view_data'),(45,'Can add param group',12,'add_paramgroup'),(46,'Can change param group',12,'change_paramgroup'),(47,'Can delete param group',12,'delete_paramgroup'),(48,'Can view param group',12,'view_paramgroup'),(49,'Can add day summary',13,'add_daysummary'),(50,'Can change day summary',13,'change_daysummary'),(51,'Can delete day summary',13,'delete_daysummary'),(52,'Can view day summary',13,'view_daysummary'),(53,'Can add weather forecast',14,'add_weatherforecast'),(54,'Can change weather forecast',14,'change_weatherforecast'),(55,'Can delete weather forecast',14,'delete_weatherforecast'),(56,'Can view weather forecast',14,'view_weatherforecast'),(57,'Can add param config',15,'add_paramconfig'),(58,'Can change param config',15,'change_paramconfig'),(59,'Can delete param config',15,'delete_paramconfig'),(60,'Can view param config',15,'view_paramconfig'),(61,'Can add crop type',16,'add_croptype'),(62,'Can change crop type',16,'change_croptype'),(63,'Can delete crop type',16,'delete_croptype'),(64,'Can view crop type',16,'view_croptype'),(65,'Can add farmer',17,'add_farmer'),(66,'Can change farmer',17,'change_farmer'),(67,'Can delete farmer',17,'delete_farmer'),(68,'Can view farmer',17,'view_farmer'),(69,'Can add crop',18,'add_crop'),(70,'Can change crop',18,'change_crop'),(71,'Can delete crop',18,'delete_crop'),(72,'Can view crop',18,'view_crop'),(73,'Can add your model',19,'add_yourmodel'),(74,'Can change your model',19,'change_yourmodel'),(75,'Can delete your model',19,'delete_yourmodel'),(76,'Can view your model',19,'view_yourmodel'),(77,'Can add gdd record',20,'add_gddrecord'),(78,'Can change gdd record',20,'change_gddrecord'),(79,'Can delete gdd record',20,'delete_gddrecord'),(80,'Can view gdd record',20,'view_gddrecord'),(81,'Can add alert',21,'add_alert'),(82,'Can change alert',21,'change_alert'),(83,'Can delete alert',21,'delete_alert'),(84,'Can view alert',21,'view_alert'),(85,'Can add task',22,'add_task'),(86,'Can change task',22,'change_task'),(87,'Can delete task',22,'delete_task'),(88,'Can view task',22,'view_task');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-23 11:39:34
