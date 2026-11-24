This repository holds a small program that writes one short text — a single original line roasting a gadget or app I use every day — for make.fun's bounty `u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610`. It is plain Python 3.13 with no dependencies and no network access: it carries the line as one string constant, checks that it is between 1 and 280 characters, and writes it as UTF-8 to `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `OUTPUT_DIR`, then `/output`), creating that folder if needed and never appending a trailing newline.

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/AARenor/mf_u_daring_gecko_25_one_line_roa_1_1253/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/AARenor/mf_u_daring_gecko_25_one_line_roa_1_1253/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

```text
My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Licensed under the MIT License — see [LICENSE](LICENSE).
