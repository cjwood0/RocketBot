# RocketBot

*Bringing Rocket to You*

RocketBot collects URLs from Rocket's Instagram and embeds them in Discord on command.

---

## Installation

Clone the repo and execute `pip install`

## Environment Variables

`ROCKET_ID` - Verify your ROCKET_ID at https://www.instagram.com/ohrocketdog/

`DISCORD_TOKEN` - Copy this value from Discord after authorizing your own RocketBot


## Running

`python RocketBot.py`

## Usage

Simply type `+rocket` wherever you see RocketBot

## Hosting

RocketBot can be easily be deployed to Heroku:

1. Install the Heroku CLI and `heroku login`
2. Create your own RocketBot app with `heroku create <optional-name>`
3. Deploy RocketBot using `git push heroku master`
4. Set your `ROCKET_ID` and `DISCORD_TOKEN` environment variables

## Contributing

*Due to the high level of demand, the RocketBot Team cannot accept pull requests at this time, and any issues will be triaged according to their severity*

## License

Copyright (c) 2020 CJ Wood, Kati and Rocket Best

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
