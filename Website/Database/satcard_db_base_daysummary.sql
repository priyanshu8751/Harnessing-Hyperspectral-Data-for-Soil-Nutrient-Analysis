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
-- Table structure for table `base_daysummary`
--

DROP TABLE IF EXISTS `base_daysummary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_daysummary` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `param` varchar(200) NOT NULL,
  `value` double NOT NULL,
  `device_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_daysummary_device_id_date_param_ffa2b7b7_uniq` (`device_id`,`date`,`param`),
  CONSTRAINT `base_daysummary_device_id_6a0ff1dd_fk_base_device_id` FOREIGN KEY (`device_id`) REFERENCES `base_device` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_daysummary`
--

LOCK TABLES `base_daysummary` WRITE;
/*!40000 ALTER TABLE `base_daysummary` DISABLE KEYS */;
INSERT INTO `base_daysummary` VALUES (1,'2024-03-19','temperature',10,1),(2,'2024-03-20','temperature',30,1),(3,'2024-03-22','temperature',25,1),(4,'2024-03-19','pressure',12,1),(5,'2024-03-18','pressure',12,1),(6,'2024-03-20','pressure',70,1),(7,'2024-03-21','pressure',12,1),(8,'2024-03-22','pressure',30,1),(9,'2024-03-18','humidity',10,1),(10,'2024-03-19','humidity',20,1),(11,'2024-03-20','humidity',30,1),(12,'2024-02-21','humidity',40,1),(13,'2024-03-22','humidity',10,1),(14,'2024-03-14','humidity',10,1),(15,'2024-03-15','humidity',14,1);
/*!40000 ALTER TABLE `base_daysummary` ENABLE KEYS */;
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
