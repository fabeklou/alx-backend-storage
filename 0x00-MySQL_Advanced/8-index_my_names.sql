-- This SQL script creates an index idx_name_first on
-- the table names and the first letter of name.

-- Add a generated column for the first letter of name
ALTER TABLE names
ADD COLUMN name_first_letter CHAR(1) AS (LEFT(name, 1)) STORED;

-- Create an index on the generated column
CREATE INDEX idx_name_first ON names (name_first_letter);
