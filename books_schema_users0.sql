-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: books_schema
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `dob` date DEFAULT NULL,
  `phone` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated` datetime DEFAULT NULL,
  `passwd` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idusers_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'amanda','spirit',NULL,'8795462789','amanda_sp24@yahoo.com','2024-10-29 09:46:13',NULL,''),(2,'Barry','Allen',NULL,'8795462233','flash_point24@yahoo.com','2024-10-29 09:47:23',NULL,'$2b$12$UWY9vmVGUlqotVfkzmmhteCPoFhCDWuia9CtlvjQGOQrOZGMXtR1C'),(3,'Jennifer','Foxx',NULL,'8095462771','Foxx_BKL21@yahoo.com','2024-10-30 09:20:39',NULL,''),(4,'Coby','Brian',NULL,'9015762789','coby04brain_23@yahoo.com','2024-10-31 23:16:55',NULL,''),(5,'Jennifer','Hewitt',NULL,'2015062789','Hewitt_Jen23@yahoo.com','2024-10-31 23:16:55',NULL,''),(6,'Gene','HACKMAN',NULL,'2055063789','Hackman_gene09@gmail.com','2024-10-31 23:16:55',NULL,''),(7,'Jason','Lee',NULL,'2051063289','Jason_Lee09@gmail.com','2024-10-31 23:16:55',NULL,''),(8,'Bobby','paterson',NULL,'1051068219','paterson-19@gmail.com','2024-10-31 23:16:55',NULL,''),(9,'jeff','marc','2011-03-18','jeffmarc07@yahoo.com','9735731824','2025-01-17 18:51:35',NULL,'$2b$12$3qPDv2bFBOCSZjRbUA408uE9MY4TIRCVl2CIqmkLDCpzsCe6Fospi'),(10,'jeff','marc','2011-03-18','jeffmarc07@yahoo.com','9735731824','2025-01-17 18:54:42',NULL,'$2b$12$c6xZ30hG5OsopKCIgoRpQetWOjnVJ2FETqCs7kvGJxIiz64.GyuRq'),(11,'jeff','marc','2011-03-18','jeffmarc07@yahoo.com','9735731824','2025-01-17 18:55:26',NULL,'$2b$12$ovCwwGLbcf9U0DakpGSC5OwQrfvsK/vVnex0V12lgiRFulSrD8DiW'),(12,'jeff','marc','2011-03-18','jeffmarc07@yahoo.com','9735731824','2025-01-17 18:58:02',NULL,'$2b$12$T9.KKy2RYf8Fw87naU0Dtup1OPJ1tHO6DpJuemZKMc.LvCmKPSfkO'),(13,'jeff','marc','2011-03-18','jeffmarc07@yahoo.com','9735731824','2025-01-17 18:58:12',NULL,'$2b$12$yM9tPvNIrBUgny1PH005X.tfw4eJXRyhU2ABsx7bAWzzVU1qRH7q2'),(14,'johnny','BOB','2000-06-06','23109812234','Johnny_bo@gmail.com','2025-01-17 19:01:42',NULL,'$2b$12$gwaXBEt0TiMipMsznm3qquB2SN8SC0CkqzXEDmkHcqlSPUGXopz9a'),(15,'amy','Angel','1987-09-19','23109812231','amy-blues@gmail.com','2025-01-17 19:13:37',NULL,'$2b$12$C.i/DxbR9aqYcKoNlqw7SuCwWcAkBJQnAps0.87nwN5dNDvrZQXLC'),(16,'billy','Angel','1987-09-19','23109812831','bill-blues@gmail.com','2025-01-17 19:28:23',NULL,'$2b$12$dYOaCHAx9Yi64DGsk1Gyie3KgyMOddJCDawZhS14.jEhcZo3mmv9.'),(17,'jullie','marc','1997-01-15','19735831824','bill-blues12@gmail.com','2025-01-17 20:53:04',NULL,'$2b$12$AgTZrHe9aATr1GuRB7fMx.ZQjGffFxH9/aK720ZhZf8Xc1vaGAaxG'),(18,'johnny','Angel','1997-04-10','9735731824','Johnny_bo23@gmail.com','2025-01-19 17:36:49',NULL,'$2b$12$Yp7YjBjw5iD/hmBlSv5TheXbqkjoJIOCJD.GCOWvQBEW/9Al1rTM2');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-21  8:21:16
