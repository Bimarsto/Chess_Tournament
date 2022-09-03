import dateparser


class Utils:

    @staticmethod
    def parse_date(date):
        try:
            return dateparser.parse(date).strftime('%d/%m/%Y')
        except:
            print('Format de date non reconnu.')
            return None
