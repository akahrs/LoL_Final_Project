mkdir -p ~/.streamlit/
echo "[theme]
# primaryColor = '#E694FF'
# backgroundColor = ‘#00172b’
# secondaryBackgroundColor = ‘#0083bb’
# textColor= ‘#ffffff’
# font = ‘sans serif’
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
