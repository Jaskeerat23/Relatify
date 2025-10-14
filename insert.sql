USE Relatify;

-- Insert into Users
INSERT INTO Users (UserName, Fname, Mname, Lname, Email, PhoneNo, AccountPassword, City, DOB, Gender)
VALUES 
('charlie1', 'Charlie', 'O', 'Gonzalez', 'charlie1@example.com', '8688595960', 'pass123', 'San Diego', '1990-06-06', 'F'),
('leo2', 'Leo', 'O', 'Martinez', 'leo2@example.com', '4264175127', 'pass123', 'Phoenix', '1991-06-14', 'M'),
('grace3', 'Grace', 'C', 'Wilson', 'grace3@example.com', '2397559435', 'pass123', 'Los Angeles', '1983-02-24', 'M'),
('mia4', 'Mia', 'M', 'Wilson', 'mia4@example.com', '1056313756', 'pass123', 'Houston', '1993-06-03', 'F'),
('jack5', 'Jack', 'O', 'Miller', 'jack5@example.com', '3144476925', 'pass123', 'Jacksonville', '2003-11-17', 'F'),
('jane6', 'Jane', 'J', 'Miller', 'jane6@example.com', '1336030973', 'pass123', 'Columbus', '1992-05-10', 'M'),
('ivy7', 'Ivy', 'E', 'Wilson', 'ivy7@example.com', '4822319037', 'pass123', 'Los Angeles', '1994-02-17', 'F'),
('charlie8', 'Charlie', 'N', 'Lopez', 'charlie8@example.com', '9275476755', 'pass123', 'Austin', '1990-12-26', 'M'),
('john9', 'John', 'A', 'Jones', 'john9@example.com', '6772227532', 'pass123', 'Columbus', '1992-08-07', 'F'),
('john10', 'John', 'M', 'Smith', 'john10@example.com', '7187410352', 'pass123', 'San Jose', '1998-03-20', 'F'),
('john11', 'John', 'L', 'Davis', 'john11@example.com', '1580990437', 'pass123', 'Philadelphia', '1996-10-02', 'F'),
('jane12', 'Jane', 'F', 'Smith', 'jane12@example.com', '0644221818', 'pass123', 'Jacksonville', '1984-12-26', 'M'),
('noah13', 'Noah', 'C', 'Lopez', 'noah13@example.com', '8781128894', 'pass123', 'Austin', '1993-01-13', 'M'),
('ivy14', 'Ivy', 'D', 'Anderson', 'ivy14@example.com', '0718334861', 'pass123', 'Chicago', '1988-12-02', 'M'),
('david15', 'David', 'O', 'Anderson', 'david15@example.com', '1596255208', 'pass123', 'San Antonio', '2003-02-18', 'M');

