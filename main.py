from utils import request_utils, soup_utils, pandas_utils
from filter import filter

df = pandas_utils.get_df()

url = "https://www.imdb.com"
route = "/chart/top/"

response = request_utils.make_request(url + route)

if response.status_code == 200:
    soup = soup_utils.make_soup(response.text)
    items = filter.get_review_item(soup)
    for item in items:
        original_name = ""
        category = []

        title = filter.get_title(item)
        year, duration, certificate = filter.get_info(item)
        value, reviewers = filter.get_review(item)
        image = filter.get_img(item)

        detail_url = filter.get_detail_url(item)
        detail_response = request_utils.make_request(url + detail_url)

        if detail_response.status_code == 200:
            r = soup_utils.make_soup(url + detail_response.text)
            original_name = filter.get_original_name(r)
            category = filter.get_category(r)
        else:
            print("請求失敗")

        review_info = pandas_utils.ReviewInfo(title, original_name, value, reviewers, year, certificate, category,
                                              duration, image)
        print(review_info.__dict__)
        df = pandas_utils.add_data(df, review_info)
else:
    print("請求失敗")

pandas_utils.save_to_csv(df)
