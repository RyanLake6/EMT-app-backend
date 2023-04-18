-- This file is to bootstrap a database for the CS3200 project. 

-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API file(s),  the AppSmith 
-- data source creation.
CREATE DATABASE `emt_db`;

-- Move into the database we just created.
use `emt_db`;

-- Via the Docker Compose file, a special user called webapp will 
-- be created in MySQL. We are going to grant that user 
-- all privilages to the new database we just created. 
grant all privileges on emt_db.* to 'webapp'@'%';
flush privileges;


-- SQL DDL here:
CREATE TABLE Truck (
    truckID varchar(50) PRIMARY KEY,
    licensePlate varchar(10) NOT NULL UNIQUE,
    model varchar(50)
);

CREATE TABLE Patient (
    MRN varchar(50) PRIMARY KEY,
    dateOfBirth date,
    firstName varchar(30) NOT NULL,
    lastName varchar(30),
    runNumber varchar(50) NOT NULL
);

CREATE TABLE Emergency (
    runNumber varchar(50) PRIMARY KEY,
    truckID varchar(50) NOT NULL,
    startingMileage long,
    endingMileage long,
    totalMiles long,
    MRN varchar(50) NOT NULL,
    CONSTRAINT truck
        FOREIGN KEY (truckID) REFERENCES Truck (truckID),
    CONSTRAINT patientMRN
        FOREIGN KEY (MRN) REFERENCES Patient (MRN)
);

ALTER TABLE Patient
ADD FOREIGN KEY (runNumber) REFERENCES Emergency (runNumber);


CREATE TABLE Inventory (
    dateTime datetime,
    expirationDate datetime,
    name varchar(50),
    count int,
    truckID varchar(50) NOT NULL,
    CONSTRAINT truckInventory
        FOREIGN KEY (truckID) REFERENCES Truck (truckID)
);


CREATE TABLE Maintenance (
    fluidsChecked boolean,
    needsService boolean,
    inspectionExpiration date,
    dateTime datetime,
    truckID varchar(50) NOT NULL,
    CONSTRAINT truckMaintenance
        FOREIGN KEY (truckID) REFERENCES Truck (truckID)
);


CREATE TABLE Times (
    dispatched datetime,
    enRoute datetime,
    onScene datetime,
    departTime datetime,
    hospitalArrival datetime,
    inService datetime,
    runNumber varchar(50) NOT NULL,
    CONSTRAINT runNumberTimes
        FOREIGN KEY (runNumber) REFERENCES Emergency (runNumber)
);


CREATE TABLE PaymentInfo (
    firstName varchar(30) NOT NULL,
    lastName varchar(30) NOT NULL,
    cardType varchar(20) NOT NULL,
    cardNumber varchar(30) PRIMARY KEY,
    CVC varchar(5) NOT NULL,
    expirationDate date NOT NULL
);


CREATE TABLE Billing (
    cost double,
    total double,
    tax double,
    runNumber varchar(50) NOT NULL,
    cardNumber varchar(30) NOT NULL,
    CONSTRAINT billingCardNumber
        FOREIGN KEY (cardNumber) REFERENCES PaymentInfo (cardNumber),
    CONSTRAINT billingRunNumber
        FOREIGN KEY (runNumber) REFERENCES Emergency (runNumber)
);


CREATE TABLE Insurance (
    subscriberID varchar(40) NOT NULL,
    groupNumber varchar(40),
    provider varchar(40) NOT NULL,
    subscriberDateOfBirth date,
    firstNameSubscriber varchar(30),
    lastNameSubscriber varchar(30),
    MRN varchar(50) NOT NULL,
    CONSTRAINT insuranceMRN
        FOREIGN KEY (MRN) REFERENCES Patient (MRN)
);


CREATE TABLE MedicalInfo (
    MRN varchar(50) NOT NULL,
    CONSTRAINT MedicalInfoMRN
        FOREIGN KEY (MRN) REFERENCES Patient (MRN)
);

