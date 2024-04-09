# Phonetic alphabet trainer
Command-line tool for practicing the NATO phonetic alphabet.

## Features
- Runs directly in the terminal.
- Randomizes order of the phonetic codes from run to run.
- Times user responses and provides warnings on slow entries.
- Prints a summary at the end of each run.
- Handles graceful quitting with `CTRL-C`.

## Example
```plaintext
❯ python3 phonetic_alphabet_trainer.py

Enter "quit" at any time.

D: Delta
G: Golf
F: Foxtrot
[...]
R: Romeo
V: Victor
J: Juliett

Time: 42.65s
Misses: 0

Took too long on:
  - Romeo: 3.68s
```

## Usage
Simply run the script from the terminal. Using a shell alias is a lot more convenient: you can add the following to your `~/.bashrc` or `~/.zshrc`.

```bash
alias nato="python3 $HOME/bin/phonetic_alphabet_trainer.py"
```

Then you can run with a few keystrokes.

```plaintext
❯ nato

Enter "quit" at any time.

C: Charlie
L: Lima
F: Foxtrot
[...]
```

## Installation
Copy and paste the raw script into a local Python file, or clone the repo.

```bash
git clone https://github.com/jpb7/phonetic-alphabet-trainer.git
```

Make sure you have Python 3.6 or newer.

```bash
python --version
```

Official Python downloads page:

- [Download Python](https://www.python.org/downloads/)

## License

- [MIT](https://github.com/jpb7/phonetic-alphabet-trainer/blob/main/LICENSE)

