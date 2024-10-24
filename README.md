# Anti-Webp

Do you like to save wallpaper images from Reddit to use later? Do you save images from Google for projects, or just to post to social media? Tired of some of them being in that pesky .webp format? Well, fret no more! Just set up a cronjob for this script to check your downloads directory for .webp files, and it'll automatically convert them to .pngs!

Save the script to file, and create an environment for it:

```
python3 -m venv webp-env
```

Activate the enviro and install Pillow:

```
source webp-env/bin/activate
```
```
pip install pillow
```

Set up the cronjob:
```
*/5 * * * * /webp-env/bin/python3 /path/to/anti-webp.py
```

Now, anything you save to downloads as a .webp will be auto-converted to .png with this job that checks said folder every five minutes (you can turn off the cronjob if you don't want it running indefinitely).
