mkdir -p ~/.streamlit/
echo "[theme]
<<<<<<< HEAD
# primaryColor = '#84a3a7'
# backgroundColor = '#EFEDE8'
# secondaryBackgroundColor = '#fafafa'
# textColor= '#424242'
# font = 'sans serif'
=======
# primaryColor = '#E694FF'
# backgroundColor = ‘#00172b’
# secondaryBackgroundColor = ‘#0083bb’
# textColor= ‘#ffffff’
# font = ‘sans serif’
>>>>>>> a15e3f04475eafe892dadd29c76565d7c77756f4
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml

# echo "\
# [theme]\n\
# primaryColor='#E694FF'\n\
# backgroundColor='#00172B'\n\
# secondaryBackgroundColor="#0083BB"
# textColor='#FFFFFF'\n\
# font='sans serif'\n\
# [deprecation]\n\
# showPyplotGlobalUse = false\n\
# [server]\n\
# headless = true\n\
# enableCORS = false\n\
# port = $PORT\n\
# " > ~/.streamlit/config.toml
