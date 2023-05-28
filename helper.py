from urlextract import URLExtract
extract = URLExtract()
from wordcloud import WordCloud

def fetch_stats(selected_user,df):
    
   if selected_user != "Overall":
        df= df[df["user"]== selected_user]
      # fetching number of messages
   num_messages = df.shape[0]


   words=[]
   for messages in df["messages"]:
      words.extend(messages.split())


   num_media_messages = df[df["messages"] =="<Media omitted>\n"].shape[0] 

   links=[]
   for messages in df["messages"]:
      links.extend(extract.find_urls(messages))
         
   return num_messages, len(words), num_media_messages, len(links)


def most_busy_user(df):
   x= df["user"].value_counts().head()
   df = round((df["user"].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={"index":"name","user":"percent"})
   return x,  df

def create_worldcloud(selected_user, df):

   if selected_user != "Overall":
      df = df[df["user"]== selected_user]

   wc= WordCloud(width=300, height=250, min_font_size=10, background_color="white")
   temp=df["messages"].replace("<Media omitted>\n", "")
   df_wc= wc.generate(temp.str.cat(sep=" "))
   return df_wc