-- USERS
CREATE TABLE USERS (
  User_id INT PRIMARY KEY,
  UserName VARCHAR(50),
  FirstName VARCHAR(50),
  MiddleName VARCHAR(50),
  LastName VARCHAR(50),
  DOB DATE,
  Age INT,
  Gender VARCHAR(10),
  Password VARCHAR(255)
);

INSERT INTO USERS VALUES
(1,'user01','Alice','M','Smith','2000-05-21',25,'F','pass1234'),
(2,'user02','Bob','A','Johnson','1998-02-11',27,'M','mysecurepwd'),
(3,'user03','Carol','L','Williams','2001-07-13',24,'F','pwCarol2025'),
(4,'user04','Daniel','K','Brown','1997-12-05',28,'M','brownie!23'),
(5,'user05','Eve','S','Davis','1999-09-30',26,'F','eve_pwd99'),
(6,'user06','Frank','C','Miller','2002-03-20',23,'M','fm_password'),
(7,'user07','Grace','Y','Wilson','2003-01-17',22,'F','grace@123'),
(8,'user08','Henry','','Moore','1996-11-25',29,'M','henmoore2025'),
(9,'user09','Ivy','J','Taylor','2004-08-14',21,'F','ivy!secret'),
(10,'user10','Jack','','Anderson','1995-04-22',30,'M','jackPwd4ever'),
(11,'user11','Nina','F','Clark','1999-06-10',26,'F','nina_clark7'),
(12,'user12','Oscar','M','Hall','2003-07-07',22,'M','oHall_pass'),
(13,'user13','Pamela','G','Lee','1998-08-18',27,'F','pLee_!2025'),
(14,'user14','Quentin','W','King','1997-09-21',28,'M','qKing1234'),
(15,'user15','Rachel','S','Scott','2002-10-22',23,'F','rScott_pw'),
(16,'user16','Samuel','E','Adams','1997-11-29',28,'M','samAdams99'),
(17,'user17','Tina','L','Jordan','2003-12-30',22,'F','tina_j22'),
(18,'user18','Umar','K','Cruz','1996-01-15',29,'M','uCruzPw!'),
(19,'user19','Vera','H','Morris','2004-04-25',21,'F','veraPass1'),
(20,'user20','Walt','J','Diaz','1995-03-10',30,'M','Walt@2025');



-- ARTISTS
CREATE TABLE ARTISTS (
  Artist_id INT PRIMARY KEY,
  FirstName VARCHAR(50),
  MiddleName VARCHAR(50),
  LastName VARCHAR(50),
  StageName VARCHAR(50),
  Genre VARCHAR(30),
  State VARCHAR(20),
  ContractFee DECIMAL(10,2)
);

INSERT INTO ARTISTS VALUES
(1,'Jim','A','Morrison','Mojo','Rock','Maharashtra',5000.00),
(2,'Amy','B','Winehouse','AmyW','Jazz','West Bengal',7500.00),
(3,'Liam','C','Gallagher','LG','Britpop','Karnataka',6200.00),
(4,'Adele','D','Adkins','Adele','Pop','Delhi',9000.00),
(5,'Dave','E','Grohl','DG','Rock','Uttar Pradesh',4200.00),
(6,'Billie','F','Eilish','BE','Pop','Gujarat',8000.00),
(7,'Ed','G','Sheeran','Eddie','Folk','Punjab',8500.00),
(8,'Taylor','H','Swift','TSwift','Pop','Kerala',9500.00),
(9,'Bruno','I','Mars','BM','R&B','Rajasthan',7700.00),
(10,'Katy','J','Perry','KP','Pop','Rajasthan',8000.00),
(11,'Ella','K','Brown','ElleB','Jazz','Madhya Pradesh',6700.00),
(12,'Sam','L','Hill','Sammy','Rock','Bihar',4000.00),
(13,'Nina','M','White','NinaW','Pop','Odisha',5300.00),
(14,'Tony','N','Black','TBlack','HipHop','Chhattisgarh',7700.00),
(15,'Eva','O','Green','EGreen','Country','Jharkhand',6000.00),
(16,'Raj','P','Singh','RajS','Folk','Haryana',8300.00),
(17,'Mia','Q','Clark','MClark','Indie','Telangana',7400.00),
(18,'Lara','R','Young','LYoung','Electronic','Goa',9000.00),
(19,'Jude','S','Foster','JFoster','Rap','Assam',4900.00),
(20,'Zara','T','Lewis','ZLewis','Pop','Puducherry',7200.00);


