
from streamlit_elements import elements, mui, html
import billboard
import streamlit as st
import datetime

def main():
    st.title("Top da Billboard - Mês/Ano")
    #cria o input para o usuario escolher a data
    date_str = st.date_input("Escolha o Dia, Mês e Ano", datetime.date(2025, 1, 1))
    
 
    if st.button("Buscar Top 10", type="primary"):
        with st.spinner("Carregando dados da Billboard..."):
            #cria as colunas para o titulo e os dados
            row_title = st.columns(5)
            with row_title[0]:
                st.write("Rank")
            with row_title[1]:
                st.write("Música")
            with row_title[2]:
                st.write("Artista")
            with row_title[3]:
                st.write("spotify")
            with row_title [4]:
                st.write("Capa álbum")
            row_data = st.columns(5,vertical_alignment="center")

            #verifica se o json existe, caso contrario ir buscar os dados no site da billboard
        if billboard.billboard_10_ano_mes_JSON(date_str):
                chart_data = billboard.billboard_10_ano_mes_JSON(date_str)
        else:
                chart_data = billboard.billboard_10_ano_mes_API(date_str)

            #verifica se os dados foram encontrados
        if chart_data:
            st.success(f"Resultados para {date_str} da billboard")
            for pos, track in enumerate(chart_data):
                #procura os dados da musica no spotify
                data = billboard.procurar_musica(track['title'])
                
                with row_data[0].container(height=120):
                        st.write(pos+1)
                with row_data[1].container(height=120):
                        st.write(data['nome'])
                with row_data[2].container(height=120):
                    st.write(data['artista'])
                with row_data[3].container(height=120):
                    st.link_button("",data['spotify_url'], icon=":material/play_arrow:")
                with row_data[4].container(height=120):
                    st.image(data['image'])
        else:
            st.error("Não foi possível obter dados para a data selecionada.")
 
if __name__ == "__main__":
    main()