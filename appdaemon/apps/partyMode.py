import appdaemon.plugins.hass.hassapi as hass
import time

class partyMode(hass.Hass):

    def initialize(self):
        self.log("Listening for party...")
        self.listen_state(self.motion, "input_boolean.party_mode")

    def motion(self, entity, attribute, old, new, kwargs):
        n=1
        while self.get_state("input_boolean.party_mode") == "on":
            self.log("Partying for  " + str(n) + " seconds...")
            n=n+1
            time.sleep(1)