-- This script prints the full description of the 'Books' table in the 'alx_book_store' database

SELECT COLUMN_NAME, 
       COLUMN_TYPE, 
       IS_NULLABLE, 
       COLUMN_DEFAULT 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Books' 
  AND TABLE_SCHEMA = 'alx_book_store';