-- Insert into Artists
INSERT INTO Artists (UserName, StageName, Fname, Mname, Lname, Email, AccountPassword, Genre, City, ContractFee)
VALUES 
('artist1', 'Stage1', 'Ivy', 'E', 'Smith', 'artist1@example.com', 'pass123', 'Folk', 'New York', 7812.50),
('artist2', 'Stage2', 'Eve', 'B', 'Martinez', 'artist2@example.com', 'pass123', 'Classical', 'San Diego', 8567.51),
('artist3', 'Stage3', 'Grace', 'E', 'Garcia', 'artist3@example.com', 'pass123', 'R&B', 'Phoenix', 3129.54),
('artist4', 'Stage4', 'Eve', 'L', 'Gonzalez', 'artist4@example.com', 'pass123', 'Blues', 'Austin', 6095.76),
('artist5', 'Stage5', 'Alice', 'B', 'Wilson', 'artist5@example.com', 'pass123', 'Metal', 'Philadelphia', 2060.31),
('artist6', 'Stage6', 'Kara', 'J', 'Rodriguez', 'artist6@example.com', 'pass123', 'Punk', 'Fort Worth', 1903.73),
('artist7', 'Stage7', 'Alice', 'F', 'Smith', 'artist7@example.com', 'pass123', 'R&B', 'Chicago', 4344.89),
('artist8', 'Stage8', 'Jane', 'B', 'Johnson', 'artist8@example.com', 'pass123', 'Soul', 'Phoenix', 1522.12),
('artist9', 'Stage9', 'Jane', 'K', 'Garcia', 'artist9@example.com', 'pass123', 'Jazz', 'Los Angeles', 9474.83),
('artist10', 'Stage10', 'Grace', 'A', 'Brown', 'artist10@example.com', 'pass123', 'Blues', 'Charlotte', 5003.00),
('artist11', 'Stage11', 'Frank', 'I', 'Jones', 'artist11@example.com', 'pass123', 'Classical', 'Phoenix', 9197.15),
('artist12', 'Stage12', 'Leo', 'B', 'Jones', 'artist12@example.com', 'pass123', 'Punk', 'Chicago', 8344.38),
('artist13', 'Stage13', 'David', 'D', 'Anderson', 'artist13@example.com', 'pass123', 'Rock', 'Houston', 1509.99),
('artist14', 'Stage14', 'Henry', 'A', 'Williams', 'artist14@example.com', 'pass123', 'R&B', 'Dallas', 2076.58),
('artist15', 'Stage15', 'Alice', 'H', 'Anderson', 'artist15@example.com', 'pass123', 'Blues', 'San Antonio', 6286.71);

-- Insert into Organizers
INSERT INTO Organizers (UserName, OrgName, Email, AccountPassword, City)
VALUES 
('org1', 'OrgName1', 'org1@example.com', 'pass123', 'Chicago'),
('org2', 'OrgName2', 'org2@example.com', 'pass123', 'Dallas'),
('org3', 'OrgName3', 'org3@example.com', 'pass123', 'Houston'),
('org4', 'OrgName4', 'org4@example.com', 'pass123', 'Fort Worth'),
('org5', 'OrgName5', 'org5@example.com', 'pass123', 'San Jose'),
('org6', 'OrgName6', 'org6@example.com', 'pass123', 'Columbus'),
('org7', 'OrgName7', 'org7@example.com', 'pass123', 'New York'),
('org8', 'OrgName8', 'org8@example.com', 'pass123', 'Phoenix'),
('org9', 'OrgName9', 'org9@example.com', 'pass123', 'Houston'),
('org10', 'OrgName10', 'org10@example.com', 'pass123', 'Phoenix'),
('org11', 'OrgName11', 'org11@example.com', 'pass123', 'Fort Worth'),
('org12', 'OrgName12', 'org12@example.com', 'pass123', 'Houston'),
('org13', 'OrgName13', 'org13@example.com', 'pass123', 'Charlotte'),
('org14', 'OrgName14', 'org14@example.com', 'pass123', 'San Jose'),
('org15', 'OrgName15', 'org15@example.com', 'pass123', 'Jacksonville');

