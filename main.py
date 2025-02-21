
from streamlit_elements import elements, mui, html
import billboard


with elements("new_element"):
    name = billboard.get_music()
    for e in name:
        music=billboard.spotify_music(e['title'])
        html.li(f"{e['title']} - {e['author']}: {music['spotify_url']}")
       


