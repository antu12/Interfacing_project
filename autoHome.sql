-- phpMyAdmin SQL Dump
-- version 4.3.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 25, 2016 at 05:26 PM
-- Server version: 5.6.24
-- PHP Version: 5.6.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `autohome`
--
CREATE DATABASE IF NOT EXISTS `autohome` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `autohome`;

-- --------------------------------------------------------

--
-- Table structure for table `switch`
--

DROP TABLE IF EXISTS `switch`;
CREATE TABLE IF NOT EXISTS `switch` (
  `id_switch` varchar(255) NOT NULL,
  `sw_1` tinyint(1) DEFAULT NULL,
  `sw_2` tinyint(1) DEFAULT NULL,
  `sw_3` tinyint(1) DEFAULT NULL,
  `temp` varchar(65) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `switch`
--

INSERT INTO `switch` (`id_switch`, `sw_1`, `sw_2`, `sw_3`, `temp`) VALUES
('room1', 1, 0, 1, '24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `switch`
--
ALTER TABLE `switch`
  ADD PRIMARY KEY (`id_switch`), ADD UNIQUE KEY `id_switch_UNIQUE` (`id_switch`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