-- Insert into Crewmembers
INSERT INTO Crewmembers (UserName, Fname, Mname, Lname, Email, PhoneNo, AccountPassword, City, DOJ, Gender, MemberRole)
VALUES 
('crew1', 'Kara', 'C', 'Davis', 'crew1@example.com', '9009368314', 'pass123', 'Phoenix', '2017-03-06', 'F', 'Designer'),
('crew2', 'Jack', 'D', 'Johnson', 'crew2@example.com', '2282786967', 'pass123', 'Dallas', '2022-01-03', 'F', 'Coordinator'),
('crew3', 'Jane', 'J', 'Smith', 'crew3@example.com', '9890537910', 'pass123', 'Chicago', '2024-04-01', 'F', 'Caterer'),
('crew4', 'David', 'J', 'Williams', 'crew4@example.com', '5206132823', 'pass123', 'San Diego', '2021-01-28', 'F', 'Technician'),
('crew5', 'Bob', 'N', 'Johnson', 'crew5@example.com', '9915186565', 'pass123', 'Fort Worth', '2012-10-18', 'F', 'Lighting'),
('crew6', 'David', 'O', 'Brown', 'crew6@example.com', '1969731800', 'pass123', 'New York', '2010-02-02', 'M', 'Sound Engineer'),
('crew7', 'Noah', 'H', 'Williams', 'crew7@example.com', '7178498122', 'pass123', 'Phoenix', '2016-07-03', 'F', 'Sound Engineer'),
('crew8', 'Leo', 'H', 'Miller', 'crew8@example.com', '0390834220', 'pass123', 'San Diego', '2021-12-08', 'M', 'Sound Engineer'),
('crew9', 'Mia', 'F', 'Martinez', 'crew9@example.com', '0661217254', 'pass123', 'Fort Worth', '2014-01-21', 'M', 'Sound Engineer'),
('crew10', 'Noah', 'G', 'Brown', 'crew10@example.com', '8608316092', 'pass123', 'San Diego', '2025-02-03', 'F', 'Promoter'),
('crew11', 'John', 'G', 'Brown', 'crew11@example.com', '0396370947', 'pass123', 'San Diego', '2016-06-17', 'M', 'Promoter'),
('crew12', 'Ivy', 'E', 'Garcia', 'crew12@example.com', '6266673230', 'pass123', 'Fort Worth', '2011-07-04', 'M', 'Usher'),
('crew13', 'Grace', 'G', 'Brown', 'crew13@example.com', '0972877043', 'pass123', 'Phoenix', '2018-03-22', 'M', 'Manager'),
('crew14', 'Leo', 'J', 'Davis', 'crew14@example.com', '9837941391', 'pass123', 'Austin', '2010-02-17', 'F', 'Photographer'),
('crew15', 'John', 'D', 'Wilson', 'crew15@example.com', '9711729887', 'pass123', 'Dallas', '2015-07-05', 'M', 'Designer');

-- Insert into Fests
INSERT INTO Fests (FestName, City, StartDate, DescriptionFest)
VALUES 
('EcoFest', 'San Jose', '2024-04-25', 'Description for EcoFest 1'),
('MusicFest', 'San Antonio', '2024-12-22', 'Description for MusicFest 2'),
('GameFest', 'Columbus', '2025-06-15', 'Description for GameFest 3'),
('ComedyFest', 'Houston', '2023-05-14', 'Description for ComedyFest 4'),
('GameFest', 'Fort Worth', '2025-05-01', 'Description for GameFest 5'),
('JazzFest', 'Charlotte', '2023-10-02', 'Description for JazzFest 6'),
('RockFest', 'New York', '2025-04-22', 'Description for RockFest 7'),
('DanceFest', 'San Diego', '2025-09-10', 'Description for DanceFest 8'),
('PopFest', 'San Diego', '2025-01-08', 'Description for PopFest 9'),
('JazzFest', 'New York', '2024-01-20', 'Description for JazzFest 10'),
('JazzFest', 'Los Angeles', '2024-03-27', 'Description for JazzFest 11'),
('FilmFest', 'Chicago', '2024-05-08', 'Description for FilmFest 12'),
('GameFest', 'Houston', '2024-12-21', 'Description for GameFest 13'),
('MusicFest', 'New York', '2023-12-02', 'Description for MusicFest 14'),
('DanceFest', 'San Jose', '2025-04-17', 'Description for DanceFest 15');

