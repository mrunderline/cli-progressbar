# Cli Progressbar

It's a lightweight and easy to use progress-bar for command-line/terminal applications.

## Install

`pip install cli-progressbar`

## Features

* **Simple**, **Lightweight** and **Easy** to use.
* Single progress bar mode.
* Multiple progress bar mode.
* Custom bar characters.
* **iterate** function to auto handle progress bar in `for` loops.

## Usage
### Single mode
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
### Multiple mode
```python
from cli_progressbar import Progress, MultiProgressManager

# define multi progress instance
manager = MultiProgressManager()

# now define any progress bar you need
progress_1 = Progress()
progress_2 = Progress()

# now add them to multi progress manager
manager.append(progress_1)
manager.append(progress_2)

# Done! It's ready to use like a single progress!
progress_1.start('start progress 1')
progress_2.start('start progress 2')
for i in progress_1.iterate(range(8), 'state progress 1'):
    for j in progress_2.iterate(range(5), 'state progress 2'):
        # Do your stuff

progress_1.stop('stop progress 1')
progress_2.stop('stop progress 2')
```

But maybe you want it more simple, so I have an easier solution!
```python
from cli_progressbar import MultiProgressManager

# define multi progress instance; but this time, pass 2 arguments
manager = MultiProgressManager(
    progress_count=2,            # default: 0
    progress_prefix='progress_'  # default: progress_
)

# now you can access 2 progressbar, just request them from manager
manager.progress_1.start('start progress 1')
manager.progress_2.start('start progress 2')
for i in manager.progress_1.iterate(range(8), 'state progress 1'):
    for j in manager.progress_2.iterate(range(5), 'state progress 2'):
        # Do your stuff

manager.progress_1.stop('stop progress 1')
manager.progress_2.stop('stop progress 2')
```

## Parameters

* `goal` to change goal in between of process, it's useful for dynamic tasks
* `bar_len` length of progress bar (default: 60)
* `fill` bar fill symbol (default: █)
* `zfill` bar zero fill symbol (default: -)
* `decimals` positive number of decimals in percent complete  (default: 1)
* `formatter` a function that formats the count and goal, useful for handling large numbers like file sizes

## Any Questions? Report a Bug? Enhancements?

Please open a new issue on [GitHub](https://github.com/mrunderline/cli-progressbar/issues)

## License

CLI-ProgressBar is OpenSource and licensed under the terms of [The MIT License (X11)](http://opensource.org/licenses/MIT). You're welcome to [contribute](https://github.com/mrunderline/cli-progressbar/blob/master/CONTRIBUTE.md)!
