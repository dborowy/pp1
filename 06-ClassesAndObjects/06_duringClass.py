########### 7,8,9
#class University():
    # konstruktorobiektu(metoda __init__)
#    def __init__(self):
        # cechyobiektu(pola)
#        self.name = 'UEK'
#        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
    # zachowaniaobiektu (metody)
#    def print_name(self):
#        print(self.name)
#    def set_name(self,new_name):
#        self.name = new_name
#    def print_fullname(self):
#        print(self.fullname)
#    def set_fullname(self,new_fullname):
#        self.fullname = new_fullname
#x = University()
#x.set_name('AGH')
#x.print_name()
#x.set_fullname('Akademia Górniczo-Hutnicza')
#x.print_fullname()

########### 10
class TV():
    def __init__(self):
        self.is_on = 0
        self.channel_no = 1
        self.channels = ['1. TVP1','2. TVP2','3. Polsat','4. TVN','5.Filmbox']
        self.channel_list = ['brak kanałów']
    def on(self):
        self.is_on = 1
    def off(self):
        self.is_on = 0
    def show_status(self):
        txt = 'Telewizor jest '
        if self.is_on  == 0:
            print(f'{txt}wyłączony')
        else:
            print(f'{txt}załączony, kanał {self.channel_no}')
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self):
        self.channel_list = self.channels
    def show_channels(self):
        print('LISTA KANAŁÓW TV')
        for i in self.channel_list:
            print(i)
telewizor = TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.show_channels()
telewizor.set_channels()
telewizor.show_channels()
telewizor.show_status()
telewizor.off()
