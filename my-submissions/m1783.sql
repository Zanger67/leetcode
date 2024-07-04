# Write your MySQL query statement below

SELECT player_id, 
        player_name, 
        sum(player_id=Wimbledon) + sum(player_id=Fr_open) + sum(player_id=US_open) + sum(player_id=Au_open) as 'grand_slams_count'
FROM Players JOIN Championships on Players.player_id = Championships.Wimbledon or 
                               Players.player_id = Championships.Fr_open or 
                               Players.player_id = Championships.US_open or 
                               Players.player_id = Championships.Au_open
GROUP BY player_id