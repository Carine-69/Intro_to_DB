-- This script prints the full description of the 'books' table in the specified database

SELECT COLUMN_NAME, 
       DATA_TYPE, 
       CHARACTER_MAXIMUM_LENGTH, 
       IS_NULLABLE, 
       COLUMN_DEFAULT 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'books' 
  AND TABLE_SCHEMA = DATABASE();
