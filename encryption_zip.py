import os
import shutil
import tempfile
import zipfile
from io import BytesIO


def main():
    in_memory_zip = BytesIO()

    contenu = None
    with open('decryption.py', 'r') as fichier_binaire:
        contenu = fichier_binaire.read()

    # zf = zipfile.PyZipFile(in_memory_zip, "a", zipfile.ZIP_BZIP2, False)
    zf = zipfile.PyZipFile(in_memory_zip, "a", zipfile.ZIP_BZIP2, False)

    dir_path = None
    with tempfile.TemporaryDirectory(delete=False) as temp_dir:
        # open your files here
        dir_path = temp_dir
        named_file = open(os.path.join(temp_dir, "__init__.py"), 'w')
        named_file.write(contenu)
        named_file.close()


    zf.writepy(os.path.join(dir_path, "__init__.py"))

    for zfile in zf.filelist:
        zfile.create_system = 0
    zf.close()

    print(in_memory_zip.getvalue())


if __name__ == "__main__":
    main()