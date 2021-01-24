# TS Data Collection from UCR/UEA suite

* Download and unpack the file [here](https://drive.google.com/file/d/13PwgJNBTnyT1IjbUxFqQlqq2VTGDVw8N/view?usp=sharing) to your preferred path
* Update the *fully qualified path* to the unpacked directory in the file `./PATH` (no `~`, `$HOME`)

## Python

At the start of your script, add this:

```
import sys
sys.path.append("full/path/to/timeseries-data") # path to this repository
import py_ts_data
```

You can use the following funtions:
```
py_ts_data.list_dir() # lists available datasets
py_ts_data.load_data("ACSF1") # lists information for dataset ACSF1
X_train, y_train, X_test, y_test, info = py_ts_data.data_info("ACSF1") # loads data for dataset ACSF1
```

## Rust

Todo
