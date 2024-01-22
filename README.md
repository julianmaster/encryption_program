# Encryption_program

> Programme test d'obfuscation de code

## Installation

Ce projet utilise [python3](https://www.python.org/) et [pip](https://pypi.org/). Allez les voir si vous ne les avez pas
déjà installés localement.

```shell
pip install pywin32
pip install pyinstaller
pip install cryptography
```

### Création de l'installeur Windows

```shell
pywin32_postinstall.py -install
pyinstaller --clean .\install_windows.spec
```

### Ordre de fonctionnement

1. Chiffrement de `code.py` au moyen de `encryption.py`.
2. Résultat ajouté à la variable `encrypted_code` de `decryption.py`
3. Transformation en une variable (qui est une archive zip) au moyen de `encryption_zip.py`
4. Résultat ajouté à la variable `module_zip` de `run.py`