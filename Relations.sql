SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `departments` (
  `id` int(11) NOT NULL,
  `department_name` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `departments` (`id`, `department_name`, `created_at`) VALUES
(1, 'Administration department', '2023-11-11 12:03:02'),
(2, 'Technical Operation Department', '2023-11-11 12:03:43'),
(3, 'Communications Department', '2023-11-11 12:04:28');

CREATE TABLE `employees` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `department_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `employees_department_relation` (`department_id`),
  CONSTRAINT `employees_department_relation` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `employees` (`id`, `username`, `department_id`, `created_at`) VALUES
(2, 'Jason Statham', 3, '2023-11-11 12:05:02'),
(3, 'Oprah Winfrey', 2, '2023-11-11 12:05:20'),
(4, 'Elon Tusk', 1, '2023-11-11 12:05:58'),
(5, 'Papuna Kvinikadze', 1, '2023-11-11 12:06:36');

CREATE TABLE `projects` (
  `id` int(11) NOT NULL,
  `project_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `projects` (`id`, `project_name`) VALUES
(1, 'Project A'),
(2, 'Project B'),
(3, 'Project C');

CREATE TABLE `employee_projects` (
  `employee_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`employee_id`, `project_id`),
  CONSTRAINT `fk_employee_projects_employee` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `fk_employee_projects_project` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `employee_projects` (`employee_id`, `project_id`) VALUES
(2, 1),
(3, 2),
(4, 1),
(5, 3);

COMMIT;
