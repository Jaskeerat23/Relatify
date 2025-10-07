USE Relatify;

--We will have a table FEST which will contain the information
--regarding the fest eg. Start Date of that fest, in which city the
--fest is organized and also number of events in that fest
CREATE TABLE Fests(
    FestId INT PRIMARY KEY AUTO_INCREMENT,
    FestName VARCHAR(50),
    City VARCHAR(50),
    StartDate DATE,
    DescriptionFest VARCHAR(500)
);

--Now we will create a table for EVENTS, this will have information
--about the events that will be taking place in the fest with FestId
--Event and Fest will have many to 1 relationship since
--one fest can have many events but many events can be mapped to single fest
CREATE TABLE EventsInFest (
    EventId INT PRIMARY KEY AUTO_INCREMENT,
    FestId INT,
    EventName VARCHAR(50),
    DescriptionEvent VARCHAR(500),
    EventDate DATE,
    EventTime TIME,
    FOREIGN KEY (FestId) REFERENCES Fests(FestId)
);

CREATE TABLE Stage(
    StageId INT PRIMARY KEY AUTO_INCREMENT,
    ArtistId INT,
    FOREIGN KEY (ArtistId) REFERENCES Artists(ArtistId)
);

CREATE TABLE Tickets(
    TicketId INT PRIMARY KEY AUTO_INCREMENT,
    FestId INT,
    UserId INT,
    Tier INT,
    CostPrice DECIMAL(10, 2),
    PurchaseDate DATE,
    FOREIGN KEY (FestId) REFERENCES Fests(FestId),
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);

CREATE TABLE Sponsors(
    SponsorId INT PRIMARY KEY AUTO_INCREMENT,
    SponsorName VARCHAR(50),
    FestId INT,
    FOREIGN KEY (FestId) REFERENCES Fests(FestId)
);