-- This SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes and store
-- the average score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN input_user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score 
    FROM corrections 
    WHERE user_id = input_user_id;

    -- Update the average_score in the users table
    UPDATE users 
    SET average_score = avg_score 
    WHERE id = input_user_id;
END $$

DELIMITER ;
