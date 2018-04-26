insert into airline(airline_name) values 
	("China Eastern");

insert into airport(airport_name, airport_city) values 
	("JFK","NYC"),("PVG","Shanghai");

insert into customer values ("zz913@nyu.edu", "Zihao Zhao", "123456", "1555", "Century Avenue", "Shanghai", "Shanghai",
		"1234567890", "E31248965", "2018-01-19", "China", "1996-10-05");

insert into booking_agent(email, password, booking_agent_id) values
	("niceprice@ctrip.com", "84729382", 41924823);

insert into airplane(airline_name, airplane_id, seats) values
	("China Eastern", 22739844, 200),
	("China Eastern", 23229179, 180);

insert into airline_staff values
	("AlphaB", "31245692", "Alpha", "Beta", "1977-09-26", "China Eastern");

insert into flight values
	("China Eastern", 798, "PVG", "2018-03-29 10:54:28", "JFK", "2018-03-30 09:54:28", 4000, "upcoming", 22739844),
	("China Eastern", 536, "PVG", "2018-03-17 10:23:54", "JFK", "2018-03-18 10:34:52", 6789, "in-progress", 23229179),
	("China Eastern", 537, "JFK", "2018-03-18 11:54:28", "PVG", "2018-03-19 22:54:28", 7869, "delayed", 23229179);

insert into ticket(ticket_id, airline_name, flight_num) values
	(94802083, "China Eastern", 798),
	(94802084, "China Eastern", 536);

insert into purchases(ticket_id, customer_email, booking_agent_id, purchase_date) values
	(94802083, "zz913@nyu.edu", 41924823, "2018-02-16");
