DROP database IF EXISTS relibs;
CREATE database relibs;
USE relibs;

CREATE TABLE Author(
    
    AuthorID INT NOT NULL auto_increment,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL,
    YearOfBirth YEAR NOT NULL,
    PRIMARY KEY (AuthorID)
);

CREATE TABLE Publisher(
    
    PublisherID INT NOT NULL auto_increment,
    Name VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL,
    State VARCHAR(255) NOT NULL,
    YearStarted YEAR NOT NULL,
    PRIMARY KEY (PublisherID)
);

CREATE TABLE Book(
    
    BookID INT NOT NULL auto_increment,
    Title VARCHAR(255) NOT NULL,
    Genre VARCHAR(255) NOT NULL,
    PublisherID INT,
    Description VARCHAR(4096) NOT NULL,
    UnitPrice DECIMAL(5,2) NOT NULL,
    YearOfRelease YEAR NOT NULL,
    PRIMARY KEY (BookID),
    FOREIGN KEY (PublisherID) REFERENCES Publisher(PublisherID)
    
);

CREATE TABLE BookAuthor (

    BookID INT,
    AuthorID INT,
    PRIMARY KEY (BookID, AuthorID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID),
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
    
);

CREATE TABLE Review (

    ReviewID INT NOT NULL AUTO_INCREMENT,
    Comment VARCHAR(4096) NOT NULL,
    Rating INT NOT NULL,
    YearOfReview YEAR NOT NULL,
    PRIMARY KEY (ReviewID)
    
);

CREATE TABLE Reader (

    ReaderID INT NOT NULL auto_increment,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL,
    PRIMARY KEY (ReaderID)
    
);

CREATE TABLE ReaderBookReview (

    ReaderID INT,
    BookID INT,
    ReviewID INT,
    PRIMARY KEY (BookID, ReviewID, ReaderID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID),
    FOREIGN KEY (ReaderID) REFERENCES Reader(ReaderID),
    FOREIGN KEY (ReviewID) REFERENCES Review(ReviewID)
);

INSERT INTO Author (FirstName, LastName, Country, YearOfBirth) VALUES 
('John', 'Green', 'USA', '1977'),
('Cassandra', 'Clare', 'USA', '1973'),
('J.R.R.', 'Tolkien', 'England', '1892'),
('William', 'Shakespeare', 'England', '1564'),
('J.K.', 'Rowling', 'England', '1965'),
('David', 'Levithan', 'USA', '1972'),
('Holly', 'Black', 'USA', '1971'),
('Lucas','Johnson','Canada','1967'),
('Sheldon','Dickinson','Jamaica','1964'),
('Jolie','Renner','Ireland','1972'),
('Esta','Kertzmann','Germany','1953'),
('Felicia','King','United States','1960'),
('Carlee','Schmitt','United States','1961'),
('Lessie','Wiegand','Germany','1969'),
('Chelsie','Roberts','United States','1958'),
('Arlene','Olson','United States','1974'); 

INSERT INTO Publisher (Name, Country, State, YearStarted) VALUES 
('Dutton Juvenile', 'USA', 'Massachusetts', '1975'),
('Margaret K. McElderry', 'USA', 'New York', '1962'),
('George Allen & Unwin', 'Australia', 'Sydney', '1973'),
('CreateSpace Independent Publishing Platform', 'USA', 'South Carolina', '1965'),
('Scholastic', 'USA', 'New York', '1980'),
('Penguin Books', 'UK', 'London', '1943'),
('Volkman Ltd','Canada', 'Toronto', '2003'),
('Bernhard Publishers', 'USA', 'California', '1998'),
('Rippin Ltd','France', 'Paris', '1982'),
('Crona PLC','England', 'Chelsea', '1970'),
('Bahringer-Eichmann', 'Germany', 'Berlin', '1974'),
('Lynch LLC', 'USA', 'Florida', '1999');


