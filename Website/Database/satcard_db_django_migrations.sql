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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-12-16 20:17:05.461080'),(2,'auth','0001_initial','2023-12-16 20:17:05.954034'),(3,'account','0001_initial','2023-12-16 20:17:06.115318'),(4,'account','0002_email_max_length','2023-12-16 20:17:06.135299'),(5,'admin','0001_initial','2023-12-16 20:17:06.249065'),(6,'admin','0002_logentry_remove_auto_add','2023-12-16 20:17:06.249065'),(7,'admin','0003_logentry_add_action_flag_choices','2023-12-16 20:17:06.270381'),(8,'contenttypes','0002_remove_content_type_name','2023-12-16 20:17:06.382780'),(9,'auth','0002_alter_permission_name_max_length','2023-12-16 20:17:06.435460'),(10,'auth','0003_alter_user_email_max_length','2023-12-16 20:17:06.449590'),(11,'auth','0004_alter_user_username_opts','2023-12-16 20:17:06.468920'),(12,'auth','0005_alter_user_last_login_null','2023-12-16 20:17:06.532966'),(13,'auth','0006_require_contenttypes_0002','2023-12-16 20:17:06.533912'),(14,'auth','0007_alter_validators_add_error_messages','2023-12-16 20:17:06.548695'),(15,'auth','0008_alter_user_username_max_length','2023-12-16 20:17:06.616619'),(16,'auth','0009_alter_user_last_name_max_length','2023-12-16 20:17:06.683171'),(17,'auth','0010_alter_group_name_max_length','2023-12-16 20:17:06.710527'),(18,'auth','0011_update_proxy_permissions','2023-12-16 20:17:06.718714'),(19,'auth','0012_alter_user_first_name_max_length','2023-12-16 20:17:06.765600'),(20,'base','0001_initial','2023-12-16 20:17:06.782685'),(21,'base','0002_device_data','2023-12-16 20:17:06.910839'),(22,'base','0003_alter_data_options_device_deployment_date_and_more','2023-12-16 20:17:06.941390'),(23,'base','0004_paramgroup','2023-12-16 20:17:06.948893'),(24,'base','0005_paramgroup_title','2023-12-16 20:17:06.970606'),(25,'base','0006_daysummary','2023-12-16 20:17:07.033877'),(26,'base','0007_data_battery_volt_data_dp_avg_and_more','2023-12-16 20:17:07.142134'),(27,'base','0008_weatherforecast','2023-12-16 20:17:07.225164'),(28,'base','0009_alter_weatherforecast_unique_together','2023-12-16 20:17:07.240123'),(29,'base','0010_alter_daysummary_unique_together','2023-12-16 20:17:07.253078'),(30,'base','0011_paramconfig','2023-12-16 20:17:07.285987'),(31,'base','0012_paramconfig_max_expected_delta','2023-12-16 20:17:07.303867'),(32,'farmer_dashboard','0001_initial','2023-12-16 20:17:07.440967'),(33,'farmer_dashboard','0002_farmerdevicemapping','2023-12-16 20:17:07.547067'),(34,'farmer_dashboard','0003_crop_device','2023-12-16 20:17:07.597532'),(35,'farmer_dashboard','0004_delete_farmerdevicemapping','2023-12-16 20:17:07.602873'),(36,'farmer_dashboard','0005_alter_croptype_icon_alter_croptype_wms_background','2023-12-16 20:17:07.618982'),(37,'farmer_dashboard','0006_alter_croptype_icon_alter_croptype_wms_background','2023-12-16 20:17:07.625989'),(38,'farmer_dashboard','0007_farmer_profile_pic','2023-12-16 20:17:07.633130'),(39,'farmer_dashboard','0008_crop_yield_predicted_crop_date_of_planting_and_more','2023-12-16 20:17:07.842292'),(40,'sessions','0001_initial','2023-12-16 20:17:07.868917'),(41,'farmer_dashboard','0009_croptype_tb','2024-01-30 05:44:03.468293'),(42,'farmer_dashboard','0010_yourmodel_alter_croptype_tb','2024-01-30 05:50:55.212302'),(43,'farmer_dashboard','0011_alter_croptype_tb_delete_yourmodel','2024-01-30 05:54:30.010357'),(44,'farmer_dashboard','0012_alter_croptype_tb','2024-01-30 05:57:59.016763'),(45,'farmer_dashboard','0013_rename_ready_to_harvest_croptype_vegetative_phase','2024-01-30 07:39:18.635907'),(46,'farmer_dashboard','0014_croptype_flowering_phase_gdd_limit_and_more','2024-01-30 11:47:28.635619'),(47,'farmer_dashboard','0015_gddrecord','2024-02-14 14:44:20.966693'),(48,'farmer_dashboard','0016_croptype_has_flowering_stage_and_more','2024-02-26 08:44:40.667649'),(49,'farmer_dashboard','0017_alter_croptype_wms_background','2024-02-29 05:23:53.335871'),(50,'farmer_dashboard','0018_alert','2024-03-30 06:37:13.443534'),(51,'farmer_dashboard','0019_alert_date','2024-03-30 06:44:02.508056'),(52,'farmer_dashboard','0020_remove_alert_date_alert_datetime','2024-04-05 08:58:54.020012'),(53,'farmer_dashboard','0021_task','2024-04-08 13:23:04.442551'),(54,'farmer_dashboard','0022_rename_date_task_deadline_and_more','2024-04-08 15:54:41.927799'),(55,'farmer_dashboard','0023_task_completed_date','2024-04-08 16:03:29.153716');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
