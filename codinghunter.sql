-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2024 at 06:08 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codinghunter`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(10) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(20) NOT NULL,
  `ph_no` varchar(12) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `ph_no`, `msg`, `date`) VALUES
(1, 'first blog of the Website', 'first@gmail.com', '1234567890', 'This is first blog of the our website', '2024-04-09 19:46:54'),
(2, 'dw,,w', 'second@gamil.com', '134432323423', 'rlwlerlelrle;rlew;l', '2024-04-10 09:05:36'),
(3, 'fjeoje', 'erjeojreo@gmail.com', '4234234234', 'rkwe ekrelk lrk elkr elkre', '2024-04-10 09:49:16'),
(4, 'ifier', 'riieii@gmail.com', '12232243243', 'eirieifini fnifn r fnri rin ', '2024-04-10 10:28:14'),
(5, 'kfwere', 'wkrkkkr@gmail.com', '13121231242', 'tjowetoew okowko eko e', '2024-04-10 16:37:36'),
(6, 'kfwere', 'wkrkkkr@gmail.com', '13121231242', 'tjowetoew okowko eko e', '2024-04-10 16:48:26'),
(7, 'j rktjkrjt', 'tjjtjr@gmail.com', '13435345343', 'rkekrk m krmke rmkrm tkr m', '2024-04-11 08:28:13'),
(8, 'check contact', 'cheie@gmail.com', '2234234344', 'this is checking for the contact form working or not', '2024-04-12 11:38:27');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'What is NLP', 'Let\'s Learn  About NLP ', 'nlp-blog', 'Natural language processing, or NLP, combines computational linguistics—rule-based modeling of human language—with statistical and machine learning models to enable computers and digital devices to recognize, understand and generate text and speech.', 'post-bg.jpg', '2024-04-16 23:55:30'),
(2, 'second Blog', 'This is second Blog.', 'second-blog', 'This second Blog of the our website you need to fetch some blog in the websites.', 'about-bg.jpg', '2024-04-10 22:38:17'),
(3, 'third Blog', 'This is third Blog.', 'third-blog', 'This third Blog of the our website you need to fetch some blog in the websites.', 'about-bg.jpg', '2024-04-10 22:38:17'),
(4, 'fourth Blog', 'This is fourth Blog.', 'fourth-blog', 'This fourth Blog of the our website you need to fetch some blog in the websites.', 'about-bg.jpg', '2024-04-10 22:38:17'),
(6, 'i wkre kekrj ek', 'rkek elk el kekl ', 'new-post5', ' ek ekr ekkw le lelkel ', 'home-bg.jpg', '2024-04-17 09:05:58'),
(7, 'orowprweor ', 'rkwelk lel klek lrkw ', 'new-post5', 'rwel k ke lkwlke lwklwl', 'home-bg.jpg', '2024-04-17 09:23:17'),
(8, 'hwei ieirw heirhe wi', 'rwei jowej iore iojwj', 'new-post8', 'rek jkrk jrk jekjekjwelkjlkj kl lkj', 'home-bg.jpg', '2024-04-17 09:25:23');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
