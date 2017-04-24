-- MySQL dump 10.13  Distrib 5.6.23, for Win64 (x86_64)
--
-- Host: localhost    Database: knowledge_db
-- ------------------------------------------------------
-- Server version	5.6.25-log

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
-- Table structure for table `collective`
--

DROP TABLE IF EXISTS `collective`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collective` (
  `id_collective` int(11) NOT NULL AUTO_INCREMENT,
  `age` int(3) NOT NULL,
  `muscle` varchar(20) NOT NULL,
  PRIMARY KEY (`id_collective`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collective`
--

LOCK TABLES `collective` WRITE;
/*!40000 ALTER TABLE `collective` DISABLE KEYS */;
INSERT INTO `collective` VALUES (1,60,'BACK'),(2,51,'BACK'),(3,38,'BACK'),(4,64,'BACK'),(5,28,'BICEPS'),(6,21,'BICEPS'),(7,35,'BICEPS'),(8,63,'BACK'),(9,34,'BICEPS'),(10,60,'BACK'),(11,36,'BACK'),(12,32,'BICEPS'),(13,64,'BACK'),(14,52,'BACK'),(15,50,'BACK'),(16,51,'BACK'),(17,25,'BICEPS'),(18,28,'BICEPS'),(19,45,'BACK'),(20,58,'BACK'),(21,64,'BACK'),(22,57,'BACK'),(23,38,'BACK'),(24,24,'BICEPS'),(25,54,'BICEPS'),(26,38,'BACK'),(27,27,'BICEPS'),(28,53,'BACK'),(29,34,'BICEPS');
/*!40000 ALTER TABLE `collective` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data` (
  `id_move` int(11) NOT NULL AUTO_INCREMENT,
  `name_move` varchar(45) NOT NULL,
  `main_muscle` varchar(20) NOT NULL,
  `other_muscle` varchar(45) DEFAULT NULL,
  `mechanics` varchar(15) NOT NULL,
  `equipment_1` varchar(20) NOT NULL,
  `equipment_2` varchar(20) DEFAULT NULL,
  `difficulty` varchar(15) NOT NULL,
  `link` varchar(100) NOT NULL,
  PRIMARY KEY (`id_move`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES (1,'BACK RELAXATION','BACK','GLUTES','COMPOUND','EXERCISE BALL',NULL,'BEGINNER','https://www.jefit.com/exercises/544/Back-Relaxation'),(2,'BARBELL BENT ARM PULLOVER','BACK','SHOULDERS','COMPOUND','BARBELL','BENCH','INTERMEDIATE','https://www.jefit.com/exercises/350/barbell-bent-arm-pullover'),(3,'BACK EXTENSION MACHINE','BACK',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/1259/Back-Extension-Machine'),(4,'BARBELL BENT OVER TWO ARM ROW','BACK',NULL,'COMPOUND','BARBELL',NULL,'INTERMEDIATE','https://www.jefit.com/exercises/807/Barbell-Bent-Over-Two-Arm-Row'),(5,'BARBELL GOOD MORNING','BACK','GLUTES','COMPOUND','BARBELL',NULL,'BEGINNER','https://www.jefit.com/exercises/7/Barbell-Good-Morning'),(6,'BARBELL INCLINE BENCH PULL','BACK','BICEPS','ISOLATION','BENCH','BARBELL','INTERMEDIATE','https://www.jefit.com/exercises/89/Barbell-Incline-Bench-Pull'),(7,'BARBELL ONE ARM BENT OVER ROW','BACK',NULL,'ISOLATION','BARBELL',NULL,'INTERMEDIATE','https://www.jefit.com/exercises/699/Barbell-One-Arm-Bent-Over-Row'),(8,'BARBELL SEATED GOOD MORNINGS','BACK','GLUTES','COMPOUND','BARBELL','BENCH','INTERMEDIATE','https://www.jefit.com/exercises/361/Barbell-Seated-Good-Mornings'),(9,'CABLE BACK INCLINE PUSHDOWN','BACK',NULL,'COMPOUND','MACHINE-STRENGTH','BENCH','BEGINNER','https://www.jefit.com/exercises/352/Cable-Back-Incline-Pushdown'),(10,'CABLE DEADLIFT','BACK',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'INTERMEDIATE','https://www.jefit.com/exercises/785/Cable-Deadlift'),(11,'CABLE INCLINE BENCH ROW','BACK','BICEPS','COMPOUND','BENCH','MACHINE-STRENGTH','INTERMEDIATE','https://www.jefit.com/exercises/1038/Cable-Incline-Bench-Row'),(12,'CABLE ROPE EXTENSION INCLINE BENCH ROW','BACK','BICEPS','COMPOUND','BENCH','MACHINE-STRENGTH','INTERMEDIATE','https://www.jefit.com/exercises/1039/Cable-Rope-Extension-Incline-Bench-Row'),(13,'CABLE ROPE LAT PULL DOWN ','BACK','BICEPS','COMPOUND','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/1244/Cable-Rope-Lat-Pull-Down'),(14,'CABLE STANDING ROW','BACK',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/701/Cable-Standing-Row'),(15,'CABLE V BAR STANDING ROW','BACK',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/1295/Cable-V-Bar-Standing-Row'),(16,'CAT STRETCH','BACK',NULL,'NA','BODY ONLY',NULL,'BEGINNER','https://www.jefit.com/exercises/809/Cat-Stretch'),(17,'DUMBBELL BENT OVER ROW','BACK','BICEPS','COMPOUND','DUMBBELL',NULL,'BEGINNER','https://www.jefit.com/exercises/88/Dumbbell-Bent-Over-Row'),(18,'CABLE ONE ARM SEATED ROW','BACK','BICEPS','COMPOUND','BENCH','MACHINE-STRENGTH','BEGINNER','https://www.jefit.com/exercises/1041/Cable-One-Arm-Seated-Row'),(19,'KNEELING LAT STRETCH','BACK','GLUTES','COMPOUND','BODY ONLY',NULL,'BEGINNER','https://www.jefit.com/exercises/560/Kneeling-Lat-Stretch'),(20,'ONE ARM AGAINST WALL','BACK',NULL,'ISOLATION','BODY ONLY',NULL,'BEGINNER','https://www.jefit.com/exercises/824/One-Arm-Against-Wall'),(21,'NARROW GRIP LAP PULL DOWN','BACK',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/696/Narrow-Grip-Lat-Pull-Down'),(22,'PULL UPS','BACK','SHOULDERS','COMPOUND','PULLUP BAR',NULL,'INTERMEDIATE','https://www.jefit.com/exercises/83/Pull-Ups'),(23,'SMITH MACHINE BENT OVER ROW','BACK','BICEPS','COMPOUND','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/91/Smith-Machine-Bent-Over-Row'),(24,'ROCKY PULL UPS AND PULLDOWNS','BACK','SHOULDERS','COMPOUND','PULLUP BAR',NULL,'EXPERT','https://www.jefit.com/exercises/360/Rocky-Pull-Ups-and-Pulldowns'),(25,'SPHINX','BACK','SHOULDERS','COMPOUND','BODY ONLY',NULL,'BEGINNER','https://www.jefit.com/exercises/575/Sphinx'),(26,'UNILATERAL ROW','BACK',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/1265/Unilateral-Row'),(27,'V BAR PULL UP','BACK','BICEPS','COMPOUND','PULLUP BAR','MACHINE-STRENGTH','EXPERT','https://www.jefit.com/exercises/81/V-Bar-Pull-Up'),(28,'WIDE GRIP PULLDOWN BEHIND THE NECK','BACK','SHOULDERS','COMPOUND','MACHINE-STRENGTH',NULL,'INTERMEDIATE','https://www.jefit.com/exercises/84/Wide-Grip-Pulldown-Behind-The-Neck'),(29,'WIDE GRIP LAT PULLDOWN','BACK','SHOULDERS','COMPOUND','MACHINE-STRENGTH',NULL,'INTERMEDIATE','https://www.jefit.com/exercises/86/Wide-Grip-Lat-Pulldown'),(30,'DUMBBELL ONE ARM PULLOVER','BACK','SHOULDERS','COMPOUND','DUMBBELL','EXERCISE BALL','INTERMEDIATE','https://www.jefit.com/exercises/697/Dumbbell-One-Arm-Pullover'),(31,'DUMBBELL ONE ARM ROW','BACK','BICEPS','COMPOUND','DUMBBELL','BENCH','BEGINNER','https://www.jefit.com/exercises/90/Dumbbell-One-Arm-Row'),(32,'DUMBBELL PALM ROTATIONAL ROW','BACK',NULL,'COMPOUND','DUMBBELL',NULL,'INTERMEDIATE','https://www.jefit.com/exercises/1042/Dumbbell-Palm-Rotational-Row'),(33,'ISO LATERAL WIDE PULLDOWN','BACK','BICEPS','ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/1275/Iso-Lateral-Wide-Pulldown'),(34,'KETTLEBELL TWO ARM ROW','BACK','BICEPS','COMPOUND','KETTLEBELL',NULL,'INTERMEDIATE','https://www.jefit.com/exercises/362/Kettlebell-Two-Arm-Row'),(35,'CABLE ROPE PULL UP','BACK','BICEPS','COMPOUND','MACHINE-STRENGTH',NULL,'EXPERT','https://www.jefit.com/exercises/1245/Cable-Rope-Pull-Up'),(36,'KETTLEBELL ALTERNATING RENEGADE ROW','BACK','CHEST','COMPOUND','KETTLEBELL',NULL,'EXPERT','https://www.jefit.com/exercises/349/Kettlebell-Alternating-Renegade-Row'),(37,'ONE ARM CHIN UP','BACK','FOREARM','COMPOUND','PULLUP BAR',NULL,'EXPERT','https://www.jefit.com/exercises/357/One-Arm-Chin-Up'),(38,'WIDE GRIP REAR PULL-UP','BACK','SHOULDERS','COMPOUND','PULLUP BAR',NULL,'EXPERT','https://www.jefit.com/exercises/85/Wide-Grip-Rear-Pull-Up'),(39,'EZ BAR CURL','BICEPS',NULL,'ISOLATION','EZ CURL BAR',NULL,'BEGINNER','https://www.jefit.com/exercises/95/EZ-Bar-Curl'),(40,'MACHINE CURL WITH REVERSE GRIP','BICEPS',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/1249/Machine-Curl-With-Reverse-Grip'),(41,'PREACHER CURL MACHINE ','BICEPS','FOREARM','ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/271/Preacher-Curl-Machine'),(42,'SMITH MACHINE BICEP CURL','BICEPS',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/1030/Smith-Machine-Bicep-Curl'),(43,'WEIGHT PLAATE REVERSE CURL','BICEPS','FOREARM','ISOLATION','WEIGHT PLATE',NULL,'BEGINNER','https://www.jefit.com/exercises/269/Weight-Plate-Reverse-Curl'),(44,'BARBELL CLOSE GRIP PREACHER CURL','BICEPS',NULL,'ISOLATION','EZ CURL BAR','MACHINE-STRENGTH','BEGINNER','https://www.jefit.com/exercises/1299/Barbell-Close-Grip-Preacher-Curl'),(45,'BARBELL STANDING WIDE GRIP BICEPS CURL','BICEPS','FOREARM','ISOLATION','BARBELL',NULL,'BEGINNER','https://www.jefit.com/exercises/275/Barbell-Standing-Wide-Grip-Biceps-Curl'),(46,'CABLE CLOSE GRIP CURL','BICEPS',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/1015/Cable-Close-Grip-Curl'),(47,'CABLE ONE ARM HIGH CURL','BICEPS',NULL,'ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/708/Cable-One-Arm-High-Curl'),(48,'CABLE PREACHER CURL','BICEPS','FOREARM','ISOLATION','MACHINE-STRENGTH','BENCH','BEGINNER','https://www.jefit.com/exercises/256/Cable-Preacher-Curl'),(49,'CABLE ROPE HAMMER CURLS','BICEPS','FOREARM','ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/257/Cable-Rope-Hammer-Curls'),(50,'CABLE STANDING ONE ARM BICEP CURL','BICEPS','FOREARM','ISOLATION','MACHINE-STRENGTH',NULL,'BEGINNER','https://www.jefit.com/exercises/273/Cable-Standing-One-Arm-Bicep-Curl'),(51,'DUMBBELL ALTERNATE INCLINE HAMMER CURL','BICEPS',NULL,'ISOLATION','BENCH','DUMBBELL','BEGINNER','https://www.jefit.com/exercises/1009/Dumbbell-Alternate-Incline-Hammer-Curl');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expert`
--

DROP TABLE IF EXISTS `expert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `expert` (
  `id_range` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(15) NOT NULL,
  `experience` varchar(15) NOT NULL,
  PRIMARY KEY (`id_range`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expert`
--

LOCK TABLES `expert` WRITE;
/*!40000 ALTER TABLE `expert` DISABLE KEYS */;
INSERT INTO `expert` VALUES (1,'LITTLE TIME','BEGINNER'),(2,'GOOD TIME','INTERMEDIATE'),(3,'LONG TIME','EXPERT');
/*!40000 ALTER TABLE `expert` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-20  2:03:21
