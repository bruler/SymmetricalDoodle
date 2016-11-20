SymmetricalDoodle
==============================

Internal Structure of DeepLibrary

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── Data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── Docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── Models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── Notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── References         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── Reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── Requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── Source             <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── config.json    
    │   │
    │   ├── DataProcessing <- Scripts to download or generate data, process it and describe it.
    │   │   └── make_dataset.py
    │   │
    │   ├── Evaluation     <- Evaluation model for every algorithm used   
    │   │  
    │   ├── Features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── logfile
    │   │
    │   ├── Models         <- Scripts to define models
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── Visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
