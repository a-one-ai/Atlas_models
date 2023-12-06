from summa.summarizer import summarize

def get_summary(user_input):
    summary = summarize(user_input,ratio=0.3, language="english")
    return summary


