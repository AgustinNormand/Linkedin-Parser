from LinkedinScraper import LinkedinScraper
import constants

if __name__ == "__main__":
    ls = LinkedinScraper(constants.PROFILE_IMAGES_PATH)
    ls.scrape_recommendations(constants.RECOMMENDATIONS_URL)