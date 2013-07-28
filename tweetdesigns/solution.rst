Tweet Designs
-------------

*Tweet Designs* is a script that allows you to post **tweets** and **images** to your *Twitter account*.

First, you need to register your own application on twitter and fill in the configuration file that *Tweet Designs* autogenerates with your credentials. *Tweet Designs* can be found on GitHub_.

.. _GitHub: https://raw.github.com/ThyArmageddon/dgplug/master/tweetdesigns/tweetdesigns.py

Code
----

.. code:: python

        #!/usr/bin/env python2
        """
        This script will post tweets and images
        to twitter
        """

        import os
        from sys import exit, argv
        import ConfigParser
        from PIL import Image
        from twython import Twython

        """
        Value pairs in here can be changed or omitted
        """
        client_args = {
            'headers': {
                'User-Agent': 'TweetDesigns'
            },
            'proxies': {
                'socks5': '127.0.0.1:9050',
            },
            'timeout': 300,
        }

        """
        read_config() will check if the configuration file
        already exists. If it doesn't, it will create an
        empty skeleton. If it does, it will return the values from it
        """

        def read_config():
            home = os.getenv("HOME")

            if not os.path.exists(home + "/.tweetdesignsrc"):

                config_file = open(home + "/.tweetdesignsrc", "w")
                config = ConfigParser.RawConfigParser()
                config.add_section("app")
                config.set("app", "app_key", "")
                config.set("app", "app_secret", "")
                config.add_section("user")
                config.set("user", "oauth_token", "")
                config.set("user", "oauth_token_secret", "")
                config.write(config_file)
                config_file.close()
                print "Configuration file created"
                print "please add your information to ~/.tweetdesignsrc"
                exit(0)
            else:
                config = ConfigParser.RawConfigParser()
                config.read(home + "/.tweetdesignsrc")
                APP_KEY = config.get("app", "app_key")
                APP_SECRET = config.get("app", "app_secret")
                OAUTH_TOKEN = config.get("user", "oauth_token")
                OAUTH_TOKEN_SECRET = config.get("user", "oauth_token_secret")

                return APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET


        if __name__ == '__main__':

            """
            We check if the arguments are of the correct size
            """
            if len(argv) < 2:
                print "Too few arguments"
                print "Please use -h or --help for futher help"
                exit(1)

            """
            Print help manual
            """
            if argv[1] == "-h" or argv[1] == "--help":
                print "Usage: tweetdesigns [OPTIONS] [VALUE]"
                print "Posts to twitter from the terminal.\n"
                print "Mandatory arguments"
                print "-h, --help\t\t\tprints this help page"
                print "-p '[POST]'\t\t\tspecifies a tweet to post"
                print "-i [IMAGE] '[DESCRIPTION]'\tspecifies an image" \
                      " to post with optional description\n"
                print "ATTENTION: wrapping 'text' with '' is mandatory"
                exit(0)

            """
            Get the values needed from the configuration file
            """
            APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = read_config()

            """
            Check if the values are all set
            """
            if not APP_KEY or not APP_SECRET or \
               not OAUTH_TOKEN or not OAUTH_TOKEN_SECRET:
                print "Please check your configuration file, missing values"
                exit(1)

            """
            Tweet posting
            Check if all arguments are of the correct number
            If so, tweet the post
            """
            elif argv[1] == "-p":
                if len(argv) < 3:
                    print "Too few arguments"
                    exit(1)
                elif len(argv) > 3:
                    print "Too many arguments"
                    exit(1)
                else:
                    twitter = Twython(APP_KEY, APP_SECRET,
                                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                      client_args=client_args)
                    twitter.update_status(status=argv[2])

            """
            Image posting
            Check if the number of arguments is correct
            Check if the file exists
            Check if the file is actually a valid image
            Post the image with/without description depending
            on how many arguments are given
            """

            elif argv[1] == "-i":
                if len(argv) < 3:
                    print "Too few arguments"
                    exit(1)

                if len(argv) > 4:
                    print "Too many arguments"
                    exit(1)

                if not os.path.exists(argv[2]):
                    print "Image file does not exist"
                    exit(1)

                try:
                    img = Image.open(open(argv[2], "rb"))

                except IOError:
                    print "The file is not a valid image"
                    exit(1)

                photo = open(argv[2])
                if len(argv) == 3:
                    twitter = Twython(APP_KEY, APP_SECRET,
                                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                      client_args=client_args)
                    twitter.update_status_with_media(status="", media=photo)
                elif len(argv) == 4:
                    twitter = Twython(APP_KEY, APP_SECRET,
                                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                      client_args=client_args)
                    twitter.update_status_with_media(status=argv[3], media=photo)

            exit(0)
