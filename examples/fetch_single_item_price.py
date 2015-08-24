from csgoprices.scraper import Scraper
from csgoprices import entities

def main():
    scraper = Scraper()
    asiimov = entities.Skin('AWP', 'Asiimov', entities.Wears.FieldTested)
    print scraper.build_request(asiimov)


if __name__ == '__main__':
    main()
