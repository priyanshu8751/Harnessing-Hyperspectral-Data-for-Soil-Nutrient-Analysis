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
-- Table structure for table `farmer_dashboard_gddrecord`
--

DROP TABLE IF EXISTS `farmer_dashboard_gddrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_dashboard_gddrecord` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `gdd_value` double NOT NULL,
  `crop_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `farmer_dashboard_gddrecord_crop_id_date_3389c039_uniq` (`crop_id`,`date`),
  CONSTRAINT `farmer_dashboard_gdd_crop_id_3a699f0f_fk_farmer_da` FOREIGN KEY (`crop_id`) REFERENCES `farmer_dashboard_crop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_dashboard_gddrecord`
--

LOCK TABLES `farmer_dashboard_gddrecord` WRITE;
/*!40000 ALTER TABLE `farmer_dashboard_gddrecord` DISABLE KEYS */;
INSERT INTO `farmer_dashboard_gddrecord` VALUES (1,'2024-02-14',18,1),(3,'2024-01-08',18,2),(4,'2024-01-29',20,1),(5,'2024-01-30',20,1),(6,'2024-02-13',20,1),(7,'2024-01-08',20,1),(8,'2024-01-09',20,1),(9,'2024-01-10',20,1),(10,'2024-01-11',20,1),(11,'2024-01-12',20,1),(12,'2024-01-13',20,1),(13,'2024-01-14',20,1),(14,'2024-01-15',20,1),(15,'2024-01-16',20,1),(16,'2024-01-17',20,1),(17,'2024-01-18',20,1),(18,'2024-01-19',20,1),(19,'2024-01-20',20,1),(20,'2024-01-21',20,1),(21,'2024-01-22',20,1),(22,'2024-01-23',20,1),(23,'2024-01-24',20,1),(24,'2024-01-25',20,1),(25,'2024-01-26',20,1),(26,'2024-01-27',20,1),(27,'2024-01-28',20,1),(28,'2024-01-31',20,1),(29,'2024-03-07',17.5,1),(30,'2024-03-12',17.5,1),(31,'2024-03-21',20,1);
/*!40000 ALTER TABLE `farmer_dashboard_gddrecord` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-23 11:39:33
