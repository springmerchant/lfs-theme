import pkgutil

# Discover all the installed themes
def get_themes():
    themes = []
    for importer, modname, is_pkg in pkgutil.iter_modules(__file__):
        if modname not in ['utils']:
            theme_module = __import__(modname)
            themes.append(theme_module.theme)

    return themes
        
 
