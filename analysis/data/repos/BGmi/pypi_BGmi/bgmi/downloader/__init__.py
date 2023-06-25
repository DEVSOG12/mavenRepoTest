from .aria2_rpc import Aria2DownloadRPC
from .deluge import DelugeRPC
from .noop import Noop
from .qbittorrent import QBittorrentWebAPI
from .transmission import TransmissionRPC

__all__ = ["Aria2DownloadRPC", "DelugeRPC", "QBittorrentWebAPI", "TransmissionRPC", "Noop"]
