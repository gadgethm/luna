import os
import stat

from xbmcswift2 import xbmcaddon

internal_path = xbmcaddon.Addon().getAddonInfo('path')

STRINGS = {
    'name':                30000,
    'addon_settings':      30100,
    'full_refresh':        30101,
    'choose_ctrl_type':    30200,
    'enter_filename':      30201,
    'starting_mapping':    30202,
    'mapping_success':     30203,
    'set_mapping_active':  30204,
    'mapping_failure':     30205,
    'pair_failure_paired': 30206,
    'configure_first':     30207,
    'reset_cache_warning': 30208
}


class Core:

    def __init__(self, plugin):
        self.plugin = plugin
        self.logger = Logger(self.plugin)

    def string(self, string_id):
        if string_id in STRINGS:
            return self.plugin.get_string(STRINGS[string_id]).encode('utf-8')
        else:
            return string_id

    def check_script_permissions(self):
        st = os.stat(internal_path + '/resources/lib/launch.sh')
        if not bool(st.st_mode & stat.S_IXUSR):
            os.chmod(internal_path + '/resources/lib/launch.sh', st.st_mode | 0111)
            self.logger.info('Changed file permissions for launch')

        st = os.stat(internal_path + '/resources/lib/launch-helper-osmc.sh')
        if not bool(st.st_mode & stat.S_IXUSR):
            os.chmod(internal_path + '/resources/lib/launch-helper-osmc.sh', st.st_mode | 0111)
            self.logger.info('Changed file permissions for launch-helper-osmc')

        st = os.stat(internal_path + '/resources/lib/moonlight-heartbeat.sh')
        if not bool(st.st_mode & stat.S_IXUSR):
            os.chmod(internal_path + '/resources/lib/moonlight-heartbeat.sh', st.st_mode | 0111)
            self.logger.info('Changed file permissions for moonlight-heartbeat')

    def get_storage(self):
        return self.plugin.get_storage('game_storage')


class Logger:
    def __init__(self, plugin):
        self.plugin = plugin

    def info(self, text):
        self.plugin.log.info(text)

    def debug(self, text):
        self.plugin.log.debug(text)

    def error(self, text):
        self.plugin.log.error(text)
