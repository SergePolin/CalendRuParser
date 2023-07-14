# CalendRuParser

## Overview

CalendRuParser is a Python tool that parses a list of official and unofficial holidays from calend.ru.

## Table of Contents

- [CalendRuParser](#calendruparser)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [General Info](#general-info)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Author](#author)

## General Info

This tool is designed to fetch and parse holidays data from calend.ru. It can be useful for identifying holiday dates, especially for applications that need to be aware of these dates.

## Dependencies

This project depends on various packages. Some major ones include:

- beautifulsoup4==4.12.2
- html5lib==1.1
- poetry==1.5.1

## Installation

To setup the project locally:

```bash
# clone the repository
git clone https://github.com/innopolisPythonSummerProject/CalendRuParser
cd CalendRuParser

# Install dependencies
poetry install
```

## Usage

To run this project, execute the following commands:

```bash
python parse.py
```

## Author

- Sergei Polin - <s.polin@innopolis.university>
