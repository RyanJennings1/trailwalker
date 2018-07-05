# Trailwalker
Walks trails to find the answers through trail and error

## Installation
After cloning the repository if `ChromeDriver` is not already downloaded then download the binary from:
`https://sites.google.com/a/chromium.org/chromedriver/downloads`
After downloading run:
```
mkdir -p ~/.chromedriver
cd ~/.chromedriver
mv ~/Downloads/chrome_driver_{osname}.zip
```

# To Run
`python main.py`

# Process
* Login ✔️
* Select Trail
* Check if trail has already been walked
* If already walked then select next trail
* If not already walked then go into trail
* Brute force guess the answers
* Write answers to json file ✔️
* Select next trail and repeat
