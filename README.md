## Intro
Have you ever wondered when is the best time for you to go to work in order to avoid traffic?  
This script gathers the data for you so that you can find that out!  
Essentially the `commute.py` script asks the GoogleMaps API how long it will take you to go to work now and then save teh result to a csv file in `data/times.csv`. Then you simply have to add this script to a scheduler and write the output to a csv file to gather some data!


## Instructions
First you need to add a script to the folder above such as `to_work.sh` which will call the `commute.py` script.
For example my `to_work.sh` looks like this:

```bash
# to_work.sh
cd path/to/folder/ && path/to/conda/env/python commute.py --pointA="Home address" \
                                                          --pointB="Work address" \
                                                          --mode="driving" \
                                                          --APIkey="Your-API-KEY" 2> logs/logs.err
```

You can change the mode of transportation to either "driving", "walking", "bicycling" or "transit".

## API Key
To get a Google API Key:
1. Go to your [Google Console](https://console.cloud.google.com/)
2. Create a project
3. Go to the Google Maps Platform tab (navigation bar on the left)
4. Click on APIs and enable "Directions API"
5. Click on Credentials, then on "+ CREATE CREDENTIALS" at the top of the page
6. Et voilà! You have created your Google API key. You can now copy paste the API key to your `to_work.sh` file and use it to run the command.


## Crontab
On Mac or Linux:
1. Type `crontab -l` in your terminal to get the list of cronjobs currently on your machine.
2. Type `crontab -e` in your terminal to edit these cronjobs.
3. Press `i` for insert (you are in `vi`).
4. Add your cronjob, for example mine is `*/5 6-9 * * 1-5 path/to/folder/to_work.sh`.
So that it runs every 5 minutes between 6am and 9am on weekdays.
5. Add execution permission to your bash script `chmod +x ./to_work.sh`.

## Troubleshoot
- Check the `logs.err` file for any error message you may get.
- If you are using Mac OS Catalina or older, you may need to give permissions to `cron` (you will get the error `Operation not permitted` otherwise). This [link](https://blog.bejarano.io/fixing-cron-jobs-in-mojave/) explains how to do it.

## References
Github repo for GoogleMaps API: https://github.com/googlemaps/google-maps-services-python