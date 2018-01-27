import os
import signal
import gi
import webbrowser
gi.require_version('Gtk', '3.0');
gi.require_version('AppIndicator3', '0.1');
from gi.repository import Gtk, AppIndicator3

currpath = os.path.dirname(os.path.realpath(__file__));

class Indicator():
    def __init__(self):
        self.app = 'show_proc';
        iconpath = currpath + '/img/btc.png';

        self.ind = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.OTHER);
        self.ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE);
        self.ind.set_menu(self.create_menu());
        self.ind.set_label('BTC: ', self.app)

    def create_menu(self):
        menu = Gtk.Menu();

        item_git = Gtk.MenuItem('Open GitHub');
        item_git.connect('activate', self.github);

        item_quit = Gtk.MenuItem('Quit');
        item_quit.connect('activate', self.stop);

        menu.append(item_git);
        menu.append(item_quit);
        menu.show_all();
        return menu;

    def github(self, source):
        webbrowser.open('https://github.com/sirajuddin97/btc-indicator');

    def stop(self, source):
        Gtk.main_quit();

Indicator();
signal.signal(signal.SIGINT, signal.SIG_DFL);
Gtk.main();
