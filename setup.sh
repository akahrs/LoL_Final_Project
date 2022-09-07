mkdir -p ~/.streamlit/

# echo "\
# [general]\n\
# email = \"${theshahidaziz@gmail.com}\"\n\
# " > ~/.streamlit/credentials.toml



echo "\
[theme]\n\
primaryColor='#E694FF'\n\
backgroundColor='#00172B'\n\
secondaryBackgroundColor="#0083BB"
textColor='#FFFFFF'\n\
font='sans serif'\n\
[deprecation]\n\
showPyplotGlobalUse = false\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
