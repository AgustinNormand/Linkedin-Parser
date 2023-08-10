from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import constants


class LinkedinParser:
    def __init__(self, src_recommendations_page):
        self. soup = BeautifulSoup(src_recommendations_page, "html.parser")
        self.recommendations_dictionary = {}
        self.recommendation_identifier = 0

    def export_results(self):
        data = pd.DataFrame.from_dict(self.recommendations_dictionary, orient='index')
        data.insert(0, "recommendation_id", list(self.recommendations_dictionary.keys()))
        data.to_csv("recommendations.csv", index=False)

    def process_profile_image(self, recommendation):
        profile_image = recommendation.find("img")
        if profile_image != None:
            profile_image_link = profile_image["src"]
            profile_filename = "{}profile_{}.jpg".format(constants.PROFILE_IMAGES_PATH, self.recommendation_identifier)
            urllib.request.urlretrieve(profile_image_link,
                                       profile_filename)
            return profile_filename
        else:
            return 'None'

    def process_name(self, recommendation):
        return recommendation.find("span", {"class": "hoverable-link-text"}).find("span").get_text()

    def process_role(self, recommendation):
        role_span = recommendation.find_all("span", {"class": "t-14"})[0]
        return role_span.get_text().replace("\n", "")

    def process_date(self, recommendation):
        date_span = recommendation.find_all("span", {"class": "t-14"})[1]
        return date_span.get_text().replace("\n", "")

    def process_description(self, recommendation):
        return recommendation.find("div", {"class":"t-14"}).get_text().replace("\n", "")

    def process_recommendations(self):

        list_of_recommendations = self.soup.find("div", {"class": "artdeco-tabpanel"}).find_all("li", {
            "class": "pvs-list__paged-list-item"})

        for recommendation in list_of_recommendations:
            self.recommendations_dictionary[self.recommendation_identifier] = {}

            self.recommendations_dictionary[self.recommendation_identifier]["profile_filename"] = \
                self.process_profile_image(recommendation)

            self.recommendations_dictionary[self.recommendation_identifier]["name"] = \
                self.process_name(recommendation)

            self.recommendations_dictionary[self.recommendation_identifier]["role"] = \
                self.process_role(recommendation)

            self.recommendations_dictionary[self.recommendation_identifier]["date"] = \
                self.process_date(recommendation)

            self.recommendations_dictionary[self.recommendation_identifier]["description"] = \
                self.process_description(recommendation)

            print(self.recommendations_dictionary[self.recommendation_identifier])

            self.recommendation_identifier += 1

        self.export_results()


