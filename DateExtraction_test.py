from DateExtraction import extractArticlePublishedDate
import unittest


class TestDateExtraction(unittest.TestCase):
    def test_extractions(self):
        """
        Test that it can sum a list of integers
        """
        data = {
            "10/08/2020": "https://kyc360.riskscreen.com/news/former-privatbank-owners-used-vast-array-of-companies-to-steal-launder-billions-doj/",
            "13/06/2021": "https://kyc360.riskscreen.com/news/doha-bank-loses-attempt-to-drop-evidence-of-alleged-witness-intimidation-from-uk-high-court-case/",
            "15/04/2010": "https://timesofmalta.com/articles/view/ubs-chief-apologises-for-banks-role-in-tax-evasion.302762",
            "10/06/2021": "https://kyc360.riskscreen.com/news/toronto-dominion-found-not-liable-in-allen-stanford-fraud-trial/",
            "31/01/2019": "http://www.businesstelegraph.co.uk/metro-bank-boss-fights-for-his-future-after-we-revealed-truth-about-accounting-error/",
            "08/04/2021": "https://www.marketscreener.com/quote/stock/JULS-BAER-76954418/news/JULS-BAER-Swiss-banker-to-Venezuelan-kleptocrats-becomes-star-witness-32917574/",
            "28/01/2021": "https://gatehouselaw.co.uk/jsc-vtb-bank-v-skurikhin-ors-2020-ewca-civ-1337/",
            "30/09/2019": "https://kyc360.riskscreen.com/news/banco-do-brasil-managers-targeted-in-48-million-money-laundering-probe/",
            "05/03/2015": "https://www.reuters.com/article/commerzbank-investigation-usa-idUSL1N0W729420150305",
            "25/08/2017": "https://www.rt.com/business/400883-societe-generale-managers-indiction/",
            "14/08/2018": "https://kyc360.riskscreen.com/news/hsbc-expects-to-pay-1-5-billion-in-fines-over-tax-evasion-money-laundering/",
            # "23/07/2014": "https://nycourts.gov/reporter//3dseries/2014/2014_02381.htm",
            "24/04/2019": "https://www.lalibre.be/economie/entreprises-startup/2019/04/24/la-banque-degroof-petercam-est-visee-par-une-enquete-de-la-bnb-pour-blanchiment-dargent-RU4K24ZZ5NGWBCCPQMCMJXZABM/",
            "19/02/2016": "https://news.yahoo.com/russias-vimpelcom-pay-835-mn-over-corruption-charges-214513855.html",
            "04/06/2010": "https://www.economywatch.com/uk-fines-jp-morgan-nearly-50-million-for-not-ringfencing-client-money",
        }
        for k, v in data.items():
            result = extractArticlePublishedDate(v)
            self.assertEqual(result.date().strftime("%d/%m/%Y"), k)


if __name__ == "__main__":
    unittest.main()
