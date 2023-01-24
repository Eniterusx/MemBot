-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Czas generowania: 16 Sty 2023, 20:46
-- Wersja serwera: 10.5.15-MariaDB-0+deb11u1
-- Wersja PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `dominikb`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `banned`
--

CREATE TABLE `banned` (
  `report_id` int(32) NOT NULL,
  `date_of_ban` timestamp NOT NULL DEFAULT current_timestamp(),
  `date_of_unban` timestamp NULL DEFAULT NULL,
  `reason_of_ban` text DEFAULT '"Unspecifed."'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pictures`
--

CREATE TABLE `pictures` (
  `picture_id` int(32) NOT NULL,
  `user_id` int(32) NOT NULL,
  `file_name` varchar(512) NOT NULL,
  `file_type` varchar(25) NOT NULL,
  `url` text NOT NULL,
  `image_hash` text NOT NULL,
  `delete_hash` text NOT NULL,
  `image_category` varchar(64) NOT NULL,
  `date_of_submission` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pictures`
--

INSERT INTO `pictures` (`picture_id`, `user_id`, `file_name`, `file_type`, `url`, `image_hash`, `delete_hash`, `image_category`, `date_of_submission`) VALUES
(5331, 1422, 'ibuprofen', 'image/jpeg', 'https://i.imgur.com/iyePh08.jpeg', 'iyePh08', 'sqhoGJb6Mpo8N0Y', 'Empty', '2023-01-14 18:53:37'),
(5344, 1429, 'spanish inquisition', 'image/png', 'https://i.imgur.com/RkGzhj1.png', 'RkGzhj1', 'TQd9q0T4ZLzazPi', 'Empty', '2023-01-14 18:56:13'),
(5356, 1422, 'pierogi', 'image/png', 'https://i.imgur.com/6fQO70f.png', '6fQO70f', 'xQdE06z0IMsyQY8', 'Empty', '2023-01-14 18:58:05'),
(5385, 1423, 'groźne pieseły', 'image/jpeg', 'https://i.imgur.com/tYdiR0n.jpeg', 'tYdiR0n', 'v3DzXIOlWJGbT2x', 'Empty', '2023-01-16 18:13:50'),
(5386, 1426, 'Wowwwww', 'video/mp4', 'https://i.imgur.com/tNr7RiE.mp4', 'tNr7RiE', 'NyYZVq7G7qV2wUY', 'Empty', '2023-01-16 18:13:53'),
(5387, 1426, 'Siberian swipe', 'video/mp4', 'https://i.imgur.com/5VwoUGC.mp4', '5VwoUGC', 'b3p25aAr3RdK0XS', 'Empty', '2023-01-16 18:13:56'),
(5388, 1423, 'który_pociąg', 'image/jpeg', 'https://i.imgur.com/oWDRbPs.jpeg', 'oWDRbPs', 'aB1HPjMq0R5pch3', 'Empty', '2023-01-16 18:14:41'),
(5389, 1426, 'Pan Bestia', 'video/mp4', 'https://i.imgur.com/8oseJt6.mp4', '8oseJt6', 'RLgr332NzUGCpOU', 'Empty', '2023-01-16 18:14:55'),
(5390, 1424, 'scott', 'image/jpeg', 'https://i.imgur.com/GHyzsVT.jpeg', 'GHyzsVT', 'TydN3EevI1OqkO6', 'Empty', '2023-01-16 18:16:03'),
(5391, 1423, 'bayesy', 'image/jpeg', 'https://i.imgur.com/kbVjprm.jpeg', 'kbVjprm', 'NYr8NsYb9bcwyiN', 'Empty', '2023-01-16 18:19:47'),
(5392, 1423, 'Polskie imiona najlepsze', 'image/jpeg', 'https://i.imgur.com/7aZazG1.jpeg', '7aZazG1', '3nvjieowrENuyD5', 'Empty', '2023-01-16 18:20:44'),
(5393, 1424, 'well it sucks', 'image/jpeg', 'https://i.imgur.com/hs9gREB.jpeg', 'hs9gREB', '6kmEybuXeL06Hzg', 'Empty', '2023-01-16 18:20:55'),
(5394, 1424, 'unacceptable', 'image/jpeg', 'https://i.imgur.com/5Q8TCo3.jpeg', '5Q8TCo3', 'IpwFLMiVlIHkAYS', 'Empty', '2023-01-16 18:21:09'),
(5395, 1423, 'kapitol', 'image/gif', 'https://i.imgur.com/rDaumE2.gif', 'rDaumE2', 'cjLV5UC0JHuOd6S', 'Empty', '2023-01-16 18:22:04'),
(5396, 1423, 'Najlepszy Microsoft', 'image/jpeg', 'https://i.imgur.com/ED9uMTW.jpeg', 'ED9uMTW', 'jUqqd4Cs2TEx5LB', 'Empty', '2023-01-16 18:22:43'),
(5397, 1423, 'Stop using', 'image/jpeg', 'https://i.imgur.com/QbCiNxl.jpeg', 'QbCiNxl', 'JuVGi0xn6tshKK8', 'Empty', '2023-01-16 18:23:13'),
(5398, 1425, 'mimi', 'image/jpeg', 'https://i.imgur.com/cNCLJz8.jpeg', 'cNCLJz8', 'aWiUvhKxoFBlek2', 'Empty', '2023-01-16 18:24:31'),
(5399, 1424, 'unstable', 'image/gif', 'https://i.imgur.com/I1Z5O2X.gif', 'I1Z5O2X', 'nNTWC747NS8yEbW', 'Empty', '2023-01-16 18:24:43'),
(5400, 1423, 'fizyka', 'image/jpeg', 'https://i.imgur.com/MtcW67M.jpeg', 'MtcW67M', 'Y1ZFU4A54cLpCXj', 'Empty', '2023-01-16 18:24:51'),
(5401, 1426, 'Furry', 'video/mp4', 'https://i.imgur.com/rAKyrJH.mp4', 'rAKyrJH', 'Fk9OIT1HFYbNN8q', 'Empty', '2023-01-16 18:24:59'),
(5402, 1424, 'geometry', 'image/jpeg', 'https://i.imgur.com/nz25uWy.jpeg', 'nz25uWy', 'SQynRMDjZ3z02YK', 'Empty', '2023-01-16 18:25:02'),
(5403, 1424, 'aeik', 'image/jpeg', 'https://i.imgur.com/QwTsvIq.jpeg', 'QwTsvIq', 'sTigWLarIyZebj1', 'Empty', '2023-01-16 18:25:17'),
(5404, 1423, 'Najlepszy matma', 'image/jpeg', 'https://i.imgur.com/kA5jkMz.jpeg', 'kA5jkMz', 'joI75ZYeV3wRKLo', 'Empty', '2023-01-16 18:25:22'),
(5405, 1425, 'wiz', 'image/jpeg', 'https://i.imgur.com/nBBdwmN.jpeg', 'nBBdwmN', '0OewMqvH4ZCIfdo', 'Empty', '2023-01-16 18:25:25'),
(5406, 1424, 'future', 'image/jpeg', 'https://i.imgur.com/gPn8Ipu.jpeg', 'gPn8Ipu', 'Ugderw0pwDjec8m', 'Empty', '2023-01-16 18:25:55'),
(5407, 1425, 'matma', 'image/jpeg', 'https://i.imgur.com/hLyYhHF.jpeg', 'hLyYhHF', 'NQ7wlhn2ujZjGCB', 'Empty', '2023-01-16 18:26:36'),
(5408, 1423, 'Latex my beloved', 'image/jpeg', 'https://i.imgur.com/EhGPIrn.jpeg', 'EhGPIrn', 'hCr5Q5l8LMTAShy', 'Empty', '2023-01-16 18:27:20'),
(5409, 1424, 'catience', 'image/jpeg', 'https://i.imgur.com/6DceQ49.jpeg', '6DceQ49', 'MEQ5sJUAm3CygUe', 'Empty', '2023-01-16 18:27:41'),
(5410, 1423, 'ce plus plusy', 'image/jpeg', 'https://i.imgur.com/DBR2n0O.jpeg', 'DBR2n0O', 'AJhABYK0y44G3tc', 'Empty', '2023-01-16 18:28:30'),
(5411, 1426, 'Matma', 'image/png', 'https://i.imgur.com/zLDniH2.png', 'zLDniH2', 'AmAW8JVJtFNF7iZ', 'Empty', '2023-01-16 18:28:35'),
(5412, 1423, 'AGHy', 'image/jpeg', 'https://i.imgur.com/8vNw925.jpeg', '8vNw925', 'NRc5V6Wds5gwcLa', 'Empty', '2023-01-16 18:28:49'),
(5413, 1424, 'invasion', 'image/jpeg', 'https://i.imgur.com/OS7lPGy.jpeg', 'OS7lPGy', 'IV7QCfhUqTj36Vg', 'Empty', '2023-01-16 18:28:59'),
(5414, 1423, 'studenci', 'image/jpeg', 'https://i.imgur.com/rFkqjiJ.jpeg', 'rFkqjiJ', 'hzOyXmFB7bFPbnS', 'Empty', '2023-01-16 18:31:51'),
(5415, 1424, 'angielski', 'image/png', 'https://i.imgur.com/GhIZm0u.png', 'GhIZm0u', 'yOIsZaVoNlIzSFe', 'Empty', '2023-01-16 18:32:50'),
(5416, 1423, 'brytole', 'image/jpeg', 'https://i.imgur.com/LJTO8AY.jpeg', 'LJTO8AY', 'ni15Rs1ZH6IMCkV', 'Empty', '2023-01-16 18:32:54'),
(5417, 1424, 'generator brukowca', 'image/jpeg', 'https://i.imgur.com/170LO60.jpeg', '170LO60', '1bZvuaNzuTAPovt', 'Empty', '2023-01-16 18:33:19'),
(5418, 1424, 'technik informatyk', 'image/png', 'https://i.imgur.com/KImqm2G.png', 'KImqm2G', '6j1g5JmqTLTIQtj', 'Empty', '2023-01-16 18:33:36'),
(5419, 1423, 'religia false confirmed', 'image/jpeg', 'https://i.imgur.com/lj7udqo.jpeg', 'lj7udqo', 'NOYpUgWETgpdsW2', 'Empty', '2023-01-16 18:33:51'),
(5420, 1425, 'tim', 'image/png', 'https://i.imgur.com/yRSL4sE.png', 'yRSL4sE', 'f0T2hWqR2aShXis', 'Empty', '2023-01-16 18:34:15'),
(5421, 1426, 'meme', 'video/mp4', 'https://i.imgur.com/E7dTLgx.mp4', 'E7dTLgx', 'tsvQLm4RfEyszdQ', 'Empty', '2023-01-16 18:34:18'),
(5422, 1426, 'o nie krindż', 'video/mp4', 'https://i.imgur.com/3FdLd0D.mp4', '3FdLd0D', 'krwjvJ0atMl2f4a', 'Empty', '2023-01-16 18:34:39'),
(5423, 1423, 'Mathn t', 'image/jpeg', 'https://i.imgur.com/ZQEJC8T.jpeg', 'ZQEJC8T', 'j2mvs6yG0aCPil0', 'Empty', '2023-01-16 18:34:46'),
(5424, 1424, 'kaczynsky', 'image/jpeg', 'https://i.imgur.com/Wlt8TpP.jpeg', 'Wlt8TpP', 'FEky7TEfDXOjeMz', 'Empty', '2023-01-16 18:35:00'),
(5425, 1424, 'lipiec', 'image/jpeg', 'https://i.imgur.com/87dXNls.jpeg', '87dXNls', 'WXQzWnKJpxObi9r', 'Empty', '2023-01-16 18:35:29'),
(5426, 1426, 'krzesło', 'video/mp4', 'https://i.imgur.com/fNMtq1y.mp4', 'fNMtq1y', 'n7IVSl1j8F48Smg', 'Empty', '2023-01-16 18:35:32'),
(5427, 1423, 'AGH tiktok XDDD', 'image/jpeg', 'https://i.imgur.com/cjmvMWT.jpeg', 'cjmvMWT', 'zxSiweiS1UobMNW', 'Empty', '2023-01-16 18:36:40'),
(5428, 1426, 'Kitkuuuu', 'video/mp4', 'https://i.imgur.com/6gv7sDR.mp4', '6gv7sDR', 'flGbyqGodARuMLD', 'Empty', '2023-01-16 18:36:53'),
(5429, 1426, 'Stefan Zawody', 'video/mp4', 'https://i.imgur.com/CJVDuj3.mp4', 'CJVDuj3', 'HTtsoek3il5pfbq', 'Empty', '2023-01-16 18:37:09'),
(5430, 1423, 'ostatnia wieczerza', 'image/jpeg', 'https://i.imgur.com/7cDJZlq.jpeg', '7cDJZlq', 'UdeUqagG1Cjl5p1', 'Empty', '2023-01-16 18:37:12'),
(5431, 1424, 'briish', 'image/jpeg', 'https://i.imgur.com/0Boz4ME.jpeg', '0Boz4ME', 'P8RPgZRs9ehk9zJ', 'Empty', '2023-01-16 18:37:23'),
(5432, 1424, 'based ye', 'image/jpeg', 'https://i.imgur.com/V7VGwKF.jpeg', 'V7VGwKF', 'rGGSyynn5DsR1iq', 'Empty', '2023-01-16 18:39:36'),
(5433, 1426, 'Payday 3 zapowiedziany', 'video/mp4', 'https://i.imgur.com/gdYUKMJ.mp4', 'gdYUKMJ', 'FlS9WFIuF7ohEKH', 'Empty', '2023-01-16 18:40:12'),
(5434, 1425, 'amongus i gwiezdne wojny', 'image/jpeg', 'https://i.imgur.com/VNZU3Kw.jpeg', 'VNZU3Kw', 'G2IqdFL9FCF1Tps', 'Empty', '2023-01-16 18:40:15');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `reports`
--

CREATE TABLE `reports` (
  `report_id` int(32) NOT NULL,
  `user_id` int(32) NOT NULL,
  `picture_id` int(32) NOT NULL,
  `reason_of_report` text NOT NULL,
  `date_of_report` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `reports`
--

INSERT INTO `reports` (`report_id`, `user_id`, `picture_id`, `reason_of_report`, `date_of_report`) VALUES
(22, 1423, 5410, '\"Zle wspomnienia\"', '2023-01-16 18:56:40'),
(23, 1424, 5401, '\"furasy okropne\"', '2023-01-16 19:01:40'),
(24, 1425, 5401, '\"Nie rozumiem mema\"', '2023-01-16 19:02:23'),
(25, 1423, 5405, '\"Nie rozumiem\"', '2023-01-16 19:05:43');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `user_id` int(32) NOT NULL,
  `discord_id` bigint(64) NOT NULL,
  `nickname` text NOT NULL,
  `date_of_join` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`user_id`, `discord_id`, `nickname`, `date_of_join`) VALUES
(1422, 172465767000965120, 'SirJosh#9645', '2023-01-14 18:52:10'),
(1423, 688106200168267776, 'ForNeus57#1722', '2023-01-14 18:52:13'),
(1424, 285509551472508939, 'haarmeggido#6891', '2023-01-14 18:53:09'),
(1425, 509765405183705119, 'Didget#1081', '2023-01-14 18:53:29'),
(1426, 307946464875642880, 'Eniter#9967', '2023-01-14 18:54:09'),
(1427, 861252548728324106, 'IKZCICKAK#0241', '2023-01-14 18:54:22'),
(1428, 192620017882234880, 'AverageAlien#9909', '2023-01-14 18:56:05'),
(1429, 404722618659373056, 'Globii#8919', '2023-01-14 18:56:13'),
(1430, 267014354438848512, '̣̣Jakub#4396', '2023-01-14 18:56:56'),
(1431, 564790167945347072, 'ThunderFlame#9925', '2023-01-14 18:58:29'),
(1432, 265467042294005760, 'Mike9090#1725', '2023-01-14 19:08:29'),
(1433, 942510192678010890, 'Niggers#9084', '2023-01-15 17:47:01'),
(1434, 1064321559830990879, 'Membot_Bot#3866', '2023-01-16 16:36:05');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `votes`
--

CREATE TABLE `votes` (
  `user_id` int(32) NOT NULL,
  `picture_id` int(32) NOT NULL,
  `vote_value` int(32) NOT NULL,
  `date_of_vote` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `votes`
--

INSERT INTO `votes` (`user_id`, `picture_id`, `vote_value`, `date_of_vote`) VALUES
(1422, 5331, 1, '2023-01-14 18:54:19'),
(1423, 5331, 1, '2023-01-14 18:54:10'),
(1423, 5344, 1, '2023-01-14 18:59:34'),
(1423, 5356, 1, '2023-01-14 19:13:27'),
(1423, 5385, 1, '2023-01-16 18:59:02'),
(1423, 5386, -1, '2023-01-16 18:56:58'),
(1423, 5387, -1, '2023-01-16 18:55:08'),
(1423, 5388, 1, '2023-01-16 18:54:22'),
(1423, 5390, 1, '2023-01-16 18:57:32'),
(1423, 5391, 1, '2023-01-16 18:57:25'),
(1423, 5392, 1, '2023-01-16 18:52:45'),
(1423, 5393, 1, '2023-01-16 18:52:52'),
(1423, 5394, 1, '2023-01-16 18:57:11'),
(1423, 5395, 1, '2023-01-16 19:00:06'),
(1423, 5396, 1, '2023-01-16 18:55:32'),
(1423, 5397, 1, '2023-01-16 18:54:42'),
(1423, 5398, -1, '2023-01-16 18:58:13'),
(1423, 5399, 1, '2023-01-16 19:01:05'),
(1423, 5400, 1, '2023-01-16 18:53:02'),
(1423, 5401, -1, '2023-01-16 19:01:25'),
(1423, 5402, 1, '2023-01-16 18:58:50'),
(1423, 5403, 1, '2023-01-16 18:56:13'),
(1423, 5404, 1, '2023-01-16 19:04:39'),
(1423, 5405, -1, '2023-01-16 19:04:01'),
(1423, 5406, -1, '2023-01-16 19:00:24'),
(1423, 5407, -1, '2023-01-16 18:55:14'),
(1423, 5408, 1, '2023-01-16 18:57:39'),
(1423, 5409, 1, '2023-01-16 19:02:24'),
(1423, 5410, -1, '2023-01-16 18:56:27'),
(1423, 5411, 1, '2023-01-16 18:53:39'),
(1423, 5412, 1, '2023-01-16 18:58:28'),
(1423, 5413, -1, '2023-01-16 18:53:18'),
(1423, 5414, 1, '2023-01-16 18:53:45'),
(1423, 5415, -1, '2023-01-16 18:55:59'),
(1423, 5416, 1, '2023-01-16 18:53:26'),
(1423, 5417, 1, '2023-01-16 18:54:30'),
(1423, 5418, -1, '2023-01-16 18:54:02'),
(1423, 5420, 1, '2023-01-16 18:56:46'),
(1423, 5423, 1, '2023-01-16 19:03:19'),
(1423, 5424, 1, '2023-01-16 18:55:10'),
(1423, 5425, 1, '2023-01-16 18:58:19'),
(1423, 5427, 1, '2023-01-16 18:53:11'),
(1423, 5428, 1, '2023-01-16 19:05:12'),
(1423, 5430, 1, '2023-01-16 19:04:29'),
(1423, 5431, -1, '2023-01-16 18:59:35'),
(1423, 5433, 1, '2023-01-16 19:00:45'),
(1423, 5434, 1, '2023-01-16 18:54:14'),
(1424, 5331, 1, '2023-01-14 18:54:24'),
(1424, 5344, 1, '2023-01-14 18:58:26'),
(1424, 5356, 1, '2023-01-14 19:13:24'),
(1424, 5385, 1, '2023-01-16 18:59:04'),
(1424, 5386, -1, '2023-01-16 18:56:57'),
(1424, 5387, 1, '2023-01-16 18:54:52'),
(1424, 5388, 1, '2023-01-16 18:54:21'),
(1424, 5389, 1, '2023-01-16 18:57:51'),
(1424, 5390, 1, '2023-01-16 18:57:30'),
(1424, 5391, 1, '2023-01-16 18:57:22'),
(1424, 5392, 1, '2023-01-16 18:52:46'),
(1424, 5393, 1, '2023-01-16 18:52:48'),
(1424, 5394, 1, '2023-01-16 18:57:09'),
(1424, 5395, 1, '2023-01-16 18:59:58'),
(1424, 5396, -1, '2023-01-16 18:55:34'),
(1424, 5397, 1, '2023-01-16 18:54:39'),
(1424, 5398, -1, '2023-01-16 18:58:09'),
(1424, 5399, 1, '2023-01-16 19:01:03'),
(1424, 5400, 1, '2023-01-16 18:53:00'),
(1424, 5401, -1, '2023-01-16 19:01:51'),
(1424, 5402, 1, '2023-01-16 18:58:49'),
(1424, 5403, 1, '2023-01-16 18:56:09'),
(1424, 5404, 1, '2023-01-16 19:04:40'),
(1424, 5405, -1, '2023-01-16 19:03:59'),
(1424, 5406, 1, '2023-01-16 19:00:18'),
(1424, 5407, -1, '2023-01-16 18:55:16'),
(1424, 5408, 1, '2023-01-16 18:57:43'),
(1424, 5409, 1, '2023-01-16 18:55:30'),
(1424, 5410, -1, '2023-01-16 18:56:29'),
(1424, 5411, 1, '2023-01-16 18:53:40'),
(1424, 5413, 1, '2023-01-16 18:53:16'),
(1424, 5414, 1, '2023-01-16 18:53:46'),
(1424, 5415, 1, '2023-01-16 18:57:59'),
(1424, 5416, -1, '2023-01-16 18:53:28'),
(1424, 5417, 1, '2023-01-16 18:54:33'),
(1424, 5418, 1, '2023-01-16 18:54:04'),
(1424, 5420, 1, '2023-01-16 18:56:42'),
(1424, 5422, 1, '2023-01-16 19:05:45'),
(1424, 5423, 1, '2023-01-16 19:03:20'),
(1424, 5424, 1, '2023-01-16 18:55:02'),
(1424, 5425, 1, '2023-01-16 18:58:18'),
(1424, 5427, 1, '2023-01-16 18:53:12'),
(1424, 5428, 1, '2023-01-16 19:04:58'),
(1424, 5429, 1, '2023-01-16 18:52:57'),
(1424, 5431, 1, '2023-01-16 18:59:34'),
(1424, 5432, 1, '2023-01-16 18:59:19'),
(1424, 5433, 1, '2023-01-16 19:00:55'),
(1424, 5434, -1, '2023-01-16 18:54:13'),
(1425, 5331, 1, '2023-01-14 18:54:13'),
(1425, 5344, 1, '2023-01-14 19:06:40'),
(1425, 5356, 1, '2023-01-14 19:13:32'),
(1425, 5385, -1, '2023-01-16 18:59:08'),
(1425, 5386, -1, '2023-01-16 18:57:02'),
(1425, 5388, 1, '2023-01-16 18:54:31'),
(1425, 5389, 1, '2023-01-16 18:58:00'),
(1425, 5391, -1, '2023-01-16 18:57:24'),
(1425, 5392, -1, '2023-01-16 18:52:56'),
(1425, 5393, 1, '2023-01-16 18:53:01'),
(1425, 5394, -1, '2023-01-16 18:57:15'),
(1425, 5395, 1, '2023-01-16 19:00:10'),
(1425, 5396, -1, '2023-01-16 18:55:53'),
(1425, 5397, -1, '2023-01-16 18:55:35'),
(1425, 5398, 1, '2023-01-16 18:58:17'),
(1425, 5399, -1, '2023-01-16 19:01:27'),
(1425, 5400, 1, '2023-01-16 18:53:09'),
(1425, 5401, -1, '2023-01-16 19:01:44'),
(1425, 5402, 1, '2023-01-16 18:58:54'),
(1425, 5404, 1, '2023-01-16 19:04:48'),
(1425, 5405, 1, '2023-01-16 19:03:58'),
(1425, 5406, -1, '2023-01-16 19:00:33'),
(1425, 5407, -1, '2023-01-16 18:55:38'),
(1425, 5408, 1, '2023-01-16 18:57:38'),
(1425, 5410, -1, '2023-01-16 18:56:32'),
(1425, 5412, -1, '2023-01-16 18:58:36'),
(1425, 5413, -1, '2023-01-16 18:53:21'),
(1425, 5414, -1, '2023-01-16 18:54:07'),
(1425, 5415, -1, '2023-01-16 18:58:30'),
(1425, 5416, -1, '2023-01-16 18:53:34'),
(1425, 5417, 1, '2023-01-16 18:54:37'),
(1425, 5418, -1, '2023-01-16 18:54:16'),
(1425, 5420, 1, '2023-01-16 18:56:44'),
(1425, 5423, -1, '2023-01-16 19:03:15'),
(1425, 5424, -1, '2023-01-16 18:55:31'),
(1425, 5425, -1, '2023-01-16 18:58:24'),
(1425, 5427, -1, '2023-01-16 18:53:14'),
(1425, 5428, -1, '2023-01-16 19:05:08'),
(1425, 5430, -1, '2023-01-16 19:04:30'),
(1425, 5434, 1, '2023-01-16 18:54:27'),
(1426, 5331, 1, '2023-01-14 18:54:09'),
(1426, 5344, 1, '2023-01-14 18:58:28'),
(1426, 5356, 1, '2023-01-14 19:13:26'),
(1426, 5385, 1, '2023-01-16 18:59:03'),
(1426, 5386, 1, '2023-01-16 18:57:01'),
(1426, 5387, 1, '2023-01-16 18:55:21'),
(1426, 5388, 1, '2023-01-16 18:54:23'),
(1426, 5389, 1, '2023-01-16 18:57:44'),
(1426, 5390, 1, '2023-01-16 18:57:31'),
(1426, 5391, 1, '2023-01-16 18:57:18'),
(1426, 5392, 1, '2023-01-16 18:52:51'),
(1426, 5393, 1, '2023-01-16 18:52:50'),
(1426, 5394, 1, '2023-01-16 18:57:10'),
(1426, 5395, 1, '2023-01-16 19:00:02'),
(1426, 5396, 1, '2023-01-16 18:55:33'),
(1426, 5397, 1, '2023-01-16 18:54:41'),
(1426, 5399, 1, '2023-01-16 19:01:09'),
(1426, 5400, -1, '2023-01-16 18:52:59'),
(1426, 5401, 1, '2023-01-16 19:01:16'),
(1426, 5402, 1, '2023-01-16 18:58:48'),
(1426, 5403, -1, '2023-01-16 18:56:20'),
(1426, 5404, 1, '2023-01-16 19:04:41'),
(1426, 5405, -1, '2023-01-16 19:03:52'),
(1426, 5406, 1, '2023-01-16 19:00:20'),
(1426, 5407, 1, '2023-01-16 18:55:15'),
(1426, 5408, 1, '2023-01-16 18:57:38'),
(1426, 5409, 1, '2023-01-16 18:55:28'),
(1426, 5410, 1, '2023-01-16 18:56:28'),
(1426, 5411, 1, '2023-01-16 18:53:40'),
(1426, 5412, 1, '2023-01-16 18:58:27'),
(1426, 5413, -1, '2023-01-16 18:53:19'),
(1426, 5414, 1, '2023-01-16 18:53:49'),
(1426, 5415, 1, '2023-01-16 18:55:56'),
(1426, 5416, -1, '2023-01-16 18:53:25'),
(1426, 5417, 1, '2023-01-16 18:54:32'),
(1426, 5418, -1, '2023-01-16 18:54:05'),
(1426, 5420, 1, '2023-01-16 18:56:43'),
(1426, 5423, 1, '2023-01-16 19:03:21'),
(1426, 5424, 1, '2023-01-16 18:56:05'),
(1426, 5425, 1, '2023-01-16 18:58:20'),
(1426, 5427, 1, '2023-01-16 18:53:10'),
(1426, 5428, 1, '2023-01-16 19:05:10'),
(1426, 5429, 1, '2023-01-16 18:52:53'),
(1426, 5431, 1, '2023-01-16 18:59:33'),
(1426, 5432, 1, '2023-01-16 18:59:28'),
(1426, 5433, 1, '2023-01-16 19:00:47'),
(1426, 5434, -1, '2023-01-16 18:54:14'),
(1427, 5331, 1, '2023-01-14 18:54:22'),
(1427, 5344, -1, '2023-01-14 18:58:33'),
(1431, 5344, 1, '2023-01-14 18:58:30'),
(1432, 5331, 1, '2023-01-14 19:08:29');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `banned`
--
ALTER TABLE `banned`
  ADD KEY `report_id_index` (`report_id`) USING BTREE;

--
-- Indeksy dla tabeli `pictures`
--
ALTER TABLE `pictures`
  ADD PRIMARY KEY (`picture_id`),
  ADD UNIQUE KEY `Image_hash` (`image_hash`) USING HASH,
  ADD UNIQUE KEY `delete_hash` (`delete_hash`) USING HASH,
  ADD UNIQUE KEY `url` (`url`) USING HASH,
  ADD KEY `user_id` (`user_id`) USING BTREE;

--
-- Indeksy dla tabeli `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`report_id`),
  ADD KEY `picture_id_index` (`picture_id`),
  ADD KEY `user_id_index` (`user_id`);

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `discord_id_unique` (`discord_id`);

--
-- Indeksy dla tabeli `votes`
--
ALTER TABLE `votes`
  ADD UNIQUE KEY `user_id_2` (`user_id`,`picture_id`) USING BTREE,
  ADD KEY `user_id` (`user_id`),
  ADD KEY `picture_id` (`picture_id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `pictures`
--
ALTER TABLE `pictures`
  MODIFY `picture_id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5435;

--
-- AUTO_INCREMENT dla tabeli `reports`
--
ALTER TABLE `reports`
  MODIFY `report_id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT dla tabeli `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(32) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1435;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `banned`
--
ALTER TABLE `banned`
  ADD CONSTRAINT `banned_ibfk_1` FOREIGN KEY (`report_id`) REFERENCES `reports` (`report_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ograniczenia dla tabeli `pictures`
--
ALTER TABLE `pictures`
  ADD CONSTRAINT `pictures_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ograniczenia dla tabeli `reports`
--
ALTER TABLE `reports`
  ADD CONSTRAINT `reports_ibfk_4` FOREIGN KEY (`picture_id`) REFERENCES `pictures` (`picture_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reports_ibfk_5` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ograniczenia dla tabeli `votes`
--
ALTER TABLE `votes`
  ADD CONSTRAINT `votes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `votes_ibfk_2` FOREIGN KEY (`picture_id`) REFERENCES `pictures` (`picture_id`) ON DELETE CASCADE ON UPDATE CASCADE;

DELIMITER $$
--
-- Zdarzenia
--
CREATE DEFINER=`dominikb`@`%` EVENT `usuwanie_slabych_zdjec_z_bazy` ON SCHEDULE EVERY 1 HOUR STARTS '2023-01-14 01:00:00' ON COMPLETION NOT PRESERVE ENABLE DO DELETE FROM pictures WHERE picture_id IN (
        SELECT v.picture_id FROM votes AS v
            INNER JOIN (SELECT picture_id, SUM(vote_value) AS suma FROM votes GROUP BY picture_id) AS s USING(picture_id)
        WHERE s.suma < -5
        GROUP BY picture_id
    )$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