-- TICKETS
CREATE TABLE TICKETS (
  Ticket_id INT PRIMARY KEY,
  Tier VARCHAR(20),
  Cost DECIMAL(8,2),
  PurchaseDate DATE
);

INSERT INTO TICKETS VALUES
(1,'VIP',1500.00,'2025-10-01'),
(2,'Gold',1200.00,'2025-10-02'),
(3,'Silver',1000.00,'2025-10-03'),
(4,'Bronze',800.00,'2025-10-04'),
(5,'VIP',1500.00,'2025-10-05'),
(6,'Gold',1200.00,'2025-10-06'),
(7,'Silver',1000.00,'2025-10-07'),
(8,'Bronze',800.00,'2025-10-08'),
(9,'VIP',1500.00,'2025-10-09'),
(10,'Gold',1200.00,'2025-10-10'),
(11,'Silver',900.00,'2025-10-11'),
(12,'Bronze',750.00,'2025-10-12'),
(13,'VIP',1600.00,'2025-10-13'),
(14,'Gold',1150.00,'2025-10-14'),
(15,'Silver',950.00,'2025-10-15'),
(16,'Bronze',700.00,'2025-10-16'),
(17,'VIP',1550.00,'2025-10-17'),
(18,'Gold',1250.00,'2025-10-18'),
(19,'Silver',980.00,'2025-10-19'),
(20,'Bronze',850.00,'2025-10-20');


-- EVENTS
CREATE TABLE EVENTS (
  Event_id INT PRIMARY KEY,
  EventName VARCHAR(100),
  EventTime TIME,
  EventDate DATE
);

INSERT INTO EVENTS VALUES
(1,'Music Fest','18:00','2025-12-15'),
(2,'Art Show','15:30','2025-12-16'),
(3,'Food Carnival','12:00','2025-12-17'),
(4,'Tech Summit','09:00','2025-12-18'),
(5,'Dance Competition','19:00','2025-12-19'),
(6,'Comedy Night','20:00','2025-12-20'),
(7,'Book Fair','11:00','2025-12-21'),
(8,'Film Premiere','21:00','2025-12-22'),
(9,'Fashion Show','17:00','2025-12-23'),
(10,'Charity Auction','14:00','2025-12-24'),
(11,'Rock Concert','19:00','2025-12-25'),
(12,'Jazz Night','20:30','2025-12-26'),
(13,'Theatre Play','18:30','2025-12-27'),
(14,'Food Festival','13:00','2025-12-28'),
(15,'Film Festival','21:00','2025-12-29'),
(16,'Technology Expo','10:00','2025-12-30'),
(17,'Dance Workshop','17:00','2025-12-31'),
(18,'Stand-up Comedy','19:30','2026-01-01'),
(19,'Literature Fest','11:00','2026-01-02'),
(20,'Charity Ball','20:00','2026-01-03');


-- ORGANIZERS
CREATE TABLE ORGANIZERS (
  Organizer_id INT PRIMARY KEY,
  OrganizerName VARCHAR(100),
  State VARCHAR(20)
);

INSERT INTO ORGANIZERS VALUES
(1,'Event Co','Maharashtra'),
(2,'Show Makers','Delhi'),
(3,'Party Planners','Karnataka'),
(4,'Music House','Tamil Nadu'),
(5,'Gala Group','Uttar Pradesh'),
(6,'FunHub','West Bengal'),
(7,'BizEvents','Gujarat'),
(8,'Artistry','Punjab'),
(9,'TalentPro','Kerala'),
(10,'TrendSetters','Rajasthan'),
(11,'Mega Events','Bihar'),
(12,'Star Performers','Telangana'),
(13,'Event Solutions','Jharkhand'),
(14,'Culture Hub','Odisha'),
(15,'City Lights','Haryana'),
(16,'Show Masters','Chhattisgarh'),
(17,'Dream Makers','Uttarakhand'),
(18,'Live Nation','Goa'),
(19,'Prime Organizers','Assam'),
(20,'NextGen Events','Madhya Pradesh');


