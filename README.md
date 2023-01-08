# Human Readable Password Generator
The purpose of this program is to generate a human-readable password so that it is easy to remember passwords. Especially now with the data breaches sometimes we need to have a stong and secure password that we do not want to store in our password manager (Eg. Bank passwords, Paypal password, etc.).

The biggest misconseption is that we need to have a password with a wide variety of characters. The main thing that a password need is a high entropy. [Source](https://www.expressvpn.com/blog/6-common-misconceptions-about-passwords/)
We get more security from a longer password than by adding more characters.

## Usage 

### Recomended Use
Build the image
```bash
docker build -t humanreadable-passwd-gen_passwd .
```

Run the docker image
```bash
docker run -it --rm --name passwd_gene humanreadable-passwd-gen_passwd:latest
```

### Using docker-compose
```bash
docker-compose up && docker-compose down
```

### Running it using python3:

Install the requirements
```bash
pip install --upgrade -r requirements.txt
```

Run the generator
```bash
python3 ./passwd_gen.py
```
## Lincense

[GNU General Public License v3.0](LICENSE)