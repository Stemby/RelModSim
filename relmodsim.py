#!/usr/bin/env python3

"""RelModSim, a relay module simulator written in Python.

RelModSim doesn't simulate electronics, but rather logic.
"""

class RelayModule(object):
    """Python class that simulates a relay module."""

    def __init__(self, channels, inverted_logic=True, poles=1, throw=2):
        """RelayModule needs some keyword arguments:
        channels:       the number of channels (1, 2, 4, 8, 16)
        inverted_logic: inverted (True, the default) or direct (False); with
                        inverted logic HIGH signal means relay OFF, and LOW
                        signal means relay ON (energized coil); with direct
                        logic we have the opposite behavior.
        """
        self.channels = channels
        self.inverted_logic = inverted_logic

        self.inputs = []
        for channel in range(self.channels):
            self.inputs.append(self.inverted_logic) # At startup, all coils OFF

    def get_inputs(self):
        """Return the status of the inputs."""
        return self.inputs

    def set_input(self, channel, status):
        """Set the status of a channel; 0 is the first channel."""
        self.inputs[channel] = status

    def get_leds_status(self):
        """Return the status of the LEDs.
        LEDs are ON when coils are energized, and OFF when coils are OFF.
        """
        return [(pin_status != self.inverted_logic)
                for pin_status in self.inputs]
