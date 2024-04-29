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
-- Table structure for table `farmer_dashboard_alert`
--

DROP TABLE IF EXISTS `farmer_dashboard_alert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_dashboard_alert` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `alert_type` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `crop_id` bigint NOT NULL,
  `datetime` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farmer_dashboard_ale_crop_id_28a7c79b_fk_farmer_da` (`crop_id`),
  CONSTRAINT `farmer_dashboard_ale_crop_id_28a7c79b_fk_farmer_da` FOREIGN KEY (`crop_id`) REFERENCES `farmer_dashboard_crop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_dashboard_alert`
--

LOCK TABLES `farmer_dashboard_alert` WRITE;
/*!40000 ALTER TABLE `farmer_dashboard_alert` DISABLE KEYS */;
INSERT INTO `farmer_dashboard_alert` VALUES (1,'Weather','lorem ipsum lorem ipsum lorem ipsum',1,'2024-03-12 09:01:06.000000'),(2,'Irrigation','lorem ipsum lorem ipsum lorem ipsum',1,'2024-03-01 00:00:00.000000'),(3,'Soil Health','lorem ipsum lorem ipsum lorem ipsum',2,'2024-04-03 12:00:00.000000'),(4,'Planting','lorem ipsum lorem ipsum lorem ipsum',2,'2024-04-01 06:00:00.000000'),(5,'Pest','lorem ipsum lorem ipsum lorem ipsum lorem ipsum',1,'2024-04-10 09:00:05.000000');
/*!40000 ALTER TABLE `farmer_dashboard_alert` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-23 11:39:35
