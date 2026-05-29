#!/bin/bash

# Script to create a Kodi addon ZIP file

ADDON_NAME="plugin.video.german.streaming"
VERSION="1.0.0"
ZIP_NAME="${ADDON_NAME}-${VERSION}.zip"

# Create temporary directory
mkdir -p temp_addon/$ADDON_NAME

# Copy addon files
cp addon.xml temp_addon/$ADDON_NAME/
cp default.py temp_addon/$ADDON_NAME/
cp icon.png temp_addon/$ADDON_NAME/ 2>/dev/null || touch temp_addon/$ADDON_NAME/icon.png
cp fanart.jpg temp_addon/$ADDON_NAME/ 2>/dev/null || touch temp_addon/$ADDON_NAME/fanart.jpg
cp screenshot.jpg temp_addon/$ADDON_NAME/ 2>/dev/null || touch temp_addon/$ADDON_NAME/screenshot.jpg

# Copy resources directory
mkdir -p temp_addon/$ADDON_NAME/resources
cp resources/settings.xml temp_addon/$ADDON_NAME/resources/
cp resources/strings.json temp_addon/$ADDON_NAME/resources/

# Create ZIP file
cd temp_addon
zip -r ../$ZIP_NAME $ADDON_NAME/
cd ..

# Cleanup
rm -rf temp_addon

echo "✅ Created: $ZIP_NAME"
echo "📦 Size: $(du -h $ZIP_NAME | cut -f1)"
echo "🎬 Ready for Kodi installation!"
