import re


def get_review_item(soup):
    items = soup.find_all('li', class_="ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent")
    return items


def get_title(item):
    title = item.find_next('h3')
    title_text = str(title.text)
    return title_text[title_text.find(".") + 2:]


def get_info(item):
    info = item.find_all(class_="sc-c7e5f54-8 hgjcbi cli-title-metadata-item")

    return info[0].text, info[1].text, info[2].text if len(info) == 3 else None


def get_review(item):
    review = (item.
              find_next("span",
                        class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"))

    review_value = ""
    reviewer = ""

    s = str(review.text)

    status = re.search(r'\d+\.\d', s)

    if status:
        review_value = status.group(0)

    status = re.search(r'\(.*?\)', s)

    if status:
        reviewer = status.group(0)[1:-1]

    return review_value, reviewer


def get_img(item):
    img = item.find_next("img")
    return img.get("src")


def get_detail_url(item):
    url = item.find_next("a", class_="ipc-lockup-overlay ipc-focusable")
    return url.get("href")


def get_original_name(item):
    result=None
    try:
        name = item.find("div", class_="sc-afe43def-3 EpHJp")
        name_text = str(name.text)
        result=name_text[name_text.find(":") + 2:]
    finally:
        return result


def get_category(item):
    category = []
    category_div = item.find("div", class_="ipc-chip-list__scroller")
    c = category_div.find_all("span", class_="ipc-chip__text")
    for i in c:
        category.append(i.text)
    return category
