# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from neopixel import *

# LED strip configuration:
LED_COUNT      = 12      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

class NeopixelLightPlugin(octoprint.plugin.StartupPlugin,
                           octoprint.plugin.AssetPlugin,
                           octoprint.plugin.TemplatePlugin):



	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/neopixel_light.js"],
			css=["css/neopixel_light.css"],
			less=["less/neopixel_light.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			neopixel_light=dict(
				displayName="Neopixel Light",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="mikefrey",
				repo="octoprint-neopixel-light",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/mikefrey/octoprint-neopixel-light/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Neopixel Light"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = NeopixelLightPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

