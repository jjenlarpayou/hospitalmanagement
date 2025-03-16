-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 21, 2023 at 12:25 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `Doctor`
--

CREATE TABLE `Doctor` (
  `Doctor_id` varchar(6) NOT NULL,
  `D_fname` varchar(50) NOT NULL,
  `D_lname` varchar(50) NOT NULL,
  `D_address` varchar(40) NOT NULL,
  `D_phonenumber` varchar(10) NOT NULL,
  `D_email` varchar(40) NOT NULL,
  `D_speciality` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Doctor`
--

INSERT INTO `Doctor` (`Doctor_id`, `D_fname`, `D_lname`, `D_address`, `D_phonenumber`, `D_email`, `D_speciality`) VALUES
('D10000', 'James', 'Dean', 'Kessels Rd, Upper Mount Gravatt QLD 4122', '0424456789', 'Dean@gmail.com', 'Cardiologists'),
('D10001', 'Kirk', 'Douglas', 'Kessels Rd, Upper Gravatt QLD 4122', '0424121678', 'Douglas@gmail.com', 'Anesthesiologists'),
('D10002', 'Natalie', 'Wood', '152 Turton St, Sunnybank QLD 4109', '0424121123', 'Wood@gmail.com', 'Endocrinologists'),
('D10003', 'Marcello', 'Mastroianni', 'Westfield Mt, Kessels Rd, QLD 4122', '0404128124', 'Mastroianni@gmail.com', 'Dermatologists'),
('D10004', 'Joan', 'Crawford', '224 Wishart Rd, Mount Gravatt QLD 4122', '0404567124', 'Crawford@gmail.com', 'Dermatologists');

-- --------------------------------------------------------

--
-- Table structure for table `Inpatient`
--

CREATE TABLE `Inpatient` (
  `Patient_id` int(11) NOT NULL,
  `R_id` char(4) DEFAULT NULL,
  `Ipt_incomingdate` date DEFAULT NULL,
  `Ipt_outgoingdate` date DEFAULT NULL,
  `P_check` enum('Check','Not check','Discharge') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Inpatient`
--

INSERT INTO `Inpatient` (`Patient_id`, `R_id`, `Ipt_incomingdate`, `Ipt_outgoingdate`, `P_check`) VALUES
(10000, 'A100', '2023-03-01', '2023-03-02', 'Discharge'),
(10001, 'A100', '2023-05-03', '2023-05-17', 'Discharge'),
(10004, 'B100', '2023-02-01', '2023-02-10', 'Discharge'),
(10005, 'C100', '2023-04-20', '2023-05-01', 'Discharge'),
(10006, 'D100', '2023-01-19', '2023-03-05', 'Discharge');

-- --------------------------------------------------------

--
-- Table structure for table `Medical Record`
--

CREATE TABLE `Medical Record` (
  `Mrecord_id` varchar(5) NOT NULL,
  `Doctor_id` varchar(6) NOT NULL,
  `Patient_id` int(11) NOT NULL,
  `Description` varchar(200) NOT NULL,
  `Prescription` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Medical Record`
--

INSERT INTO `Medical Record` (`Mrecord_id`, `Doctor_id`, `Patient_id`, `Description`, `Prescription`) VALUES
('10000', 'D10000', 10000, 'Acute Tonsilitis', 'Paracetamol 20\r\nChlorpheiramine 20'),
('10001', 'D10001', 10001, 'Acute Diarrhea', 'Oral Rehydration salt 5'),
('10002', 'D10002', 10002, 'Benign paroxysmal positional vertigo', 'Dimenhydrinate 20'),
('10003', 'D10003', 10003, 'De Quervain right hand', 'Diclofinac Na 20'),
('10004', 'D10004', 10004, 'Tension headache', 'Paracetamol 20'),
('10005', 'D10001', 10005, 'Covid-19 Infection', 'Paracetamol 20\r\nDextromethorphan 20'),
('10006', 'D10002', 10006, 'Alcoholic gastritis', 'Alum milk30cc 1\r\nBuscopan 20\r\n'),
('10007', 'D10003', 10007, 'Hemorrhoid', 'Diosmin 40');

-- --------------------------------------------------------

--
-- Table structure for table `Medicine`
--

CREATE TABLE `Medicine` (
  `Medicine_id` varchar(5) NOT NULL,
  `Mdc_medname` varchar(50) NOT NULL,
  `Mdc_incomingdate` date NOT NULL,
  `Mdc_expdate` date NOT NULL,
  `Mdc_tablet` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Medicine`
--

INSERT INTO `Medicine` (`Medicine_id`, `Mdc_medname`, `Mdc_incomingdate`, `Mdc_expdate`, `Mdc_tablet`) VALUES
('10000', 'Paracetamol', '2023-04-04', '2024-05-01', 1000),
('10001', 'Chlorpheiramine', '2023-03-07', '2023-05-20', 500),
('10002', 'Oral Rehydration salt', '2023-02-06', '2023-05-03', 700),
('10003', 'Dimenhydrinate', '2022-05-19', '2023-07-05', 300),
('10004', 'Diclofinac Na', '2023-01-02', '2023-08-10', 200),
('10005', 'Dextromethorphan', '2023-03-07', '2023-05-02', 50),
('10006', 'Alum milk 30cc', '2023-03-06', '2023-08-16', 70),
('10007', 'Buscopan', '2023-04-03', '2023-10-12', 100),
('10008', 'Diosmin', '2023-03-22', '2023-11-03', 80),
('20001', 'Paracetamol', '2023-05-25', '2024-05-01', 1500);

-- --------------------------------------------------------

--
-- Table structure for table `Outpatient`
--

CREATE TABLE `Outpatient` (
  `Patient_id` int(11) NOT NULL,
  `Opt_incomingdate` date DEFAULT NULL,
  `Opt_outgoingdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Outpatient`
--

INSERT INTO `Outpatient` (`Patient_id`, `Opt_incomingdate`, `Opt_outgoingdate`) VALUES
(10002, '2023-05-03', '2023-05-03'),
(10003, '2023-05-11', '2023-05-11'),
(10007, '2023-05-10', '2023-05-10');

-- --------------------------------------------------------

--
-- Table structure for table `Patient`
--

CREATE TABLE `Patient` (
  `Patient_id` int(11) NOT NULL,
  `P_fname` varchar(30) NOT NULL,
  `P_lname` varchar(30) NOT NULL,
  `P_gender` enum('Male','Female') NOT NULL,
  `P_dob` date NOT NULL,
  `P_address` varchar(60) NOT NULL,
  `P_phonenumber` varchar(10) NOT NULL,
  `P_status` enum('Inpatient','Outpatient') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Patient`
--

INSERT INTO `Patient` (`Patient_id`, `P_fname`, `P_lname`, `P_gender`, `P_dob`, `P_address`, `P_phonenumber`, `P_status`) VALUES
(10000, 'Jack', 'Nicholson', 'Male', '1968-11-01', '149 Merivale St. Brisbane', '0402445678', 'Inpatient'),
(10001, 'Marlon', 'Brando', 'Male', '1978-05-02', '5 Boundary St, Brisbane City QLD 4000', '0405790442', 'Inpatient'),
(10002, 'Denzel', 'Washington', 'Male', '1988-03-13', 'Corner Creek &, Wecker Rd, Mount Gravatt QLD 4122', '0434888999', 'Outpatient'),
(10003, 'Katharine', 'Hepburn', 'Female', '1990-02-05', 'Mount Cotton &, Pittwin Rd N, Capalaba QLD 4157', '0408927474', 'Outpatient'),
(10004, 'Meryl', 'Streep', 'Female', '1945-06-14', '9 Brookfield Rd, Kenmore QLD 4069', '0412456789', 'Inpatient'),
(10005, 'Elizabeth', 'Taylor', 'Female', '1933-07-12', '156 Inala Ave, Inala QLD 4077', '0407662345', 'Inpatient'),
(10006, 'Gregory', 'Peck', 'Male', '2012-11-05', '481 Settlement Rd, Keperra QLD 4054', '0489227897', 'Inpatient'),
(10007, 'Leonardo', ' DiCaprio', 'Male', '2008-05-15', '18th Ave, Brisbane Airport QLD 4008', '0420774665', 'Outpatient');

-- --------------------------------------------------------

--
-- Table structure for table `Roomtype`
--

CREATE TABLE `Roomtype` (
  `R_id` varchar(4) NOT NULL,
  `Type` enum('Medical-Surgical','Intensive Care','Maternity Care','Behavioral and Mental Health') NOT NULL,
  `R_cost` int(11) DEFAULT NULL,
  `R_quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Roomtype`
--

INSERT INTO `Roomtype` (`R_id`, `Type`, `R_cost`, `R_quantity`) VALUES
('A100', 'Medical-Surgical', 1000, 5),
('B100', 'Intensive Care', 2000, 10),
('C100', 'Maternity Care', 3000, 15),
('D100', 'Behavioral and Mental Health', 1500, 20);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Doctor`
--
ALTER TABLE `Doctor`
  ADD PRIMARY KEY (`Doctor_id`);

--
-- Indexes for table `Inpatient`
--
ALTER TABLE `Inpatient`
  ADD KEY `Patient_id` (`Patient_id`) USING BTREE,
  ADD KEY `Inpatient_room` (`R_id`);

--
-- Indexes for table `Medical Record`
--
ALTER TABLE `Medical Record`
  ADD PRIMARY KEY (`Mrecord_id`),
  ADD KEY `Patient_id` (`Patient_id`) USING BTREE,
  ADD KEY `Doctor_id` (`Doctor_id`) USING BTREE;

--
-- Indexes for table `Medicine`
--
ALTER TABLE `Medicine`
  ADD PRIMARY KEY (`Medicine_id`);

--
-- Indexes for table `Outpatient`
--
ALTER TABLE `Outpatient`
  ADD KEY `Patient_id` (`Patient_id`) USING BTREE;

--
-- Indexes for table `Patient`
--
ALTER TABLE `Patient`
  ADD PRIMARY KEY (`Patient_id`) USING BTREE;

--
-- Indexes for table `Roomtype`
--
ALTER TABLE `Roomtype`
  ADD PRIMARY KEY (`R_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Inpatient`
--
ALTER TABLE `Inpatient`
  ADD CONSTRAINT `Inpatient_patient` FOREIGN KEY (`Patient_id`) REFERENCES `Patient` (`Patient_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Inpatient_room` FOREIGN KEY (`R_id`) REFERENCES `Roomtype` (`R_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Medical Record`
--
ALTER TABLE `Medical Record`
  ADD CONSTRAINT `Medical Record_doctor` FOREIGN KEY (`Doctor_id`) REFERENCES `Doctor` (`Doctor_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Medical Record_patient` FOREIGN KEY (`Patient_id`) REFERENCES `Patient` (`Patient_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Outpatient`
--
ALTER TABLE `Outpatient`
  ADD CONSTRAINT `Outpatient_patient` FOREIGN KEY (`Patient_id`) REFERENCES `Patient` (`Patient_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
