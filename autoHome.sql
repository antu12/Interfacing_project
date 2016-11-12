-- MySQL Script generated by MySQL Workbench
-- 11/07/16 02:27:43
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema autohome
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema autohome
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `autohome` DEFAULT CHARACTER SET utf8 ;
USE `autohome` ;

-- -----------------------------------------------------
-- Table `autohome`.`switch`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `autohome`.`switch` ;

CREATE TABLE IF NOT EXISTS `autohome`.`switch` (
  `id_switch` VARCHAR(255) NOT NULL,
  `sw_1` TINYINT(1) NULL,
  `sw_2` TINYINT(1) NULL,
  `sw_3` TINYINT(1) NULL,
  `sw_4` TINYINT(1) NULL,
  `sw_5` TINYINT(1) NULL,
  PRIMARY KEY (`id_switch`),
  UNIQUE INDEX `id_switch_UNIQUE` (`id_switch` ASC))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `autohome`.`switch`
-- -----------------------------------------------------
START TRANSACTION;
USE `autohome`;
INSERT INTO `autohome`.`switch` (`id_switch`, `sw_1`, `sw_2`, `sw_3`, `sw_4`, `sw_5`) VALUES ('r1', 0, 1, 0, 0, 1);

COMMIT;

