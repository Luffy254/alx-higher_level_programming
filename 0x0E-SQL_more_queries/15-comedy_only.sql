-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT s.title
FROM tv_shows s, tv_show_genres sg, tv_genres g
WHERE s.id = sg.show_id
AND g.id = sg.genre_id
AND g.name = 'Comedy'
ORDER BY s.title ASC;
