Duplicate Image Finder
----------------------

This script will take any number of directories, search them recursively and return the duplicate images with their locations. The *dup_images* script can be found on GitHub_.

.. _GitHub: https://raw.github.com/ThyArmageddon/dgplug/master/dup_images/dup_images.py


Code
----

.. code:: python

        #!/use/bin/env python2
        """
        This Python script will scan one of more directories and return
        the duplicate images in them based on their md5sum
        """

        import os
        import sys
        import Image
        import hashlib


        def md5sum(img):
            """
            md5sum returns the md5sum of the file given to it
            """
            md5 = hashlib.md5()
            with open(img, "rb") as f:
                for chunk in iter(lambda: f.read(128 * md5.block_size), b''):
                    md5.update(chunk)
                    return md5.hexdigest()


        def find_files(path):
            """
            The following function will take a path
            search it recursively and find all the images
            inside the directories inside. Then it will find
            the md5 checksum of each image and return in a
            dictionary.
            """
            for root, dirs, files in os.walk(path):
                if files:
                    for _file in files:
                        try:
                            Image.open(root + "/" + _file)
                            md5 = md5sum(root + "/" + _file)
                            yield {md5: root + "/" + _file}

                        except IOError:
                            continue


        def parse_paths(paths):
            """
            This function will take a list of paths and check if the paths
            are valid, if not, it will drop them.
            """
            file_list = []
            for path in paths:
                if os.path.isdir(path):
                    file_list = find_files(path)
                    yield file_list

                else:
                    print path + " is not a valid path"


        def find_dups(_list):
            """
            This function will search through the dictionary
            comparing md5 checksums in search of duplicates.
            If it finds duplicates it will output the duplicates'
            path and filename
            """
            md5_list = {}
            print "Duplicate images are:"
            for items in _list:
                for item in items:
                    for _md5 in item:
                        if _md5 in md5_list:
                            print "'" + item[_md5] + "' and '" + \
                                md5_list[_md5] + "' are duplicates"
                        else:
                            md5_list[_md5] = item[_md5]


        if __name__ == "__main__":
            if len(sys.argv) < 1:
                print "Please provide at least one direcrory"
                sys.exit(1)

            else:
                sys.argv.pop(0)
                file_list = parse_paths(sys.argv)
                find_dups(file_list)