INSERT INTO Book (Title, Genre, PublisherID, Description, UnitPrice, YearOfRelease) VALUES 
('Looking for Alaska', 'Young Adult', 1, 'Miles Halter is fascinated by famous last words–and tired of his safe life at home. He leaves for boarding school to seek what the dying poet Francois Rabelais called the “Great Perhaps.” Much awaits Miles at Culver Creek, including Alaska Young. Clever, funny, screwed-up, and dead sexy, Alaska will pull Miles into her labyrinth and catapult him into the Great Perhaps.', 7.49,  '2005'),
('City of Heavenly Fire', 'Fantasy', 2, 'Darkness has descended on the Shadowhunter world. Chaos and destruction overwhelm the Nephilim as Clary, Jace, Simon, and their friends band together to fight the greatest evil they have ever faced: Clary’s own brother. Sebastian Morgenstern is on the move, systematically turning Shadowhunter against Shadowhunter. Bearing the Infernal Cup, he transforms Shadowhunters into creatures of nightmare, tearing apart families and lovers as the ranks of his Endarkened army swell. Nothing in this world can defeat Sebastian—but if they journey to the realm of demons, they just might have a chance… Lives will be lost, love sacrificed, and the whole world will change. Who will survive the explosive sixth and final installment of the Mortal Instruments series?', 14.58 ,'2014'),
('The Fellowship of the Ring', 'Fantasy', 3, 'The future of civilization rests in the fate of the One Ring, which has been lost for centuries. Powerful forces are unrelenting in their search for it. But fate has placed it in the hands of a young Hobbit named Frodo Baggins (Elijah Wood), who inherits the Ring and steps into legend. A daunting task lies ahead for Frodo when he becomes the Ringbearer - to destroy the One Ring in the fires of Mount Doom where it was forged.', 11.45, '2004'),
('Romeo & Juliet', 'Tragedy', 4, 'two young star-crossed lovers whose deaths ultimately reconcile their feuding families.', 6.99, '1997'),
("Harry Potter & the Sorcerer's Stone", 'Young Adult', 5, "Harry Potter has no idea how famous he is. That's because he's being raised by his miserable aunt and uncle who are terrified Harry will learn that he's really a wizard, just as his parents were. But everything changes when Harry is summoned to attend an infamous school for wizards, and he begins to discover some clues about his illustrious birthright. From the surprising way he is greeted by a lovable giant, to the unique curriculum and colorful faculty at his unusual school, Harry finds himself drawn deep inside a mystical world he never knew existed and closer to his own noble destiny.", 6.59, '1997'),
('Will Grayson, Will Grayson', 'Young Adult', 6, 'One cold night, in a most unlikely corner of Chicago, Will Grayson crosses paths with . . . Will Grayson. Two teens with the same name, running in two very different circles, suddenly find their lives going in new and unexpected directions, and culminating in epic turns-of-heart and the most fabulous musical ever to grace the high school stage.', 9.45, '2010' ),
('The Iron Trail', 'Fantasy', 6, 'Most kids would do anything to pass the Iron Trial. Not Callum Hunt. He wants to fail. ', 7.19, '2014'),
('The Hands of Time','Crime', 12,'Thrilling novel about a time criminal.', 3.99,'2000'),
('Just Like a Saturday','Romance', 9,'A tear filled journey through millenial love.', 5.99,'2000'),
('Lost in the Sauce','Comedy', 8,'Biography of young Smino Grigio.', 4.99,'2017'),
('Soul Food','Cookbook', 8,'A collection of Southern inspired dishes.', 7.00,'1999'),
('Python for Dummies','Education', 10,'Handbook with documentation and CD.', 2.34,'2013'),
('Love Languages','Romance', 7,'Timeless journey to love your partner through good and bad.', 7.77,'2008'),
('Road to Riches','Education', 12,'Investing in ETFs and mutual stocks to build wealth.', 5.00,'2007'),
('Gaza Christmas','Crime', 8,'A crippling tell all story of the Lizard murder by Vybz Kartel.', 3.00,'2018'),
('Bloody Hell','Comedy', 10,'A young lady trips and falls into a well, bloody hell.', 1.23,'1989'),
('Italian Recipes','Cookbook', 9,'The best dishes Italy has to offer.', 0.99,'1999'),
('Rise and Fall of the Nazi','Education', 11,'Adolf Hitler and his historic rise to and fall from power.', 6.67,'1988');


