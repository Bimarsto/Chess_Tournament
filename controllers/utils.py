import warnings
import dateparser


warnings.filterwarnings(
        "ignore",
        message="The localize method is no longer necessary, as this time zone supports the fold attribute",
    )


class Utils:

    @staticmethod
    def parse_date(date):
        try:
            return dateparser.parse(f'le {date}', languages=['fr']).strftime('%d/%m/%Y')

        except:
            print('Format de date non reconnu.')
            return None

