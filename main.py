import keypirinha as kp
import keypirinha_util as kpu

folder_dict = {
    "My Computer": "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}",
    "My Documents": "::{450d8fba-ad25-11d0-98a8-0800361b1103}",
}

class SystemFolder(kp.Plugin):

    def __init__(self):
        super().__init__()
        self.category = kp.ItemCategory.USER_BASE + 1

    def on_catalog(self):
        catalog = []
        for name in folder_dict.keys():
            catalog.append(self.create_item(
                category=self.category,
                label=name,
                short_desc=name,
                target=name,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE,
                icon_handle=None))
            
        self.set_catalog(catalog)

    def on_execute(self, item, action):
        if item.category() == self.category:
            kpu.shell_execute("explorer.exe", args="/e," + folder_dict[item.label()])

