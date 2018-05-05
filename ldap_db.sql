-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 05, 2018 at 06:50 PM
-- Server version: 5.5.60-0+deb8u1
-- PHP Version: 5.6.33-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ldap_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `groupes`
--

CREATE TABLE IF NOT EXISTS `groupes` (
`id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `numGroupe` int(11) NOT NULL,
  `description` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `groupes`
--

INSERT INTO `groupes` (`id`, `nom`, `numGroupe`, `description`) VALUES
(1, 'administrateur', 1, 'groupe des administrateurs'),
(2, 'developpeur', 2, 'groupe des développeurs'),
(3, 'bd', 3, 'groupe des bandes dessinées');

-- --------------------------------------------------------

--
-- Table structure for table `groupe_membres`
--

CREATE TABLE IF NOT EXISTS `groupe_membres` (
  `idUtilisateur` int(11) NOT NULL,
  `idGroupe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `groupe_membres`
--

INSERT INTO `groupe_membres` (`idUtilisateur`, `idGroupe`) VALUES
(1, 1),
(2, 1),
(1, 2),
(2, 2),
(3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `utilisateurs`
--

CREATE TABLE IF NOT EXISTS `utilisateurs` (
`id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `identifiant` varchar(255) NOT NULL,
  `motDePasse` varchar(255) NOT NULL,
  `numUtilisateur` varchar(255) NOT NULL,
  `numGroupe` varchar(255) NOT NULL,
  `adresseCourriel` varchar(255) NOT NULL,
  `dateFinSejour` date NOT NULL,
  `isUpdate` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `utilisateurs`
--

INSERT INTO `utilisateurs` (`id`, `nom`, `prenom`, `identifiant`, `motDePasse`, `numUtilisateur`, `numGroupe`, `adresseCourriel`, `dateFinSejour`, `isUpdate`) VALUES
(1, 'Kheiry', 'Ismail', 'ikheiry', '034e8c59b49cdc2eb19851e4401e9949', '1000', '500', 'ikheiry@kheiry.fr', '2018-05-10', 0),
(2, 'mansouri', 'salah eddine', 'semansouri', '9d861a9302d3456c8c2694829be5e60a', '2', '1', 'semansouri@kheiry.fr', '2018-05-31', 0),
(3, 'ku', 'go', 'goku', '8d2ea1afa94c834a448c645ec3878650', '3', '2', 'goku@kheiry.fr', '2018-05-31', 0);

--
-- Triggers `utilisateurs`
--
DELIMITER //
CREATE TRIGGER `before_isUpdate` BEFORE UPDATE ON `utilisateurs`
 FOR EACH ROW BEGIN
    IF OLD.isUpdate = 0
      THEN
        SET NEW.isUpdate = 1;
    END IF;
END
//
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `groupes`
--
ALTER TABLE `groupes`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `NomGroupe` (`nom`), ADD UNIQUE KEY `NumGroupe` (`numGroupe`);

--
-- Indexes for table `groupe_membres`
--
ALTER TABLE `groupe_membres`
 ADD PRIMARY KEY (`idUtilisateur`,`idGroupe`), ADD KEY `IdGroupe` (`idGroupe`);

--
-- Indexes for table `utilisateurs`
--
ALTER TABLE `utilisateurs`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `Identifiant` (`identifiant`), ADD UNIQUE KEY `NumUtilisateur` (`numUtilisateur`), ADD UNIQUE KEY `AdresseCourriel` (`adresseCourriel`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `groupes`
--
ALTER TABLE `groupes`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `utilisateurs`
--
ALTER TABLE `utilisateurs`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `groupe_membres`
--
ALTER TABLE `groupe_membres`
ADD CONSTRAINT `IdGroupe` FOREIGN KEY (`idGroupe`) REFERENCES `groupes` (`id`),
ADD CONSTRAINT `IdUtilisateur` FOREIGN KEY (`idUtilisateur`) REFERENCES `utilisateurs` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
