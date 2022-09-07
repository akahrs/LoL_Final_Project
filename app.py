# from optparse import Option
# from ssl import Options
import matplotlib.pyplot as plt
from turtle import width
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from PIL import Image
from LoL_Final_Project.data.retrieve_data import get_local_data
from LoL_Final_Project.data.prepare_data import filter_major_leagues, aggregate_team_data, create_agg_dataframe
from LoL_Final_Project.logic.preprocess import preprocess
from LoL_Final_Project.logic.model import fit_model, visualize_model
from LoL_Final_Project.logic.predict import predict_teams, visualize_predictions
from LoL_Final_Project.main.main import get_data, preprocess_run, visualize, visualize2

df = get_data()
result = preprocess_run(df)
X = result[0]
model = result[1]

st.set_page_config(page_title='Our Data Science Project', page_icon='🍁', layout='wide')



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#load assist
lottie_coding = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_j0i4xsk9.json')
cluster_chart = Image.open('images/features_means.png')
means_of_last_10 = Image.open('images/mean_of_last_10.png')
gen_g = Image.open('images/Geng.png')

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

# background photo

CSS = """
h1 {
    color: red;
}
.stApp {
    #background-image: url(https://cdn.vox-cdn.com/uploads/chorus_asset/file/22991847/Sisters4.JPG);
    background-image: url(https://cdna.artstation.com/p/assets/images/images/015/608/430/large/artur-sadlos-leg-duo-sh030-background-as-v002.jpg);
    background-size: cover;
}
"""

#if st.checkbox('click me', True):
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


#  Header section
with st.container():
    st.subheader('**Hi Everyone! We are Data Science #955 legends**')
    st.title('**Project League of Legends**')
    st.write('**Our trained model will help you plan your strategy to win against the oponent based on their last matches tactics and gameplans**')


#   What do I do

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2,  gap= 'large')
    with left_column:
        st.header("Let's have a look together")
        st.write('##')
        st.write(
        '''
        - **We have collected data of all the matches that's been played in 2022**
        - **We have then created a model which group each team in different cluster based on their game style and match planning**
        - **The idea of our model is to help individuals find out their opponents or favorite teams game tactics**
        - **This can also help E-sports team coaches to prepare their teams accordingly by looking at their opponents weakness and strong points**
        - **lets find more in details**

        '''
    )

    with right_column:
        st.image('https://giffiles.alphacoders.com/527/52742.gif', width = 500)


with st.container():
    st.write('---')
    chart_column, exp_column = st.columns((2, 2))
    with chart_column:
        #st.image(cluster_chart, width= 600,  caption='Chart representing all teams in 7 clusters')
        fig = visualize(model, X, df)
        st.pyplot(fig)

    with exp_column:
        st.subheader('**Chart representing all matches in 8 clusters**')
        st.write(
                         '''
                        - **Here you can see 7 different colors which represent each clusters**
                        - **All LoL matches played during 2022 been clustered by our model based on their method of playing**
                        - **Some teams try tend to go monsterkills more, some go for barons and canons and some go for structures**
                        - **Keep in mind, we have also looked at sides because each side has different advantages**

                        '''
        )


with st.container():
    # st.write('---')
    # chart_column, exp_column = st.columns((2, 2))
    # with chart_column:
    #    st.image(means_of_last_10, width= 600,  caption='Last 10 matches of all teams')

    with exp_column:
        st.subheader('key words in chart')
        st.write('''

                 - **vspm = Vision score per minute**
                 - **dpm = Damage per minute**
                 - **team kpm = Team kill per minute**
                 - **earned gpm = Earned gold per minute**
                 - **gamelength = Duration of the game**
                 - **structure_pm = Specific structure taken down per minute**
                 - **teamdeaths_pm = Team player killed per minute**
                 ''' )



teams1 = ['','Oh My God','ThunderTalk Gaming','FunPlus Phoenix','Royal Never Give Up',
         'JD Gaming', 'EDward Gaming', 'LGD Gaming','Anyones Legend','DRX', 'Liiv SANDBOX',
         'Rare Atom ','Top Esports', 'T1', 'Kwangdong Freecs', 'Ultra Prime', 'LNG Esports',
        'Nongshim RedForce','Hanwha Life Esports','Invictus Gaming','KT Rolster','DWG KIA',
        'Team WE','Weibo Gaming','Gen.G','Fredit BRION','MAD Lions','Team Vitality','Rogue',
        'SK Gaming','Excel Esports','G2 Esports','Astralis','Misfits Gaming','Fnatic','Team BDS',
        'TSM', '100 Thieves', 'Cloud9','Golden Guardians','FlyQuest','Dignitas','Team Liquid',
        'Counter Logic Gaming','Immortals','Evil Geniuses','Victory Five','Bilibili Gaming',
        'Deep Cross Gaming', 'J Team','Frank Esports','Impunity','Meta Falcon Team','Hurricane Gaming',
        'PSG Talon','Beyond Gaming', 'CTBC Flying Oyster','SEM9', 'Dewish Team']



teams2 =['', 'Oh My God','ThunderTalk Gaming','FunPlus Phoenix','Royal Never Give Up',
         'JD Gaming', 'EDward Gaming', 'LGD Gaming','Anyones Legend','DRX', 'Liiv SANDBOX',
         'Rare Atom ','Top Esports', 'T1', 'Kwangdong Freecs', 'Ultra Prime', 'LNG Esports',
        'Nongshim RedForce','Hanwha Life Esports','Invictus Gaming','KT Rolster','DWG KIA',
        'Team WE','Weibo Gaming','Gen.G','Fredit BRION','MAD Lions','Team Vitality','Rogue',
        'SK Gaming','Excel Esports','G2 Esports','Astralis','Misfits Gaming','Fnatic','Team BDS',
        'TSM', '100 Thieves', 'Cloud9','Golden Guardians','FlyQuest','Dignitas','Team Liquid',
        'Counter Logic Gaming','Immortals','Evil Geniuses','Victory Five','Bilibili Gaming',
        'Deep Cross Gaming', 'J Team','Frank Esports','Impunity','Meta Falcon Team','Hurricane Gaming',
        'PSG Talon','Beyond Gaming', 'CTBC Flying Oyster','SEM9', 'Dewish Team']

st.title('Choose any of the following teams')



team_1 = st.selectbox(label = 'Choose your team', options= teams1)
team_2 = st.selectbox(label = 'Choose the opponent', options = teams2)

with st.container():
    st.write('---')
    graph_column, new_column = st.columns((2, 2))

    with graph_column:
        if team_1 != '' and team_2 != '':
            fig2 = visualize2(model, X, df, team1 = team_1, team2 = team_2)
            st.pyplot(fig2)

    with new_column:
        if team_1 != '' and team_2 != '':
            st.subheader('Chart representing both teams')
            st.write('''

                    - **High first blood**: Aggressive in the beginning; average across all other metrics
                    - **High Game length**: Playing it slow and steady, Usually strong and above average in most of the mertics

                    - **High vision score per minute(vspm)**:
                    - **High damage per minute(dpm)**:
                    - **More gold earned per minute(gpm)**:
                    - **Low team death per minute**:
                    - **More monsters killed per minute**:
                    - **More structure taken per minute**:
                    - **Big monster taken per minute**:
                    - **Team kills per minute(team kpm)**:
                    - **High result rate**:
                 ''' )
