from .const import COLLECTION_TYPE_MOVIES as COLLECTION_TYPE_MOVIES, COLLECTION_TYPE_MUSIC as COLLECTION_TYPE_MUSIC, CONF_AUDIO_CODEC as CONF_AUDIO_CODEC, DOMAIN as DOMAIN, ITEM_KEY_COLLECTION_TYPE as ITEM_KEY_COLLECTION_TYPE, ITEM_KEY_ID as ITEM_KEY_ID, ITEM_KEY_IMAGE_TAGS as ITEM_KEY_IMAGE_TAGS, ITEM_KEY_INDEX_NUMBER as ITEM_KEY_INDEX_NUMBER, ITEM_KEY_MEDIA_SOURCES as ITEM_KEY_MEDIA_SOURCES, ITEM_KEY_MEDIA_TYPE as ITEM_KEY_MEDIA_TYPE, ITEM_KEY_NAME as ITEM_KEY_NAME, ITEM_TYPE_ALBUM as ITEM_TYPE_ALBUM, ITEM_TYPE_ARTIST as ITEM_TYPE_ARTIST, ITEM_TYPE_AUDIO as ITEM_TYPE_AUDIO, ITEM_TYPE_EPISODE as ITEM_TYPE_EPISODE, ITEM_TYPE_LIBRARY as ITEM_TYPE_LIBRARY, ITEM_TYPE_MOVIE as ITEM_TYPE_MOVIE, ITEM_TYPE_SEASON as ITEM_TYPE_SEASON, ITEM_TYPE_SERIES as ITEM_TYPE_SERIES, MAX_IMAGE_WIDTH as MAX_IMAGE_WIDTH, MEDIA_SOURCE_KEY_PATH as MEDIA_SOURCE_KEY_PATH, MEDIA_TYPE_AUDIO as MEDIA_TYPE_AUDIO, MEDIA_TYPE_NONE as MEDIA_TYPE_NONE, MEDIA_TYPE_VIDEO as MEDIA_TYPE_VIDEO, PLAYABLE_ITEM_TYPES as PLAYABLE_ITEM_TYPES, SUPPORTED_COLLECTION_TYPES as SUPPORTED_COLLECTION_TYPES
from .coordinator import JellyfinConfigEntry as JellyfinConfigEntry
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from homeassistant.core import HomeAssistant as HomeAssistant
from jellyfin_apiclient_python.client import JellyfinClient as JellyfinClient
from typing import Any

_LOGGER: Incomplete

async def async_get_media_source(hass: HomeAssistant) -> MediaSource: ...

class JellyfinSource(MediaSource):
    name: str
    hass: Incomplete
    entry: Incomplete
    client: Incomplete
    api: Incomplete
    url: Incomplete
    def __init__(self, hass: HomeAssistant, client: JellyfinClient, entry: JellyfinConfigEntry) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    async def _build_libraries(self) -> BrowseMediaSource: ...
    async def _get_libraries(self) -> list[dict[str, Any]]: ...
    async def _build_library(self, library: dict[str, Any], include_children: bool) -> BrowseMediaSource: ...
    async def _build_music_library(self, library: dict[str, Any], include_children: bool) -> BrowseMediaSource: ...
    async def _build_artists(self, library_id: str) -> list[BrowseMediaSource]: ...
    async def _build_artist(self, artist: dict[str, Any], include_children: bool) -> BrowseMediaSource: ...
    async def _build_albums(self, parent_id: str) -> list[BrowseMediaSource]: ...
    async def _build_album(self, album: dict[str, Any], include_children: bool) -> BrowseMediaSource: ...
    async def _build_tracks(self, album_id: str) -> list[BrowseMediaSource]: ...
    def _build_track(self, track: dict[str, Any]) -> BrowseMediaSource: ...
    async def _build_movie_library(self, library: dict[str, Any], include_children: bool) -> BrowseMediaSource: ...
    async def _build_movies(self, library_id: str) -> list[BrowseMediaSource]: ...
    def _build_movie(self, movie: dict[str, Any]) -> BrowseMediaSource: ...
    async def _build_tv_library(self, library: dict[str, Any], include_children: bool) -> BrowseMediaSource: ...
    async def _build_tvshow(self, library_id: str) -> list[BrowseMediaSource]: ...
    async def _build_series(self, series: dict[str, Any], include_children: bool) -> BrowseMediaSource: ...
    async def _build_seasons(self, series_id: str) -> list[BrowseMediaSource]: ...
    async def _build_season(self, season: dict[str, Any], include_children: bool) -> BrowseMediaSource: ...
    async def _build_episodes(self, season_id: str) -> list[BrowseMediaSource]: ...
    def _build_episode(self, episode: dict[str, Any]) -> BrowseMediaSource: ...
    async def _get_children(self, parent_id: str, item_type: str) -> list[dict[str, Any]]: ...
    def _get_thumbnail_url(self, media_item: dict[str, Any]) -> str | None: ...
    def _get_stream_url(self, media_item: dict[str, Any]) -> str: ...

def _media_mime_type(media_item: dict[str, Any]) -> str | None: ...