CREATE TABLE PastMedicalHistory (
    MRN varchar(50) NOT NULL,
    pastMedicalHistory varchar(200),
    CONSTRAINT PastMedicalHistoryMRN
        FOREIGN KEY (MRN) REFERENCES MedicalInfo (MRN)
);

CREATE TABLE Medications (
    MRN varchar(50) NOT NULL,
    medications varchar(100),
    CONSTRAINT MedicationsMRN
        FOREIGN KEY (MRN) REFERENCES MedicalInfo (MRN)
);

CREATE TABLE Allergies (
    MRN varchar(50) NOT NULL,
    Allergies varchar(100),
    CONSTRAINT AllergiesMRN
        FOREIGN KEY (MRN) REFERENCES MedicalInfo (MRN)
);


CREATE TABLE Survey (
    rating INT CHECK (rating >= 1 AND rating <= 10),
    response varchar(100),
    MRN varchar(50) NOT NULL,
    CONSTRAINT SurveyMRN
        FOREIGN KEY (MRN) REFERENCES Patient (MRN)
);


CREATE TABLE Shifts (
    shiftID varchar(30) PRIMARY KEY,
    startTime datetime,
    endTime datetime,
    durationHours double
);

CREATE TABLE Employees (
    firstName varchar(30) NOT NULL,
    lastName varchar(30) NOT NULL,
    employeeID varchar(30) PRIMARY KEY,
    qual varchar(30),
    shiftID varchar(30) NOT NULL,
    CONSTRAINT shiftsID
        FOREIGN KEY (shiftID) REFERENCES Shifts (shiftID)
);

CREATE TABLE EmergencyEmployee (
    runNumber varchar(50) NOT NULL,
    employeeID varchar(30) NOT NULL,
    CONSTRAINT emergencyEmployeeRunNumber
        FOREIGN KEY (runNumber) REFERENCES Emergency (runNumber),
    CONSTRAINT emergencyEmployeeEmployeeID
        FOREIGN KEY (employeeID) REFERENCES Employees (employeeID)
);

CREATE TABLE Vitals (
    bpSystolic int UNSIGNED,
    bpDiastolic int UNSIGNED,
    oxygenSaturation int UNSIGNED CHECK (oxygenSaturation > 0 AND oxygenSaturation <= 100),
    oxygenRoute ENUM('Room air', '1-6 lmp', '7-12 lmp', '13+ lmp'),
    respRate int UNSIGNED,
    respEffort ENUM('Normal', 'Labored'),
    gcsEyes int UNSIGNED CHECK ( gcsEyes > 0 AND gcsEyes <= 4),
    gcsVerbal int UNSIGNED CHECK ( gcsVerbal > 0 AND gcsVerbal <= 5),
    gcsMotor int UNSIGNED CHECK ( gcsMotor > 0 AND gcsMotor <= 6),
    gcsTotal int AS (gcsEyes + gcsMotor + gcsVerbal) STORED,
    heartRate int UNSIGNED,
    hrQuality ENUM ('Strong', 'Weak', 'Thready'),
    LOC ENUM('Alert', 'Verbal', 'Pain', 'Unresponsive'),
    skinColor char(50),
    skinCondition char(50),
    skinTemp char(50),
    painLevel int UNSIGNED check ( painLevel <= 10 ),
    bodyTemp double UNSIGNED,
    pupilsLeft char(50),
    pupilsRight char(50),
    MRN varchar(50),
    timeTaken datetime NOT NULL,
    CONSTRAINT vitalsMRN
        FOREIGN KEY (MRN) references Patient (MRN)
);

CREATE TABLE DispatchInfo (
    dateTime datetime,
    callType varchar(50),
    address varchar(50),
    agency varchar(30),
    runNumber varchar(50),
    CONSTRAINT dispatchInfoRunNumber
        FOREIGN KEY (runNumber) REFERENCES Patient (runNumber)
);

-- Adding Sample Data:
-- INSERT INTO test_table
--   (name, color)
-- VALUES
--   ('dev', 'blue'),
--   ('pro', 'yellow'),
--   ('junior', 'red');