# found this here
# https://gist.github.com/potsky/90ba39e15ea9284348f2
# all its based on this
# to make it work again in ST3 for me
# https://github.com/icio/sublime-text-marked
#

import os
import sys
import subprocess
import sublime
import sublime_plugin


class MarkedCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        print(filename)

        if filename is None:
            return
        proc_env = os.environ.copy()
        encoding = sys.getfilesystemencoding()
        for k, v in proc_env.items():
            proc_env[k] = os.path.expandvars(v).encode(encoding)

        subprocess.call(['open', '-a', 'Marked 2', filename], env=proc_env)

    def is_enabled(self):
        return True
