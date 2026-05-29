#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xbmcgui
import xbmcplugin
import xbmcaddon
import sys
import os
from urllib.parse import urlencode, parse_qsl
import json

# Get addon info
ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = ADDON.getAddonInfo('path')
ADDON_VERSION = ADDON.getAddonInfo('version')

# Plugin handle
HANDLE = int(sys.argv[1])

# German Streaming Services
STREAMING_SERVICES = {
    'netflix': {
        'name': 'Netflix',
        'package': 'com.netflix.mediaclient',
        'icon': 'https://www.netflix.com/favicon.ico',
        'description': 'Filme, Serien und Dokumentationen'
    },
    'prime': {
        'name': 'Amazon Prime Video',
        'package': 'com.amazon.venezia',
        'icon': 'https://www.primevideo.com/favicon.ico',
        'description': 'Filme, Serien und Originales'
    },
    'disney': {
        'name': 'Disney+',
        'package': 'com.disney.disneyplus',
        'icon': 'https://www.disneyplus.com/favicon.ico',
        'description': 'Disney, Pixar, Marvel und Star Wars'
    },
    'sky': {
        'name': 'Sky',
        'package': 'de.sky.go',
        'icon': 'https://www.sky.de/favicon.ico',
        'description': 'Filme, Serien und Live-TV'
    },
    'dazn': {
        'name': 'DAZN',
        'package': 'com.dazn',
        'icon': 'https://www.dazn.com/favicon.ico',
        'description': 'Sport Live und On-Demand'
    },
    'rtl': {
        'name': 'RTL+',
        'package': 'de.rtl.kundencenter.mobile',
        'icon': 'https://www.rtlplus.de/favicon.ico',
        'description': 'RTL Serien, Filme und Shows'
    },
    'prosiebenmaxx': {
        'name': 'Joyn (ProSieben)',
        'package': 'de.sevenone.assetclient.joyn',
        'icon': 'https://www.joyn.de/favicon.ico',
        'description': 'ProSieben, Sat.1 und Kabel Eins'
    },
    'maxdome': {
        'name': 'MagentaTV',
        'package': 'de.telekom.magenta.tv',
        'icon': 'https://www.magentaTV.de/favicon.ico',
        'description': 'Deutsche Telekom Streaming-Dienst'
    },
    'mubi': {
        'name': 'MUBI',
        'package': 'com.mubi',
        'icon': 'https://mubi.com/favicon.ico',
        'description': 'Kino Klassiker und Independent Filme'
    },
    'youtube': {
        'name': 'YouTube',
        'package': 'com.google.android.youtube',
        'icon': 'https://www.youtube.com/favicon.ico',
        'description': 'Videos und Kanäle'
    }
}

def log(msg, level=xbmc.LOGINFO):
    """Log message to Kodi log"""
    xbmc.log(f'[{ADDON_ID}] {msg}', level)

def show_main_menu():
    """Show main menu with all streaming services"""
    log('Showing main menu')
    
    for service_id, service in STREAMING_SERVICES.items():
        item = xbmcgui.ListItem(label=service['name'])
        item.setInfo('video', {'title': service['name'], 'plot': service['description']})
        item.setArt({'icon': service['icon']})
        
        url = get_url(action='service', service=service_id)
        xbmcplugin.addDirectoryItem(HANDLE, url, item, isFolder=True)
    
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL)
    xbmcplugin.endOfDirectory(HANDLE)

def show_service_menu(service_id):
    """Show menu for selected streaming service"""
    log(f'Showing menu for service: {service_id}')
    
    if service_id not in STREAMING_SERVICES:
        xbmcgui.Dialog().notification('Fehler', 'Streaming-Dienst nicht gefunden')
        return
    
    service = STREAMING_SERVICES[service_id]
    
    # Menu items for the service
    menu_items = [
        {'label': f'{service["name"]} öffnen', 'action': 'open_app', 'service': service_id},
        {'label': 'Beliebte Filme', 'action': 'search', 'service': service_id},
        {'label': 'Nach Film suchen', 'action': 'search_dialog', 'service': service_id},
    ]
    
    for menu_item in menu_items:
        item = xbmcgui.ListItem(label=menu_item['label'])
        url = get_url(**menu_item)
        xbmcplugin.addDirectoryItem(HANDLE, url, item, isFolder=menu_item.get('folder', False))
    
    xbmcplugin.endOfDirectory(HANDLE)

def open_app(service_id):
    """Open native streaming app"""
    log(f'Opening app for service: {service_id}')
    
    if service_id not in STREAMING_SERVICES:
        xbmcgui.Dialog().notification('Fehler', 'App nicht gefunden')
        return
    
    service = STREAMING_SERVICES[service_id]
    package_name = service['package']
    
    try:
        import subprocess
        # Android intent to open app
        cmd = f'am start -n {package_name}/{package_name}.MainActivity'
        subprocess.run(cmd, shell=True, check=True)
        log(f'App {package_name} opened successfully')
    except Exception as e:
        log(f'Error opening app: {str(e)}', xbmc.LOGERROR)
        xbmcgui.Dialog().notification('Fehler', f'App konnte nicht geöffnet werden: {str(e)}')

def search_dialog(service_id):
    """Open search dialog for user input"""
    log(f'Opening search dialog for service: {service_id}')
    
    keyboard = xbmc.Keyboard('', 'Nach Film suchen...')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        search_query = keyboard.getText()
        search_movies(service_id, search_query)
    
    xbmcplugin.endOfDirectory(HANDLE)

def search_movies(service_id, query):
    """Search for movies (placeholder)"""
    log(f'Searching for: {query} in {service_id}')
    xbmcgui.Dialog().notification('Info', f'Suche nach "{query}" wird in {STREAMING_SERVICES[service_id]["name"]} geöffnet')
    open_app(service_id)

def get_url(**kwargs):
    """Create URL for menu items"""
    return f'{sys.argv[0]}?{urlencode(kwargs)}'

def router(paramstring):
    """Router for different menu actions"""
    params = dict(parse_qsl(paramstring))
    log(f'Router params: {params}')
    
    action = params.get('action', 'main')
    service = params.get('service')
    
    if action == 'main':
        show_main_menu()
    elif action == 'service':
        show_service_menu(service)
    elif action == 'open_app':
        open_app(service)
    elif action == 'search_dialog':
        search_dialog(service)
    elif action == 'search':
        search_movies(service, params.get('query', ''))
    else:
        log(f'Unknown action: {action}')
        show_main_menu()

if __name__ == '__main__':
    log(f'Starting {ADDON_NAME} v{ADDON_VERSION}')
    router(sys.argv[2][1:])