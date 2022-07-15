# Inflam

"Come on, get inflamed!"

![Continuous Integration build in GitHub Actions](https://github.com/christophra/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Work on trial data in Comma-Separated Value (CSV) and JavaScript Object Notation (JSON) format
- Generate plots of trial data
- Administer corticosteroids via the ThinkPad TrackPoint
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Credits

- All glory to the hypnotoad
- [The Intermediate Python course](https://carpentries-incubator.github.io/python-intermediate-development)

## Citation

see CITATION.cff

## License

GNU GPL v3

# Installation

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install .``` 

## Contact

M