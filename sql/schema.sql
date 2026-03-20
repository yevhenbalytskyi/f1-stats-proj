CREATE TABLE drivers(
    id SERIAL PRIMARY KEY,
    driver_number INT,
    session_key INT,
    full_name VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    name_acronym VARCHAR(10)
);

CREATE TABLE meetings(
    meeting_key INT PRIMARY KEY,
    year_ INT,
    meeting_name VARCHAR(255),
    country VARCHAR(255),
    location_ VARCHAR(255),
    circuit_short_name VARCHAR(255)
);


CREATE TABLE sessions(
    session_key INT PRIMARY KEY,
    meeting_key INT,
    CONSTRAINT meeting_key FOREIGN KEY (meeting_key)
    REFERENCES meetings(meeting_key),
    session_name VARCHAR(255),
    session_type VARCHAR(255),
    date_start TIMESTAMP WITH TIME ZONE,
    date_end TIMESTAMP WITH TIME ZONE
);


CREATE TABLE pit_stops(
    pit_stop_id SERIAL PRIMARY KEY,
    session_key INT REFERENCES sessions(session_key),
    driver_number INT,
    lap_number INT,
    lane_duration FLOAT,
    stop_duration FLOAT
);