#!/bin/bash

# Mute the sound
amixer -D pulse sset Master mute

# Wait for 30 seconds
sleep 30

# Unmute the sound
amixer -D pulse sset Master unmute
