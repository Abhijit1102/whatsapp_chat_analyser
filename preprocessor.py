import re
import pandas as pd


def preprocessor(data):
    """
    Preprocesses the WhatsApp chat data.

    Args:
        data (str): The WhatsApp chat data.

    Returns:
        pd.DataFrame: The preprocessed dataset.
    """

    pattern = '\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s[AP]M\s-\s'

    messages = re.split(pattern, data)
    patterns = '\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s[AP]M'
    dates = re.findall(patterns, data)

    df = pd.DataFrame({"user_message": messages[1:], "message_date": dates})

    df["message_date"] = pd.to_datetime(df["message_date"])
    df.rename(columns={"message_date": "date"}, inplace=True)

    users = []
    msgs = []
    for msg in df["user_message"]:
        # Split the message by the first colon and space that occur
        parts = re.split(': ', msg, maxsplit=1)
        if len(parts) == 2:
            user = parts[0]
            message = parts[1]
        else:
            user = "group_notification"
            message = parts[0]
        users.append(user)
        msgs.append(message)

    df["user"] = users
    df["messages"] = msgs

    df.drop(columns=["user_message"], inplace=True)
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month_name()
    df["day"] = df["date"].dt.day
    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute

    return df

