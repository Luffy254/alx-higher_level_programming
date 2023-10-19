-- list all shows from hbtn_0d_tvshows_rate by their rating.
SELECT s.title AS Show_Title,
       SUM(r.rate) AS Show_Rating
  FROM tv_shows s
       JOIN tv_show_ratings r ON s.id = r.show_id
 GROUP BY Show_Title
 ORDER BY Show_Rating DESC;
