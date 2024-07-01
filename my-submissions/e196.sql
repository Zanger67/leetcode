# Write your MySQL query statement below
DELETE largerRepeat 
FROM Person largerRepeat, Person smallerRepeat 
WHERE largerRepeat.id > smallerRepeat.id 
    AND largerRepeat.email = smallerRepeat.email