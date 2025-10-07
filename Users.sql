USE Relatify;

--Creating USERS table, that will store information of
--Normal Audiences using this application for exploring events
CREATE TABLE Users(
    UserId INT PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(25),
    Fname VARCHAR(25),
    Mname VARCHAR(25),
    Lname VARCHAR(25),
    Email VARCHAR(50),
    PhoneNo VARCHAR(11),
    AccountPassword VARCHAR(25),
    City VARCHAR(25),
    DOB DATE,
    Gender CHAR(1)
);

--Next up, we create a table for Artists, this table will contain
--info about different artists that can be used by organizers to book
--artists for their fest and also users can flag their favourite artists
--this info of users will be used in future expansion to provide recommendations to users
--about the fest of their favourite artists
CREATE TABLE Artists(
    ArtistId INT PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(25),
    StageName VARCHAR(25),
    Fname VARCHAR(25),
    Mname VARCHAR(25),
    Lname VARCHAR(25),
    Email VARCHAR(50),
    AccountPassword VARCHAR(25),
    Genre VARCHAR(25),
    City VARCHAR(25),
    ContractFee DECIMAL(10, 2)
);
--We have taken username and stagename as two different attributes because
--there can be situations where stagename of two artists can be same leading to data redundancy


--Next we are going to create a table for organizers, i.e. organizations that
--organizes fest for eg Graphic Era organizes Grafest
CREATE TABLE Organizers(
    OrgId INT PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(25),
    OrgName VARCHAR(50),
    Email VARCHAR(50),
    AccountPassword VARCHAR(25),
    City VARCHAR(25)
);

CREATE TABLE Crewmembers(
    MemberId INT PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(25),
    Fname VARCHAR(25),
    Mname VARCHAR(25),
    Lname VARCHAR(25),
    Email VARCHAR(50),
    PhoneNo VARCHAR(11),
    AccountPassword VARCHAR(25),
    City VARCHAR(25),
    DOJ DATE,
    Gender CHAR(1),
    MemberRole VARCHAR(25)
)