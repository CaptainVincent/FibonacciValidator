# Fibonacci Validator

A tool for verify fibonacci number. Use data resource from [link](http://www.protocol5.com/Fibonacci).

### Feature

1. Use local file as cache for fibonacci table.
2. One times http request get fibonacci table.
3. Flexible Command line optional arguments:
    - -h, --help            show this help message and exit
    - --file FILE, -f FILE  Use a file as input (Each line has a pair idx fibonacci seperated by space)
    - --inline N N, -i N N  Check a pair index and fibonacci Number
    - --silence, -s         Silence output

### How to prepare environment

**Get the source code**

```bash
git clone git@github.com:CaptainVincent/FibonacciValidator.git
```

**Install packages**

This project manage packages use pipenv. But you can manually install below packages.

- tinydb
- requests
- bs4
- lxml

Use pipenv directly.

```bash
pipenv install
```

### Example

**Use idx and fib number pair directly verify in command**

```bash
> python validator.py -i 447 2175802127494856116713672426425688880595219724476419600966267302098624954951397614199316858899137282

447 False
```

```bash
> python validator.py -i 477 2175802127494856116713672426425688880595219724476419600966267302098624954951397614199316858899137282

477 True
```

**Use test file as input**
```bash
> python validator.py -f example/test.txt

0 True
1 False
2 True
3 True
4 False
```