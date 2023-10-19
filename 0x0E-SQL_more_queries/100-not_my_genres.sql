-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres AS g
LEFT JOIN (
    SELECT g.id
    FROM tv_genres AS g
    JOIN tv_show_genres AS sg ON g.id = sg.genre_id
    JOIN tv_shows AS s ON s.id = sg.show_id
    WHERE s.title = 'Dexter'
) AS linked_genres
ON g.id = linked_genres.id
WHERE linked_genres.id IS NULL
ORDER BY g.name ASC;
