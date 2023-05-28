import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat anlyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    
    data=bytes_data.decode("utf-8")
    
    df = preprocessor.preprocessor(data)

    st.dataframe(df, width=800, height=600)

    # fetching unique user

    user_list = df["user"].unique().tolist()
    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0,"Overall")


    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)
    
    if st.sidebar.button("show analysis"):


        num_messages, words,  num_media_messages, num_links = helper.fetch_stats(selected_user,df)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header("Total messages")
            st.title(num_messages)

        with col2:
            st.header("Total words")
            st.title(words) 

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages) 
        
        with col4:
            st.header("No of links Shared")
            st.title(num_links) 

        # finding the busiest user in Group
        if selected_user == "Overall":
            st.title("Most busy user")
            x, new_df = helper.most_busy_user(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)
        
        #wordcloud
        st.title("Wordcloud")
        df_wc = helper.create_worldcloud(selected_user, df)
        fig, ax = plt.subplots()
        plt.imshow(df_wc)
        st.pyplot(fig)