-- SPONSORS
CREATE TABLE SPONSORS (
  Sponsor_id INT PRIMARY KEY,
  CompanyName VARCHAR(100),
  SponsorshipType VARCHAR(30),
  Industry VARCHAR(50),
  Budget DECIMAL(10,2)
);

INSERT INTO SPONSORS VALUES
(1,'Google','Tech','IT',10000.00),
(2,'CocaCola','Food','Beverage',9500.00),
(3,'Audi','Auto','Automobile',12000.00),
(4,'Pepsi','Food','Beverage',9600.00),
(5,'Apple','Tech','IT',20000.00),
(6,'Nike','Brand','Sportswear',8500.00),
(7,'Sony','Tech','Media',11000.00),
(8,'Ford','Auto','Automobile',10500.00),
(9,'Shell','Energy','Oil',12400.00),
(10,'Disney','Media','Entertainment',15000.00),
(11,'Amazon','Tech','E-commerce',22000.00),
(12,'Facebook','Tech','IT',21000.00),
(13,'Tesla','Auto','Automobile',18000.00),
(14,'Samsung','Tech','Electronics',19000.00),
(15,'HP','Tech','Computers',14000.00),
(16,'LG','Tech','Electronics',13000.00),
(17,'Microsoft','Tech','Software',25000.00),
(18,'Intel','Tech','Chip Manufacturing',23000.00),
(19,'IBM','Tech','IT',17000.00),
(20,'Adobe','Tech','Software',16000.00);


-- STAGES
CREATE TABLE STAGES (
  Stage_id INT PRIMARY KEY,
  Artists VARCHAR(100)
);

INSERT INTO STAGES VALUES
(1,'Mojo'),
(2,'AmyW'),
(3,'LG'),
(4,'Adele'),
(5,'DG'),
(6,'BE'),
(7,'Eddie'),
(8,'TSwift'),
(9,'BM'),
(10,'KP'),
(11,'EJ'),
(12,'Sammy'),
(13,'NinaW'),
(14,'TonyB'),
(15,'EvaG'),
(16,'RajS'),
(17,'MiaC'),
(18,'LaraY'),
(19,'JudeF'),
(20,'ZaraL');


-- CREWMEMBER
CREATE TABLE CREWMEMBER (
  Member_id INT PRIMARY KEY,
  FirstName VARCHAR(50),
  MiddleName VARCHAR(50),
  LastName VARCHAR(50),
  Age INT,
  Gender VARCHAR(10),
  DOJ DATE,
  Role VARCHAR(30)
);

INSERT INTO CREWMEMBER VALUES
(1,'Jake','A','Miller',32,'M','2023-04-10','Light Engineer'),
(2,'Anna','B','Moore',28,'F','2024-06-11','Sound Technician'),
(3,'Emily','C','Stone',34,'F','2022-11-21','Stage Manager'),
(4,'Ryan','D','Smith',29,'M','2024-03-12','Security'),
(5,'Luke','E','Perry',31,'M','2023-11-04','Coordinator'),
(6,'Sophie','F','Willis',26,'F','2025-01-14','Catering'),
(7,'Matt','G','Nelson',35,'M','2022-10-09','Transport'),
(8,'Kate','H','Bond',27,'F','2022-08-19','Makeup Artist'),
(9,'Mason','I','Knight',30,'M','2023-12-29','Camera'),
(10,'Chloe','J','Evans',33,'F','2024-05-07','Wardrobe'),
(11,'Tom','J','King',34,'M','2023-04-12','Manager'),
(12,'Lucy','K','Brown',29,'F','2024-06-14','Assistant'),
(13,'Mark','L','Taylor',37,'M','2022-09-24','Technician'),
(14,'Dana','M','Adams',31,'F','2024-03-17','Coordinator'),
(15,'Alex','N','White',28,'M','2023-10-20','Security'),
(16,'Nancy','O','Scott',26,'F','2025-02-11','Logistics'),
(17,'George','P','Lewis',29,'M','2022-11-08','Driver'),
(18,'Mia','Q','Walker',30,'F','2023-04-25','Photographer'),
(19,'Harry','R','Hall',35,'M','2024-12-15','Sound Engineer'),
(20,'Olivia','S','Green',27,'F','2024-07-13','Assistant');
