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
-- Table structure for table `farmer_dashboard_croptype`
--

DROP TABLE IF EXISTS `farmer_dashboard_croptype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_dashboard_croptype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `wms_background` varchar(100) DEFAULT NULL,
  `flowering_phase` varchar(100) DEFAULT NULL,
  `vegetative_phase` varchar(100) DEFAULT NULL,
  `ripening_phase` varchar(100) DEFAULT NULL,
  `seed_phase` varchar(100) DEFAULT NULL,
  `seedling_phase` varchar(100) DEFAULT NULL,
  `Tb` int DEFAULT NULL,
  `flowering_phase_gdd_limit` double DEFAULT NULL,
  `ripening_phase_gdd_limit` double DEFAULT NULL,
  `seed_phase_gdd_limit` double DEFAULT NULL,
  `seedling_phase_gdd_limit` double DEFAULT NULL,
  `vegetative_phase_gdd_limit` double DEFAULT NULL,
  `has_flowering_stage` tinyint(1) NOT NULL,
  `has_ripening_stage` tinyint(1) NOT NULL,
  `has_seed_stage` tinyint(1) NOT NULL,
  `has_seedling_stage` tinyint(1) NOT NULL,
  `has_vegetative_stage` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_dashboard_croptype`
--

LOCK TABLES `farmer_dashboard_croptype` WRITE;
/*!40000 ALTER TABLE `farmer_dashboard_croptype` DISABLE KEYS */;
INSERT INTO `farmer_dashboard_croptype` VALUES (1,'Tomato','static/farmer_dashboard/assets/crop_icons/tomato_khVIZxb.png','static/farmer_dashboard/assets/wms_backgrounds/White_Yellow_My_Self_Portrait_Worksheet.png','static/farmer_dashboard/assets/total_growth_card/floweringstage.webp','static/farmer_dashboard/assets/total_growth_card/vegetativestage.webp','static/farmer_dashboard/assets/total_growth_card/ripeningstage.webp','static/farmer_dashboard/assets/total_growth_card/seedstage.webp','static/farmer_dashboard/assets/total_growth_card/seedlingstage.webp',10,2000,2500,500,1000,1500,1,1,1,1,1),(2,'cabbage','static/farmer_dashboard/assets/crop_icons/cabbage-_1OkphFO.png','static/farmer_dashboard/assets/wms_backgrounds/White_Yellow_My_Self_Portrait_Worksheet_e91aO6R.png','static/farmer_dashboard/assets/total_growth_card/floweringstage_H7tsRCw.webp','static/farmer_dashboard/assets/total_growth_card/vegetativestage_dUdMyjW.webp','static/farmer_dashboard/assets/total_growth_card/ripeningstage_Pp64DUO.webp','static/farmer_dashboard/assets/total_growth_card/seedstage_mZkuFd7.webp','static/farmer_dashboard/assets/total_growth_card/seedlingstage_w7S90gk.webp',5,2000,2500,500,1000,1500,1,1,1,0,1);
/*!40000 ALTER TABLE `farmer_dashboard_croptype` ENABLE KEYS */;
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
