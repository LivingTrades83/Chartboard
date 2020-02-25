import glob, os, yaml
from src.tipboard.app.properties import user_config_dir
from src.tipboard.app.utils import getTimeStr


def analyseCols(tiles, dashboard_config):
    """ Build a dict with all tiles present in dashboard.yml with the configs of this tiles """
    for tile_dict in tiles:
        if tile_dict['tile_id'] not in dashboard_config:  # TODO: protect against double inclusion of same id for 2 tile
            tile_config = dict(tile_id='unknown', tile_template='unknown', title='No title', weight=1)
            for key in tile_config:
                if key not in tile_dict:  # setting default value when not present
                    tile_dict[key] = tile_config[key]
            dashboard_config[tile_dict['tile_id']] = tile_dict


def findTilesNames(cols_data):
    """ Find tile_template & tile_id in all cols of .yaml """
    dash_config = dict()
    for col_dict in cols_data:
        for tiles_dict in list(col_dict.values()):
            analyseCols(tiles=tiles_dict, dashboard_config=dash_config)
    return dash_config


def yamlFileToPythonDict(layout_name='layout_config'):
    """ Parse in yaml the .yaml file to return python object """
    layout_name = layout_name if layout_name else 'layout_config'
    config_path = f'{user_config_dir}{layout_name}'
    try:
        with open(config_path, 'r') as layout_config:
            config = yaml.safe_load(layout_config)
    except FileNotFoundError:
        if '.yaml' not in config_path:
            config_path += '.yaml'
        with open(config_path, 'r') as layout_config:
            config = yaml.safe_load(layout_config)
    return config


def parseXmlLayout(layout_name='layout_config'):
    """ Parse all tiles, cols, rows from a specific .yaml """
    config = yamlFileToPythonDict(layout_name=layout_name)
    rows = [row for row in [row for row in config['layout']]]
    cols = [col for col in [[col for col in list(row.values())[0]] for row in rows]]
    cols_data = [colsValue for colsList in cols for colsValue in colsList]
    config['tiles_conf'] = findTilesNames(cols_data)
    return config


def getConfigNames():
    """ Return all dashboard file name from Config/ """
    configs_names = list()
    configs_dir = os.path.join(user_config_dir, '*.yaml')
    for config_path in glob.glob(configs_dir):  # Get all name of different *.yml present in Config/ directory
        configs_names.append(config_path.split('/')[-1].replace('.yaml', ''))
        if not configs_names:
            raise Exception(f'No config (.yaml) file found in {os.path.join(user_config_dir, "*.yaml")}')
    return configs_names


def getDashboardName():
    """ Returns title to display as a html title. """
    title = ''
    config_names = getConfigNames()  # get all name of files present in ./Config/*.yaml
    try:
        if len(config_names) == 1:  # if only one file, return the one
            config = parseXmlLayout(config_names[0])
            title = config['details']['page_title']
        else:  # if multiple file, need to have the .yaml displayed for the client
            title = 'Flipboard Mode'
    except KeyError:
        print(f"{getTimeStr()} (+) config {config_names[0]} has no key: details/page_title'", flush=True)
    return title


def getFlipboardTitles():
    """ Get title of all dashboard inside Config/ """
    config_names = getConfigNames()
    listNameDashboard = list()
    rcx = 1
    for config in config_names:
        config = parseXmlLayout(config)
        if 'details' in config and 'page_title' in config['details']:
            listNameDashboard.append(config['details']['page_title'])
        else:
            listNameDashboard.append(f'Dashboard {rcx}')
        rcx += 1
    return listNameDashboard
