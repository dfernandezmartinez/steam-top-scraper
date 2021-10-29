import argparse
import sys
import web_scraper
import csv


def export_results(filename, file_headers, games_data):
    with open(filename, mode='w', encoding="utf-8", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(file_headers)
        for game_id in games_data:
            csv_writer.writerow([game_id] + games_data.get(game_id))


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--top", help="number of games to fetch from the current top (max. 100), defaults to 100")
    args = parser.parse_args()

    top_games = 100
    if args.top:
        if args.top.isdigit():
            top_games_arg = int(args.top)
            if top_games_arg > 100 or top_games_arg < 1:
                print("'top' argument should be between 1 and 100 ({} found), defaulting to 100 instead"
                      .format(top_games_arg))
            else:
                top_games = top_games_arg
        else:
            print("Unexpected 'top' argument value ({}), use an integer between 1 and 100"
                  .format(args.top))
            sys.exit(-1)

    # Define CSV file data
    csv_headers = ['Steam id', 'Game', 'Current players', 'Peak players today', 'Release date',
                   'Review summary', 'Total reviews', 'Tags']
    output_filename = 'steam_top_{}.csv'.format(top_games)

    # Request and parse the top games and their details, and export them to a CSV file
    print("Requesting Steam top {} games...".format(top_games))
    steam_data = web_scraper.get_steam_data(top_games)

    print("Requesting additional game details...")
    web_scraper.add_game_details(steam_data)

    print("Exporting results...")
    export_results(output_filename, csv_headers, steam_data)

    print("Execution ended. Generated file {}".format(output_filename))


