CREATE TABLE drivers(
    driver_id SERIAL PRIMARY KEY,
    driver_number INT,
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