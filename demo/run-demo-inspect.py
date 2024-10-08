#!/usr/bin/env python3
from livekey import animate_commands


commands = [
    'python',
    'import wat',
    'wat',
    'wat / {7}',
    'wat.short / (1,)',
    'wat.s / {}',
    'import re',
    'wat / re',
    'wat / re.match',
    'wat.locals',
]


if __name__ == '__main__':
    animate_commands(commands, key_delay=0.1, line_delay=1.0)

"""
- Run script: python docs/demo/run-demo-inspect.py
- Record with OBS recorder
- Upload MP4 to Github issue: https://github.com/igrek51/wat/issues/1
- Get source URL like:
  <video src="https://private-user-images.githubusercontent.com/12595017/330394505-3585123a-c1c4-4ca3-85cd-f52e82e9c744.mp4?jwt=
  <video src="https://private-user-images.githubusercontent.com/12595017/352510889-022ef89a-9e35-45be-9e2f-08d2c6af9075.mp4?jwt=
- Turn it into (trim first dashed fragment of filename and drop extension):
  https://github.com/igrek51/wat/assets/12595017/3585123a-c1c4-4ca3-85cd-f52e82e9c744
  or
  https://github.com/user-attachments/assets/022ef89a-9e35-45be-9e2f-08d2c6af9075
  or edit the post to get the full URL
- Test with curlie if you get 302. Give Github some time to fully upload it.
- Embed URL in your `<video src="..">` player
"""
