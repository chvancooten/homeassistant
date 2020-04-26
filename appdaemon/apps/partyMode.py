import appdaemon.plugins.hass.hassapi as hass
import time

class partyMode(hass.Hass):

    def initialize(self):
        self.log("Listening for party...")
        self.listen_state(self.motion, "input_boolean.party_mode", new = "on")

    def motion(self, entity, attribute, old, new, kwargs):
        self.log("Party engaged!")
        self.call_service("media_player/play_media", entity_id="media_player.tonecas", media_content_type="music",
            media_content_id="http://192.168.2.100:8123/local/audio/running.mp3")
        self.call_service("light/turn_off", entity_id="all")
        time.sleep(2)
        self.call_service("media_player/play_media", entity_id="media_player.tonecas", media_content_type="music",
            media_content_id="http://192.168.2.100:8123/local/audio/running.mp3")
        self.call_service("light/turn_on", entity_id="light.nanoleaf", brightness=255, effect="80s Burst Synth")
        time.sleep(1.6)
        self.call_service("light/turn_on", entity_id="light.livingroom", brightness=255, effect="Strobe color")
        self.call_service("light/turn_on", entity_id="light.toilet", brightness=255, effect="Strobe color")
        while self.get_state("input_boolean.party_mode") == "on":
            self.turn_off("light.livingroom_spot4")
            self.turn_on("switch.terrariumlight")
            self.turn_on("light.livingroom_spot1", brightness=255, color_temp=250)
            time.sleep(1)
            self.turn_off("light.livingroom_spot1")
            self.turn_on("light.livingroom_spot2", brightness=255, color_temp=250)
            time.sleep(1)
            self.turn_off("light.livingroom_spot2")
            self.turn_off("switch.terrariumlight")
            self.turn_on("light.livingroom_spot3", brightness=255, color_temp=250)
            time.sleep(1)
            self.turn_off("light.livingroom_spot3")
            self.turn_on("light.livingroom_spot4", brightness=255, color_temp=250)
            time.sleep(1)
        
        self.call_service("media_player/media_stop", entity_id="media_player.tonecas")
        self.call_service("light/turn_off", entity_id="all")
        time.sleep(0.1)
        self.call_service("script/turn_on", entity_id="script.reset_scene")