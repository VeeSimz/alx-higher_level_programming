-- Lists all the records of second_table of database hbtn_0c_0
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY  score DESC;
