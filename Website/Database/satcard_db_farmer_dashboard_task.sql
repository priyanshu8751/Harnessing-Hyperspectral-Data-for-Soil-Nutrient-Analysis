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
-- Table structure for table `farmer_dashboard_task`
--

DROP TABLE IF EXISTS `farmer_dashboard_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_dashboard_task` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `deadline` date NOT NULL,
  `description` longtext NOT NULL,
  `crop_id` bigint NOT NULL,
  `is_completed` tinyint(1) NOT NULL,
  `completed_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farmer_dashboard_tas_crop_id_e8cfa084_fk_farmer_da` (`crop_id`),
  CONSTRAINT `farmer_dashboard_tas_crop_id_e8cfa084_fk_farmer_da` FOREIGN KEY (`crop_id`) REFERENCES `farmer_dashboard_crop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_dashboard_task`
--

LOCK TABLES `farmer_dashboard_task` WRITE;
/*!40000 ALTER TABLE `farmer_dashboard_task` DISABLE KEYS */;
INSERT INTO `farmer_dashboard_task` VALUES (1,'2024-04-30','water the tomato',1,0,NULL),(2,'2024-04-15','add pesticide',1,0,NULL),(3,'2024-04-20','add fertilizer',1,0,NULL),(4,'2024-04-13','harvest the crop',2,0,NULL),(5,'2024-04-22','water the crop',2,0,NULL),(6,'2024-04-12','add pesticides and fertilizers',2,1,'2024-04-19'),(7,'2024-04-28','complete task1',1,1,'2024-04-08');
/*!40000 ALTER TABLE `farmer_dashboard_task` ENABLE KEYS */;
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