INSERT INTO BookAuthor (BookID, AuthorID) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(6, 1),
(7, 2),
(1, 13),
(2, 16),
(2, 9),
(3, 13),
(4, 13),
(4, 15),
(5, 12),
(6, 10),
(7, 11),
(8, 11),
(8, 16),
(9, 14);


INSERT INTO Review (Comment, Rating) VALUES 
('“What sets this novel apart is the brilliant, insightful, suffering but enduring voice of Miles Halter.”', 10),
('Love the style of the writing, and the characters', 10),
('I WAS HOOKED SINCE START TO FINISH', 9),
('I have never been torn by a book before', 6),
('Interesting', 4),
('Forever a classic', 8),
('I prefer The fault in our stars', 2),
('Loved it, had me on edge all the way through.', 5),
('It was corny, but still somewhat enjoyable.', 3),
('Funniest book I have ever read hands down. Smino is so crazy.', 5),
('I finally learned how make good cornbread with these recipes, Praise God!', 4),
('This book is it. The explanations are so simple yet effective.', 5),
('Useless advice and even some grammatical errors post publishing, terrible.', 1),
('I knew nothing about the stock market before and now I feel like DiCaprio in Wolf of Wall St.', 3),
('Gaza man crazy! Free world boss still nah go round it.', 4),
('Dumb book. Dont buy this crap.',1),
('My pasta seems to have gotten a little better so I cant complain', 3),
('Gully mi seh! Kartel can stay a jail yuh mad!', 1),
('Im too grown to teach you how to ride - Smino does it again lmaooo.', 5),
('My mac and cheese is finna slap now on foenem', 5),
('Book too long, not a pleasure to read', 1),
('To Hell with Hitler! Very informative book though.', 4);


INSERT INTO Reader (FirstName, LastName, Country) VALUES 
('Jainel', 'Torres', 'Puerto Rico'),
('Cynthia', 'Sustaita', 'USA'),
('Eduardo', 'Jimenez', 'Mexico'),
('Pedro', 'Rivera', 'Puerto Rico'),
('Fernando', 'Rodriguez', 'Puerto Rico'),
('Victoria', 'Black', 'UK'),
('Yang', 'Lu', 'China'),
('Larry','Yost','Canada'),
('Celine','Keebler','Cayman Islands'),
('Keisha','Brown','USA'),
('Kenneth','Aufderhar','Israel'),
('Ashley','Kertzmann','Germany'),
('Floy','Leuschke','France'),
('Lionel','Jacobs','Jamaica'),
('Chance','Predovic','Russia'),
('Ronny','Towne','Cuba'),
('Brennon','Ward','USA'),
('Dedric','Zulauf','Germany'),
('Dudley','Green','Jamaica'),
('Arvilla','McClure','Jamaica');


INSERT INTO ReaderBookReview(ReaderID, BookID, ReviewID) VALUES 
(1, 1, 1), 
(2, 3, 2),
(6, 2, 3),
(3, 4, 4),
(7, 7, 5),
(5, 5, 6),
(4, 6, 7),
(9, 8, 9),
(15, 9, 9),
(13, 10, 10),
(17, 11, 11),
(8, 12, 12),
(17, 13, 13),
(14, 14, 14),
(14, 15, 15),
(9, 16, 16),
(12, 17, 17),
(19, 18, 18),
(16, 10, 19),
(10, 11, 20),
(14, 13, 21),
(20, 18, 22);