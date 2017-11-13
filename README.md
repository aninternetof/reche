# Description

Automatically set your MacOS background to track a Tumblr feed.

# Installation and Usage

[Make sure you have Python 3 installed.](http://docs.python-guide.org/en/latest/starting/install3/osx/)

```bash
$ python3 setup.py install
$ reche --url http://a-la-recherche.tumblr.com/ --back_url http://i.imgur.com/AoInTCS.jpg
```

# Running Periodically

```bash
$ nano com.aninternetof.reche.plist # change the Tumblr/background URLs to what you want, and check the application path to reche
$ cp com.aninternetof.reche.plist ~/Library/LaunchAgents
$ sudo launchctl load ~/Library/LaunchAgents/com.aninternetof.reche.plist
```

# Credit

Default background image credit [freestocktextures.com](https://freestocktextures.com/texture/cement-rough-parget,807.html).
