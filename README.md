#Cli Progressbar

It's a lightweight and easy to use progress-bar for command-line/terminal applications.

## Install

`pip install cli-progressbar`

## Features

* **Simple**, **Lightweight** and **Easy** to use.
* Single progressbar mode
* Custom Bar Characters
* **iterate** function to auto handle progressbar in `for` loops

## Usage

```python
from cli_progressbar import Progress

# define progressbar instance
progressbar = Progress(85)

# start function pass 0 to update function and print progressbar
# you can pass an string to show as status 
progressbar.start('start status')

users = find_users()  # return a list of users

# you can fill goal like this
progressbar.goal = len(users)

for i, user in enumerate(users):
    # this function will update progressbar with new data and status
    progressbar.update(i, 'processing status')
    
    # Do your stuff

# stop function pass goal itself to update function
progressbar.stop('stop status')
```

But it's boaring... so use `iterate` function:
```python
from cli_progressbar import Progress

progressbar = Progress()
progressbar.start('start status')

users = find_users()
for user in progressbar.iterate(users, 'processing status'):
    # Do your stuff

progressbar.stop('stop status')
```

**iterate** function also support dynamic status, by passing a function and each element of list as it input.
```python
for user in progressbar.iterate(users, lambda user: 'processing ' + user):
    # Do your stuff
```

## Parameters

* `goal` to change goal in between of process, it's useful for dynamic tasks
* `bar_len` length of progressbar (default: 60)
* `fill` bar fill symbol (default: █)
* `zfill` bar zero fill symbol (default: -)
* `decimals` positive number of decimals in percent complete  (default: 1)

## Any Questions? Report a Bug? Enhancements?

Please open a new issue on [GitHub](https://github.com/mrunderline/cli-progressbar/issues)

## License

CLI-Progress is OpenSource and licensed under the terms of [The MIT License (X11)](http://opensource.org/licenses/MIT). You're welcome to [contribute](https://github.com/mrunderline/cli-progressbar/blob/master/CONTRIBUTE.md)!
