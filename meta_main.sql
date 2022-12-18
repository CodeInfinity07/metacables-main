-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 13, 2022 at 02:24 PM
-- Server version: 8.0.31-0ubuntu0.22.04.1
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `meta_main2`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill_book`
--

CREATE TABLE `bill_book` (
  `id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `customer_phone` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cust_trans`
--

CREATE TABLE `cust_trans` (
  `customer_id` int NOT NULL,
  `customer_trans_id` int NOT NULL,
  `data` varchar(10) NOT NULL,
  `amount` int NOT NULL,
  `inv_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `daily_expenses`
--

CREATE TABLE `daily_expenses` (
  `id` int NOT NULL,
  `expense_name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `expense_cost` int NOT NULL,
  `date` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `contact_no` bigint DEFAULT NULL,
  `date` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `salary` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `id` int NOT NULL,
  `item_id` int NOT NULL,
  `quantity` int NOT NULL,
  `expense` int NOT NULL,
  `date` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`id`, `item_id`, `quantity`, `expense`, `date`) VALUES
(1, 25, 86, 1750, '2022-08-04'),
(2, 26, 70, 1750, '2022-08-04'),
(3, 31, 30, 3600, '2022-08-04'),
(4, 32, 30, 3600, '2022-08-04'),
(5, 55, 51, 450, '2022-08-31'),
(6, 55, 51, 450, '2022-08-31'),
(7, 53, 50, 600, '2022-09-05'),
(8, 54, 50, 600, '2022-09-06'),
(9, 33, 60, 1100, '2022-09-06'),
(10, 34, 75, 1100, '2022-09-06'),
(11, 39, 24, 2400, '2022-09-06'),
(12, 40, 24, 2400, '2022-09-06'),
(13, 51, 30, 1600, '2022-10-18'),
(14, 58, 29, 2600, '2022-10-23'),
(15, 57, 36, 3700, '2022-10-27'),
(16, 49, 35, 2500, '2022-10-27'),
(17, 50, 16, 1900, '2022-10-27'),
(18, 37, 25, 1100, '2022-11-05'),
(19, 45, 31, 2600, '2022-11-05'),
(20, 46, 21, 5600, '2022-11-05'),
(21, 33, 60, 1100, '2022-11-09'),
(22, 34, 15, 1100, '2022-11-09'),
(23, 1, 41, 2600, '2022-11-12'),
(24, 2, 15, 2600, '2022-11-12'),
(25, 7, 10, 5200, '2022-11-12'),
(26, 8, 10, 5200, '2022-11-12'),
(27, 4, 19, 2600, '2022-11-12'),
(28, 41, 15, 6800, '2022-11-14'),
(29, 43, 15, 6800, '2022-11-14'),
(30, 3, 3, 2600, '2022-11-16'),
(31, 57, 40, 3700, '2022-11-22'),
(32, 49, 40, 2500, '2022-11-22'),
(33, 7, 25, 5200, '2022-11-24'),
(34, 8, 15, 5200, '2022-11-24'),
(35, 1, 12, 2600, '2022-11-24'),
(36, 48, 30, 4500, '2022-11-28'),
(37, 47, 37, 2100, '2022-11-28'),
(38, 23, 10, 4250, '2022-11-30'),
(39, 24, 10, 4250, '2022-11-30'),
(40, 17, 37, 2100, '2022-11-30'),
(41, 18, 26, 2100, '2022-11-30'),
(42, 52, 67, 650, '2022-12-07'),
(43, 39, 25, 2400, '2022-12-08'),
(44, 40, 25, 2400, '2022-12-08'),
(45, 33, 171, 1100, '2022-12-08'),
(46, 34, 110, 1100, '2022-12-08'),
(47, 37, 17, 1100, '2022-12-08'),
(48, 4, 12, 2600, '2022-12-10'),
(49, 2, 16, 2600, '2022-12-10'),
(50, 1, 33, 2600, '2022-12-10'),
(51, 7, 9, 5200, '2022-12-10'),
(52, 8, 4, 5200, '2022-12-10');

-- --------------------------------------------------------

--
-- Table structure for table `payouts`
--

CREATE TABLE `payouts` (
  `id` int NOT NULL,
  `employee_id` int NOT NULL,
  `amount` int NOT NULL,
  `date` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `purchase_bill`
--

CREATE TABLE `purchase_bill` (
  `purchase_id` int NOT NULL,
  `balance` int NOT NULL,
  `date` varchar(10) NOT NULL,
  `mode` int NOT NULL,
  `amount` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `purchase_stock`
--

CREATE TABLE `purchase_stock` (
  `purchase_id` int NOT NULL,
  `item_no` int NOT NULL,
  `qty` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `raw_materials`
--

CREATE TABLE `raw_materials` (
  `id` int NOT NULL,
  `name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `quantity` int NOT NULL,
  `price` bigint NOT NULL,
  `date` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `registered_customers`
--

CREATE TABLE `registered_customers` (
  `id` int NOT NULL,
  `customer_name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `customer_contact` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `customer_address` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registered_customers`
--

INSERT INTO `registered_customers` (`id`, `customer_name`, `customer_contact`, `customer_address`) VALUES
(8, 'Abdul Rehman', '', 'Lahore'),
(9, 'Amanat Hardware Store', '', 'Sahianwala FSD'),
(10, 'Bismillah Electric Store', '', 'JOHAL ADDA'),
(11, 'Usman Electric Store', '', 'Bhai Wala'),
(12, 'Imran Electric Store', '', 'Millat Chowk'),
(13, 'Haideri Electric Store', '', 'Rasoolpur Gaedri'),
(14, 'Dubai Electric Store', '', 'D Type FSD'),
(15, 'Abid Electric Store', '', 'Al Noor Garden'),
(16, 'Usman Autos', '', 'Balochni Adda'),
(17, 'Mazhar Electric Store', '', 'Balochni Adda'),
(18, 'Makkah Electric Store', '', 'Johal Adda'),
(19, 'Hajveri Electric Store', '', '61 Chak'),
(20, 'Ibrahim Electric Store', '', 'Satyana Road'),
(21, 'Ababeel Electric Store', '', 'Khurrianwala');

-- --------------------------------------------------------

--
-- Table structure for table `sales_bill`
--

CREATE TABLE `sales_bill` (
  `id` int NOT NULL,
  `inv_id` varchar(50) NOT NULL,
  `date` varchar(10) NOT NULL,
  `amount` int NOT NULL,
  `customer_id` int NOT NULL,
  `is_registered` int NOT NULL DEFAULT '0',
  `is_paid` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sales_stocks`
--

CREATE TABLE `sales_stocks` (
  `id` int NOT NULL,
  `inv_id` varchar(50) NOT NULL,
  `item_no` int NOT NULL,
  `qty` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `stocks`
--

CREATE TABLE `stocks` (
  `name` varchar(50) NOT NULL,
  `price` int NOT NULL,
  `color` varchar(100) DEFAULT NULL,
  `guage` varchar(100) NOT NULL,
  `item_no` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stocks`
--

INSERT INTO `stocks` (`name`, `price`, `color`, `guage`, `item_no`) VALUES
('3/.029 Special', 3320, 'Red', '29', 1),
('3/.029 Special', 3320, 'Black', '29', 2),
('3/.029 Special', 3320, 'Blue', '29', 3),
('3/.029 Special', 3320, 'White', '29', 4),
('3/.029 Special', 3320, 'Green', '29', 5),
('3/.029 Special', 3320, 'Yellow', '29', 6),
('7/.029 Special', 6740, 'Red', '29', 7),
('7/.029 Special', 6740, 'Black', '29', 8),
('3/.029 Nitro', 2890, 'Red', '29', 9),
('3/.029 Nitro', 2890, 'Black', '29', 10),
('3/.029 Nitro', 2890, 'Blue', '29', 11),
('3/.029 Nitro', 2890, 'Green', '29', 12),
('3/.029 Nitro', 2890, 'White', '29', 13),
('3/.029 Nitro', 2890, 'Yellow', '29', 14),
('7/.029 Nitro', 5750, 'Red', '29', 15),
('7/.029 Nitro', 5750, 'Black', '29', 16),
('3/.029', 2770, 'Red', '27', 17),
('3/.029', 2770, 'Black', '27', 18),
('3/.029', 2770, 'Blue', '27', 19),
('3/.029', 2770, 'Green', '27', 20),
('3/.029', 2770, 'White', '27', 21),
('3/.029', 2770, 'Yellow', '27', 22),
('7/.029', 5480, 'Red', '27', 23),
('7/.029', 5480, 'Black', '27', 24),
('3/.029', 2325, 'Red', '24', 25),
('3/.029', 2325, 'Black', '24', 26),
('3/.029', 2325, 'Blue', '24', 27),
('3/.029', 2325, 'Green', '24', 28),
('3/.029', 2325, 'White', '24', 29),
('3/.029', 2325, 'Yellow', '24', 30),
('7/.029', 4410, 'Red', '24', 31),
('7/.029', 4410, 'Black', '24', 32),
('3/.029', 1545, 'Red', '20', 33),
('3/.029', 1545, 'Black', '20', 34),
('3/.029', 1545, 'Blue', '20', 35),
('3/.029', 1545, 'Green', '20', 36),
('3/.029', 1545, 'White', '20', 37),
('3/.029', 1545, 'Yellow', '20', 38),
('7/.029', 3250, 'Red', '20', 39),
('7/.029', 3250, 'Black', '20', 40),
('7/.036', 9045, 'Red', '32', 41),
('7/.044', 13765, 'Red', '42', 42),
('7/.036', 9045, 'Black', '32', 43),
('7/.044', 13765, 'Black', '42', 44),
('3/.029 Double core', 3365, 'Black', '20', 45),
('7/.029 Double core', 7150, 'Black', '20', 46),
('3/.029 Double core', 2900, 'Black', '17', 47),
('7/.029 Double core', 5850, 'Black', '17', 48),
('23/76 Gol ', 3475, 'White', '6', 49),
('23/76 Gol ', 2925, 'White', '4.5', 50),
('23/76 Flat ', 2250, 'White', '4.5', 51),
('23/76 Flat CC', 980, 'White', 'CC', 52),
('23/76 Single', 1020, 'Red', '4.5', 53),
('23/76 Single', 1020, 'Black', '4.5', 54),
('23/76 Single CC', 660, 'Red', 'CC', 55),
('23/76 Single CC', 660, 'Black', 'CC', 56),
('40/76 Gol', 4960, 'White', '6', 57),
('40/76 Gol', 3535, 'White', '4.5', 58),
('40/76 Gol CC', 1950, 'White', 'CC', 59),
('40/76 Flat CC', 1950, 'White', 'CC', 60),
('23/76 Gol CC', 1050, 'White', 'CC', 61),
('40/76 Flat', 3535, 'White', '4.5', 62);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sr` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sr`, `username`, `pass`) VALUES
(1, 'rashi1868', 'rashid1868'),
(3, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `wholesaler`
--

CREATE TABLE `wholesaler` (
  `whole_id` int NOT NULL,
  `whole_name` varchar(50) NOT NULL,
  `whole_phone` int NOT NULL,
  `whole_address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `whole_trans`
--

CREATE TABLE `whole_trans` (
  `whole_id` int NOT NULL,
  `purchase_id` int NOT NULL,
  `date` varchar(10) NOT NULL,
  `amount` int NOT NULL,
  `whole_trans` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `cust_trans`
--
ALTER TABLE `cust_trans`
  ADD PRIMARY KEY (`customer_trans_id`);

--
-- Indexes for table `daily_expenses`
--
ALTER TABLE `daily_expenses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payouts`
--
ALTER TABLE `payouts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchase_bill`
--
ALTER TABLE `purchase_bill`
  ADD PRIMARY KEY (`purchase_id`);

--
-- Indexes for table `raw_materials`
--
ALTER TABLE `raw_materials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registered_customers`
--
ALTER TABLE `registered_customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales_bill`
--
ALTER TABLE `sales_bill`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales_stocks`
--
ALTER TABLE `sales_stocks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stocks`
--
ALTER TABLE `stocks`
  ADD PRIMARY KEY (`item_no`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sr`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `wholesaler`
--
ALTER TABLE `wholesaler`
  ADD PRIMARY KEY (`whole_id`);

--
-- Indexes for table `whole_trans`
--
ALTER TABLE `whole_trans`
  ADD PRIMARY KEY (`whole_trans`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `daily_expenses`
--
ALTER TABLE `daily_expenses`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `payouts`
--
ALTER TABLE `payouts`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `raw_materials`
--
ALTER TABLE `raw_materials`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `registered_customers`
--
ALTER TABLE `registered_customers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `sales_bill`
--
ALTER TABLE `sales_bill`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sales_stocks`
--
ALTER TABLE `sales_stocks`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stocks`
--
ALTER TABLE `stocks`
  MODIFY `item_no` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sr` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
