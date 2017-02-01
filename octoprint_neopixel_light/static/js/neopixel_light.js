/*
 * View model for Neopixel Light
 *
 * Author: Mike Frey
 * License: MIT
 */
$(function() {
    function Neopixel_lightViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        Neopixel_lightViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_neopixel_light, #tab_plugin_neopixel_light, ...
        [ /* ... */ ]
    ]);
});
