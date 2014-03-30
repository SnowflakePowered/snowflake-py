import subprocess

NINTENDO_SNES = "NINTENDO_SNES"


class PlatformInfo:
    def __init__(self, platform_id, full_name, short_name, company, release_date, emulator,
                 commandline, scrapers, file_extensions, images={}, metadata=[]):
        self.platform_id = platform_id
        self.full_name = full_name
        self.short_name = short_name
        self.company = company
        self.emulator = emulator
        self.commandline = commandline
        self.scrapers = scrapers
        self.file_extensions = file_extensions
        self.metadata = metadata
        self.release_date = release_date
        self.images = images


class EmulatorInfo:
    def __init__(self, name, executable, config):
        self.name = name
        self.executable = executable
        self.config = config

    def execute_rom(self, commandline):
        subprocess.call(self.executable, commandline)