__author__ = 'aferreiradominguez'
from  gi.repository import Gtk


class TreeView:
    def __init__(self):
        self.fiestra = Gtk.Window()
        self.fiestra.set_title("Exemplo tree view")
        self.fiestra.set_size_request(200, 200)
        self.fiestra.connect("delete_event", self.pecha_fiestra)

        # crea modelo
        self.treestore = Gtk.TreeStore(str)

        for pai in range(4):
            punteiro_pai = self.treestore.append(None, ['Pai %i' % pai])
            for fillo in range(3):
                self.treestore.append(punteiro_pai, ["Fillo %i do pai %i" % (fillo, pai)])
        # crea vista link a modelo
        self.treeview = Gtk.TreeView(self.treestore)
        self.tvcolumna = Gtk.TreeViewColumn('Columna 0')
        self.treeview.append_column(self.tvcolumna)
        self.celda = Gtk.CellRendererText()
        self.tvcolumna.pack_start(self.celda, True)
        self.tvcolumna.add_attribute(self.celda, 'text', 0)

        self.treeview.set_search_column(0)
        self.tvcolumna.set_sort_column_id(0)

        self.treeview.set_reorderable(True)

        self.fiestra.add(self.treeview)
        self.fiestra.show_all()



    def pecha_fiestra(self):
        Gtk.main_quit()
        return False

def main():
    Gtk.main()




if __name__ == "__main__":
    HolaTreeV = TreeView()
    main()
