import appdaemon.plugins.hass.hassapi as hass
import time

class partyMode(hass.Hass):

    def initialize(self):
        self.log("Listening for party...")
        self.listen_state(self.motion, "input_boolean.party_mode")

    def motion(self, entity, attribute, old, new, kwargs):
        self.log("Party engaged!")
        while self.get_state("input_boolean.party_mode") == "on":
            self.turn_on("switch.terrariumlight")
            time.sleep(2)
            self.turn_off("switch.terrariumlight")
            time.sleep(2)

            ###
            ### TODO : Replicate party mode automation in python loop
            ###