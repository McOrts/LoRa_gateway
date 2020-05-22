--
-- Table structure for table `system_info_RAK831`
--

DROP TABLE IF EXISTS `system_info_RAK831`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_info_RAK831` (
  `load` double NOT NULL,
  `ram` tinyint(4) NOT NULL,
  `disk` tinyint(4) NOT NULL,
  `temperature` double NOT NULL,
  `dtg` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;