Mount Assignment
----------------

The assignment was to write a python script that imitates the mount command that can be ran from the terminal using::

        $ mount

The python script wrote is called, conveniently, *mount.py* and runs using::

        $ python mount.py

or if made *executable*::

        $ ./mount.py

The python script can be found at the following link_.

.. _link: https://raw.github.com/ThyArmageddon/dgplug/master/mount/mount.py


Code and Explanation
--------------------

The code is shown below with comments to explain each part of it::

        #!/usr/bin/env python
        """
         This script will act like the mount command
         it will format what's found in /proc/mounts
        """
        
        import sys
        
        
        def mountinfo():
        
            """
            This function will open /proc/mounts
            Then it will read the contents line by line
            It will parse it and call printmount() function to display it
            """
        
            fd = open("/proc/mounts")  # Open /proc/mounts in read only mode
            for line in fd:            # Read line by line the content
        
                """
                The following will split the line using spaces as delimiters
                Then the first 4 outputs will be saved in 4 variables
                and the rest disregarded
                """
        
                mountname, mountpath, mounttype, mountdesc, _, _ = line.split(" ")
        
                """
                Call printmount() function to print the output
                """
        
                printmount(mountname, mountpath, mounttype, mountdesc)
            fd.close()  # Never forget to close the file once done using it
        
        
        def printmount(mountname, mountpath, mounttype, mountdesc):
        
            """
            printmout() function will print the arguments formatted correctly
            We also breka the line to keep each conform with python's < 80 chars
            """
        
            print "%s on %s type %s (%s)" % \
                (mountname, mountpath, mounttype, mountdesc)
        
        if __name__ == '__main__':
            mountinfo()  # call the mountinfo() function
            sys.exit(0)
