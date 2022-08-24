<h1 align="center">
  <a href="https://github.com/ju-djangun/cyes">
    <img src="https://user-images.githubusercontent.com/104500082/183292900-745172a1-0cb9-4f29-8cd5-c84247f1be87.png" alt="Logo" height="300">
  </a>
</h1>

<div align="center">
  Cyes - C without {;}&nbsp;&nbsp;&nbsp; :hammer:
  <br />
  <br />
  <br />
  <a href="https://github.com/ju-djangun/cyes/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/ju-djangun/cyes/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/ju-djangun/cyes/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<!-- shields here -->
<div align="center">
  <br />

  [![codecov](https://codecov.io/gh/ju-djangun/cyes/branch/main/graph/badge.svg?token=033RLYW21H)](https://codecov.io/gh/ju-djangun/cyes)
  [![Project license](https://img.shields.io/github/license/ju-djangun/cyes?style=flat-square)](LICENSE)
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Rules](#rules)
  - [Example](#example)
- [Motivation](#motivation)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)



</details>

----



## About

'cyes' is the transcompiler for Pythonistas who should code with C-like language(C/C++/C#...). 

It is simple, idiot CLI tool that auto semicolons&braces inserting by python-like 4-spacing indent and colons.

For this project, you can use both 'C-yes' and 'cy-es' depending on your preference. 

<br />

'cyes'는 C-like 프로그래밍 언어(C/C++/C#...)를 써야 하는 파이썬 개발자를 위한 트랜스파일러입니다.

간단하고 멍청하게 파이썬처럼 4개 공백문자와 쌍점으로 세미콜론과 중괄호를 자동 삽입하는 CLI 툴입니다.

취향껏 'C-yes(씨-예스)'나 'cy-es(싸이-스)'로 부르시면 됩니다.


### Built With

- python 3.8+
- [typer](https://github.com/tiangolo/typer)
- [anytree](https://github.com/c0fec0de/anytree)
- [poetry](https://python-poetry.org/)
- [amazing-github-template](https://github.com/dec0dOS/amazing-github-template)


## Getting started

### Prerequisites

> Python 3.8 or higher

> pip3

### Installation

```bash
pip install cyes
```

### Usage

```bash
cyes translate <file_name>
```

Translate .cy file to .c (with {;}) file.

```bash
cyes new <project_name>
```

Create <project_name> directory with template main.cy file.

```bash
cyes build <project_name>/<file_name.cy>
```

Translate and build using ```gcc``` command. This command will create <file_name.out> executive file in <project_name> directory.

```bash
cyes run <project_name>/main.cy
```

Build and execute .out file on your shell. 

### Rules

Now, cyes only accept indenting by 4-spaces.

And It ignores lines that begin with #.

If you want use one-line comment(//), now you should follow indenting rule like this.

```C
int main():
    printf("Commnet example")
    // printf("Comment!")
    // printf("Comments follow 4-space indenting too!)
```


### Example

print_googoo.cy

```C
#include <stdio.h>
#include <stdlib.h>


void print_googoo():
    for (int i=2; i<=9; i++):
        for (int j=1; j<=9; j++):
            printf("%d x %d = %d\n", i, j, (i*j))
        printf("\n")

int main(void):
    printf("hello world!\n")
    print_googoo()

    return 0
```

```bash
cyes translate print_googoo.cy
```

print_googoo.c(result)

```C
#include <stdio.h>
#include <stdlib.h>


void print_googoo() {
    for (int i=2; i<=9; i++) {
        for (int j=1; j<=9; j++) {
            printf("%d x %d = %d\n", i, j, (i*j));
        }
        printf("\n");
    }
}

int main(void) {
    printf("hello world!\n");
    print_googoo();

    return 0;
}
```


## Motivation

1. studying transpiler
2. My little finger is more important than C language tradition.

<br />

1. 트랜스파일러(컴파일러 및 형식 언어) 공부를 위한 토이 프로젝트
2. 새끼손가락을 아껴 사용합시다.


## FAQ
## Contributing

Thanks for taking the time to contribute.

<br />

기여에 관심을 가져주셔서 감사합니다.




## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.

<br />

이 프로젝트는 MIT 라이선스를 따릅니다.

[LICENSE](LICENSE) 파일에서 전문을 확인하실 수 있습니다.


