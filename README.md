[![make.fun bounty](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/lolipo8988-bot/long-roast-lawmakers/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/lolipo8988-bot/long-roast-lawmakers/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

# The Long Roast: Lawmakers and the File They Cannot Convert

A one-sentence entry for the make.fun **Long Roast** contest: a single
satirical sentence of at most 320 characters roasting lawmakers who would
regulate AI, crypto or the internet but cannot convert a file to PDF, judged
head-to-head on bite, aim and freshness.

## The sentence

> The lawmakers who voted to regulate AI, crypto, and the entire internet couldn't convert their own tech bill to a PDF, so the law went live as a tilted phone photo of a Word doc titled FINAL_BILL.pdf.docx.

205 characters. The setup grants the lawmakers maximal authority — they voted
to regulate AI, crypto and the entire internet — and the turn takes it away
with their own tech bill, the one file they could not convert to a PDF. The
punch lands on the last words: the law itself went live as a tilted phone
photo of a Word doc, wearing the double extension FINAL_BILL.pdf.docx — a
specific, visual detail instead of a generic tech-illiteracy cliché, and the
aim stays on the lawmakers and the law they wrote throughout.

## How it works

`main.py` (Python 3, standard library only) writes the sentence, with no
trailing newline, to `/output/entry.txt` in UTF-8. It is deterministic:
every run writes exactly the same bytes, verified locally by running it
twice and comparing the outputs byte for byte. An alternate output path may
be passed as the first argument for isolated local testing; with no argument
it writes to the competition path.

## License

MIT — see `LICENSE`.
