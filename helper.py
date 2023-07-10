from urlextract import URLExtract
extract = URLExtract()
from wordcloud import WordCloud


def fetch_stats(selected_user, df):
    """
    Fetches stats for the selected user or overall chat.

    Args:
        selected_user (str): The user to fetch stats for. If None, stats for overall chat will be fetched.
        df (pd.DataFrame): The preprocessed dataset.

    Returns:
        tuple: A tuple of (number of messages, number of words, number of media messages, number of links).
    """

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # fetching number of messages
    num_messages = df.shape[0]

    # fetching words
    words = []
    for messages in df["messages"]:
        words.extend(messages.split())

    # fetching number of media messages
    num_media_messages = df[df["messages"] == "<Media omitted>\n"].shape[0]

    # fetching links
    links = []
    for messages in df["messages"]:
        links.extend(extract.find_urls(messages))

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_user(df):
    """
    Fetches the most busy user in the chat.

    Args:
        df (pd.DataFrame): The preprocessed dataset.

    Returns:
        tuple: A tuple of (most busy user, percentage of messages sent by the user).
    """

    x = df["user"].value_counts().head()
    df = round((df["user"].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={"index": "name", "user": "percent"})
    return x, df


def create_worldcloud(selected_user, df):
    """
    Create a wordcloud for the selected user or overall chat.

    Args:
        selected_user (str): The user to create the wordcloud for. If None, a wordcloud for overall chat will be created.
        df (pd.DataFrame): The preprocessed dataset.

    Returns:
        WordCloud: A wordcloud object.
    """

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    wc = WordCloud(width=300, height=250, min_font_size=10, background_color="white")
    temp = df["messages"].replace("<Media omitted>\n", "")
    df_wc = wc.generate(temp.str.cat(sep=" "))
    return df_wc
