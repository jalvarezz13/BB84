# 🔑 BB84 Protocol Simulation in Python

This project implements a **basic simulation of the BB84 protocol** for Quantum Key Distribution (QKD).
It demonstrates how Alice and Bob can generate and share a secret key securely using principles of quantum mechanics.

## 🚀 Features

- Random generation of bits and bases for Alice.
- Random basis selection for Bob.
- Simulation of measurement with correct or random results depending on bases.
- Sifting process to obtain the shared key between Alice and Bob.
- Reproducible results with a fixed random seed.

## 🖥️ Run the simulation

Clone the repository and run the script with Python 3:

```bash
git clone https://github.com/jalvarezz13/BB84
cd bb84
python bb84.py
```

## 📊 Example output

```
Alice's original bits:        [1, 0, 1, 1, 0, ...]
Alice's bases:                ['Z', 'X', 'Z', 'X', ...]
Bob's bases:                  ['X', 'Z', 'Z', 'X', ...]
Bob's results:                [0, 0, 1, 1, ...]

--- RESULTS ---
Alice's sifted key:           [1, 0, 1, 1, ...]
Bob's sifted key:             [1, 0, 1, 1, ...]
Matches:                      18 / 20
```

## 📖 References

- [BB84 protocol on Wikipedia](https://en.wikipedia.org/wiki/BB84)
- Bennett, C. H., & Brassard, G. (1984). _Quantum cryptography: Public key distribution and coin tossing._

## 📜 License

This project is released under the MIT License.
Feel free to use, modify, and share it!
