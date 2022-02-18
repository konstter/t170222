# Тестовое задание

- Ответ в файле [answer.py](https://github.com/konstter/t170222/blob/master/answer.py)
- Тесты в папке tests
- Результаты тестов в report.html

## Результат работы решения:
Возввращает список кортежей. Кортеж - первый элемент: имя файла, второй элемент - список папок до файла.

```bash
[konstter@fedora t170222]$ python3 answer.py
[('product_logo_24.png', ['chrome', 'product_logo_24.png']), ('google-chrome', ['chrome', 'cron', 'google-chrome']), ('default-app-block', ['chrome', 'default-app-block']), ('google-chrome', ['chrome', 'default-app-block']), ('libEGL.so', ['chrome', 'libEGL.so']), ('nacl_irt_x86_64.nexe', ['chrome', 'nacl_irt_x86_64.nexe']), ('libGLESv2.so', ['chrome', 'libGLESv2.so']), ('product_logo_16.png', ['chrome', 'product_logo_16.png']), ('manifest.json', ['chrome', 'MEIPreload', 'manifest.json']), ('preloaded_data.pb', ['chrome', 'MEIPreload', 'preloaded_data.pb']), ('xdg-settings', ['chrome', 'xdg-settings']), ('product_logo_32.png', ['chrome', 'product_logo_32.png']), ('product_logo_64.png', ['chrome', 'product_logo_64.png']), ('nacl_helper_bootstrap', ['chrome', 'nacl_helper_bootstrap']), ('product_logo_128.png', ['chrome', 'product_logo_128.png']), ('chrome-sandbox', ['chrome', 'chrome-sandbox']), ('v8_context_snapshot.bin', ['chrome', 'v8_context_snapshot.bin']), ('product_logo_256.png', ['chrome', 'product_logo_256.png']), ('drive.crx', ['chrome', 'default_apps', 'drive.crx']), ('youtube.crx', ['chrome', 'default_apps', 'youtube.crx']), ('external_extensions.json', ['chrome', 'default_apps', 'external_extensions.json']), ('docs.crx', ['chrome', 'default_apps', 'docs.crx']), ('gmail.crx', ['chrome', 'default_apps', 'gmail.crx']), ('chrome', ['chrome', 'chrome']), ('chrome_200_percent.pak', ['chrome', 'chrome_200_percent.pak']), ('resources.pak', ['chrome', 'resources.pak']), ('product_logo_48.png', ['chrome', 'product_logo_48.png']), ('xdg-mime', ['chrome', 'xdg-mime']), ('crashpad_handler', ['chrome', 'crashpad_handler']), ('nacl_helper', ['chrome', 'nacl_helper']), ('product_logo_32.xpm', ['chrome', 'product_logo_32.xpm']), ('icudtl.dat', ['chrome', 'icudtl.dat']), ('libwidevinecdm.so', ['chrome', 'WidevineCdm', '_platform_specific', 'linux_x64', 'libwidevinecdm.so']), ('manifest.json', ['chrome', 'WidevineCdm', 'manifest.json']), ('LICENSE', ['chrome', 'WidevineCdm', 'LICENSE']), ('am.pak', ['chrome', 'locales', 'am.pak']), ('fr.pak', ['chrome', 'locales', 'fr.pak']), ('ru.pak', ['chrome', 'locales', 'ru.pak']), ('chrome_100_percent.pak', ['chrome', 'chrome_100_percent.pak']), ('libEGL.so', ['chrome', 'swiftshader', 'libEGL.so']), ('libGLESv2.so', ['chrome', 'swiftshader', 'libGLESv2.so']), ('google-chrome', ['chrome', 'google-chrome'])]

```
