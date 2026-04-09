-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: spotlike
-- ------------------------------------------------------
-- Server version	8.4.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album` (
  `PK_albumID` int NOT NULL AUTO_INCREMENT,
  `albumName` varchar(100) NOT NULL,
  `releaseDate` date DEFAULT NULL,
  PRIMARY KEY (`PK_albumID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `albumartist`
--

DROP TABLE IF EXISTS `albumartist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albumartist` (
  `artist_PK_artistID` int NOT NULL,
  `album_PK_albumID` int NOT NULL,
  PRIMARY KEY (`artist_PK_artistID`,`album_PK_albumID`),
  KEY `fk_albumArtist_artist1_idx` (`artist_PK_artistID`),
  KEY `fk_albumArtist_album1_idx` (`album_PK_albumID`),
  CONSTRAINT `fk_albumArtist_album1` FOREIGN KEY (`album_PK_albumID`) REFERENCES `album` (`PK_albumID`) ON DELETE CASCADE,
  CONSTRAINT `fk_albumArtist_artist1` FOREIGN KEY (`artist_PK_artistID`) REFERENCES `artist` (`PK_artistID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albumartist`
--

LOCK TABLES `albumartist` WRITE;
/*!40000 ALTER TABLE `albumartist` DISABLE KEYS */;
/*!40000 ALTER TABLE `albumartist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `albumband`
--

DROP TABLE IF EXISTS `albumband`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albumband` (
  `band_PK_bandID` int NOT NULL,
  `album_PK_albumID` int NOT NULL,
  PRIMARY KEY (`band_PK_bandID`,`album_PK_albumID`),
  KEY `fk_albumBand_band1_idx` (`band_PK_bandID`),
  KEY `fk_albumBand_album1_idx` (`album_PK_albumID`),
  CONSTRAINT `fk_albumBand_album1` FOREIGN KEY (`album_PK_albumID`) REFERENCES `album` (`PK_albumID`) ON DELETE CASCADE,
  CONSTRAINT `fk_albumBand_band1` FOREIGN KEY (`band_PK_bandID`) REFERENCES `band` (`PK_bandID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albumband`
--

LOCK TABLES `albumband` WRITE;
/*!40000 ALTER TABLE `albumband` DISABLE KEYS */;
/*!40000 ALTER TABLE `albumband` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `albummusica`
--

DROP TABLE IF EXISTS `albummusica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albummusica` (
  `album_PK_albumID` int NOT NULL,
  `songs_PK_songID` int NOT NULL,
  PRIMARY KEY (`album_PK_albumID`,`songs_PK_songID`),
  KEY `fk_albumMusica_songs1_idx` (`songs_PK_songID`),
  CONSTRAINT `fk_albumMusica_album1` FOREIGN KEY (`album_PK_albumID`) REFERENCES `album` (`PK_albumID`) ON DELETE CASCADE,
  CONSTRAINT `fk_albumMusica_songs1` FOREIGN KEY (`songs_PK_songID`) REFERENCES `songs` (`PK_songID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albummusica`
--

LOCK TABLES `albummusica` WRITE;
/*!40000 ALTER TABLE `albummusica` DISABLE KEYS */;
/*!40000 ALTER TABLE `albummusica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist` (
  `PK_artistID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text,
  `imageArtist` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`PK_artistID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artistsband`
--

DROP TABLE IF EXISTS `artistsband`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artistsband` (
  `artist_PK_artistID` int NOT NULL,
  `band_PK_bandID` int NOT NULL,
  PRIMARY KEY (`artist_PK_artistID`,`band_PK_bandID`),
  KEY `fk_artistsband_artist1_idx` (`artist_PK_artistID`),
  KEY `fk_artistsband_band1_idx` (`band_PK_bandID`),
  CONSTRAINT `fk_artistsband_artist1` FOREIGN KEY (`artist_PK_artistID`) REFERENCES `artist` (`PK_artistID`) ON DELETE CASCADE,
  CONSTRAINT `fk_artistsband_band1` FOREIGN KEY (`band_PK_bandID`) REFERENCES `band` (`PK_bandID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artistsband`
--

LOCK TABLES `artistsband` WRITE;
/*!40000 ALTER TABLE `artistsband` DISABLE KEYS */;
/*!40000 ALTER TABLE `artistsband` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add songs',15,'add_songs'),(26,'Can change songs',15,'change_songs'),(27,'Can delete songs',15,'delete_songs'),(28,'Can view songs',15,'view_songs'),(29,'Can add album',7,'add_album'),(30,'Can change album',7,'change_album'),(31,'Can delete album',7,'delete_album'),(32,'Can view album',7,'view_album'),(33,'Can add albummusica',10,'add_albummusica'),(34,'Can change albummusica',10,'change_albummusica'),(35,'Can delete albummusica',10,'delete_albummusica'),(36,'Can view albummusica',10,'view_albummusica'),(37,'Can add albumartist',8,'add_albumartist'),(38,'Can change albumartist',8,'change_albumartist'),(39,'Can delete albumartist',8,'delete_albumartist'),(40,'Can view albumartist',8,'view_albumartist'),(41,'Can add artist',11,'add_artist'),(42,'Can change artist',11,'change_artist'),(43,'Can delete artist',11,'delete_artist'),(44,'Can view artist',11,'view_artist'),(45,'Can add artistsband',12,'add_artistsband'),(46,'Can change artistsband',12,'change_artistsband'),(47,'Can delete artistsband',12,'delete_artistsband'),(48,'Can view artistsband',12,'view_artistsband'),(49,'Can add albumband',9,'add_albumband'),(50,'Can change albumband',9,'change_albumband'),(51,'Can delete albumband',9,'delete_albumband'),(52,'Can view albumband',9,'view_albumband'),(53,'Can add band',13,'add_band'),(54,'Can change band',13,'change_band'),(55,'Can delete band',13,'delete_band'),(56,'Can view band',13,'view_band'),(57,'Can add playlist',14,'add_playlist'),(58,'Can change playlist',14,'change_playlist'),(59,'Can delete playlist',14,'delete_playlist'),(60,'Can view playlist',14,'view_playlist'),(61,'Can add songsplaylist',16,'add_songsplaylist'),(62,'Can change songsplaylist',16,'change_songsplaylist'),(63,'Can delete songsplaylist',16,'delete_songsplaylist'),(64,'Can view songsplaylist',16,'view_songsplaylist'),(65,'Can add users',17,'add_users'),(66,'Can change users',17,'change_users'),(67,'Can delete users',17,'delete_users'),(68,'Can view users',17,'view_users'),(69,'Can add usersplaylists',18,'add_usersplaylists'),(70,'Can change usersplaylists',18,'change_usersplaylists'),(71,'Can delete usersplaylists',18,'delete_usersplaylists'),(72,'Can view usersplaylists',18,'view_usersplaylists');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `band`
--

DROP TABLE IF EXISTS `band`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `band` (
  `PK_bandID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(300) DEFAULT NULL,
  `imageBand` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`PK_bandID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `band`
--

LOCK TABLES `band` WRITE;
/*!40000 ALTER TABLE `band` DISABLE KEYS */;
/*!40000 ALTER TABLE `band` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'api','album'),(8,'api','albumartist'),(9,'api','albumband'),(10,'api','albummusica'),(11,'api','artist'),(12,'api','artistsband'),(13,'api','band'),(14,'api','playlist'),(15,'api','songs'),(16,'api','songsplaylist'),(17,'api','users'),(18,'api','usersplaylists'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-04-05 18:50:12.803561'),(2,'auth','0001_initial','2026-04-05 18:50:13.747517'),(3,'admin','0001_initial','2026-04-05 18:50:13.975789'),(4,'admin','0002_logentry_remove_auto_add','2026-04-05 18:50:13.988026'),(5,'admin','0003_logentry_add_action_flag_choices','2026-04-05 18:50:13.997659'),(6,'contenttypes','0002_remove_content_type_name','2026-04-05 18:50:14.121075'),(7,'auth','0002_alter_permission_name_max_length','2026-04-05 18:50:14.221673'),(8,'auth','0003_alter_user_email_max_length','2026-04-05 18:50:14.247683'),(9,'auth','0004_alter_user_username_opts','2026-04-05 18:50:14.258455'),(10,'auth','0005_alter_user_last_login_null','2026-04-05 18:50:14.360654'),(11,'auth','0006_require_contenttypes_0002','2026-04-05 18:50:14.366085'),(12,'auth','0007_alter_validators_add_error_messages','2026-04-05 18:50:14.374013'),(13,'auth','0008_alter_user_username_max_length','2026-04-05 18:50:14.479893'),(14,'auth','0009_alter_user_last_name_max_length','2026-04-05 18:50:14.581673'),(15,'auth','0010_alter_group_name_max_length','2026-04-05 18:50:14.602814'),(16,'auth','0011_update_proxy_permissions','2026-04-05 18:50:14.612937'),(17,'auth','0012_alter_user_first_name_max_length','2026-04-05 18:50:14.731896'),(18,'sessions','0001_initial','2026-04-05 18:50:14.789846'),(19,'api','0001_initial','2026-04-09 00:41:01.639694'),(20,'api','0002_generomusical_alter_songs_options','2026-04-09 00:53:05.391331');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generomusical`
--

DROP TABLE IF EXISTS `generomusical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generomusical` (
  `idgeneroMusical` int NOT NULL,
  `nomeGenero` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`idgeneroMusical`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generomusical`
--

LOCK TABLES `generomusical` WRITE;
/*!40000 ALTER TABLE `generomusical` DISABLE KEYS */;
/*!40000 ALTER TABLE `generomusical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playlist`
--

DROP TABLE IF EXISTS `playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playlist` (
  `PK_playlistID` int NOT NULL AUTO_INCREMENT,
  `plName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PK_playlistID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlist`
--

LOCK TABLES `playlist` WRITE;
/*!40000 ALTER TABLE `playlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs` (
  `PK_songID` int NOT NULL AUTO_INCREMENT,
  `songTitle` varchar(150) NOT NULL,
  `timeMusic` time DEFAULT NULL,
  `lyrics` text,
  `generomusical_idgeneroMusical` int NOT NULL,
  PRIMARY KEY (`PK_songID`),
  KEY `songs_generomusical_FK` (`generomusical_idgeneroMusical`),
  CONSTRAINT `songs_generomusical_FK` FOREIGN KEY (`generomusical_idgeneroMusical`) REFERENCES `generomusical` (`idgeneroMusical`) ON DELETE SET DEFAULT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songsplaylist`
--

DROP TABLE IF EXISTS `songsplaylist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songsplaylist` (
  `playlist_PK_playlistID` int NOT NULL,
  `songs_PK_songID` int NOT NULL,
  PRIMARY KEY (`playlist_PK_playlistID`,`songs_PK_songID`),
  KEY `fk_songsPlaylist_playlist1_idx` (`playlist_PK_playlistID`),
  KEY `fk_songsPlaylist_songs1_idx` (`songs_PK_songID`),
  CONSTRAINT `fk_songsPlaylist_playlist1` FOREIGN KEY (`playlist_PK_playlistID`) REFERENCES `playlist` (`PK_playlistID`) ON DELETE CASCADE,
  CONSTRAINT `fk_songsPlaylist_songs1` FOREIGN KEY (`songs_PK_songID`) REFERENCES `songs` (`PK_songID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songsplaylist`
--

LOCK TABLES `songsplaylist` WRITE;
/*!40000 ALTER TABLE `songsplaylist` DISABLE KEYS */;
/*!40000 ALTER TABLE `songsplaylist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `PK_userID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(250) DEFAULT NULL,
  `senha` varchar(45) NOT NULL,
  `profilePicture` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`PK_userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usersplaylists`
--

DROP TABLE IF EXISTS `usersplaylists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usersplaylists` (
  `users_PK_userID` int NOT NULL,
  `playlist_PK_playlistID` int NOT NULL,
  PRIMARY KEY (`users_PK_userID`,`playlist_PK_playlistID`),
  KEY `fk_usersplaylists_users1_idx` (`users_PK_userID`),
  KEY `fk_usersplaylists_playlist1_idx` (`playlist_PK_playlistID`),
  CONSTRAINT `fk_usersplaylists_playlist1` FOREIGN KEY (`playlist_PK_playlistID`) REFERENCES `playlist` (`PK_playlistID`) ON DELETE CASCADE,
  CONSTRAINT `fk_usersplaylists_users1` FOREIGN KEY (`users_PK_userID`) REFERENCES `users` (`PK_userID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersplaylists`
--

LOCK TABLES `usersplaylists` WRITE;
/*!40000 ALTER TABLE `usersplaylists` DISABLE KEYS */;
/*!40000 ALTER TABLE `usersplaylists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'spotlike'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-08 21:54:21
