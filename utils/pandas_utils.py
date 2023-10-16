import pandas as pd


class ReviewInfo:
    def __init__(self, title, original_title, value, reviewer, year, certificate, category, duration, image):
        self.title = title
        self.original_title = original_title
        self.value = value
        self.reviewer = reviewer
        self.year = year
        self.certificate = certificate
        self.category = category
        self.duration = duration
        self.image = image


def get_df():
    return pd.DataFrame()


def add_data(d, val):
    new_row = pd.DataFrame([val.__dict__])
    d = pd.concat([d, new_row], ignore_index=True)
    return d


def save_to_csv(d, path="result.csv"):
    d.to_csv(path)
