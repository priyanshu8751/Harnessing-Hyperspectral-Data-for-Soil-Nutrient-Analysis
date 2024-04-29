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
-- Table structure for table `farmer_dashboard_crop`
--

DROP TABLE IF EXISTS `farmer_dashboard_crop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_dashboard_crop` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `boundary_coordinates` longtext NOT NULL,
  `area_covered` double NOT NULL,
  `crop_type_id` bigint NOT NULL,
  `farmer_id` bigint NOT NULL,
  `device_id` bigint DEFAULT NULL,
  `Yield_predicted` double DEFAULT NULL,
  `date_of_planting` date DEFAULT NULL,
  `is_available` tinyint(1) NOT NULL,
  `total_growth` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farmer_dashboard_cro_crop_type_id_ec0e5218_fk_farmer_da` (`crop_type_id`),
  KEY `farmer_dashboard_cro_farmer_id_66e0d78c_fk_farmer_da` (`farmer_id`),
  KEY `farmer_dashboard_crop_device_id_734afcc8_fk_base_device_id` (`device_id`),
  CONSTRAINT `farmer_dashboard_cro_crop_type_id_ec0e5218_fk_farmer_da` FOREIGN KEY (`crop_type_id`) REFERENCES `farmer_dashboard_croptype` (`id`),
  CONSTRAINT `farmer_dashboard_cro_farmer_id_66e0d78c_fk_farmer_da` FOREIGN KEY (`farmer_id`) REFERENCES `farmer_dashboard_farmer` (`id`),
  CONSTRAINT `farmer_dashboard_crop_device_id_734afcc8_fk_base_device_id` FOREIGN KEY (`device_id`) REFERENCES `base_device` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_dashboard_crop`
--

LOCK TABLES `farmer_dashboard_crop` WRITE;
/*!40000 ALTER TABLE `farmer_dashboard_crop` DISABLE KEYS */;
INSERT INTO `farmer_dashboard_crop` VALUES (1,'tomato','10.728485, 76.620757|\r\n10.728465, 76.620858|\r\n10.728385, 76.620959|\r\n10.728305, 76.620858|\r\n10.728285, 76.620757|\r\n10.728305, 76.620656|\r\n10.728385, 76.620555|\r\n10.728465, 76.620656|\r\n10.728485, 76.620757',420,1,1,1,11,'2023-11-01',1,22.919999999999998),(2,'cabbage','10.728385,  76.620757|\r\n10.728454,  76.620993|\r\n10.728307,  76.621071|\r\n10.728094,  76.621077|    \r\n10.727927,  76.621134|\r\n10.727836,  76.620885|\r\n10.727951,  76.620837|\r\n10.728385,  76.620757',22,2,1,2,11,'2024-01-07',1,0.72);
/*!40000 ALTER TABLE `farmer_dashboard_crop` ENABLE KEYS */;
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
