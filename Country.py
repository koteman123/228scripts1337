from .. import loader, utils
import logging
import asyncio
import requests

logger = logging.getLogger(__name__)

def register(cb):
    cb(countryMod())

class countryMod(loader.Module):
    """Country info module"""
    strings = {'name' : 'countryMod'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._rateLimit = []

    async def client_ready(self, client, db):
        self.client = client   
    async def countrycmd(self, message):
        """Syntax: .country YOUR_COUNTRY"""
        try:
            countryname = utils.get_args(message)

            url = "https://restcountries-v1.p.rapidapi.com/name/" + countryname[0]

            headers = {
                'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
                'x-rapidapi-key': "7dc2b52c64msh3421bf334a46615p1de0cfjsn3113a7446dfd"
                }

            response = requests.request("GET", url, headers=headers)

            new = response.json()

            for i in new:
                name = new[0]['name']
                phonecode = new[0]['callingCodes']
                capital = new[0]['capital']
                altnames = new[0]['altSpellings']
                region = new[0]['region']
                ppl = new[0]['population']
                area = new[0]['area']
                timezone = new[0]['timezones']
                borderswith = new[0]['borders']
                currency = new[0]['currencies']
                altnamestrue = (', '.join(new[0]['altSpellings']))
                timezonetrue = (', '.join(new[0]['timezones']))
                borderstrue = (', '.join(new[0]['borders']))
                await utils.answer(message, f'<code>Contry: {name}\nPhone Code: {phonecode[0]}\nCapital: {capital}\nAlternative Names: {altnamestrue}\nIts located in {region}\nPopulation: {ppl}\nArea: {area}\nTimezone: {timezonetrue}\nShares borders with: {borderstrue}\nUses {currency[0]} as their currency.</code>')
        except KeyError:
            await utils.answer(message, f'Country "<b>{countryname[0]}</b>" does not exist.')
        except:
            await utils.answer(message, 'Something went wrong, contact @KOTEMAN123 for a fix.')