# from optparse import Option
# from ssl import Options
#import matplotlib.pyplot as plt
#from turtle import width
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
from LoL_Final_Project.main.main import get_data, preprocess_run, visualize, visualize2, get_team_values



df = get_data()
result = preprocess_run(df)
X = result[0]
model = result[1]

st.set_page_config(page_title='Our Data Science Project', page_icon='🍁', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)


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
    st.subheader('**Hi Everyone! We are Data Science batch #955 legends**')
    st.title('**Project: League of Legends Intelligence**')
    st.write("**Our trained model will help you as a coach to plan your strategy for winning against your oponent's team by analyzing your team's and the opponent team's most recent playstyle (based on the last 10 games played)**")


#   What do I do

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2,  gap= 'large')
    with left_column:
        st.header("Let's have a look together")
        st.write('##')
        st.write(
        '''
        - **The data used to identify the 8 clusters is based on matches played in the major leagues (LEC, LCS, LCK, LPL, PCS) in 2022**
        - **The trained model groups each team into one of those 8 clusters based on their playstyle in the 10 most recent games played**
        - **The purpose of the model is to help coaches find out their team's and their opponent team's playstyle**
        - **Overall, it aims to help LoL E-sports teams to better prepare their teams accordingly for upcoming matches by looking at their opponents' weaknesses and strong points**

        '''
    )

    with right_column:
        #st.image('https://giffiles.alphacoders.com/527/52742.gif', width = 500)
        st.image('https://giffiles.alphacoders.com/527/52704.gif', width = 500)


with st.container():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.write('---')
    chart_column, exp_column = st.columns((2, 2))
    with chart_column:
        #st.image(cluster_chart, width= 600,  caption='Chart representing all teams in 7 clusters')
        fig = visualize(model, X, df)
        st.pyplot(fig)

    with exp_column:
        st.subheader('**Chart representing 8 playstyle cluster**')
        st.write(
                         '''
                        - **The 8 colors represent the different clusters**
                        - **All teams of major LoL leagues have been clustered by our model based on their last 10 games played (August 2022)**
                        - **You can select two teams to see their most recent playstyle cluster and to compare their performances based on the metrics below**

                        **In the following, each cluster is explained in some more detail:**

                        **Cluster 0**:
                        - Average across all other metrics
                        - Aggressive in the beginning with highest first blood ratio across all clusters

                        **Cluster 1**:
                        - Slightly below average in all metrics
                        - Tend to play especially longer games

                        **Cluster 2**:
                        - Strong across all metrics
                        - Especially high CS numbers and low teamdeaths)
                        - Tend to play longer games on average

                        **Cluster 3**:
                        - Below average across metrics
                        - Frequent teamdeaths with decent CS numbers

                        **Cluster 4**:
                        - Above average across metrics;
                        - Very aggressive playstyle with frequent skirmishes (high kills per min but also frequent deaths)
                        - Quite low vision score

                        **Cluster 5**:
                        - Weakest across all metrics
                        - Highest deaths across all clusters

                        **Cluster 6**:
                        - Strong/above average in most metrics
                        - Longest game duration on average
                        - Slightly weaker CS with high vision score, however

                        **Cluster 7**:
                        - Strongest across all metrics with highest win rate
                        - High control of the game with quick game closure (i.e. short games)

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
                 **result = Winrate of last games**; **vspm = Vision score per minute**; **dpm = Damage per minute**; **team kpm = Team kills per minute**; **earned gpm = Earned gold per minute**; **gamelength = Duration of the game (in seconds)**; **structures_pm = Structures (towers, inhibitors) taken down per minute**; **teamdeaths_pm = Team deaths per minute**
                 ''' )



teams1 = ['','Oh My God','ThunderTalk Gaming','FunPlus Phoenix','Royal Never Give Up',
         'JD Gaming', 'EDward Gaming', 'LGD Gaming',"Anyone's Legend",'DRX', 'Liiv SANDBOX',
         'Rare Atom ','Top Esports', 'T1', 'Kwangdong Freecs', 'Ultra Prime', 'LNG Esports',
        'Nongshim RedForce','Hanwha Life Esports','Invictus Gaming','KT Rolster','DWG KIA',
        'Team WE','Weibo Gaming','Gen.G','Fredit BRION','MAD Lions','Team Vitality','Rogue',
        'SK Gaming','Excel Esports','G2 Esports','Astralis','Misfits Gaming','Fnatic','Team BDS',
        'TSM', '100 Thieves', 'Cloud9','Golden Guardians','FlyQuest','Dignitas','Team Liquid',
        'Counter Logic Gaming','Immortals','Evil Geniuses','Victory Five','Bilibili Gaming',
        'Deep Cross Gaming', 'J Team','Frank Esports','Impunity','Meta Falcon Team','Hurricane Gaming',
        'PSG Talon','Beyond Gaming', 'CTBC Flying Oyster','SEM9', 'Dewish Team']



teams2 =['', 'Oh My God','ThunderTalk Gaming','FunPlus Phoenix','Royal Never Give Up',
         'JD Gaming', 'EDward Gaming', 'LGD Gaming',"Anyone's Legend",'DRX', 'Liiv SANDBOX',
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
team_2 = st.selectbox(label = "Choose opponent's team", options = teams2)

with st.container():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.write('---')
    graph_column, new_column = st.columns((2, 2))

    with graph_column:
        if team_1 != '' and team_2 != '':
            fig2 = visualize2(model, X, df, team1 = team_1, team2 = team_2)
            st.pyplot(fig2)


    with new_column:
        if team_1 != '' and team_2 != '':
            st.subheader('Table with values and differences for both teams')
            #st.write('''

                    #- **High first blood**: Aggressive in the beginning; average across all other metrics
                    #- **High Game length**: Playing it slow and steady, Usually strong and above average in most of the mertics

                    #- **High vision score per minute(vspm)**:
                    #- **High damage per minute(dpm)**:
                    #- **More gold earned per minute(gpm)**:
                    #- **Low team death per minute**:
                    #- **More monsters killed per minute**:
                    #- **More structure taken per minute**:
                    #- **Big monster taken per minute**:
                    #- **Team kills per minute(team kpm)**:
                    #- **High result rate**:
                 #''' )

            table = get_team_values(df, team1 = team_1, team2 = team_2)
            st.table(table)
