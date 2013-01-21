import pkgutil

# Discover all the installed themes
def get_themes():
    themes = []
    for importer, modname, is_pkg in pkgutil.iter_modules(__file__):
        if modname not in ['utils']:
            themes.append(__import__(modname))

    return themes
        
 
