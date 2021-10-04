Select  Distinct ACTOR_PELICULA 
from ACTOR
where split_part(ACTOR_PELICULA,' ',2) LIKE '%son%'

order by ACTOR_PELICULA DESC;