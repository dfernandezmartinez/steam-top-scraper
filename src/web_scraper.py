import requests
import locale
from bs4 import BeautifulSoup
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession


def get_steam_data(top):
    url = "https://store.steampowered.com/stats/Steam-Game-and-Player-Statistics"
    response = requests.get(url)
    soup = BeautifulSoup(response.content.decode("utf-8"), "html.parser")
    stat_rows = soup.select_one("#detailStats").select_one("table").select("tr")
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    result = {}

    for row in stat_rows[2:top+2]:
        row_data = row.select("td")

        anchor_tag = row_data[3].select_one("a")
        game_code = anchor_tag["href"].split("/")[4]
        game_name = anchor_tag.text
        current_players = locale.atoi(row_data[0].select_one("span").text)
        today_peak = locale.atoi(row_data[1].select_one("span").text)

        result[game_code] = [game_name, current_players, today_peak]

    return result


def add_game_details(games_data):
    with FuturesSession() as session:
        base_hover_url = "https://store.steampowered.com/apphoverpublic/{}"
        futures = [session.get(base_hover_url.format(game_id)) for game_id in games_data]

        for future in as_completed(futures):
            response = future.result()
            game_id = response.request.url.split('/')[-1]
            soup = BeautifulSoup(response.content, "html.parser")
            try:
                release_date = soup.select_one(".hover_release").select_one("span").text
                release_date = release_date.split(":")[1].replace(",", "").strip()
                total_reviews = soup.select_one(".hover_review_summary").text
                total_reviews = locale.atoi(total_reviews.split("(")[1].split(" ")[0])
                review_summary = soup.select_one(".game_review_summary").text
                tags = ":".join([tag.text for tag in soup.select(".app_tag")])

                game_data = games_data.get(game_id)
                game_data += [release_date, review_summary, total_reviews, tags]

            # Should only fail to obtain data for Spacewar (id 480, a hidden game used by developers
            # for testing purposes) and games without a steam store page
            except AttributeError:
                print("Additional data could not be found for the game with steam id {}".format(game_id))
                continue
