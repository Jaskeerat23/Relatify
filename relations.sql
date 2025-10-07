USE Relatify;

CREATE TABLE UserFavourites(
    UserId INT,
    ArtistId INT,
    FOREIGN KEY (UserId) REFERENCES Users(UserId),
    FOREIGN KEY (ArtistId) REFERENCES Artists(ArtistId)
)

CREATE TABLE UserFests(
    UserId INT,
    FestId INT,
    FOREIGN KEY (UserId) REFERENCES Users(UserId),
    FOREIGN KEY (FestId) REFERENCES Fests(FestId)
)

--Note that we will have relationship between artist and event that artist have performed not b/w artist and fest
CREATE TABLE ArtistEvents(
    ArtistId INT,
    EventId INT,
    FOREIGN KEY (ArtistId) REFERENCES Artists(ArtistId),
    FOREIGN KEY (EventId) REFERENCES EventsInFest(EventId)
);