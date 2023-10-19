-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT title, NULL AS genre_id
FROM tv_shows
WHERE id NOT IN (SELECT show_id FROM tv_show_genres)
ORDER BY title, genre_id;
