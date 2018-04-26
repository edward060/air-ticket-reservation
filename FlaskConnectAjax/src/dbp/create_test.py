# -*- coding: utf-8 -*-
# @Time:    18/04/2018 8:28 PM
# @Author:  Zihao Zhao
# @E-mail:  zz913@nyu.edu

import pymysql.cursors

# configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       db='dbp',
                       cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()

cursor.execute("CREATE TABLE `airline` ("
               "`airline_name` varchar(50) NOT NULL,"
               "PRIMARY KEY(`airline_name`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")

cursor.execute("CREATE TABLE `airline_staff` ("
               "`username` varchar(50) NOT NULL,"
               "`password` varchar(50) NOT NULL,"
               "`first_name` varchar(50) NOT NULL,"
               "`last_name` varchar(50) NOT NULL,"
               "`date_of_birth` date NOT NULL,"
               "`airline_name` varchar(50) NOT NULL,"
               "PRIMARY KEY(`username`),"
               "FOREIGN KEY(`airline_name`) REFERENCES `airline`(`airline_name`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")

cursor.execute("CREATE TABLE `airplane` ("
               "`airline_name` varchar(50) NOT NULL,"
               "`airplane_id` int(11) NOT NULL,"
               "`seats` int(11) NOT NULL,"
               "PRIMARY KEY(`airline_name`, `airplane_id`),"
               "FOREIGN KEY(`airline_name`) REFERENCES `airline`(`airline_name`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")

cursor.execute("CREATE TABLE `airport` ("
               "`airport_name` varchar(50) NOT NULL,"
               "`airport_city` varchar(50) NOT NULL,"
               "PRIMARY KEY(`airport_name`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")

cursor.execute("CREATE TABLE `booking_agent` ("
               "`email` varchar(50) NOT NULL,"
               "`password` varchar(50) NOT NULL,"
               "`booking_agent_id` int(11) NOT NULL,"
               "PRIMARY KEY(`email`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")

cursor.execute("CREATE TABLE `customer` ("
               "`email` varchar(50) NOT NULL,"
               "`name` varchar(50) NOT NULL,"
               "`password` varchar(50) NOT NULL,"
               "`building_number` varchar(30) NOT NULL,"
               "`street` varchar(30) NOT NULL,"
               "`city` varchar(30) NOT NULL,"
               "`state` varchar(30) NOT NULL,"
               "`phone_number` int(11) NOT NULL,"
               "`passport_number` varchar(30) NOT NULL,"
               "`passport_expiration` date NOT NULL,"
               "`passport_country` varchar(50) NOT NULL,"
               "`date_of_birth` date NOT NULL,"
               "PRIMARY KEY(`email`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")

cursor.execute("CREATE TABLE `flight` ("
               "`airline_name` varchar(50) NOT NULL,"
               "`flight_num` int(11) NOT NULL,"
               "`departure_airport` varchar(50) NOT NULL,"
               "`departure_time` datetime NOT NULL,"
               "`arrival_airport` varchar(50) NOT NULL,"
               "`arrival_time` datetime NOT NULL,"
               "`price` decimal(10,0) NOT NULL,"
               "`status` varchar(50) NOT NULL,"
               "`airplane_id` int(11) NOT NULL,"
               "PRIMARY KEY(`airline_name`, `flight_num`),"
               "FOREIGN KEY(`airline_name`, `airplane_id`) REFERENCES `airplane`(`airline_name`, `airplane_id`),"
               "FOREIGN KEY(`departure_airport`) REFERENCES `airport`(`airport_name`),"
               "FOREIGN KEY(`arrival_airport`) REFERENCES `airport`(`airport_name`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")

cursor.execute("CREATE TABLE `ticket` ("
               "`ticket_id` int(11) NOT NULL,"
               "`airline_name` varchar(50) NOT NULL,"
               "`flight_num` int(11) NOT NULL,"
               "PRIMARY KEY(`ticket_id`),"
               "FOREIGN KEY(`airline_name`, `flight_num`) REFERENCES `flight`(`airline_name`, `flight_num`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")

cursor.execute("CREATE TABLE `purchases` ("
               "`ticket_id` int(11) NOT NULL,"
               "`customer_email` varchar(50) NOT NULL,"
               "`booking_agent_id` int(11),"
               "`purchase_date` date NOT NULL,"
               "PRIMARY KEY(`ticket_id`, `customer_email`),"
               "FOREIGN KEY(`ticket_id`) REFERENCES `ticket`(`ticket_id`),"
               "FOREIGN KEY(`customer_email`) REFERENCES `customer`(`email`)"
               ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")