-- Insert into EventsInFest
INSERT INTO EventsInFest (FestId, EventName, DescriptionEvent, EventDate, EventTime)
VALUES 
(10, 'Tour', 'Desc for Tour 1', '2025-05-25', '17:35:00'),
(12, 'Showcase', 'Desc for Showcase 2', '2024-11-19', '21:31:00'),
(15, 'Workshop', 'Desc for Workshop 3', '2024-03-16', '07:46:00'),
(8, 'Party', 'Desc for Party 4', '2023-10-16', '16:48:00'),
(14, 'Exhibition', 'Desc for Exhibition 5', '2024-05-17', '00:41:00'),
(12, 'Carnival', 'Desc for Carnival 6', '2023-01-21', '08:11:00'),
(14, 'Workshop', 'Desc for Workshop 7', '2024-01-18', '15:23:00'),
(5, 'Panel', 'Desc for Panel 8', '2023-05-17', '12:37:00'),
(1, 'Performance', 'Desc for Performance 9', '2025-03-27', '00:32:00'),
(15, 'Carnival', 'Desc for Carnival 10', '2023-07-12', '01:49:00'),
(2, 'Parade', 'Desc for Parade 11', '2023-05-01', '11:11:00'),
(12, 'Panel', 'Desc for Panel 12', '2023-10-05', '08:23:00'),
(1, 'Seminar', 'Desc for Seminar 13', '2023-02-14', '12:27:00'),
(11, 'Workshop', 'Desc for Workshop 14', '2024-05-26', '04:24:00'),
(14, 'Festival', 'Desc for Festival 15', '2023-09-04', '03:57:00');

-- Insert into Stage
INSERT INTO Stage (ArtistId)
VALUES 
(3), (2), (10), (3), (6), (6), (12), (1), (3), (6), (10), (15), (6), (11), (14);

-- Insert into Tickets
INSERT INTO Tickets (FestId, UserId, Tier, CostPrice, PurchaseDate)
VALUES 
(5, 8, 3, 54.61, '2023-01-06'),
(14, 4, 2, 457.46, '2024-04-20'),
(6, 5, 3, 254.57, '2024-05-06'),
(7, 10, 2, 250.23, '2024-06-19'),
(14, 8, 3, 329.10, '2025-12-25'),
(9, 13, 3, 298.60, '2023-03-18'),
(14, 9, 1, 251.73, '2023-10-28'),
(2, 6, 1, 141.53, '2024-10-16'),
(7, 1, 2, 125.35, '2025-01-13'),
(1, 11, 2, 106.76, '2024-11-11'),
(15, 3, 1, 170.86, '2024-08-06'),
(15, 6, 2, 239.11, '2025-09-07'),
(15, 10, 1, 305.39, '2023-05-22'),
(14, 12, 3, 275.20, '2023-04-01'),
(13, 9, 1, 370.24, '2024-01-23');
-- Insert into Sponsors
INSERT INTO Sponsors (SponsorName, FestId)
VALUES 
('SyndicateO', 14),
('AssocJ', 8),
('AssocJ', 4),
('CorpA', 11),
('IncG', 8),
('AssocJ', 11),
('CompanyC', 14),
('LtdH', 3),
('UnionK', 8),
('OrgI', 8),
('PartnersN', 6),
('SyndicateO', 3),
('BrandB', 10),
('LtdH', 14),
('AssocJ', 12);

-- Insert into UserFavourites
INSERT INTO UserFavourites (UserId, ArtistId)
VALUES 
(6, 3), (1, 4), (13, 14), (15, 12), (6, 11),
(2, 5), (14, 14), (10, 2), (11, 9), (7, 13),
(15, 4), (1, 5), (11, 12), (15, 6), (1, 3);

-- Insert into UserFests
INSERT INTO UserFests (UserId, FestId)
VALUES 
(10, 9), (10, 11), (8, 1), (7, 15), (4, 10),
(9, 4), (11, 3), (4, 3), (6, 4), (10, 5),
(1, 4), (15, 14), (12, 7), (4, 2), (14, 3);

-- Insert into ArtistEvents
INSERT INTO ArtistEvents (ArtistId, EventId)
VALUES 
(3, 6), (1, 4), (7, 3), (15, 5), (12, 1),
(7, 1), (15, 9), (10, 15), (3, 7), (9, 7),
(9, 3), (10, 5), (13, 14), (13, 12), (1, 12);