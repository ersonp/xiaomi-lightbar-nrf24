"""The Xiaomi Monitor Light Bar integration."""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.LIGHT]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Xiaomi Monitor Light Bar from a config entry."""

    hass.data[DOMAIN] = entry.data
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

# async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
#     """Unload a config entry."""
#     if unload_ok := await hass.config_entries.async_unload_platforms(
#         entry, PLATFORMS
#     ):
#         hass.data[DOMAIN].pop(entry.entry_id)
#
#     return unload_ok