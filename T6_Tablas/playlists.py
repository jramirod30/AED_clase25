from typing import List, Set, Dict

lucia: Set[str] = {"C. Tangana", "Rosalia", "Taylor Swift", "Tame Impala", "Delaossa"}
javi: Set[str] = {"Bad Bunny", "Karol G", "Taylor Swift", "Tame Impala"}
sofia: Set[str] = {"Rosalia", "Tame Impala", "The Weeknd", "Bad Bunny", "Taylor Swift"}

# a) ¿Qué artistas están en todas las playlists?
todos_los_artistas: Set[str] = lucia | javi | sofia
print("a) todos:")
print(todos_los_artistas)

print("b) en comun:")
print(lucia & javi & sofia)

print("c) Solo lucia:")
solo_lucia: Set[str] = lucia - (javi | sofia)
print(solo_lucia)
# TODO print()

# Lista de todas las playlists
todasPlaylists: List[Set[str]] = [lucia, javi, sofia]
# Contador de artistas
conteo_artistas: Dict[str, int] = {}
for playlist in todasPlaylists:
    for artista in playlist:
        conteo_artistas[artista] = conteo_artistas.get(artista, 0) + 1
# Crear la playlist para la fiesta
playlist_fiesta: Set[str] = set()
for artista, veces in conteo_artistas.items():
    if veces >= 2:
        playlist_fiesta.add(artista)
print("e) Playlist para la fiesta:", sorted(playlist_fiesta))
