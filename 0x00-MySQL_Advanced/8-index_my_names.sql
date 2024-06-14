-- This SQL script creates an index idx_name_first on
-- the table names and the first letter of name.

ALTER TABLE names
ADD first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED,
ADD INDEX idx_name_first (first_letter);
